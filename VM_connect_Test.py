import subprocess

# Define the instance name
instance_name = 'instance-605-0'

# Define the project ID
project_id = 'th-vm-tutorial'

# Set the project
subprocess.run(['gcloud', 'config', 'set', 'project', project_id])

# Connect to the instance
subprocess.run(['gcloud', 'compute', 'ssh', instance_name])


# Define the command to run
cmd = 'ls -l /'

# Connect to the instance
subprocess.run(['gcloud', 'compute', 'ssh', instance_name, '--', 'bash', '-c', cmd])
