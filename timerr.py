import time
import subprocess

def pomidorka_go():
    while True:
        print "Ready, Steady, Go TO WORK! "
        subprocess.call("python play.py /home/alexeybel/workspace/Python/timer/eye_tiger.wav", shell = True)
        time.sleep(1500.0)
        print "Take it easy, you can RELAX"
        subprocess.call("python play.py /home/alexeybel/workspace/Python/timer/big.wav", shell = True)
        time.sleep(300.0)
#1500
pomidorka_go()
