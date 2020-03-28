import wave
from bitstring import BitArray

f = wave.open('/Users/macbook/Desktop/HW5/zeineb.sahnoun@epfl.ch.wav', 'rb')
token= ''
for x in (f.readframes(f.getnframes())[::2]):
    token = token + str(x & 1)    
s = BitArray(bin=token).tobytes().decode()
s[s.find('COM402'):][0:52]