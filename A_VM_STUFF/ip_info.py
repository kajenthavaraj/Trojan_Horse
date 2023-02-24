import random
import requests
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

def external_ip_request(instance_name, project_id, your_zone):
    credentials = GoogleCredentials.get_application_default()

    service = discovery.build('compute', 'v1', credentials=credentials)
    request = service.instances().get(project=project_id, zone=your_zone, instance=instance_name)

    response = request.execute()

    # Extract the networkIP and natIP fields
    external_ip = response['networkInterfaces'][0]['accessConfigs'][0]['natIP']

    # Print the values
    print("The external ip is: " + external_ip)

    return external_ip