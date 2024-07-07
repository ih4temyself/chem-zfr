import numpy as np


torsion_angles = np.array([15.6, 1, 11.8, -40.8, 57, -41.9]) 

torsion_angles_rad = np.radians(torsion_angles)

sin_half_torsion_angles = np.sin(torsion_angles_rad / 2)

N = len(torsion_angles)
m = 1 

sm_cos_psi_m = -(2 / N) ** 0.5 * np.sum(sin_half_torsion_angles * np.sin(np.pi * m * (2 * np.arange(1, N+1) + 1) / N))

sm_sin_psi_m = -(2 / N) ** 0.5 * np.sum(sin_half_torsion_angles * np.cos(np.pi * m * (2 * np.arange(1, N+1) + 1) / N))

S_square = np.sum(np.sin(torsion_angles_rad / 2) ** 2)
S = np.sqrt(S_square)



print(f"sm cos(Ψm): {sm_cos_psi_m}")
print(f"sm sin(Ψm): {sm_sin_psi_m}")
print(f"S^2: {S_square}")
print(f"S: {S}")

