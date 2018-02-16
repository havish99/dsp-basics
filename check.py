from __future__ import division
import soundfile as sf 
from scipy import signal
import numpy as np 
input1,fs=sf.read('Soundlol.wav')
input2,fs=sf.read('Sound_check.wav')

print(input1-input2)