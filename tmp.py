import pylab as pl
import numpy as np
# xs = np.linspace(0, 2 * np.pi, 300)
# # ys = np.sin(xs)
# for i in range(300):
#     list(xs).append(0)
# ys = np.sin(xs)
# an_xs = np.linspace(0, 4 * np.pi, 600)
# an_ys = np.sin(an_xs)
#
#
# fft = np.fft.fft(ys)
# fft = abs(fft)
# an_fft = np.fft.fft(an_ys)
# an_fft = abs(an_fft)
# fig = pl.figure('test')
#
# pl.plot(xs, fft, 'ob-')
# # pl.plot(an_xs, an_fft, 'ob-')
# pl.show()

def main():
    sum = 0
    for i in range(101):
        sum += i
    print(sum)
main()