#!/bin/sh -v

# Install java 8 on macOS
#brew tap caskroom/versions
#brew cask install java8


# Install offical launcher
#brew cask install minecraft


# Install unoffical launcher
rm -rf client
mkdir -p client
# Download TLauncher-MCL.jar from https://mc-launcher.com/special/minecraft.html
MCL_URL="http://tlaun.ch/dl/mcl/jar"
wget -O client/TLauncher-MCL.jar $MCL_URL


# Install server
rm -rf server
mkdir -p server
# Download spigot-1.12.2.jar from https://getbukkit.org/
SPIGOT_URL="https://cdn.getbukkit.org/spigot/spigot-1.12.2.jar"
wget -O server/spigot.jar $SPIGOT_URL

mkdir -p server/plugins
# Download raspberryjuice-1.9.1.jar from Github
RJUICE_URL="https://github.com/zhuowei/RaspberryJuice/raw/master/jars/raspberryjuice-1.9.1.jar"
wget -O server/plugins/raspberryjuice.jar $RJUICE_URL

# Config server
echo "eula=true" > server/eula.txt
cat > server/server.properties << EOF
allow-flight=true
online-mode=false
gamemode=1
EOF


# Config virtualenv
PY_VERSION=3.6.0
VENV=minecraft
#pyenv install $PY_VERSION
pyenv local --unset
pyenv uninstall $VENV
pyenv virtualenv $PY_VERSION $VENV
pyenv local $VENV


# Install mcpi-multiplayer-api module
rm -rf mcpi-multiplayer-api
git clone https://github.com/mengbo/mcpi-multiplayer-api.git
(cd mcpi-multiplayer-api && python setup.py install)
rm -rf mcpi-multiplayer-api
