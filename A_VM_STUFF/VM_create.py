import subprocess

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



# create one with a mentioned container:
#gcloud compute instances create yourmom --machine-type "e2-micro" --image-project ubuntu-os-cloud --image-family ubuntu-1804-lts --project th-vm-tutorial --zone northamerica-northeast2-a