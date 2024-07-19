
import json
import hashlib as h

import requests


url = 'https://api.jsonbin.io/v3/b/668eb5d7acd3cb34a8641d4a'

headers = {
  'Content-Type': 'application/json',
  'X-Master-Key': '$2a$10$kzhtRfaa2pI4NMy2.D/Nseff7/O4FrURoNLIhc1Hs//IvOoAbidBG'
}


def get_session_by_id(user_id):
    try:
        req = requests.get(url, json=None, headers=headers)
        data = json.loads(req.text)['record']
        for session in data:
           
            if session[0]["user_id"] == user_id:
                return session[0]
       
        print(f"No session found with user_id: {user_id}")
        return None
    except:
        print("issue retrieving short term memory")
        return None   

def append_to_json_file(new_data):

    req = requests.put(url, json=[new_data], headers=headers)
    return True


def reset_short_term_memory():
    data = {
            "initial_state": True,
            "is_process_running": False,
            "current_action": None,
            "current_state": None,
            "states": [],
            "environment_state_actions_sequences": {},
        }
    req = requests.put(url, json=data, headers=headers)
    return True


def create_bin():
    initial_data = {
        "initial_state": True,
        "is_process_running": False,
        "parent": None,
        "current_state": None,
        "is_current_state_final_state": False,
        "states": [],
        "user_responses": {},
    }
    response = requests.post(url, json=initial_data, headers=headers)
    if response.status_code == 200:
        return response.json()["metadata"]["id"]
    else:
        raise Exception(f"Failed to create bin: {response.text}")









def hashblock(req):
    encoded_block = json.dumps(req, sort_keys=True).encode()
    block_encryption = h.sha256()
    block_encryption.update((encoded_block))
    return block_encryption.hexdigest()

