import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Authenticate with Google Cloud
credentials, project = google.auth.default()

# Set up the Compute Engine API client
service = build('compute', 'v1', credentials=credentials)

# Define the properties of the virtual machine instances
instance_properties = {
    'zone': 'us-central1-a',
    'machineType': 'zones/us-central1-a/machineTypes/n1-standard-1',
    'disks': [{'boot': True, 'autoDelete': True, 'initializeParams': {'sourceImage': 'projects/debian-cloud/global/images/family/debian-9'}}],
    'networkInterfaces': [{'network': 'global/networks/default', 'accessConfigs': [{'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}]}]
}

# Create a list of virtual machine instances
instances = []
for i in range(3):
    instance_name = f'vm-{i}'
    instance = {
        'name': instance_name,
        'properties': instance_properties
    }
    instances.append(instance)

# Create the virtual machine instances
request = service.instances().insert(project=project, zone='us-central1-a', body={'items': instances})
response = request.execute()

print(f'Created {len(instances)} virtual machine instances:')
for instance in response['items']:
    print(instance['name'])
