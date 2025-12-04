import argparse
import json
import struct
import sys
from pathlib import Path
from typing import Tuple

import numpy as np

try:
    import cv2  
    HAS_OPENCV = True
except Exception:
    HAS_OPENCV = False
    from PIL import Image  


def _read_visual_data(file_path: str) -> np.ndarray:
    path_obj = Path(file_path)
    if not path_obj.exists():
        raise FileNotFoundError(f"Входное изображение не найдено: {file_path}")
    if HAS_OPENCV:
        visual_data = cv2.imdecode(np.fromfile(str(path_obj), dtype=np.uint8), cv2.IMREAD_COLOR)
        if visual_data is None:
            raise ValueError(f"Неподдерживаемое или поврежденное изображение: {file_path}")
        visual_data = cv2.cvtColor(visual_data, cv2.COLOR_BGR2RGB)
        return visual_data
    else:
        visual_data = Image.open(str(path_obj)).convert("RGB")
        return np.array(visual_data)


def _write_visual_data(file_path: str, visual_rgb_array: np.ndarray) -> None:
    path_obj = Path(file_path)
    path_obj.parent.mkdir(parents=True, exist_ok=True)
    if HAS_OPENCV:
        bgr_data = cv2.cvtColor(visual_rgb_array, cv2.COLOR_RGB2BGR)
        extension = path_obj.suffix.lower()
        success, buffer_data = cv2.imencode(extension if extension else ".png", bgr_data)
        if not success:
            raise RuntimeError("Не удалось закодировать выходное изображение")
        buffer_data.tofile(str(path_obj))
    else:
        Image.fromarray(visual_rgb_array).save(str(path_obj))


def calculate_intensity_histogram(visual_rgb_array: np.ndarray) -> np.ndarray:
    if visual_rgb_array.ndim == 3 and visual_rgb_array.shape[2] == 3:
        if HAS_OPENCV:
            ycrcb_data = cv2.cvtColor(visual_rgb_array, cv2.COLOR_RGB2YCrCb)
            intensity_plane = ycrcb_data[..., 0]
        else:
            red_channel, green_channel, blue_channel = visual_rgb_array[..., 0], visual_rgb_array[..., 1], visual_rgb_array[..., 2]
            intensity_plane = (0.299 * red_channel + 0.587 * green_channel + 0.114 * blue_channel).astype(np.uint8)
    else:
        intensity_plane = visual_rgb_array.astype(np.uint8)
    hist_counts, _ = np.histogram(intensity_plane, bins=256, range=(0, 255))
    return hist_counts.astype(np.int64)


def save_histogram_data(file_path: str, hist_array: np.ndarray) -> None:
    path_obj = Path(file_path)
    path_obj.parent.mkdir(parents=True, exist_ok=True)
    suffix = path_obj.suffix.lower()
    if suffix in (".txt", ".dat"):
        path_obj.write_text(" ".join(map(str, hist_array.tolist())), encoding="utf-8")
    elif suffix == ".csv":
        path_obj.write_text(",".join(map(str, hist_array.tolist())), encoding="utf-8")
    elif suffix == ".json":
        path_obj.write_text(json.dumps(hist_array.tolist()), encoding="utf-8")
    elif suffix in (".bin", ".raw"):
        with open(path_obj, "wb") as f_handle:
            f_handle.write(struct.pack("<256I", *hist_array.tolist()))
    elif suffix == ".wav":
        write_hist_as_wav_file(str(path_obj), hist_array)
    else:
        path_obj.with_suffix(".txt").write_text(" ".join(map(str, hist_array.tolist())), encoding="utf-8")


