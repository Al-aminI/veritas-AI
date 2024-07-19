from flask_restx import Api
from flask import Blueprint


from .main.controller.action_controller import api as agent_name_space




blueprint = Blueprint('api_v1', __name__, url_prefix='/ai/api/v1/agent/')
authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(
    
    blueprint,
    title='Vertisa AI API enpoints',
    version='3.0.0',
    description='Vertisa AI endpoints',
    # authorizations=authorizations,
    security='apikey',
    default_mediatype='multipart/form-data',
   
    license =  {
      "name": "Vertisa",
      "url": "https://opensource.org/licenses/MIT"
    },
    tags = [
    {
      "name": "Vertisa AI APIs",
      "description": "Vertisa backend API endpoints"
    }
  ],
)


api.add_namespace(agent_name_space)