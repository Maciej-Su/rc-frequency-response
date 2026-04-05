from bode_plot import plot_bode, plot_R_variation, plot_C_variation

R = 1000      # Ω
C = 1e-6      # F

# Bode
plot_bode(R, C)

# Analysis
plot_R_variation(C)
plot_C_variation(R)