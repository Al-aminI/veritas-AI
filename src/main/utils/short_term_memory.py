
import json
import hashlib as h

import requests


base_url = 'https://api.jsonbin.io/v3/b'

headers = {
  'Content-Type': 'application/json',
  'X-Master-Key': '$2a$10$kzhtRfaa2pI4NMy2.D/Nseff7/O4FrURoNLIhc1Hs//IvOoAbidBG'
}


def get_session_by_id(bin_id):
  
    url = f"{base_url}/{bin_id}"
    req = requests.get(url, json=None, headers=headers)
    if req.status_code == 200:
        # print(req.json())
        return req.json()["record"]
    else:
        raise Exception(f"Failed to load data: {req.text}")
      

def update_session_history(new_data, bin_id):
    url = f"{base_url}/{bin_id}"
    req = requests.put(url, json=new_data, headers=headers)
    return True


def reset_short_term_memory(bin_id):
    data = {
        "conversation_history": "not_given",
        "user_prompt": "not_given",
        "recent_response": "not_given",
        "context": "not_given",
        "current_webpage": "not_given",
        "list_of_all_webpages": "not_given",
        "your_response": "not_given",
        "next_webpage_to_navigate_to": "not_given"
    }
    url = f"{base_url}/{bin_id}"
    req = requests.put(url, json=data, headers=headers)
    return True


def create_bin():
    initial_data = {
        "conversation_history": "not_given",
        "user_prompt": "not_given",
        "recent_response": "not_given",
        "context": "not_given",
        "current_webpage": "not_given",
        "list_of_all_webpages": "not_given",
        "ai_response": "not_given",
        "next_webpage_to_navigate_to": "not_given"
        
    }
    
    response = requests.post(base_url, json=initial_data, headers=headers)
    if response.status_code == 200:
        return response.json()["metadata"]["id"]
    else:
        raise Exception(f"Failed to create bin: {response.text}")









def hashblock(req):
    encoded_block = json.dumps(req, sort_keys=True).encode()
    block_encryption = h.sha256()
    block_encryption.update((encoded_block))
    return block_encryption.hexdigest()

