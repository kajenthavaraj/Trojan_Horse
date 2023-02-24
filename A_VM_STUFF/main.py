import paramiko
import random
import subprocess
import requests
import json
import time

import VM_create
import ip_info
import privatekeyparo

# Define the instance name
initial_code = random.randint(100, 999)
i=0
instance_name = 'instance-{0}-{1}'.format(initial_code, i)

# Define the project ID
project_id = 'th-vm-tutorial'

# Define zone - northamerica-northeast2-a
your_zone = 'northamerica-northeast2-a'
#your_zone = 'us-central1-a'

########################################################

#Create VM
VM_create.create_VM(instance_name, project_id, your_zone)


########################################################
#wait for VM to initialize
time.sleep(60)
########################################################

privatekeyparo.connect_VM(instance_name, project_id, your_zone)