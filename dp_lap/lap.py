import numpy as np

def lapAddNoise(list,sensitivity,privacy_budget):
    laplace_noise = np.random.laplace(0, sensitivity/privacy_budget, len(list))
    return laplace_noise + list