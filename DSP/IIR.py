from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

b, a = signal.iirfilter(4, [50, 250], btype='band', analog=False,ftype='butter', fs=1500, output='ba')
sos = signal.iirfilter(2, [50, 180], btype='band', ftype='butter', fs=1500, output='sos')
# w, h = signal.freqz(b, a, 750)
w, h = signal.sosfreqz(sos, 750)
# signal.sosfilt()
plt.plot(w*750/np.pi, 20 * np.log10(abs(h)))
plt.xlabel('Frequency')
plt.ylabel('Amplitude response [dB]')
# plt.xlim(0, 500)
plt.grid()
plt.show()
