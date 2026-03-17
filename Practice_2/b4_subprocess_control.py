import os
import time 
import subprocess
import signal

proc = subprocess.Popen(["sleep","100"])

print(f"Started process with PID: {proc.pid}")

print("Sending SIGSTOP")
os.kill(proc.pid, signal.SIGSTOP)
time.sleep(2)

print("Sending SIGCONT")
os.kill(proc.pid, signal.SIGCONT)
time.sleep(2)

print("Sending SIGTERM")
proc.terminate()

proc.wait()

print(f"Process finished with returncode: {proc.returncode}")