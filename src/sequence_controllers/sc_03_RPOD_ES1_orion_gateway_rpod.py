# external library imports
import krpc
import numpy as np
from time import sleep, time

# internal imports
from src.util import constants
from src.util.rpod.util import close_the_gap, around_town, line_it_up, touch_the_butt
from src.param import Param


def main(param):
    # noinspection PyBroadException
    try:
        # load in parameters
        conn = param.conn
        vessel_ctl = param.ships['orion']
        vessel_tgt = param.ships['gateway']
        kerbin = param.bodies['kerbin']
        mun = param.bodies['mun']

        # set control from Orion docking port
        vessel_ctl.parts.controlling = vessel_ctl.parts.with_tag('dockingPortOrion')[0]
        ctl_port = vessel_ctl.parts.with_tag('dockingPortOrion')[0].docking_port

        # set target to Gateway docking port
        tgt_port = vessel_tgt.parts.with_tag('dockingPortGatewayForOrion')[0].docking_port
        conn.space_center.target_vessel = vessel_tgt
        conn.space_center.target_docking_port = tgt_port

        close_the_gap(vessel_ctl, vessel_tgt, twr=0.1)  # get the vehicles close together
        around_town(vessel_ctl, tgt_port)  # translate around target until on side of target port
        line_it_up(ctl_port, tgt_port)  # kill off translational error with target port
        touch_the_butt(ctl_port, tgt_port)  # approach and dock to target port

        # TODO: set new ships in param

        # set success code
        param.status = constants.SUCCESS

    except TimeoutError:
        param.status = constants.ERROR_OUT_OF_TIME

    # except:
    #     param.status = constants.ERROR_GENERAL

    return param


if __name__ == '__main__':
    # this is for testing only
    param = Param()
    param.conn = krpc.connect(name='Orion')
    param.ships = {
        'orion': param.conn.space_center.vessels[1],
        'gateway': param.conn.space_center.vessels[0]
    }
    param.bodies = {
        'kerbin': param.conn.space_center.bodies['Kerbin'],
        'mun': param.conn.space_center.bodies['Mun']
    }
    param.status = constants.SUCCESS

    ret = main(param)
    print('exit status:', ret.status)
