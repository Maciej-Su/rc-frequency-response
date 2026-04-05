import numpy as np
import matplotlib.pyplot as plt
from transfer_function import transfer_function


def plot_bode(R, C):
    omega = np.logspace(1, 6, 500)

    T = transfer_function(omega, R, C)

    magnitude = 20 * np.log10(np.abs(T))
    phase = np.angle(T, deg=True)

    omega_c = 1 / (R * C)

    plt.figure(figsize=(10, 7))

    # M
    plt.subplot(2, 1, 1)
    plt.semilogx(omega, magnitude, label="Magnitude")
    plt.axvline(omega_c, linestyle="--", color="r", label="Cutoff")

    plt.ylabel("Magnitude (dB)")
    plt.title("Bode Plot (RC Low-pass)")
    plt.grid(True, which="both")
    plt.legend()

    # P
    plt.subplot(2, 1, 2)
    plt.semilogx(omega, phase, label="Phase")
    plt.axvline(omega_c, linestyle="--", color="r")

    plt.xlabel("Frequency (rad/s)")
    plt.ylabel("Phase (deg)")
    plt.grid(True, which="both")
    plt.legend()

    plt.tight_layout()
    plt.show()


#  R
def plot_R_variation(C):
    omega = np.logspace(1, 6, 500)

    R_values = [500, 1000, 5000]

    plt.figure(figsize=(8, 5))

    for R in R_values:
        T = transfer_function(omega, R, C)
        magnitude = 20 * np.log10(np.abs(T))

        plt.semilogx(omega, magnitude, label=f"R={R}Ω")

    plt.title("Effect of R on Frequency Response")
    plt.xlabel("Frequency (rad/s)")
    plt.ylabel("Magnitude (dB)")
    plt.grid(True, which="both")
    plt.legend()

    plt.show()


#  C
def plot_C_variation(R):
    omega = np.logspace(1, 6, 500)

    C_values = [1e-7, 1e-6, 1e-5]

    plt.figure(figsize=(8, 5))

    for C in C_values:
        T = transfer_function(omega, R, C)
        magnitude = 20 * np.log10(np.abs(T))

        plt.semilogx(omega, magnitude, label=f"C={C}F")

    plt.title("Effect of C on Frequency Response")
    plt.xlabel("Frequency (rad/s)")
    plt.ylabel("Magnitude (dB)")
    plt.grid(True, which="both")
    plt.legend()

    plt.show()