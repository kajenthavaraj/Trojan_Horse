import paramiko
import ip_info
import time

import deploy_VM

def connect_VM(instance_name, project_id, your_zone):
    # Create an SSH client
    client = paramiko.SSHClient()

    # Automatically add the server's host key (recommended)
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    VM_username = "projectwideuser"

    # Connect to the server using the private key
    private_key_file = '/Users/kajenthavaraj/Trojan Horse SaaS/A_VM_STUFF/projectwideuser_key'
    private_key = paramiko.RSAKey.from_private_key_file(private_key_file)

    external_ip = ip_info.external_ip_request(instance_name, project_id, your_zone)

    #external_ip = '34.172.221.81'

    client.connect(external_ip, username=VM_username, pkey=private_key)

    # Execute a command
    stdin, stdout, stderr = client.exec_command('hostname')

    #update sudo
    stdin, stdout, stderr = client.exec_command("sudo apt-get update")
    # Print the command's output
    print(stdout.read().decode())
    print(stderr.read().decode())

    #install docker
    stdin, stdout, stderr = client.exec_command("sudo snap install docker")
    # Print the command's output
    print(stdout.read().decode())
    print(stderr.read().decode())

    #install python3 pip
    stdin, stdout, stderr = client.exec_command("sudo apt-get install -y python3.8")
    # Print the command's output
    print(stdout.read().decode())
    print(stderr.read().decode())

    deploy_VM.transfer_requirements(client)
    deploy_VM.transfer_pythonfile(client)
    deploy_VM.transfer_dockerfile(client)

    #stdin, stdout, stderr = client.exec_command('cd dockerfiles')

    #Build Dockerfile
    #stdin, stdout, stderr = client.exec_command('sudo docker build -t my-image -f Dockerfile .')

    #print(stdout.read().decode())
    print(stderr.read().decode())

    stdin, stdout, stderr = client.exec_command('python3 server_run.py')

    #Run Dockerfile
    #stdin, stdout, stderr = client.exec_command('sudo docker run')

    # Close the connection
    client.close()


#instance_name = 'instance-779-0'
#project_id = 'th-vm-tutorial'
#your_zone = 'us-central1-a'

#connect_VM(instance_name, project_id, your_zone)