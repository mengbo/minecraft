import mcpi.minecraft as minecraft
import subprocess
from pathlib import Path

def magic(command):
    if "go to ten" in line:
        go_to_ten()
    elif "where am i" in line:
        where_am_i()

def go_to_ten():
    mc.player.setPos(10, 10, 10)
    where_am_i()

def where_am_i():
    pos = mc.player.getTilePos()
    name = mc.player.name
    place = name + ': ' + str(pos.x) + ' ' + str(pos.y) + ' ' + str(pos.z)
    print(place)
    mc.postToChat(place)


username = input("Username: ")
magicword = input("Magicword: ")

# mc = minecraft.Minecraft.create(address="127.0.0.1")
mc = minecraft.Minecraft.create(address="127.0.0.1", name=username)


home = str(Path.home())
file = Path("%s/Library/Application Support/%s/logs/latest.log" %
        (home, "for Mc-launcher.com"))
if not file.exists():
    file = Path("%s/Library/Application Support/%s/logs/latest.log" %
            (home, "minecraft"))

f = subprocess.Popen(['tail', '-0', '-F', file],
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)

while True:
    line = str(f.stdout.readline(), 'utf-8')
    print(line.strip())
    lead = "[CHAT] <%s> %s" % (username, magicword)
    if lead in line:
        magic(line)
