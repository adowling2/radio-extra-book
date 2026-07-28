"""The three two-element patterns the pool names, all from the one array factor
|F| = 2|cos((phi + beta d cos theta)/2)| of sec:arrayfactor. The cardioid panel also
carries the two pattern measurements the exam asks for -- 3 dB beamwidth and
front-to-back ratio -- read off the same curve. Angles are measured from the array
axis. See sec:arrayfactor."""
import numpy as np
import matplotlib.pyplot as plt
from _style import apply_style, save, GUIDE_BLUE, GUIDE_GREEN, GUIDE_AMBER, GUIDE_RED

apply_style()

th = np.linspace(0, 2*np.pi, 3000)


def F(d_lam, phi):
    """Array factor magnitude, normalised to its own maximum."""
    bd = 2*np.pi*d_lam
    f = 2*np.abs(np.cos((phi + bd*np.cos(th))/2))
    return f/f.max()


cases = [
    (0.5, 0.0,      r"$d=\lambda/2$, $\phi=0$",        "figure-eight,\nbroadside",  GUIDE_BLUE),
    (0.5, np.pi,    r"$d=\lambda/2$, $\phi=180^\circ$", "figure-eight,\nend-fire",  GUIDE_GREEN),
    (0.25, np.pi/2, r"$d=\lambda/4$, $\phi=90^\circ$",  "cardioid",                 GUIDE_AMBER),
]

fig, axes = plt.subplots(1, 3, figsize=(6.6, 2.85),
                         subplot_kw={"projection": "polar"})

for ax, (d, phi, title, name, col) in zip(axes, cases):
    f = F(d, phi)
    ax.plot(th, f, color=col, lw=1.6)
    ax.fill(th, f, color=col, alpha=0.10)
    ax.set_theta_zero_location("E")     # 0 deg along the array axis, to the right
    ax.set_rmax(1.05)
    ax.set_rticks([0.5, 1.0])
    ax.set_yticklabels([])
    ax.set_xticks(np.radians([0, 90, 180, 270]))
    ax.set_xticklabels([])
    ax.grid(color="0.85", lw=0.4)
    ax.set_title(title + "\n" + name, fontsize=8, pad=5)
    # the array axis runs left-right through the pattern; show the two elements on it
    ax.plot([0, np.pi], [0.30, 0.30], color="0.45", lw=0.8, ls="-", zorder=6)
    ax.plot([0, np.pi], [0.30, 0.30], "s", color="0.25", ms=3.0, zorder=7)

# ---- annotate the cardioid with the two measurements the pool asks for ----
axc = axes[2]
fc = F(0.25, np.pi/2)
half = 1/np.sqrt(2)
above = fc >= half
idx = np.where(np.diff(above.astype(int)) != 0)[0]
edges = th[idx]
bw = np.degrees(np.abs(np.diff(sorted(edges))[0]))
axc.plot(edges, [half]*len(edges), "o", color=GUIDE_RED, ms=3.5, zorder=8)
axc.annotate(rf"$-3$ dB points, so the" "\n" rf"beamwidth is ${bw:.0f}^\circ$",
             xy=(np.radians(270), 0.72), xytext=(np.radians(288), 1.62),
             color=GUIDE_RED, fontsize=7, ha="center",
             arrowprops=dict(arrowstyle="->", color=GUIDE_RED, lw=0.7))
axc.annotate("a null, not a\nsmall lobe",
             xy=(0.0, 0.05), xytext=(np.radians(26), 1.48),
             color="0.30", fontsize=7, ha="center",
             arrowprops=dict(arrowstyle="->", color="0.45", lw=0.7))

fig.subplots_adjust(wspace=0.55, bottom=0.04, top=0.84)
save(fig, "array_patterns")
