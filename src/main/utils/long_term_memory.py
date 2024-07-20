
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import json
from qdrant_client import QdrantClient

from .actor import take_action
from .settings import session_summarizer_system_prompt


client = QdrantClient(
    url="https://6cc54879-9ceb-47c6-8fcb-5c1ff9f3956a.us-east4-0.gcp.cloud.qdrant.io:6333", 
    api_key="eDw0HtaRX-uKeBClWZZ7Jxso3eitNpJe8t0V_HUdJmv24XcRJvepGw",
)


def save_memory_to_databank(memory_data, session_id):
   
    docs = [str(memory_data)]
    try:
        memory_to_save = json.loads(memory_data)

        metadata = [
            {"source": str(memory_to_save['memory_entities'])},
        ]
    except:
        metadata = [
            {"source": str(memory_data)},
        ]
    

    client.add(
    collection_name=str(session_id),
    documents=docs,
    metadata=metadata,
    )
    return "i have added the following memory to my memory bank: " + memory_data


def retrieve_memory_from_databank(memory_description, session_id):
    search_result = client.query(
    collection_name=str(session_id),
    query_text=memory_description,
    limit=6
    )
    return "i have searched my memory bank, and here is what i come up about the user memory reference: " +  search_result
    
        

def session_summarizer(session_data, system_prompt):
    session_summarizer_prompt = session_summarizer_system_prompt+session_data
    
    session_summary = take_action(session_summarizer_prompt, system_prompt)
    return session_summary
    