def load_histogram_data(file_path: str) -> np.ndarray:
    path_obj = Path(file_path)
    suffix = path_obj.suffix.lower()
    if suffix in (".txt", ".dat"):
        data_list = list(map(int, path_obj.read_text(encoding="utf-8").split()))
    elif suffix == ".csv":
        data_list = list(map(int, path_obj.read_text(encoding="utf-8").replace("\n", "").split(",")))
    elif suffix == ".json":
        data_list = json.loads(path_obj.read_text(encoding="utf-8"))
    elif suffix in (".bin", ".raw"):
        with open(path_obj, "rb") as f_handle:
            data_list = list(struct.unpack("<256I", f_handle.read(256 * 4)))
    elif suffix == ".wav":
        data_list = read_hist_from_wav_file(str(path_obj))
    else:
        raise ValueError(f"Неподдерживаемый формат гистограммы: {suffix}")
    result_array = np.array(data_list, dtype=np.int64)
    if result_array.size != 256:
        raise ValueError(f"Гистограмма должна иметь 256 значений, получено {result_array.size}")
    return result_array


def perform_histogram_equalization(visual_rgb_array: np.ndarray) -> np.ndarray:
    if HAS_OPENCV:
        if visual_rgb_array.ndim == 3 and visual_rgb_array.shape[2] == 3:
            ycrcb_data = cv2.cvtColor(visual_rgb_array, cv2.COLOR_RGB2YCrCb)
            ycrcb_data[..., 0] = cv2.equalizeHist(ycrcb_data[..., 0])
            return cv2.cvtColor(ycrcb_data, cv2.COLOR_YCrCb2RGB)
        else:
            return cv2.equalizeHist(visual_rgb_array)
    else:
        if visual_rgb_array.ndim == 3 and visual_rgb_array.shape[2] == 3:
            red_channel, green_channel, blue_channel = visual_rgb_array[..., 0], visual_rgb_array[..., 1], visual_rgb_array[..., 2]
            intensity_plane = (0.299 * red_channel + 0.587 * green_channel + 0.114 * blue_channel).astype(np.uint8)
            hist_counts, bins_edges = np.histogram(intensity_plane.flatten(), 256, [0, 256])
            cumulative_distrib_func = hist_counts.cumsum()
            masked_cdf = np.ma.masked_equal(cumulative_distrib_func, 0)
            scaled_cdf = (masked_cdf - masked_cdf.min()) * 255 / (masked_cdf.max() - masked_cdf.min())
            final_cdf = np.ma.filled(scaled_cdf, 0).astype(np.uint8)
            equalized_intensity = final_cdf[intensity_plane]
            scale_factor = (equalized_intensity.astype(np.float32) + 1e-6) / (intensity_plane.astype(np.float32) + 1e-6)
            red_equalized = np.clip(red_channel.astype(np.float32) * scale_factor, 0, 255).astype(np.uint8)
            green_equalized = np.clip(green_channel.astype(np.float32) * scale_factor, 0, 255).astype(np.uint8)
            blue_equalized = np.clip(blue_channel.astype(np.float32) * scale_factor, 0, 255).astype(np.uint8)
            return np.stack([red_equalized, green_equalized, blue_equalized], axis=-1)
        else:
            intensity_plane = visual_rgb_array
            hist_counts, bins_edges = np.histogram(intensity_plane.flatten(), 256, [0, 256])
            cumulative_distrib_func = hist_counts.cumsum()
            masked_cdf = np.ma.masked_equal(cumulative_distrib_func, 0)
            scaled_cdf = (masked_cdf - masked_cdf.min()) * 255 / (masked_cdf.max() - masked_cdf.min())
            final_cdf = np.ma.filled(scaled_cdf, 0).astype(np.uint8)
            return final_cdf[intensity_plane]


def apply_gamma_correction(visual_rgb_array: np.ndarray, correction_value: float = 1.0) -> np.ndarray:
    if correction_value <= 0:
        raise ValueError("correction_value (gamma) должно быть > 0")
    inv_gamma = 1.0 / correction_value
    lookup_table = (np.linspace(0, 1, 256) ** inv_gamma * 255.0).astype(np.uint8)
    output_array = lookup_table[visual_rgb_array]
    return output_array


