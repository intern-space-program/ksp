# RPOD Event Sequence 4
## HLS Approaches Gateway and Docks

**Starting Assumptions**
- HLS at least 100 m from Gateway bounding box
- HLS within 1000 m of Gateway bounding box
- HLS-Gateway relative velocity magnitude < 10 m/s

Unless otherwise specified, all actions below are done by HLS. Where a target value is given, the error is given in brackets following that value.

**BEGIN RPOD EVENT SEQUENCE 4**

1. Attitude maneuver to point toward Gateway CG.
2. Tug burn until HLS approaching Gateway at 10 m/s [1 m/s].
   - Throttle such that TWR is 0.1 for safety.
3. Attitude maneuver to point opposite from Gateway CG.
4. Wait until HLS less than 100 m from Gateway bounding box.
5. Tug burn until HLS-Gateway relative velocity at 0 m/s [0.1 m/s].
6. Calculate arc path at constant distance until HLS docking port pointing directly to Gateway's HLS docking port.
7. RCS maneuver to translate and rotate gateway along arc path determined in step 6.
   - HLS velocity to be within the range of 4 m/s to 6 m/s during this maneuver.
8. Use RCS to kill relative velocity with Gateway.
9. Set Gateway's HLS docking port as target.
10. Roll to 0 degrees [1 degree].
11. RCS thrust toward target. Relative velocity target in range of 2 m/s to 4 m/s.
12. Wait until distance from HLS docking port and target less than 20 m.
13. RCS thrust to decrease approach velocity to 0.5 m/s [0.1 m/s].
14. Wait until docked.

**END RPOD EVENT SEQUENCE 4**