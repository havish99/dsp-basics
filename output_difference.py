from __future__ import division
import soundfile as sf 
from scipy import signal
input_signal,fs=sf.read('Sound_Noise.wav')
sampl=fs

order=4

cutoff=4000

Wn=2*cutoff/sampl

b, a=signal.butter(order,Wn,'low')
x=[]

for i in range(0,len(input_signal)):
	x.append(input_signal[i])

x.append(0)
x.append(0)
x.append(0)
x.append(0)
y=[]
for i in range(0,len(x)-4):
	y.append(0)
for i in range(0,len(x)-4):
	p=b[0]*x[i]+b[1]*x[i-1]+b[2]*x[i-2]+b[3]*x[i-3]+b[4]*x[i-4]
	q=a[1]*y[i-1]+a[2]*y[i-2]+a[3]*y[i-3]+a[4]*y[i-4]
	y[i]=p-q/a[0]

sf.write('Sound_butter1.wav',y,fs)
