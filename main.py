import subprocess
import webbrowser
import re
def ready(name, ip, server_port_over, game_version):
    if game_version=="1.21.8":
        username = name   # Microsoft account or offline username
        server_ip = ip
        server_port = "25565"
        if server_port_over != "null":
            server_port = server_port_over
        # Start the Node.js bot with arguments
        process = subprocess.Popen(
            ["/home/jetson/.nvm/versions/node/v22.21.0/bin/node", "bot.js", username, server_ip, server_port],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )

        # Capture the link from bot output
        while True:
            line = process.stdout.readline()
            if not line:
                break
            print(f"[BOT] {line.strip()}")

            # Auto-detect device login link
            if "https://" in line:
                print(line)
                link = line.strip()
                id = re.search(r'(?:code\s|otc=)([A-Z0-9]+)', link).group(1)
                print(f"Device login link detected: {id}")
                return "http://microsoft.com/link?otc="+id
    else: return "Error game version is not in supported versions. (This is proabally not your fault) Please report this."
        
