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
---

## Experimental Results

Two configurations were tested to validate the theoretical model:

### Configuration 1 (R = 5100 Ω, C = 47 nF)

![Magnitude](comparison1_mf.png)

![Phase](comparison1_pf.png)

### Configuration 2 (R = 1000 Ω, C = 220 nF)

![Magnitude](comparison2_mf.png)

![Phase](comparison2_pf.png)

---

## Discussion

The experimental results are consistent with the theoretical predictions of the RC low-pass filter.

For both configurations:

- The magnitude remains close to 0 dB at low frequencies  
- The magnitude decreases as frequency increases  
- The phase shifts gradually from 0° toward -90°  

The cutoff frequency can be identified near the point where:

- Magnitude ≈ -3 dB  
- Phase ≈ -45°  

Although the cutoff point is not explicitly marked in all figures, it can be inferred from the trend of the curves.

A strong agreement between theoretical (simulation) and experimental results is observed:

- The overall shape of the Bode plots is consistent  
- The slope in the high-frequency region approaches -20 dB/decade  
- The phase transition region aligns with theoretical expectations  

Minor deviations are observed, especially at higher frequencies. These can be attributed to:

- Component tolerances (resistor and capacitor inaccuracies)  
- Measurement limitations  
- Non-ideal effects (e.g., parasitic resistance or capacitance)  

---

## Conclusion

This project presents a complete analysis of the frequency response of an RC low-pass filter through theoretical derivation, simulation, and experimental validation.

The theoretical model accurately predicts the system behavior:

- Constant gain at low frequencies  
- Attenuation at high frequencies  
- Phase shift from 0° to -90°  

Simulation results generated using Python successfully reproduce the expected Bode characteristics.

Experimental data confirms these predictions, demonstrating strong agreement with the theoretical and simulated results.

The addition of an interactive visualization tool further enhances understanding by allowing real-time adjustment of parameters (R and C) and observing their influence on the system.

Overall, the consistency between theory, simulation, and experiment validates the RC low-pass filter model and demonstrates the effectiveness of combining analytical and computational approaches.

---

## How to Run

Run main simulation:


python code/main.py

Interactive Visualization (Advanced Feature)

An interactive simulation tool is implemented using sliders to dynamically adjust R and C.

This allows:

- Real-time observation of Bode plot changes
- Visualization of cutoff frequency shift
- Direct verification of ωc = 1 / (RC)

Run:

```bash
python code/interactive_plot.py

