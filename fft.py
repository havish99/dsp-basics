from __future__ import division
import soundfile as sf 
from scipy import signal
import numpy as np  

x,fs1=sf.read('Sound_Noise.wav')
h,fs2=sf.read('transfer.wav')

# def dft(x):
# 	N=len(x)
# 	X=np.zeros((N,),dtype=complex)
# 	for k in range(0,N):
# 		for n in range(0,N):
# 			X[k]=X[k]+x[n]*np.exp(-np.pi*2j*k*n/N)
# 	return X

x1=np.fft.fft(x)
h1=np.fft.fft(h)

y=x1*h1

y1=np.fft.ifft(y)
y1=y1.real
sf.write('fft.wav',y1,fs1)
