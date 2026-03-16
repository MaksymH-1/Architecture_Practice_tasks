import os #робота з системою
import subprocess #запуск зовнішніх команд

PID = os.getpid()
PPID = os.getppid()

print(f"My PID: {PID}")
print(f"My PPID: {PPID}")
print("------------------------")

print("Detailed information: ")
subprocess.run(["ps", "-p", str(PID), "-o", "pid,ppid,stat,ni,comm"])