"""A hand-built Smith chart (matplotlib only) with the reflection-coefficient
locus of an idealized antenna. The antenna is modeled as a series RLC one-port,
Z(f)=R_rad + j(wL - 1/(wC)), a resonant dipole reduced to ideal elements. The
locus Gamma(f)=(z-1)/(z+1), z=Z/Z0, is what a NanoVNA traces as it sweeps."""
import numpy as np
import matplotlib.pyplot as plt
from _style import apply_style, save, GUIDE_BLUE, GUIDE_GREEN, GUIDE_AMBER, GUIDE_LINE, GUIDE_RED

apply_style()

Z0 = 50.0

fig, ax = plt.subplots(figsize=(5.2, 5.0))
ax.set_aspect("equal")

# ---- Smith grid: constant-r circles and constant-x arcs in the Gamma plane ----
def r_circle(rn):
    # center, radius of a constant-resistance circle (normalized r)
    return (rn/(1+rn), 0.0), 1.0/(1+rn)

def x_arc(xn):
    # center, radius of a constant-reactance circle
    return (1.0, 1.0/xn), 1.0/abs(xn)

th = np.linspace(0, 2*np.pi, 400)
# outer boundary |Gamma|=1
ax.plot(np.cos(th), np.sin(th), color="0.4", lw=1.0)

for rn in [0.2, 0.5, 1.0, 2.0, 5.0]:
    (cx, cy), rad = r_circle(rn)
    ax.plot(cx + rad*np.cos(th), cy + rad*np.sin(th), color=GUIDE_LINE,
            lw=0.6, alpha=0.8)

for xn in [0.2, 0.5, 1.0, 2.0, 5.0]:
    for sgn in (+1, -1):
        (cx, cy), rad = x_arc(sgn*xn)
        # keep only the part inside the unit circle
        ang = np.linspace(0, 2*np.pi, 800)
        px = cx + rad*np.cos(ang)
        py = cy + rad*np.sin(ang)
        inside = px**2 + py**2 <= 1.0 + 1e-9
        ax.plot(px[inside], py[inside], color=GUIDE_LINE, lw=0.6, alpha=0.8,
                marker="", ls="none" if False else "-")
ax.axhline(0, color=GUIDE_LINE, lw=0.6, alpha=0.8)

# ---- idealized antenna model: series RLC ----
f0 = 14.1e6                       # design resonance, Hz (20 m band)
w0 = 2*np.pi*f0
Xc = 200.0                        # characteristic reactance w0*L = 1/(w0*C)
L = Xc/w0
C = 1.0/(w0*Xc)
Rrad = 35.0                       # radiation resistance at resonance

f = np.linspace(13.2e6, 15.0e6, 400)
w = 2*np.pi*f
Z = Rrad + 1j*(w*L - 1.0/(w*C))
z = Z/Z0
G = (z - 1)/(z + 1)
ax.plot(G.real, G.imag, color=GUIDE_BLUE, lw=2.2, zorder=5,
        label="antenna sweep $\\Gamma(f)$")

# resonance point (X=0 -> Z=Rrad)
zr = Rrad/Z0
Gr = (zr - 1)/(zr + 1)
ax.plot(Gr, 0, "o", color=GUIDE_RED, ms=6, zorder=6)
ax.annotate(r"$f_0$: $Z=R_{\mathrm{rad}}=35\,\Omega$", xy=(Gr, 0),
            xytext=(-0.95, -0.62), color=GUIDE_RED, fontsize=8,
            arrowprops=dict(arrowstyle="->", color=GUIDE_RED, lw=0.9))
# perfect-match center
ax.plot(0, 0, "+", color=GUIDE_GREEN, ms=11, mew=2.0, zorder=6)
ax.annotate(r"center: $50\,\Omega$ match", xy=(0, 0), xytext=(0.1, 0.72),
            color=GUIDE_GREEN, fontsize=8,
            arrowprops=dict(arrowstyle="->", color=GUIDE_GREEN, lw=0.9))

# endpoint labels (inductive above, capacitive below axis)
ax.annotate("high $f$\n(inductive)", xy=(G.real[-1], G.imag[-1]),
            xytext=(0.35, 0.42), color="0.35", fontsize=7.5,
            arrowprops=dict(arrowstyle="->", color="0.5", lw=0.7))
ax.annotate("low $f$\n(capacitive)", xy=(G.real[0], G.imag[0]),
            xytext=(0.35, -0.5), color="0.35", fontsize=7.5,
            arrowprops=dict(arrowstyle="->", color="0.5", lw=0.7))

ax.set_xlim(-1.08, 1.08)
ax.set_ylim(-1.08, 1.08)
ax.set_xticks([])
ax.set_yticks([])
ax.grid(False)
for spine in ax.spines.values():
    spine.set_visible(False)
ax.legend(loc="upper left", fontsize=8, bbox_to_anchor=(-0.02, 1.02))

save(fig, "smith_chart_antenna")
