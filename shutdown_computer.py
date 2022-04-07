import subprocess as sub
def shutdown_computer():
    try:
        p = sub.Popen("shutdown /s /t 1", shell=True, stdout=sub.PIPE, stderr=sub.PIPE).communicate()[0]
        a=p.decode("utf-8")
    except:
        return "Problem -- "+a

shutdown_computer()