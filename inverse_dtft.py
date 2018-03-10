from __future__ import division
import soundfile as sf 
from scipy import signal
#from matplotlib import pyplot as plt 
import numpy as np
input_signal,fs=sf.read('Sound_Noise.wav')

sampl=fs

order=4

cutoff=4000

Wn=2*cutoff/sampl

b, a=signal.butter(order,Wn,'low')

b1,a1,k=signal.residuez(b,a)

h=[]
n=[]
for i in range(0,30):
	temp=0
	n.append(i)
	for j in range(0,len(b1)):
		temp=temp+b1[j]*(a1[j]**i)
	h.append(temp.real)
h[0]+=k[0]
y=np.convolve(input_signal,h)
# plt.stem(n,h)
# plt.show()
sf.write('Soundlol.wav',y,fs)
