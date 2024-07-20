import json
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ..utils.actor import take_action
from ..utils.settings import format_memory_prompt, system_prompt
from ..utils.short_term_memory import update_session_history, get_session_by_id, reset_short_term_memory, create_bin
from ..utils.long_term_memory import retrieve_memory_from_databank, save_memory_to_databank




class Memory:
   
        
     
    # long term memory services --------------------------------------------------------------
    @staticmethod
    def runMemoryAgent(start_of_user_prompts_and_memory_agent):
        
        memory_agent_system_prompt = format_memory_prompt(start_of_user_prompts_and_memory_agent)
       
        response = take_action(memory_agent_system_prompt, system_prompt)

        model_output = (response).replace("json", "").replace("`", "")

        return model_output
    @staticmethod
    def checkMemoryAgentOutput(output):
        desierialized_output = json.loads(output)

        memory_status = desierialized_output["memory_agent_response"]
        return memory_status


    def retriveMemory(output, user_id):
        # desierialized_output = json.loads(output)
        # memory_description = desierialized_output["message"]
        try:
            retrieve_memory = retrieve_memory_from_databank(output, user_id)
            print(retrieve_memory)
            return retrieve_memory
        except:
            return "sorry, i was'nt able to fine this memory"
    
    @staticmethod
    def saveMemory(output, user_id):
        seved_memory_respone = save_memory_to_databank(output, user_id)
        return seved_memory_respone




    # short term memory services ///////////////
    @staticmethod
    def reset():
        reset_short_term_memory()

    @staticmethod
    def update(new_data, bin_id):
        update_session_history(new_data, bin_id)
        
    @staticmethod
    def get(bin_id):
        data = get_session_by_id(bin_id)
        return data
    
    @staticmethod
    def create():
        bin_id = create_bin()
        return bin_id
    
    


