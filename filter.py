 # Import a lot of functions to keep it simple to use
from pylab import *
# 1 second of data samples at spacing of 1/1000 seconds
t = arange(0, 1, 1.0/1000)
# sine wave of 100 Hz
s = sin(2 * pi * 100 * t)
# plot first 20 points of the resulting data (why not all 1000?)
plot(s[:20])
show()
# Another signal with two sine waves
s = sin(2*pi*100*t)+sin(2*pi*200*t)
# Note: you may need to use fft.fft is you are using ipython
ft = fft(s)/len(s)
plot(20*log10(abs(ft)))
show()
t=arange(0,1.001,1.0/1000)
noise_amp = 5.0
s = sin(2*pi*100*t)+sin(2*pi*200*t)+noise_amp * randn(len(t))
from scipy.signal import remez
lpf = remez(21, [0, 0.2, 0.3, 0.5], [1.0, 0.0])
from scipy.signal import freqz
w, h = freqz(lpf)
plot(w/(2*pi), 20*log10(abs(h)))
show()
from scipy.signal import lfilter
sout = lfilter(lpf, 1, s)
plot(20*log10(abs(fft.fft(s))))
plot(20*log10(abs(fft.fft(sout))))
show()