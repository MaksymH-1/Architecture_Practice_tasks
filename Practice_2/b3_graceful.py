import signal
import os
import time

stop = False

def handle_signal(signum, frame):
    global stop
    print(f"\nReceived signal from {signum}")
    stop = True

signal.signal(signal.SIGINT, handle_signal)
signal.signal(signal.SIGTERM, handle_signal)

print(f"Process PID: {os.getpid()}")

tick = 0
while not stop:
    print(f"tick = {tick}")
    tick+=1
    time.sleep(1)

print("Stopping... cleaning up")
time.sleep(1)
print("Cleanup done. Exit.")