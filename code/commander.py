'''
Filename: commander.py
Programmed by: Mike Bernard
Date: 2020-06-25

Description: The main file that controls event sequences
and delegates control to submodules for different phases
of the mission.
'''


import krpc
from code.param import Param
from code.sequence_controllers import (
    sc_00_COM_ES1_mission_setup,
    sc_01_AE_ES1_kerbin_ascent,
    sc_02_ORBIT_ES1_trans_lunar_injection,
    sc_03_RPOD_ES1_orion_gateway_rpod,
    sc_04_RPOD_ES2_hls_gateway_separation
    # TODO: add more sequence controllers as they get defined
)


def main():
    ''' This function commands the entire mission. '''
    # mission setup
    param = Param()
    param = sc_00_COM_ES1_mission_setup.main(param)

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

    pass


if __name__ == '__main__':
    main()
