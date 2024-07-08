import numpy as np


def main(torsion_angles):
    N = 6
    M = (N - 1) // 2

    torsion_angles_rad = np.radians(torsion_angles)
    sin_half_torsion_angles = np.sin(torsion_angles_rad / 2)

    psi_deg = psi_calcs(sin_half_torsion_angles, N, M)
    S = s_calcs(torsion_angles_rad)
    theta_deg = theta_calcs(sin_half_torsion_angles, S, N)
    return (
        S,
        theta_deg,
        abs(psi_deg),
    )


def psi_calcs(sin_half_torsion_angles, N, M):
    sm_cos_psi_m = -((2 / N) ** 0.5) * np.sum(
        sin_half_torsion_angles * np.sin(np.pi * M * (2 * np.arange(1, N + 1) + 1) / N)
    )
    sm_sin_psi_m = -((2 / N) ** 0.5) * np.sum(
        sin_half_torsion_angles * np.cos(np.pi * M * (2 * np.arange(1, N + 1) + 1) / N)
    )

    psi = np.arctan2(sm_sin_psi_m, sm_cos_psi_m)

    # adjust Psi if necessary
    while psi > np.pi / 3:
        psi -= np.pi / 3
    while psi < -np.pi / 3:
        psi += np.pi / 3

    # convert Psi to degrees
    psi_deg = np.degrees(psi)

    return psi_deg


def s_calcs(torsion_angles_rad):
    S_square = np.sum(np.sin(torsion_angles_rad / 2) ** 2)
    S = np.sqrt(S_square)
    return S


def theta_calcs(sin_half_torsion_angles, S, N):
    sm3 = ((N - 1) / 2) ** 0.5 * np.sum(
        sin_half_torsion_angles * np.cos(np.pi * (np.arange(1, N + 1) - 1) / N)
    )

    theta = np.arctan2(S, sm3)
    theta_deg = abs(np.degrees(theta))
    theta_deg = round(theta_deg, 2)

    return theta_deg


if __name__ == "__main__":
    test_cases = [
        np.array([8, -15.3, 40.8, -59, 49.4, -26]),
        np.array([-24.6, 5.6, -11.8, 37.4, -58, 51.1]),
        np.array([15.6, 1, 11.8, -40.8, 57, -41.9]),
        np.array([55.7, -53, 54, -57.2, 60, -59.8]),
        np.array([-53.2, 31.6, -1.6, -5.1, -18.7, 47]),
        np.array([59.1, -34.2, 4.4, 1.4, 22.8, -51.8]),
        np.array([28.2, -26.6, 6.7, 14.8, -13.1, -10]),
    ]
    for test in test_cases:
        result = main(test)
        print(result)
