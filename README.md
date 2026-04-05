# RC Frequency Response Analysis

This project investigates the frequency response of an RC low-pass filter using theoretical modeling, Python simulation, and experimental validation.

---

## Overview

This project combines:

- Analytical modeling (transfer function)
- Python-based simulation (Bode plots)
- Experimental validation
- Interactive visualization (parameter tuning)

---

## Theory

The transfer function is:

T(jω) = 1 / (1 + jωRC)

Cutoff frequency:

ωc = 1 / (RC)

At cutoff:
- Magnitude ≈ -3 dB
- Phase ≈ -45°
- System behaves as a first-order LTI system
- Roll-off rate: -20 dB/decade

---

## Simulation Results (Python)

### Bode Plot
![Bode Plot](bode_te.png)

### Effect of Resistance (R)
![R Variation](bode_te_mf_R.png)

### Effect of Capacitance (C)
![C Variation](bode_te_mf_C.png)

---

## Interactive Visualization (Advanced Feature)

An interactive simulation tool is implemented using sliders to dynamically adjust R and C.

This allows:

- Real-time observation of Bode plot changes
- Visualization of cutoff frequency shift
- Direct verification of ωc = 1 / (RC)

Run:

```bash
python code/interactive_plot.py
