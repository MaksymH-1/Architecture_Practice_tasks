import os

pid = os.fork()

if pid == 0:
    #Child
    print("Child PID (from child): ", os.getpid())

    os.execlp("bash","bash","-lc","echo ---Child process 'exec'---; exit 7")

else:
    #Parent
    print("Parent PID: ", os.getpid())

    child_pid, status = os.waitpid(pid,0)

    exit_code = os.WEXITSTATUS(status)

    print(f"Child PID (from parent): {child_pid}")
    print(f"Exit code: {exit_code}")
