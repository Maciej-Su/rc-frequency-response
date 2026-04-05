import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from transfer_function import transfer_function

# Initial Params
R_init = 1000
C_init = 1e-6
omega = np.logspace(1, 6, 800)

# Computation
def compute(R, C):
    T = transfer_function(omega, R, C)
    mag = 20 * np.log10(np.abs(T))
    phase = np.angle(T, deg=True)
    omega_c = 1 / (R * C)
    return mag, phase, omega_c

mag, phase, omega_c = compute(R_init, C_init)

# Canvas
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
plt.subplots_adjust(bottom=0.25, hspace=0.35)

# M
line_mag, = ax1.semilogx(omega, mag, label="Magnitude", lw=1.5)
# Note: Use list [omega_c, omega_c] to ensure it updates as a vertical segment
vline_mag, = ax1.plot([omega_c, omega_c], [-100, 10], 'r--', alpha=0.6, label="Cutoff")
point_mag, = ax1.plot([omega_c], [-3], 'ro')  # Cutoff point at -3dB

ax1.set_ylabel("Magnitude (dB)")
ax1.set_title("Interactive Bode Plot (RC Low-pass)")
ax1.set_ylim(-60, 5) # Fixed limits prevent "jumping" during interaction
ax1.grid(True, which="both", linestyle="--", alpha=0.5)
ax1.legend(loc='lower left')

# P
line_phase, = ax2.semilogx(omega, phase, label="Phase", lw=1.5, color='orange')
vline_phase, = ax2.plot([omega_c, omega_c], [-100, 10], 'r--', alpha=0.6)
point_phase, = ax2.plot([omega_c], [-45], 'ro') # Cutoff point at -45 deg

ax2.set_xlabel("Frequency (rad/s)")
ax2.set_ylabel("Phase (deg)")
ax2.set_ylim(-100, 10)
ax2.grid(True, which="both", linestyle="--", alpha=0.5)
ax2.legend(loc='lower left')

# Sliders
ax_R = plt.axes([0.2, 0.1, 0.6, 0.03])
slider_R = Slider(ax_R, "R (Ohm)", 100, 10000, valinit=R_init, valfmt='%1.0f')

ax_C = plt.axes([0.2, 0.05, 0.6, 0.03])
slider_C = Slider(ax_C, "C (F)", 1e-8, 1e-5, valinit=C_init, valfmt='%.1e')

# Update Function
def update(val):
    # Get current slider values
    R = slider_R.val
    C = slider_C.val

    # Recalculate data
    mag, phase, omega_c = compute(R, C)

    # Update main curves
    line_mag.set_ydata(mag)
    line_phase.set_ydata(phase)

    # Update vertical lines (X-coordinates must be updated as a list)
    vline_mag.set_xdata([omega_c, omega_c])
    vline_phase.set_xdata([omega_c, omega_c])

    # Update markers (set_data requires x and y as sequences)
    point_mag.set_data([omega_c], [-3])
    point_phase.set_data([omega_c], [-45])

    # Redraw the figure
    fig.canvas.draw_idle()

# ===== 绑定事件 (Event Binding) =====
slider_R.on_changed(update)
slider_C.on_changed(update)

plt.show()
