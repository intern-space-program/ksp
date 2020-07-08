'''
Filename: util.py
Programmed by: Mike Bernard
Date: 2020-07-07

Description: General-use orbital mechanics utility functions.
'''


import numpy as np


def dt_burn(vessel, dv):
    '''
    Calculate the time duration of a burn assuming throttle locked to 1.0.
    :param vessel: the vessel object, with an activated engine
    :param dv: float, the delta-V of the burn
    :return: float, the burn duration in seconds
    '''
    term1 = (vessel.mass * vessel.specific_impulse * 9.81) / vessel.available_thrust
    term2 = (1-np.exp(dv/(vessel.specific_impulse*9.81)))
    return np.abs(term1*term2)
