import magics
import importlib
import subprocess
from pathlib import Path

home = str(Path.home())
file = Path("%s/Library/Application Support/%s/logs/latest.log" %
            (home, "tlauncher/for Mc-launcher.com"))
if not file.exists():
    file = Path("%s/Library/Application Support/%s/logs/latest.log" %
                (home, "minecraft"))

f = subprocess.Popen(['tail', '-0', '-F', file],
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)

lead = "[CHAT] <%s> %s" % (magics.username, magics.magicword)

while True:
    line = str(f.stdout.readline(), 'utf-8').strip()
    print(line)
    if lead in line:
        command = line.split(lead, 1)[1]
        magics.magic(command)
