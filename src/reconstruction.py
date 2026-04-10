from skimage.transform import iradon

def fbp_reconstruction(sinogram, angles, filter_type='ramp'):
    return iradon(sinogram, theta=angles, filter_name=filter_type)
