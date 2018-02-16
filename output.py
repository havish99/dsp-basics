from __future__ import division
import soundfile as sf 
from scipy import signal
import numpy as np 

x,fs=sf.read('Sound_Noise.wav')
h,fs=sf.read('transfer.wav')

y=np.convolve(x,h)

sf.write('Labrat.wav',y,fs)