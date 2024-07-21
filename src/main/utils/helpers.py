import json
import ast


def convert_string_to_json(input_string):
    # Remove the <class 'str'> prefix if present
    cleaned_string = input_string.replace("<class 'str'>", "").strip()
    
    try:
        # Convert the string to a dictionary using ast.literal_eval
        dict_data = ast.literal_eval(cleaned_string)
        
        # Convert the dictionary to a JSON string
        json_string = json.dumps(dict_data, indent=2)
        # print(json_string, type(json_string))
        return json_string
    except (SyntaxError, ValueError) as e:
        return f"Error: Unable to convert the string to JSON. {str(e)}"