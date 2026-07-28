"""Ground as an image antenna. A horizontal antenna at height h over conducting ground
is a two-element array with spacing 2h and the image inverted, so the array factor of
sec:arrayfactor collapses to |F| = 2|sin(beta h sin psi)|: a null at the horizon at
every height, and a first lobe at sin(psi) = lambda/4h. Raising the antenna lowers the
lobe. The right panel shows why the vertical case, whose image is NOT inverted,
behaves oppositely. See sec:groundimage."""
import numpy as np
import matplotlib.pyplot as plt
from _style import apply_style, save, GUIDE_BLUE, GUIDE_GREEN, GUIDE_AMBER, GUIDE_RED

apply_style()

psi = np.linspace(0, np.pi/2, 3000)          # elevation angle above the horizon

fig, (axh, axv) = plt.subplots(1, 2, figsize=(6.6, 2.95),
                               subplot_kw={"projection": "polar"},
                               gridspec_kw={"width_ratios": [1.35, 1]})

# ---------------- horizontal antenna: image inverted ----------------
heights = [(0.25, GUIDE_RED), (0.5, GUIDE_AMBER), (1.0, GUIDE_BLUE)]
for h, col in heights:
    F = 2*np.abs(np.sin(2*np.pi*h*np.sin(psi)))
    lobe = np.degrees(np.arcsin(min(1.0, 1/(4*h))))
    axh.plot(psi, F/2, color=col, lw=1.5,
             label=rf"$h={h:g}\lambda$   lobe at ${lobe:.0f}^\circ$")
axh.set_thetamin(0)
axh.set_thetamax(90)
axh.set_theta_zero_location("E")
axh.set_rmax(1.02)
axh.set_rticks([0.5, 1.0])
axh.set_yticklabels([])
axh.set_xticks(np.radians([0, 15, 30, 45, 60, 75, 90]))
axh.set_xticklabels([r"$0^\circ$", "", r"$30^\circ$", "", r"$60^\circ$", "",
                     r"$90^\circ$"], fontsize=8)
axh.grid(color="0.85", lw=0.4)
axh.legend(loc="upper right", bbox_to_anchor=(1.30, 1.04), fontsize=7.2)
axh.set_title("Horizontal: image inverted\n" r"$|F|=2|\sin(\beta h\sin\psi)|$",
              fontsize=8.5, pad=10)
# The horizon null is visible in every curve and is stated in the caption rather
# than annotated here, where any label would sit on top of the h = 1 lambda lobe.

# ---------------- vertical antenna: image in phase ----------------
for h, col in [(0.25, GUIDE_RED), (0.5, GUIDE_AMBER)]:
    F = 2*np.abs(np.cos(2*np.pi*h*np.sin(psi)))
    axv.plot(psi, F/2, color=col, lw=1.5, label=rf"$h={h:g}\lambda$")
axv.set_thetamin(0)
axv.set_thetamax(90)
axv.set_theta_zero_location("E")
axv.set_rmax(1.02)
axv.set_rticks([0.5, 1.0])
axv.set_yticklabels([])
axv.set_xticks(np.radians([0, 30, 60, 90]))
axv.set_xticklabels([r"$0^\circ$", r"$30^\circ$", r"$60^\circ$", r"$90^\circ$"],
                    fontsize=8)
axv.grid(color="0.85", lw=0.4)
axv.legend(loc="upper right", bbox_to_anchor=(1.20, 1.04), fontsize=7.2)
axv.set_title("Vertical: image in phase\n" r"$|F|=2|\cos(\beta h\sin\psi)|$",
              fontsize=8.5, pad=10)
axv.annotate("maximum AT\nthe horizon", xy=(0.012, 0.95),
             xytext=(np.radians(30), 0.62), color="0.30", fontsize=7.4,
             arrowprops=dict(arrowstyle="->", color="0.45", lw=0.7))

fig.subplots_adjust(wspace=0.42)
save(fig, "ground_image_lobes")
