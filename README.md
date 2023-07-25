# Discord Numpad Soundboard

[![](https://dcbadge.vercel.app/api/server/nzJgMjt)](https://discord.gg/nzJgMjt)
[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence)

A simple Python script to allow you to use your numpad to activate default Discord Soundboard sounds.

> **Note**  
> Tested with **Python 3.11.3** on macOS Ventura 13.4

## Instruction (WIP)

### Installation (Unix)
```
$ git clone https://github.com/Valokoodari/dc-numpad-soundboard
$ cd dc-numpad-soundboard
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Create a `.env` file with the following
```
CLIENT_ID=<Discord Application Client ID>
CLIENT_SECRET=<Discord Application Client Secret>
TOKEN=<Discord Access Token after first run> (Optional, asks for Authorization every time if not set)
```

Start the script with `python main.py`.
