import pyaudio  
import wave
import sys  

#define stream chunk   
chunk = 1024  

#open a wav format music  
f = wave.open(sys.argv[1],"rb")  
#instantiate PyAudio  
p = pyaudio.PyAudio()  
#open stream  
stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                channels = f.getnchannels(),  
                rate = f.getframerate(),  
                output = True)  
#read data  
data = f.readframes(chunk)  

#play stream
icnt = 0
while ((data) and (icnt<500)):  
    stream.write(data)  
    data = f.readframes(chunk)  
    icnt+=1

#stop stream  
stream.stop_stream()  
stream.close()  

#close PyAudio  
p.terminate()  
