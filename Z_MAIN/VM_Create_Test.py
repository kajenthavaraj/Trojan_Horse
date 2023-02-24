import subprocess
import random
import time

# Define the instance name
initial_code = random.randint(100, 999)
i=0
instance_name = 'instance-{0}-{1}'.format(initial_code, i)


 # Define the passphrase
passphrase = 'Kajen'

# Define the project ID
project_id = 'th-vm-tutorial'

# Define zone
your_zone = 'us-central1-a'

# Function to create VM
def create_VM(instance_name, project_id, your_zone):

    # Define the machine type - ex.) n1-standard-1
    machine_type = 'e2-micro'

    # Define the command to create the instance
    create_cmd = ['gcloud', 'compute', 'instances', 'create', instance_name,
        '--machine-type', machine_type,
        '--image-project', 'ubuntu-os-cloud',
        '--image-family', 'ubuntu-1804-lts',
        '--project', project_id,
        '--zone', your_zone]

    # Create the instance
    subprocess.run(create_cmd)


# Connect to VM Instance
def connect_VM(project_id, instance_name):
    # Set the project
    subprocess.run(['gcloud', 'config', 'set', 'project', project_id])

    # Connect to the instance
    subprocess.run(['gcloud', 'compute', 'ssh', instance_name])



create_VM(instance_name, project_id, your_zone)

# Set the project
subprocess.run(['gcloud', 'config', 'set', 'project', project_id])

# Connect to the instance
subprocess.run(['gcloud', 'compute', 'ssh', instance_name])