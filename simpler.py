import openai
import re
import os

# Function to execute Python code
def execute_python_code(code):
    try:
        exec(code)
    except Exception as e:
        print(f"An error occurred while executing the code: {e}")

# Initialize OpenAI API
openai.api_key = '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'

# Read the script from a file
with open("/Users/quaidbulloch/Documents/Code/Recu/Sep7thStart/simpler.py", "r") as f:
    script = f.read()

# Define the model engine and prompt
MODEL_ENGINE = "gpt-4"  # Replace with your preferred model
PROMPT = script

def apiCall(prompt):
    model_engine = MODEL_ENGINE
    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=[
            {'role': 'system', 'content': script},
            {'role': 'user', 'content': 'Please extend, expand, broaden, and improve this code!'}
        ],
        max_tokens=1500
    )
    full_response = response['choices'][0]['message']['content']
    print(f"Generated Text: {full_response}")

    # Use regex to extract Python code enclosed in ```python ... ```
    code_match = re.search(r'```python(.*?)```', full_response, re.DOTALL)
    if code_match:
        executable_code = code_match.group(1).strip()
        print(f"Executing the following code:\n{executable_code}")
        execute_python_code(executable_code)
        
        # Write the executable code to a new file
        with open("latest_output_script.py", "w") as f:
            f.write(executable_code)
        print("The latest output script has been saved to 'latest_output_script.py'")
    else:
        print("No executable code found.")

# Call the apiCall function
apiCall(PROMPT)
