import os
import numpy as np


def get_lrt_folder():
    user_location = os.path.expanduser('~/.pylrtrc')
    try:
        with open(user_location, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError('No default location for LibRadTran found. Place the path in ~/.pylrtrc.')


def planck_function(temperature, wavelength=None, frequency=None, wavenumber=None):
    '''Supply one of wavelength in m, frequency in Hz, wavenumber in m-1'''
    import scipy.constants
    h = scipy.constants.h
    c = scipy.constants.c
    kb = scipy.constants.Boltzmann
    if wavelength is not None:
        return ((2*h*c**2)/(wavelength**5))*(1/(np.exp(h*c/(kb*temperature*wavelength))-1))
    elif frequency is not None:
        return ((2*h*frequency**3)/(c**2))*(1/(np.exp(h*frequency/(kb*temperature))-1))
    elif wavenumber is not None:
        return ((2*h*c**2*wavenumber**3))*(1/(np.exp(h*c*wavenumber/(kb*temperature))-1))


def brightness_temperature(radiance, wavelength=None, frequency=None, wavenumber=None):
    '''Supply one of wavelength in m, frequency in Hz, wavenumber in m-1'''
    import scipy.constants
    h = scipy.constants.h
    c = scipy.constants.c
    kb = scipy.constants.Boltzmann
    if wavelength is not None:
        return ((h*c)/(kb*wavelength))/(np.log(1+(2*h*c**2)/(radiance*wavelength**5)))
    elif frequency is not None:
        return ((h*frequency)/(kb))/(np.log(1+(2*h*frequency**3)/(radiance*c**2)))
    elif wavenumber is not None:
        return ((h*c*wavenumber)/(kb))/(np.log(1+(2*h*c*frequency**3)/(radiance)))
