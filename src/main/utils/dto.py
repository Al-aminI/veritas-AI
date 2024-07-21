from flask_restx import Namespace, fields


class AgentDto:
    api = Namespace('Agent', description='Agentic Operations')
    agent = api.model('Agent', {
        # "conversation_history": fields.String(required=False, description='conversation_history'),
        "user_prompt": fields.String(required=True, description='user prompt'),
        # "recent_response": fields.String(required=False, description='recent response'),
        # "context": fields.String(required=False, description='context'),
        "current_webpage": fields.String(required=False, description='current webpage'),
        # "list_of_all_webpages": fields.String(required=False, description='list of webpages'),
        # "ai_response": fields.String(required=False, description='ai response'),
        # "next_webpage_to_navigate_to": fields.String(required=False, description='next_webpage'),
        'session_id': fields.String(required=False, description='session_id'),
        
        # we could add fields like audio prompt, files and images and etc kinds of input prompt.
        
    })
   