def write_hist_as_wav_file(file_path: str, hist_array: np.ndarray, sampling_rate: int = 8000) -> None:
    path_obj = Path(file_path)
    path_obj.parent.mkdir(parents=True, exist_ok=True)
    histogram_float = hist_array.astype(np.float64)
    if histogram_float.max() > 0:
        histogram_float = (histogram_float - histogram_float.min()) / (histogram_float.max() - histogram_float.min()) * 255.0
    audio_samples = histogram_float.astype(np.uint8).tobytes() * 64  
    channel_count = 1
    bits_per_sample_val = 8
    byte_rate_val = sampling_rate * channel_count * bits_per_sample_val // 8
    block_align_val = channel_count * bits_per_sample_val // 8
    audio_data_size = len(audio_samples)
    riff_chunk_size = 36 + audio_data_size
    with open(path_obj, "wb") as f_handle:
        f_handle.write(b"RIFF")
        f_handle.write(struct.pack("<I", riff_chunk_size))
        f_handle.write(b"WAVEfmt ")
        f_handle.write(struct.pack("<IHHIIHH", 16, 1, channel_count, sampling_rate, byte_rate_val, block_align_val, bits_per_sample_val))
        f_handle.write(b"data")
        f_handle.write(struct.pack("<I", audio_data_size))
        f_handle.write(audio_samples)


def read_hist_from_wav_file(file_path: str) -> list:
    with open(file_path, "rb") as f_handle:
        all_data = f_handle.read()
    data_chunk_index = all_data.find(b"data")
    if data_chunk_index < 0:
        raise ValueError("Неверный WAV: отсутствует data chunk")
    data_size_val = struct.unpack("<I", all_data[data_chunk_index + 4 : data_chunk_index + 8])[0]
    audio_content = all_data[data_chunk_index + 8 : data_chunk_index + 8 + data_size_val]
    if len(audio_content) < 256:
        raise ValueError("WAV не содержит 256 сэмплов")
    first_256_samples = audio_content[:256]
    return list(first_256_samples)


def parse_arguments(cli_args=None):
    arg_parser = argparse.ArgumentParser(description="Обработка изображений: выравнивание гистограммы и гамма-коррекция.")
    arg_parser.add_argument("-i", "--input", required=True, help="Путь к входному изображению (jpg/png/bmp/...)")
    arg_parser.add_argument("-o", "--output", required=True, help="Путь для сохранения обработанного изображения")
    arg_parser.add_argument("-m", "--method", choices=["equalize", "gamma"], required=True, help="Метод преобразования")
    arg_parser.add_argument("--gamma", type=float, default=1.0, help="Значение гаммы для --method gamma")
    arg_parser.add_argument("--save-hist", help="Необязательный путь для сохранения 256-корзинной гистограммы (txt/csv/json/bin/wav)")
    arg_parser.add_argument("--load-hist", help="Необязательный путь для загрузки 256-корзинной гистограммы (txt/csv/json/bin/wav). Не требуется для преобразований, только для изучения/демонстрации.")
    return arg_parser.parse_args(cli_args)


def main_func(cli_args=None):
    params = parse_arguments(cli_args)

    input_visual = _read_visual_data(params.input)

    if params.load_hist:
        _ = load_histogram_data(params.load_hist)  

    if params.method == "equalize":
        output_visual = perform_histogram_equalization(input_visual)
    elif params.method == "gamma":
        output_visual = apply_gamma_correction(input_visual, params.gamma)
    else:
        raise ValueError("Неизвестный метод")

    if params.save_hist:
        save_histogram_data(params.save_hist, calculate_intensity_histogram(output_visual))

    _write_visual_data(params.output, output_visual)


if __name__ == "__main__":
    try:
        main_func()
    except Exception as error_message:
        print(f"Ошибка: {error_message}", file=sys.stderr)

        sys.exit(1)
