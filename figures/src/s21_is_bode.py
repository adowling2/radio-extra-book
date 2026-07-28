"""S21 of a Z0-terminated band-pass, drawn as what it is: a Bode plot. Magnitude and
phase are what a vector network analyzer puts on its screen; the pole pair in the
inset is what Part II computed. Same object, two ways of arriving at it.

Model: a series L-C-r resonator coupling a Z0 source to a Z0 load, so
S21 = 2*Z0/(2*Z0 + r + j(wL - 1/wC)) -- the transmitted wave ratio of sec:sparams.
See sec:sparams and sec:vna."""
import numpy as np
import matplotlib.pyplot as plt
from _style import apply_style, save, GUIDE_BLUE, GUIDE_GREEN, GUIDE_AMBER, GUIDE_RED

apply_style()

Z0 = 50.0
L, C, r = 10.0e-6, 20e-12, 6.0    # loaded Q ~ 6.7: narrow enough to read as a
                                  # filter, wide enough to annotate
w0 = 1/np.sqrt(L*C)
f0 = w0/(2*np.pi)
Rtot = 2*Z0 + r                  # everything the resonating current flows through
QL = w0*L/Rtot                   # loaded Q
BW = f0/QL                       # exact, by sec:halfpower
IL = -20*np.log10(2*Z0/Rtot)     # insertion loss, sec:qlqu

f = np.logspace(np.log10(f0/6), np.log10(f0*6), 8000)
w = 2*np.pi*f
S21 = 2*Z0/(Rtot + 1j*(w*L - 1/(w*C)))
mag = 20*np.log10(np.abs(S21))
pha = np.degrees(np.angle(S21))

fig, (axm, axp) = plt.subplots(2, 1, figsize=(6.3, 4.3), sharex=True,
                               gridspec_kw={"height_ratios": [1.5, 1]})

# ---------------- magnitude ----------------
axm.semilogx(f/1e6, mag, color=GUIDE_BLUE, zorder=4)
axm.axhline(-IL, color=GUIDE_AMBER, ls="--", lw=1.0)
axm.axhline(-IL - 3.0, color=GUIDE_RED, ls="--", lw=1.0)
axm.annotate(rf"insertion loss $=-20\log_{{10}}|S_{{21}}|={IL:.2f}$ dB",
             xy=(f0/5.7/1e6, -IL + 1.8), color=GUIDE_AMBER, fontsize=8.5)
axm.annotate(r"$-3$ dB from the peak", xy=(f0/5.7/1e6, -IL - 5.4),
             color=GUIDE_RED, fontsize=8.5)

# band edges, and the bracket that is the bandwidth
rr = 1/(2*QL) + np.sqrt(1 + 1/(4*QL**2))
f1, f2 = f0/rr, f0*rr
for x in (f1, f2):
    axm.plot([x/1e6, x/1e6], [-IL - 3.0, -12.5], color=GUIDE_RED, ls=":", lw=0.9)
axm.annotate("", xy=(f1/1e6, -12.0), xytext=(f2/1e6, -12.0),
             arrowprops=dict(arrowstyle="<->", color=GUIDE_RED, lw=1.0))
axm.annotate(rf"$BW=f_0/Q_L={BW/1e6:.2f}$ MHz", xy=(f2/1e6, -12.0),
             xytext=(f0*1.75/1e6, -8.2), color=GUIDE_RED, ha="left", fontsize=8.5,
             arrowprops=dict(arrowstyle="->", color=GUIDE_RED, lw=0.8))

# the two skirts: one pole each side, so +/- 20 dB/decade
axm.annotate(r"$+20$ dB/dec", xy=(f0/3.5/1e6, -19.0), color="0.35",
             fontsize=8.5, rotation=40)
axm.annotate(r"$-20$ dB/dec", xy=(f0*2.15/1e6, -19.0), color="0.35",
             fontsize=8.5, rotation=-40)

axm.set_ylabel(r"$|S_{21}|$  (dB)")
axm.set_ylim(-30, 7)
axm.set_title("What a VNA shows, and what Part II computed", fontsize=9.5)

# ---------------- phase ----------------
axp.semilogx(f/1e6, pha, color=GUIDE_GREEN, zorder=4)
axp.axhline(0, color="0.5", lw=0.7)
for y in (90, -90):
    axp.axhline(y, color="0.75", ls=":", lw=0.8)
axp.plot([f0/1e6], [0], "o", color=GUIDE_AMBER, ms=5, zorder=5)
axp.annotate(r"$\angle S_{21}=0$ at $f_0$", xy=(f0/1e6, 0),
             xytext=(f0*2.1/1e6, 44), color=GUIDE_AMBER, fontsize=8.5,
             arrowprops=dict(arrowstyle="->", color=GUIDE_AMBER, lw=0.8))
axp.annotate(r"slope $=$ group delay $\tau_g=-\,d\phi/d\omega$",
             xy=(f0/5.7/1e6, -80), color="0.35", fontsize=8.5)
axp.set_xlabel(r"frequency (MHz)")
axp.set_ylabel(r"$\angle S_{21}$  (deg)")
axp.set_ylim(-105, 105)
axp.set_yticks([-90, -45, 0, 45, 90])
axp.set_xlim(f[0]/1e6, f[-1]/1e6)
axp.set_xticks([2, 5, 10, 20, 50])
axp.set_xticklabels(["2", "5", "10", "20", "50"])
axp.minorticks_off()

# ---------------- inset: the pole pair that produced all of it ----------------
ins = axm.inset_axes([0.795, 0.055, 0.19, 0.42])
alpha = Rtot/(2*L)
wd = np.sqrt(max(0.0, w0**2 - alpha**2))
sc = 1/w0
th = np.linspace(0, 2*np.pi, 300)
ins.plot(np.cos(th), np.sin(th), color="0.75", ls="--", lw=0.7)
ins.plot([-alpha*sc, -alpha*sc], [wd*sc, -wd*sc], "o", color=GUIDE_BLUE, ms=4.5)
ins.axhline(0, color="0.4", lw=0.6)
ins.axvline(0, color="0.4", lw=0.6)
ins.set_xlim(-1.35, 0.45)
ins.set_ylim(-1.35, 1.35)
ins.set_aspect("equal")
ins.set_xticks([])
ins.set_yticks([])
ins.grid(False)
ins.set_title("the pole pair", fontsize=7, pad=1.5)

save(fig, "s21_is_bode")
