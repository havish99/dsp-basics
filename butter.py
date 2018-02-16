from __future__ import division
import soundfile as sf 
from scipy import signal

input_signal,fs=sf.read('Sound_Noise.wav')

sampl=fs

order=4

cutoff=4000

Wn=2*cutoff/sampl

b, a=signal.butter(order,Wn,'low')
print(a)
output=signal.filtfilt(b,a,input_signal)

sf.write('Sound_butter.wav',output,fs)

