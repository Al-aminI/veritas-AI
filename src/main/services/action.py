from typing import Dict, List, Any

import sys
import os

from main.services.memory import Memory

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from ..utils.actor import take_action
from ..utils.settings import system_prompt





def runAgent(user_prompt, user_id):
    
    
    memory = Memory()
    
    memory_output = memory.runMemoryAgent(user_prompt, user_id)
    memory_output = memory.checkMemoryAgentOutput(memory_output)
    
    if memory_output["store_memory"] == "true":
        memory.saveMemory(memory_output["memory"]["description"], user_id)
    
    retrieved_context = memory.retriveMemory(user_prompt, user_id)
    
    temporary_memory = memory.get(user_id) 
     

    history = temporary_memory['conversation_history']
    states = temporary_memory['list_of_possible_webpages']
    current_state = temporary_memory['next_webpge']
    current_action = temporary_memory['your_response']
    data = {
        "conversation_history": history,
        "user_prompt": user_prompt,
        "recent_response": current_action,
        "context": retrieved_context,
        "current_webpage": current_state,
        "list_of_possible_webpages": states,
        "your_response": "your response should be here for the prompt",
        "next_webpage_to_navigate_to": ""
    }
    formatted_prompt = 
    state_action_result = take_action(str(data), system_prompt)
    
    
    