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
    LANGUAGE_CODE = 'EN'

    def __init__(self):
        self.session_id = str(uuid.uuid4())
        self.project_id = config.get('project_id')
        self.agent = config.get('agent')
        
        self.agent = 'projects/{}/{}'.format(self.project_id, self.agent)
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

    def importAgent(self, file):
        client = dialogflow.AgentsClient()

        f = open(file, 'rb')
        data = f.read()
        f.close()
		
        response = client.import_agent(self.project, agent_content=data)
				
        def callback(operation_future):
            result = operation_future.result()
        
        response.add_done_callback(callback)
		
    def restoreAgent(self, file):
        client = dialogflow.AgentsClient()

        f = open(file, 'rb')
        data = f.read()
        f.close()
		
        response = client.restore_agent(self.project, agent_content=data)
				
        def callback(operation_future):
            result = operation_future.result()
        
        response.add_done_callback(callback)