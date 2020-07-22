# external library imports
import krpc
import numpy as np
from time import sleep, time

# internal imports
from src.util import constants
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
        target = vessel_tgt.parts.with_tag('dockingPortGatewayForOrion')[0].docking_port
        conn.space_center.target_vessel = vessel_tgt
        conn.space_center.target_docking_port = target

        # attitude maneuver to point at Gateway
        vessel_ctl.auto_pilot.target_direction = \
            np.array(target.position(mun.non_rotating_reference_frame)) \
            - np.array(vessel_ctl.position(mun.non_rotating_reference_frame))

        vessel_ctl.auto_pilot.reference_frame = mun.non_rotating_reference_frame

        vessel_ctl.auto_pilot.engage()

        time_start = time()
        timeout = False

        attitude_tolerance = 1.0  # (degrees)
        attitude_rate_tolerance = 0.01  # (radians/second)

        attitude_pass = vessel_ctl.auto_pilot.error < attitude_tolerance
        attitude_rate_pass = np.linalg.norm(vessel_ctl.angular_velocity(mun.non_rotating_reference_frame)) < attitude_rate_tolerance

        while not(attitude_pass and attitude_rate_pass) and not timeout:
            attitude_pass = vessel_ctl.auto_pilot.error < attitude_tolerance
            attitude_rate_pass = np.linalg.norm(vessel_ctl.angular_velocity(mun.non_rotating_reference_frame)) < attitude_rate_tolerance

            sleep(0.1)  # limit processing rate
            timeout = time()-time_start > constants.TIME_LIMIT_1_MIN

        if timeout:
            raise TimeoutError

        vessel_ctl.auto_pilot.sas_mode = conn.space_center.SASMode.target

        # OMS approach burn
        tgt_twr = 0.1
        tgt_thrust = tgt_twr * vessel_ctl.mass * kerbin.surface_gravity
        vessel_ctl.control.throttle = tgt_thrust / vessel_ctl.available_thrust

        time_start = time()
        timeout = False
        burn_done = False
        while not burn_done and not timeout:
            if vessel_ctl.flight(target.reference_frame).speed >= 10.0:
                vessel_ctl.control.throttle = 0.0
                burn_done = True
            elif time()-time_start > constants.TIME_LIMIT_1_MIN:
                timeout = True

        if timeout:
            raise TimeoutError

        # stop at boundary sphere (OMS stop burn)
        time_start = time()
        timeout = False
        within_boundary_box = False
        while not within_boundary_box and not timeout:
            sleep(0.1)
            within_boundary_box = np.linalg.norm(vessel_ctl.position(target.reference_frame)) < 200.0
            timeout = time()-time_start > constants.TIME_LIMIT_1_MIN

        if timeout:
            raise TimeoutError

        vessel_ctl.auto_pilot.target_direction = -1 * (
            np.array(target.position(mun.non_rotating_reference_frame))
            - np.array(vessel_ctl.position(mun.non_rotating_reference_frame))
        )

        time_start = time()
        timeout = False

        attitude_pass = vessel_ctl.auto_pilot.error < attitude_tolerance
        attitude_rate_pass = np.linalg.norm(vessel_ctl.angular_velocity(mun.non_rotating_reference_frame)) < attitude_rate_tolerance

        while not(attitude_pass and attitude_rate_pass) and not timeout:
            attitude_pass = vessel_ctl.auto_pilot.error < attitude_tolerance
            attitude_rate_pass = np.linalg.norm(vessel_ctl.angular_velocity(mun.non_rotating_reference_frame)) < attitude_rate_tolerance

            sleep(0.1)  # limit processing rate
            timeout = time()-time_start > constants.TIME_LIMIT_1_MIN

        if timeout:
            raise TimeoutError

        vessel_ctl.auto_pilot.sas_mode = conn.space_center.SASMode.anti_target

        tgt_twr = 0.1
        tgt_thrust = tgt_twr * vessel_ctl.mass * kerbin.surface_gravity
        vessel_ctl.control.throttle = tgt_thrust / vessel_ctl.available_thrust

        time_start = time()
        timeout = False
        burn_done = False
        while not burn_done and not timeout:
            if vessel_ctl.flight(target.reference_frame).speed <= 1.0:
                vessel_ctl.control.throttle = 0.0
                burn_done = True
            elif time()-time_start > constants.TIME_LIMIT_1_MIN:
                timeout = True

        if timeout:
            print('here')
            raise TimeoutError


        # translational maneuver around gateway to line up with docking port


        # attitude maneuver to point at target docking port


        # RCS approach burn


        # docking


        # set new ships in param


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
