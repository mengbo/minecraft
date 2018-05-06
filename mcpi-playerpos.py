import mcpi.minecraft as minecraft
import time

username = input("Username: ")

# mc = minecraft.Minecraft.create(address="127.0.0.1")
mc = minecraft.Minecraft.create(address="127.0.0.1", name=username)

while True:
    time.sleep(3)
    pos = mc.player.getTilePos()
    name = mc.player.name
    place = name + ': ' + str(pos.x) + ' ' + str(pos.y) + ' ' + str(pos.z)
    print(place)
    mc.postToChat(place)
