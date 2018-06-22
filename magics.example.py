import mcpi.minecraft as minecraft

username = input("Username: ")
magicword = input("Magicword: ")
# mc = minecraft.Minecraft.create(address="127.0.0.1")
mc = minecraft.Minecraft.create(address="127.0.0.1", name=username)


def magic(command):
    if "go to" in command:
        go_to(command)
    elif "where am i" in command:
        where_am_i()


def go_to(command):
    pos = command.split('go to ', 1)[1].split(' ')
    mc.player.setPos(pos[0], pos[1], pos[2])
    where_am_i()

def where_am_i():
    pos = mc.player.getTilePos()
    name = mc.player.name
    place = name + ': ' + str(pos.x) + ' ' + str(pos.y) + ' ' + str(pos.z)
    mc.postToChat(place)
