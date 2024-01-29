import numpy as np
import matplotlib.pyplot as plt

np.warnings.filterwarnings("ignore")

def complex_matrix(x_i, x_o, y_i, y_o, number_pixel):
    re = np.linspace(x_i, x_o, int((x_o-x_i)*number_pixel))
    im = np.linspace(y_i, y_o, int((y_o-y_i)*number_pixel))
    return re[np.newaxis, :] + im[:, np.newaxis] * 1j

def is_stable(c, num_iterat):
    z = 0
    for i in range(num_iterat):
        z = z **2 + c
    return abs(z) <= 2


def get_members(c, num_iterations):

    mask = is_stable(c, num_iterations)

    return c[mask]


c = complex_matrix(-2, 0.5, -1.5, 1.5, number_pixel=121)
members = get_members(c, num_iterations=20)


plt.scatter(members.real, members.imag, color="black", marker=",", s=1)

plt.gca().set_aspect("equal")

plt.axis("off")

plt.tight_layout()

plt.show()
