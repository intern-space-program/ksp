'''
Filename: sc_00_COM_ES1_mission_setup.py
Programmed by: Mike Bernard
Date: 2020-06-27

Description: Sets up all the relevant mission data, including
celestial bodies, reference frames, vessels, and named parts.
'''


import krpc
from code.util.commander.constants import *


def main(param):
    status = SMOOTH_FLYING

    # noinspection PyBroadException
    try:
        # establish connection
        conn = krpc.connect(name='Artemis 3')

        # TODO: load celestial bodies
        for name, obj in conn.space_center.bodies.items():
            if name == 'Kerbin':
                kerbin = obj
            elif name == 'Mun':
                mun = obj

        # TODO: load reference frames
        kerbin_nrrf = kerbin.non_rotating_reference_frame

        # TODO: load vessels
        orion = conn.space_center.active_vessel

        # TODO: load named parts (i.e. docking ports)

        # TODO: set all loaded objects to param
        param.conn = conn
        param.orion = orion

        param.kerbin = kerbin
        param.mun = mun

        param.kerbin_nrrf = kerbin_nrrf

    except:
        status = COMMANDER_ERROR

    # set status
    param.status = status

    return param
