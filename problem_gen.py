import os
import json
import openai 
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


json_collection = []
def get_folder_path(folder_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory containing the script
    dir_path = os.path.join(script_dir, "raw_problems", folder_name)  # Build the desired path
    
    # Check if the folder exists
    if not os.path.exists(dir_path):
        print(f"The folder {dir_path} does not exist.")
        return None
    
    return dir_path

def convert(problem):
    prompt = '''
    {
	"identifier": "add_numbers",
	"description": "Write a function to add two numbers.",
	"function_prototype": {
		"function_name": "add",
		"parameters": [{"name": "a", "type": "int"}, {"name": "b", "type": "int"}],
		"return_values": [{"type": "int"}]
	},
	"correctness_test_suite": [
		{"input": {"a": 1, "b": 2}, "expected_output": [3]},
		{"input": {"a": -1, "b": 2}, "expected_output": [1]}
	],
	"tags": ["Arithmetic", "Easy"],
	"prompts": [
		{
			"prompt_id": "detailed_prompt",
			"prompt": "Write a function named 'add' that takes two integer arguments, 'a' and 'b', and returns their sum as an integer."
		}
	]
} 

Here is an example problem description. 

Can you generate a problem following format for the JSON file below?
Only return the JSON file, no other words.
Make sure the format is a correct json that can loaded with python json library.
    '''

    prompt = prompt + "\n" + str(problem)

    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        max_tokens=1000,
        messages = messages)
    
    # Extract the generated code
    response = str(response.choices[0].message.content.strip())
    
    print(response)
    new_json_obj = json.loads(response)  

    json_collection.append(new_json_obj)


    

def parse_json_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for problem in data:  # Assuming each item in data is a problem
                    convert(problem)  # Call convert function for each problem

if __name__ == "__main__":
    folder_name = input("Please enter the input folder name: ")
    folder_path = get_folder_path(folder_name)
    if folder_path:
        parse_json_files(folder_path)

    with open('edited_jsons.json', 'w') as file:
        json.dump(json_collection, file, indent=4)
    
    

    
