from __future__ import division
import soundfile as sf 
from scipy import signal
import numpy as np  
input_signal,fs=sf.read('Sound_Noise.wav')
sampl=fs
order=4
cutoff=4000
Wn=2*cutoff/sampl
b, a=signal.butter(order,Wn,'low')
x=[]
s1=[]
n=[]
for i in range(0,len(input_signal)):
	x.append(0)
	s1.append(input_signal)
	n.append(i)
h=[]
x[0]=1
for i in range(0,31):
	h.append(0)
for i in range(0,31):
	p=b[0]*x[i]+b[1]*x[i-1]+b[2]*x[i-2]+b[3]*x[i-3]+b[4]*x[i-4]
	q=a[1]*h[i-1]+a[2]*h[i-2]+a[3]*h[i-3]+a[4]*h[i-4]
	h[i]=p-q/a[0]
sf.write('transfer.wav',h,fs)

