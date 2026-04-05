# RC Frequency Response Analysis

This project investigates the frequency response of an RC low-pass filter using theoretical modeling, Python simulation, and experimental validation.

---

## Theory

The transfer function of the RC circuit is given by:

T(jω) = 1 / (1 + jωRC)

where:
- R is the resistance
- C is the capacitance
- ω is the angular frequency (rad/s)

The cutoff frequency is defined as:

ωc = 1 / (RC)

At this frequency:
- The magnitude drops to approximately -3 dB
- The phase shift is approximately -45°

This confirms that the circuit behaves as a first-order linear time-invariant (LTI) system with a roll-off rate of -20 dB/decade.

---

## Methods

The project consists of three main components:

- Analytical derivation of the transfer function
- Python-based simulation of Bode plots
- Experimental measurement and validation

---

## Simulation (Python)

Theoretical Bode plots were generated using Python to visualize:

- Magnitude response
- Phase response
- Influence of R and C on system behavior

### Parameter Analysis

- Increasing R shifts the cutoff frequency to lower values
- Increasing C has the same effect
- The shape of the curve remains consistent, confirming first-order behavior

---

## Interactive Visualization (Advanced Feature)

An interactive tool is implemented using Python to dynamically explore the effect of circuit parameters on the frequency response.

By adjusting the resistance (R) and capacitance (C) values using sliders, the Bode magnitude and phase plots update in real time.

This allows:

- Visualization of how the cutoff frequency shifts with changing parameters
- Direct verification of the relationship ωc = 1 / (RC)
- Better understanding of system sensitivity to parameter variations

This interactive approach extends beyond static analysis and reflects practical engineering tools used in system design.

To run the interactive tool:

```bash
python interactive_plot.py
