import time

def transfer_requirements(client):
    sftp = client.open_sftp()

    local_path = '/Users/kajenthavaraj/Trojan Horse SaaS/A_VM_STUFF/piprequirements.txt'
    remote_path = '/home/projectwideuser/piprequirements.txt'

    sftp.put(local_path, remote_path)

    local_path = '/Users/kajenthavaraj/Trojan Horse SaaS/credential.json'
    remote_path = '/home/projectwideuser/credential.json'

    sftp.put(local_path, remote_path)

    sftp.close()

def transfer_pythonfile(client):
    sftp = client.open_sftp()

    local_path = '/Users/kajenthavaraj/Trojan Horse SaaS/New Code/testw2342.py'
    remote_path = '/home/projectwideuser/server_run.py'

    sftp.put(local_path, remote_path)

    sftp.close()


def transfer_dockerfile(client):
    sftp = client.open_sftp()
    
    stdin, stdout, stderr = client.exec_command('sudo mkdir dockerfiles')

    local_path = '/Users/kajenthavaraj/Trojan Horse SaaS/A_VM_STUFF/Dockerfile'
    remote_path = '/home/projectwideuser/Dockerfile'

    sftp.put(local_path, remote_path)
    
    sftp.close()























def all_commands(client):
    stdin, stdout, stderr = client.exec_command("DEBIAN_FRONTEND=noninteractive")
    print(stdout.read().decode())
    print(stderr.read().decode())
    stdin, stdout, stderr = client.exec_command("sudo apt-get update")
    print(stdout.read().decode())
    print(stderr.read().decode())
    stdin, stdout, stderr = client.exec_command("sudo apt-add-repository -y ppa:yubico/stable")
    print(stdout.read().decode())
    print(stderr.read().decode())
    stdin, stdout, stderr = client.exec_command("sudo apt-get install -y libu2f-udev")
    print(stdout.read().decode())
    print(stderr.read().decode())   
    stdin, stdout, stderr = client.exec_command("sudo dpkg-reconfigure libu2f-udev")
    print(stdout.read().decode())
    print(stderr.read().decode())
    stdin, stdout, stderr = client.exec_command("sudo apt-get install -y --no-install-recommends debconf-utils")
    print(stdout.read().decode())
    print(stderr.read().decode())
    stdin, stdout, stderr = client.exec_command("sudo apt-get install -y xvfb")
    print(stdout.read().decode())
    print(stderr.read().decode())
    stdin, stdout, stderr = client.exec_command("sudo apt-get -y install xorg xvfb gtk2-engines-pixbuf")
    print(stdout.read().decode())
    print(stderr.read().decode())
    stdin, stdout, stderr = client.exec_command("sudo apt-get -y install dbus-x11 xfonts-base xfonts-100dpi xfonts-75dpi xfonts-cyrillic xfonts-scalable")
    print(stdout.read().decode())
    print(stderr.read().decode())
    stdin, stdout, stderr = client.exec_command("Xvfb -ac :99 -screen 0 1280x1024x16 &")
    print(stdout.read().decode())
    print(stderr.read().decode())
    stdin, stdout, stderr = client.exec_command("export DISPLAY=:99")
    print(stdout.read().decode())
    print(stderr.read().decode())
    stdin, stdout, stderr = client.exec_command("sudo apt-get install -f")
    print(stdout.read().decode())
    print(stderr.read().decode())   
    stdin, stdout, stderr = client.exec_command("sudo apt-get install -y chromium-browser")
    print(stdout.read().decode())
    print(stderr.read().decode())   
    stdin, stdout, stderr = client.exec_command("sudo apt-get install -y python3.8")
    print(stdout.read().decode())
    print(stderr.read().decode())
    stdin, stdout, stderr = client.exec_command("pip3 install -r piprequirements.txt")
    print(stdout.read().decode())
    print(stderr.read().decode())
    stdin, stdout, stderr = client.exec_command("pip3 install selenium chromedriver-binary")
    print(stdout.read().decode())
    print(stderr.read().decode())
    stdin, stdout, stderr = client.exec_command("pip install --upgrade google-api-python-client")
    print(stdout.read().decode())
    print(stderr.read().decode())
    stdin, stdout, stderr = client.exec_command("pip3 install google-auth google-auth-oauthlib")
    print(stdout.read().decode())
    print(stderr.read().decode())


















def all_commands_2(client):
    stdin, stdout, stderr = client.exec_command("DEBIAN_FRONTEND=noninteractive")
    print(stdout.read().decode())
    print(stderr.read().decode())
    stdin, stdout, stderr = client.exec_command("sudo apt-get update")
    print(stdout.read().decode())
    print(stderr.read().decode())
    stdin, stdout, stderr = client.exec_command("sudo apt-add-repository -y ppa:yubico/stable")
    print(stdout.read().decode())
    print(stderr.read().decode())
    stdin, stdout, stderr = client.exec_command("sudo apt-get install -y libu2f-udev")
    print(stdout.read().decode())
    print(stderr.read().decode())   
    stdin, stdout, stderr = client.exec_command("sudo dpkg-reconfigure libu2f-udev")
    print(stdout.read().decode())
    print(stderr.read().decode())
    stdin, stdout, stderr = client.exec_command("sudo apt-get install -y --no-install-recommends debconf-utils")
    print(stdout.read().decode())
    print(stderr.read().decode())
    stdin, stdout, stderr = client.exec_command("sudo apt-get install -y xvfb")
    print(stdout.read().decode())
    print(stderr.read().decode())
    stdin, stdout, stderr = client.exec_command("sudo apt-get -y install xorg xvfb gtk2-engines-pixbuf")
    print(stdout.read().decode())
    print(stderr.read().decode())
    stdin, stdout, stderr = client.exec_command("sudo apt-get -y install dbus-x11 xfonts-base xfonts-100dpi xfonts-75dpi xfonts-cyrillic xfonts-scalable")
    print(stdout.read().decode())
    print(stderr.read().decode())
    stdin, stdout, stderr = client.exec_command("Xvfb -ac :99 -screen 0 1280x1024x16")
    print(stdout.read().decode())
    print(stderr.read().decode())
    stdin, stdout, stderr = client.exec_command("export DISPLAY=:99")
    print(stdout.read().decode())
    print(stderr.read().decode())
    stdin, stdout, stderr = client.exec_command("sudo wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
    print(stdout.read().decode())
    print(stderr.read().decode())
    stdin, stdout, stderr = client.exec_command("sudo apt-get install -f")
    print(stdout.read().decode())
    print(stderr.read().decode())
    stdin, stdout, stderr = client.exec_command("sudo apt install -y ./google-chrome-stable_current_amd64.deb")
    print(stdout.read().decode())
    print(stderr.read().decode())   
    stdin, stdout, stderr = client.exec_command("sudo apt-get -y install python3-pip")
    print(stdout.read().decode())
    print(stderr.read().decode())
    stdin, stdout, stderr = client.exec_command("pip3 install -r piprequirements.txt")
    print(stdout.read().decode())
    print(stderr.read().decode())
    stdin, stdout, stderr = client.exec_command("pip3 install selenium chromedriver-binary")
    print(stdout.read().decode())
    print(stderr.read().decode())
    stdin, stdout, stderr = client.exec_command("pip install --upgrade google-api-python-client")
    print(stdout.read().decode())
    print(stderr.read().decode())
    stdin, stdout, stderr = client.exec_command("pip3 install google-auth google-auth-oauthlib")
    print(stdout.read().decode())
    print(stderr.read().decode())