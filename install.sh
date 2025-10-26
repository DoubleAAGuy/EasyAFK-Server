#!/bin/bash
rm -rf *
git clone https://github.com/DoubleAAGuy/EasyAFK-Server.git .
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.8/install.sh | bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
nvm install 22.21.0
nvm use 22.21.0
npm install mineflayer
