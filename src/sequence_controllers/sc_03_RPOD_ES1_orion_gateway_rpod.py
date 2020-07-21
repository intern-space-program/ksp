import numpy as np
import krpc
from src.util import constants
from src.param import Param


def main(param):

    # noinspection PyBroadException
    try:
        # load in parameters
        conn = param.conn
        vessel_ctl = param.ships['orion']
        vessel_tgt = param.ships['gateway']

        # set control from Orion docking port
        vessel_ctl.parts.controlling = vessel_ctl.parts.with_tag('dockingPortOrion')[0]

        # set target to Gateway docking port
        target = vessel_tgt.parts.with_tag('dockingPortGatewayForOrion')[0]
        conn.space_center.target_vessel = vessel_tgt
        conn.space_center.target_docking_port = target

        # attitude maneuver to point at Gateway


        # OMS approach burn


        # stop at boundary sphere (OMS stop burn)


        # set target to specific Gateway docking port


        # translational maneuver around gateway to line up with docking port


        # attitude maneuver to point at target docking port


        # RCS approach burn


        # docking


        # set new ships in param


        # set success code
        param.status = constants.SUCCESS

    except:
        param.status = constants.ERROR

    return param


if __name__ == '__main__':
    # this is for testing only
    param = Param()
    param.conn = krpc.connect(name='Orion')
    param.ships = {
        'orion': param.conn.space_center.vessels[1],
        'gateway': param.conn.space_center.vessels[0]
    }
    param.status = constants.SUCCESS

    main(param)
