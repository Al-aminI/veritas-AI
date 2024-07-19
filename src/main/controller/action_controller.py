
from ..services.agent import act
from ..utils.dto import AgentDto
from flask import request
from flask_restx import Resource


api = AgentDto.api
actionFields = AgentDto.agent



@api.route('/Act')
class Act(Resource):
    # @CustomJWTRequired() 
    @api.expect(actionFields, validate=True)
    @api.response(200, 'success')
    @api.doc('Environment Aware Markov Agent')
    def post(self):
       
        """take action given your current state and the following action data"""
        
        action_data = request.json
        response= act(action_data)
        
       
        return response