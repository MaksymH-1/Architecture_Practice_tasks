import subprocess
import time

MAX_RESTARTS = 3
restarts_count = 0

while restarts_count < MAX_RESTARTS:
    print(f"Attemt №{restarts_count + 1}. Starting worker")

    process = subprocess.Popen(["python3", "Practice_2/worker.py"])

    try:
        return_code = process.wait()
    except KeyboardInterrupt:
        print("Terminating worker")
        process.terminate()
        process.wait()
        return_code = process.returncode

    print(f"Worker exited with code {return_code}")

    restarts_count += 1

    if restarts_count < MAX_RESTARTS:
        print("Restarting worker\n")
        time.sleep(1)
    else:
        print("Max restarts reached.")