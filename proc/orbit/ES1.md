# Orbit Event Sequence 1
## Orion Performs TLI and Rendezvouses with Gateway 

**Starting Assumptions**
- Orion docked to ICPS
- Orion & ICPS in low Kerbin orbit
- Orbit description:
  - 100 km apoapsis [100 m]
  - 100 km periapsis [100 m]
  - 0 degrees inclination [0.1 degrees]
- Circular orbit velocity: 2.246 km/s 
- Position vector at TLI: 700 km (R0)
- Distance from center of Kerbin to edge of Mun's sphere of influence: 9570440.9 m (R1)
- Position vector to Mun's sphere of influence relative to Mun: 2429559.1 m (R2)
- Mun's orbital velocity: 543 m/s (V<sub>m</sub>) 
- Kerbin's gravitational parameter: 3.5316 * 10<sup>12</sup> m<sup>3</sup> / s<sup>2</sup>
- delta V = V1 - V0



**BEGIN ORBIT EVENT SEQUENCE 1**

1. Determine position of maneuver node for Trans-Lunar Injection burn
2. Determine delta V and direction for Trans-Lunar Injection burn
3. Perform Trans-Lunar Injection burn
  *TODO: duration of burn*
  - Fire ICPS
  - Approximately 800-900 m/s delta V required (Vis-viva equation)
4. Separate ICPS from Orion
5. Determine time of flight to Mun sphere of influence
  - Determine period of transfer orbit
  - Kerbin's gravitational parameter: 3.5316 * 10^12 m^3/s^2
  - Determine semi-major axis of transfer orbit
  - Calculate 
6. Perform OTC (outbound trajectory correction) after crossing into Mun sphere of influence
  *TODO: duration of burn*
  - Initial estimate to target
  TODO: determine range in which to perform OTC
7. Gateway orbit insertion burn
  *TODO: duration of burn*
  // Attitude maneuver?
  // Main engine burn (thrust, velocity)
  // What distance away from Gateway?
  - Hand over between 100 m - 1 km in matching orbit with Gateway

**END ORBIT EVENT SEQUENCE 1**
