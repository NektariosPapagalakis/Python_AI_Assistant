import subprocess
import time
def shutdown_computer(waiting_time):
    if waiting_time != '0':
        time.sleep(int(waiting_time))
    try:
        subprocess.Popen("shutdown /s /t 1", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
        return "Computer Off"
    except Exception as e:
        return e