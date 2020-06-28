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


def check_status(status):
    ''' Reacts to various param status messages. '''
    ret = 0

    # this conditional ladder may be expanded for fine-grain debugging
    if status != SMOOTH_FLYING:
        ret = 1

    return ret


def main(param):
    ''' This function commands the entire mission. '''
    event_sequence_mains = (
        sc_00_COM_ES1_mission_setup,
        # sc_01_AE_ES1_kerbin_ascent,
        # sc_02_ORBIT_ES1_trans_lunar_injection,
        # sc_03_RPOD_ES1_orion_gateway_rpod,
        # sc_04_RPOD_ES2_hls_gateway_separation
    )

    for controller in event_sequence_mains:
        param = controller.main(param)
        ex = check_status(param.status)
        if ex:
            break
        else:
            continue

    print('Thanks for flying with us.\nY\'all come back now, y\'hear!')
    return param


if __name__ == '__main__':
    param = Param()
    param = main(param)
    sys.exit(0)
