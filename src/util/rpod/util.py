'''
Filename: util.py
Programmed by: Mike Bernard
Date: 2020-07-21

Description: Utility functions for docking two vessels.
'''


# external library imports
import numpy as np
from time import sleep, time

# internal imports
from src.util import constants
from src.util.rpod.constants import pull, push


def get_vector(obj1, obj2):
    ''' Get the vector from obj1 to obj2. '''
    return obj2.position(obj1.reference_frame)


def hold_until(cond, max_time=constants.TIME_LIMIT_1_MIN, updates=[]):
    '''
    Hold until cond is True. Timeout if time elapsed exceeds max_time (s).
    If something should be updated each iteration of the hold loop, do it.
    '''

    status = constants.SUCCESS

    if not cond():
        timeout = False
        time_start = time()
        while not cond() and not timeout:
            if updates != []:
                for update in updates:
                    update()
            timeout = time()-time_start > max_time

        if timeout:
            raise TimeoutError

    return status


def point_at_target(ctl, tgt, away=False, intervector=None, how=None, suppress=False):
    ''' Point the active vessel's controlling part (ctl) at the target. '''
    status = constants.SUCCESS

    if not suppress:
        if not away:
            print('Attitude maneuver: pointing toward target... ', end='')
        else:
            print('Attitude maneuver: pointing away from target... ', end='')

    try:
        ctl.auto_pilot.engage()

        r_ctl_in_tgt = np.array(ctl.position(tgt.reference_frame))
        ctl.auto_pilot.reference_frame = tgt.reference_frame

        if away:
            # point away from target
            target_direction = np.array(ctl.velocity(tgt.reference_frame))

        else:
            target_direction = r_ctl_in_tgt

        target_direction /= np.linalg.norm(target_direction)

        if intervector is not None:
            # close gap between intervector and target vector
            if how == pull:
                vec = intervector() / np.linalg.norm(intervector())
                target_direction = 0.5 * (target_direction + vec)
            elif how == push:
                vec = intervector() / np.linalg.norm(intervector())
                ang = np.arccos(np.dot(target_direction, vec))
                ang *= 2
                rotvec = np.cross(target_direction, vec)
                v = target_direction
                target_direction = v*np.cos(ang) + np.cross(v, rotvec)*np.sin(ang) + rotvec*np.dot(rotvec, v)*(1-np.cos(ang))

        ctl.auto_pilot.target_direction = -1.0 * target_direction
        ctl.auto_pilot.wait()

        if not suppress:
            print('done.')

    except:
        if not suppress:
            print('FAILED.')
        status = constants.ERROR_GENERAL

    return status


def close_the_gap(ctl, tgt, speed=10.0, twr=0.25, dist=100.0):
    '''
    Do two burns to close the gap between the active vessel and the target vessel.
    :param ctl: `Vessel` the active vessel
    :param tgt: `Vessel` the target vessel
    :param speed: `float` (m/s) the desired approach speed
    :param twr: `float` (--) the desired thrust-to-weight ratio of the burns
    :param dist: `float` (m) the target distance from the target
    '''
    status = constants.SUCCESS
    point_at_target(ctl, tgt)

    if status == constants.SUCCESS:
        try:
            print('Burn: burning toward target... ', end='')
            thrust = twr * ctl.mass * constants.SURFACE_GRAVITY['Kerbin']
            throttle = thrust / ctl.available_thrust
            ctl.control.throttle = throttle
            status = hold_until(
                cond=lambda: np.linalg.norm(ctl.velocity(tgt.reference_frame)) >= speed,
                updates=[lambda: point_at_target(ctl, tgt, intervector=lambda: ctl.flight().velocity(tgt.reference_frame), how=pull, suppress=True)]
            )
            ctl.control.throttle = 0.0
            print('done.')

            point_at_target(ctl, tgt, away=True)

            print('Hold: approaching target... ', end='')
            v_ctl_wrt_tgt_in_tgt = ctl.velocity(tgt.reference_frame)  # relative velocity wrt target
            s_ctl_wrt_tgt_in_tgt = np.linalg.norm(v_ctl_wrt_tgt_in_tgt)  # relative speed wrt target
            a = thrust/ctl.mass  # approximately constant deceleration rate
            dt_burn = s_ctl_wrt_tgt_in_tgt/a  # burn time
            dr_burn = 0.5 * s_ctl_wrt_tgt_in_tgt * dt_burn  # distance covered during burn
            status = hold_until(
                cond=lambda: np.linalg.norm(ctl.position(tgt.reference_frame)) <= dist+dr_burn,
                updates=[lambda: point_at_target(ctl, tgt, away=True, suppress=True)]
            )
            print('done.')

            print('Burn: killing relative velocity... ', end='')
            point_at_target(ctl, tgt, away=True, suppress=True)
            thrust = twr * ctl.mass * constants.SURFACE_GRAVITY['Kerbin']
            ctl.control.throttle = thrust / ctl.available_thrust
            status = hold_until(
                # the following condition fails if the twr is too high (can't check in time)
                cond=lambda: -0.1 <= np.linalg.norm(ctl.velocity(tgt.reference_frame)) <= 0.1,
                updates=[lambda: point_at_target(ctl, tgt, away=True, suppress=True)]
            )
            ctl.control.throttle = 0.0
            print('done.')

        except:
            status = constants.ERROR_GENERAL

    return status


def around_town(vessel_ctl, tgt_port):
    # TODO: translate around target bounding box until in front of correct face
    pass


def line_it_up(ctl_port, tgt_port):
    ''' Line up two docking ports, given two vessels which are already close. '''
    status = constants.SUCCESS

    vessel_ctl = ctl_port.vessel
    vessel_tgt = tgt_port.vessel

    # point anti-parallel to direction of target point
    vessel_ctl.auto_pilot.engage()
    vessel_ctl.auto_pilot.reference_frame = vessel_tgt.orbit.body.non_rotating_reference_frame
    vessel_ctl.auto_pilot.target_direction = -1 * np.array(tgt_port.direction(vessel_tgt.orbit.body.non_rotating_reference_frame))
    vessel_ctl.auto_pilot.wait()

    # TODO: kill off translational error

    return status


def touch_the_butt(ctl_port, tgt_port):
    # TODO: approach and dock to target port
    pass
