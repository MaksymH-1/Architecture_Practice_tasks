import signal
import sys
import time

stop = False

def handle_signal(signum, frame):
    global stop
    print(f"\nWorker received signal from {signum}. Shutting dowm...")
    stop = True

signal.signal(signal.SIGINT, handle_signal)
signal.signal(signal.SIGTERM, handle_signal)

print(f"Worker started work")
tick = 0
while not stop:
    print(f"worker tick = {tick}")
    tick+=1
    time.sleep(1)

print(f"Worker cleanup.")
sys.exit(0)