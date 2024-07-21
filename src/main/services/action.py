import json
from typing import Dict, List, Any

import sys
import os


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from .memory import Memory
from ..utils.helpers import convert_string_to_json
from ..utils.actor import take_action
from ..utils.settings import format_actor_prompt, system_prompt





def runAgent(prompt_data):
    
    user_prompt = prompt_data['user_prompt']
    session_id = prompt_data['session_id']
    
    memory = Memory()
    
    # memory_output = memory.runMemoryAgent(user_prompt, session_id)
    # memory_output = memory.checkMemoryAgentOutput(memory_output)
    
    # if memory_output["store_memory"] == "true":
    #     memory.saveMemory(memory_output["memory"]["description"], session_id)
    if session_id == "":
        session_id = memory.create()
        # print(session_id)
        temporary_memory = {
            "conversation_history": "not_given",
            "user_prompt": user_prompt,
            "recent_response": "not_given",
            "context": "not_given",
            "current_webpage": prompt_data['current_webpage'],
            "list_of_all_webpages": prompt_data['list_of_all_webpages'],
            "ai_response": "not_given",
            "next_webpage_to_navigate_to": "not_given"
        }
    else:
        temporary_memory = memory.get(session_id) 
    # retrieved_context = memory.retriveMemory(f"History: {prompt_data['conversation_history']}. User: {user_prompt}.") #, session_id)
    retrieved_context = "no contxt available, go ahead and answer"
     

    history = temporary_memory['conversation_history']
    states = temporary_memory['list_of_all_webpages']
    current_state = temporary_memory['next_webpage_to_navigate_to']
    current_action = temporary_memory['ai_response']
    data = {
        "conversation_history": history,
        "user_prompt": user_prompt,
        "recent_response": current_action,
        "some_context": retrieved_context,
        "current_webpage": current_state,
        "list_of_all_webpages": states,
        "ai_response": "your response should be here for the user prompt",
        "next_webpage_to_navigate_to": ""
    }
    formatted_prompt = format_actor_prompt(data)
    response = take_action(str(formatted_prompt), system_prompt)
    try:
        response_data = convert_string_to_json(response)
        # print(type(response_data), response_data)

    except:
        state_action_result = json.dumps(response)
        state_action = json.loads(str(state_action_result))
        response_data = convert_string_to_json(state_action)

        # response_data = json.loads(state_action)


    # response_data["session_id"] = str(session_id)
    
    memory.update(response_data, str(session_id))
    return [response_data, session_id]

# data = {
#   "user_prompt": "what is the address of the school",
#   "current_webpage": "Home",
#   "list_of_all_webpages": "[Home, Programs, About, Contact Us]",
#   "session_id": "669a9dd1e41b4d34e414331b"
# }

# print(runAgent(data))