import subprocess
TERMS = {"kgx" : "kgx", "gnome-terminal" : "gnome-terminal --zoom=1.2 --geometry=128x16 --", "xterm" : "xterm -r -e"}

for term in TERMS:
    cmd = ['which', term]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    o, e = proc.communicate()
    if proc.returncode == 0:
        print('command: ' + TERMS[term])