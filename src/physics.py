from skimage.transform import radon

def compute_sinogram(image, angles):
    return radon(image, theta=angles)
