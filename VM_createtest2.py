#from google.cloud import compute
import googleapiclient.discovery
import random

# Define the instance name
initial_code = random.randint(100, 999)
i=0
instance_name = 'instance-{0}-{1}'.format(initial_code, i)
instance_name = 'instanc-1'

# Define the project ID
project_id = 'th-vm-tutorial'

# Define the machine type - ex.) n1-standard-1
machine_type = 'e2-micro'

# Define zone
your_zone = 'us-central1-a'


# Define the passphrase
passphrase = 'Kajen'

compute = googleapiclient.discovery.build('compute', 'v1')

compute_client = compute.Client()

# Define the passphrase
passphrase = 'Kajen'

# Create the instance
instance = compute_client.create_instance(
    project_id,
    your_zone,
    instance_name,
    machine_type='f1-micro',
    source_image_project='ubuntu-os-cloud',
    source_image_family='ubuntu-1804-lts',
    ssh_keys={
        'user': 'kajenthavaraj:{}'.format(passphrase)
    }
)

# Wait for the instance to start
operation = instance.create()
operation.wait()
