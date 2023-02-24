import ip_info

 # Define the passphrase
passphrase = 'Kajen'

# Define the project ID
project_id = 'th-vm-tutorial'

# Define zone
your_zone = 'us-central1-a'

instance_name = 'instance-115-0'

# Get the name of the instance
VM_name = instance_name
external_ip = ip_info.external_ip_request(instance_name, project_id, your_zone)

print("Instance IP:", external_ip)
print("Instance Name:", VM_name)