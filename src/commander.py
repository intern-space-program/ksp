'''
Filename: commander.py
Programmed by: Mike Bernard
Date: 2020-06-25

Description: The main file that controls event sequences
and delegates control to submodules for different phases
of the mission.
'''


import krpc
import sys
from src.util.commander.constants import SMOOTH_FLYING, COMMANDER_ERROR
from src.param import Param
from src.sequence_controllers import (
    sc_00_COM_ES1_mission_setup,
    sc_01_AE_ES1_kerbin_ascent,
    sc_02_ORBIT_ES1_trans_lunar_injection,
    sc_03_RPOD_ES1_orion_gateway_rpod,
    sc_04_RPOD_ES2_hls_gateway_separation
    # TODO: add more sequence controllers as they get defined
)


def main(param):
    ''' This function commands the entire mission. '''
    # mission setup
    param = sc_00_COM_ES1_mission_setup.main(param)
    if param.status != SMOOTH_FLYING:
        print('Something went wrong with initializing the connection.')
        sys.exit(1)

    # Kerbin ascent

    # Trans-Lunar Injection

    # Orion-Gateway RPOD

    # HLS-Gateway separation

    # HLS deorbit

    # HLS landing

    # HLS ascent and tug rendezvous

    # HLS-Tug RPOD

    # HLS-Gateway intercept

    # HLS-Gateway RPOD

    # Orion-Gateway separation

    # Trans-Kerbin Injection

    # Kerbin re-entry and splashdown

    print('Thanks for flying with us.\nY\'all come back now, y\'hear!')
    return param


if __name__ == '__main__':
    param = Param()
    main(param)
    sys.exit(0)
