"""
    Script for the EE671 Assignment 1.
    This script is used for easy changing of NMOS and PMOS widths, lengths and areas with a singe variable change
    rather than retyping.

    Usage:
    run in terminal
    python3 <file_name>.py > inverter.spice

    Example:
    python3 EE671_A1_inverter.py > inverter.spice
"""

## All Lengths are in micro meters(um)
wn = 0.42
ln = 0.15
wp = 3*0.42  #Change 3 to the amount you want
lp = 0.15

## Calculated values

##NMOS
asn = 2*wn*ln ##Source Area
adn = 2*wn*ln ##Drain Area
psn = 2*(wn + 2*ln) ##Source Perimeter
pdn = 2*(wn + 2*ln) ##Drain Perimeter

##PMOS
asp = 2*wp*lp ##Source Area
adp = 2*wp*lp ##Drain Area
psp = 2*(wp + 2*lp) ##Source Perimeter
pdp = 2*(wp + 2*lp) ##Drain Perimeter

string = f"""
* Skywater PDK Simple Inverter Testbench
* Geometric Formulas:
* as = W * 2 * L
* ad = W * 2 * L
* ps = 2 * (W + 2 * L)
* pd = 2 * (W + 2 * L)

.lib /foss/pdks/sky130A/libs.tech/ngspice/sky130.lib.spice tt

.subckt not1 a vdd vss z
xm01 z a vdd vdd sky130_fd_pr__pfet_01v8 l={lp} w={wp} as={asp} ad={adp} ps={psp} pd={pdp}
xm02 z a vss vss sky130_fd_pr__nfet_01v8 l={ln} w={wn} as={asn} ad={adn} ps={psn} pd={pdn}
c3 a vss 0.385f
c2 z vss 0.576f
.ends

* the voltage source:
Vdd vdd gnd DC 1.8
Xnot1 in vdd gnd out not1

* dc analysis
V1 in 0 DC 0
.dc V1 0 1.8 0.01

.control
run
plot V(in) V(out)
let slope=deriv(V(out))
plot slope
.endc
.end
"""

print(string)