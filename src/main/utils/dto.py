from flask_restx import Namespace, fields


class AgentDto:
    api = Namespace('Agent', description='Agentic Operations')
    agent = api.model('Agent', {
        'prompt': fields.String(required=True, description='user prompt'),
        'user_id': fields.String(required=True, description='user system ip address'),
        
        
        # we could add fields like audio prompt, files and images and etc kinds of input prompt.
        
    })
   