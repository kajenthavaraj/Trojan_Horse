
from google.cloud import compute_v1

# Initialize the client
compute_client = compute_v1.ComputeClient()

# Define the instance name
instance_name = 'instance-1'

# Define the project ID
project_id = 'th-vm-tutorial'

# Get the instance
instance = compute_client.get_instance(instance_name, project_id)

# Connect to the instance
operation = instance.start_ssh()
operation.wait()
