import datetime
import base64
import os
import uuid
import dialogflow
from config import config

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(os.path.dirname(__file__),
                                                            config.get('dialogflow_secret'))

now = datetime.datetime.now()

class DialogFlowService:
    def __init__(self):
        self.project_id = config.get('project_id')
        self.project = 'projects/{}'.format(self.project_id)

    def exportAgent(self):
        client = dialogflow.AgentsClient()
        response = client.export_agent(self.project)
				
        def callback(operation_future):
            result = operation_future.result()

        response.add_done_callback(callback)
        bytes = response.result().agent_content
		
        filename = '{}_{}.zip'.format(self.project_id, now.strftime('%Y-%m-%d'))
		
        f = open(filename, 'wb')
        f.write(bytes)
        f.close()
        print(filename, 'exported.')

    def importAgent(self, file):
        client = dialogflow.AgentsClient()

        f = open(file, 'rb')
        data = f.read()
        f.close()
		
        response = client.import_agent(self.project, agent_content=data)
				
        def callback(operation_future):
            result = operation_future.result()
        
        response.add_done_callback(callback)
        print('Agent imported with the file', file)

    def restoreAgent(self, file):
        client = dialogflow.AgentsClient()

        f = open(file, 'rb')
        data = f.read()
        f.close()
		
        response = client.restore_agent(self.project, agent_content=data)
				
        def callback(operation_future):
            result = operation_future.result()

        response.add_done_callback(callback)
        print('Agent restored with the file', file)