import numpy as np

def apply_gamma_cor(img, alpha, beta):
    return np.clip(img * alpha + beta, 0, 255)