import os
import json
import openai 
from dotenv import find_dotenv, load_dotenv
from schema import main_schema, test_case_schema, prompt_schema
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


#things to add: multi threading so this doesn't take forever
def convert(problem, number, output_name):
    print(problem)
    completion = openai.ChatCompletion.create(
    model="gpt-4-0613",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Generate entries in the schema. Use the following data to create the entries. DO NOT follow the data's format: " + "\n" + str(problem)},
    ],
    functions=[{"name": "generate_schema", "parameters": main_schema}],
    function_call={"name": "generate_schema"},
    temperature=0,
    )

    main_json = (completion.choices[0].message.function_call.arguments)
    main_json = json.loads(main_json)

    completion = openai.ChatCompletion.create(
    model="gpt-4-0613",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Generate entries in the schema. Use the following data to create the entries. DO NOT follow the data's format: " + "\n" + str(problem)},
    ],
    functions=[{"name": "generate_schema", "parameters": test_case_schema}],
    function_call={"name": "generate_schema"},
    temperature=0,
    )

    test_json = (completion.choices[0].message.function_call.arguments)
    test_json = json.loads(test_json)

    
    completion = openai.ChatCompletion.create(
    model="gpt-4-0613",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Generate entries in the schema. Use the following data to create the entries. DO NOT follow the data's format: " + "\n" + str(problem)},
    ],
    functions=[{"name": "generate_schema", "parameters": prompt_schema}],
    function_call={"name": "generate_schema"},
    temperature=0,
    )

    prompt_json = (completion.choices[0].message.function_call.arguments)
    prompt_json = json.loads(prompt_json)

    combined_json = {**main_json, **test_json, **prompt_json}

    dir_path = './problem_sets/' + output_name + '/problems'
    json_string = 'problem' + str(number) + '.json'
    os.makedirs(dir_path, exist_ok=True)

    file_path = os.path.join(dir_path, json_string)

    with open(file_path, 'w') as file:
        json.dump(combined_json, file, indent=4)


#Converts a JSON file into our schema.
#We only need a one sentence description so this input can be changed to fit any type of data
def parse_json_files(folder_path, output_name):
    count = 1
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for problem in data:  # Assuming each item in data is a problem
                    convert(problem["description"], count, output_name)  # Call convert function for each problem
                    count += 1

if __name__ == "__main__":
    folder_name = input("Please enter the input folder name: ")

    output_name = input("Please enter the output folder name: ")
    #print(folder_name)
    #folder_name = "test_problems"
    folder_path = get_folder_path(folder_name)

    if folder_path:
        json_collection = parse_json_files(folder_path, output_name)
    else:
        print("Folder does not exist.")

    

    
