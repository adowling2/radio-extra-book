"""Feed-line attenuation versus frequency, showing the two terms of

    alpha ~ R'/(2 Z0) + G' Z0 / 2

separately. Skin effect makes the conductor term go as sqrt(f); dielectric
leakage makes the second term go as f. The point of the figure is the difference
in SLOPE on log-log axes (1/2 versus 1), and that ordinary coax sits in the
conductor-dominated regime across the amateur bands.

Curves are the two-term model
    loss(dB per 100 ft) = k_c * sqrt(f_MHz) + k_d * f_MHz
with the pair (k_c, k_d) fitted to the two representative figures quoted in the
book's table (RG-58 ~1.5 and ~5 dB per 100 ft at 14 and 144 MHz; RG-213 ~0.6 and
~2 dB). Illustrative, not a substitute for a data sheet -- and note that two
points in the conductor-dominated regime pin k_c well but constrain k_d only
loosely, which is why no crossover frequency is claimed here.
"""
import numpy as np
import matplotlib.pyplot as plt
from _style import apply_style, save, GUIDE_BLUE, GUIDE_GREEN, GUIDE_AMBER, GUIDE_LINE

apply_style()

f = np.logspace(0, 3.5, 600)          # 1 MHz to ~3 GHz


def fit(f1, l1, f2, l2):
    """Solve k_c*sqrt(f) + k_d*f = loss at two frequencies."""
    A = np.array([[np.sqrt(f1), f1], [np.sqrt(f2), f2]])
    return np.linalg.solve(A, np.array([l1, l2]))


kc_58, kd_58 = fit(14.0, 1.5, 144.0, 5.0)
kc_213, kd_213 = fit(14.0, 0.6, 144.0, 2.0)

fig, (ax, ax2) = plt.subplots(1, 2, figsize=(6.4, 3.0))

# ---- left: the two mechanisms, separated ----
cond = kc_58 * np.sqrt(f)
diel = kd_58 * f
ax.loglog(f, cond + diel, color=GUIDE_BLUE, lw=2.0, label="total")
ax.loglog(f, cond, color=GUIDE_GREEN, lw=1.3, ls="--",
          label=r"conductor $\propto\sqrt{f}$")
ax.loglog(f, diel, color=GUIDE_AMBER, lw=1.3, ls=":",
          label=r"dielectric $\propto f$")
# The two mechanisms are named in the legend and explained in the caption; the
# panel is too narrow for sentence-length annotations, so only the amateur-band
# span is marked here.
ax.axvspan(1.8, 450, color=GUIDE_LINE, alpha=0.10, lw=0)
ax.annotate("amateur bands", xy=(28, 0.033), fontsize=7.5, color="0.40",
            ha="center", va="bottom")
ax.set_xlabel("Frequency (MHz)")
ax.set_ylabel("Loss (dB per 100 ft)")
ax.set_title("Two loss mechanisms (RG-58)", fontsize=9)
ax.set_ylim(0.02, 200)
ax.legend(loc="upper left", fontsize=7.5)

# ---- right: two cables, with the book's table points marked ----
for kc, kd, name, col in ((kc_58, kd_58, "RG-58", GUIDE_BLUE),
                          (kc_213, kd_213, "RG-213", GUIDE_GREEN)):
    ax2.loglog(f, kc * np.sqrt(f) + kd * f, color=col, lw=2.0, label=name)

for fx, ly, col in ((14, 1.5, GUIDE_BLUE), (144, 5.0, GUIDE_BLUE),
                    (14, 0.6, GUIDE_GREEN), (144, 2.0, GUIDE_GREEN)):
    ax2.plot(fx, ly, "o", color=col, ms=4.5, zorder=6)

# the sqrt(f) check the worked example makes
ax2.plot([14, 144], [0.6, 0.6], color=GUIDE_LINE, lw=0.7, ls="-")
ax2.plot([144, 144], [0.6, 2.0], color=GUIDE_LINE, lw=0.7, ls="-")
ax2.annotate(r"$\times10.3$ in $f$" "\n" r"$\times3.3$ in loss",
             xy=(45, 0.66), xytext=(20, 0.16), fontsize=7.5, color="0.35",
             ha="left")
ax2.annotate("table values", xy=(144, 5.0), xytext=(260, 1.1),
             fontsize=7.5, color="0.35",
             arrowprops=dict(arrowstyle="->", color="0.45", lw=0.7))
ax2.set_xlabel("Frequency (MHz)")
ax2.set_ylabel("Loss (dB per 100 ft)")
ax2.set_title("Bigger cable, lower loss", fontsize=9)
ax2.set_ylim(0.1, 60)
ax2.legend(loc="upper left", fontsize=7.5)

fig.tight_layout()
save(fig, "line_attenuation")
