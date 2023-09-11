import openai
import networkx as nx
import matplotlib.pyplot as plt
import ast
import os

# Initialize OpenAI API key and model engine
API_KEY = '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'
MODEL_ENGINE = 'gpt-4'  # or whatever engine you're using
openai.api_key = API_KEY

import time

def general_api_call(prompt, retries=3, delay=5):
    system_content = 'Please summarize the following code:'
    user_content = prompt

    for i in range(retries):
        try:
            # Make the API call
            response = openai.ChatCompletion.create(
                model=MODEL_ENGINE,
                messages=[
                    {'role': 'system', 'content': system_content},
                    {'role': 'user', 'content': user_content}
                ],
                max_tokens=1500
            )
            return response['choices'][0]['message']['content']
        except openai.error.RateLimitError as e:
            print(f"Rate limit exceeded. Retrying in {delay} seconds...")
            time.sleep(delay)


def extract_functions(filename):
    with open(filename, 'r') as f:
        tree = ast.parse(f.read())
    
    functions = {}
    
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            functions[node.name] = ast.dump(node)
    
    return functions

def compare_summaries(summary1, summary2):
    # You can use more advanced similarity metrics here
    return summary1 == summary2

def main():
    startpath = '/Users/quaidbulloch/Documents/Code/Recu/FileA'
    file_function_map = {}
    
    for root, dirs, files in os.walk(startpath):
        for f in files:
            if f.endswith('.py'):
                full_path = os.path.join(root, f)
                functions = extract_functions(full_path)
                file_function_map[full_path] = {name: general_api_call(code) for name, code in functions.items()}
    
    G = nx.DiGraph()
    
    for file1, functions1 in file_function_map.items():
        for file2, functions2 in file_function_map.items():
            if file1 != file2:
                for name1, summary1 in functions1.items():
                    for name2, summary2 in functions2.items():
                        if compare_summaries(summary1, summary2):
                            G.add_edge(file1, file2)
    
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', font_size=8, font_color='black', node_size=700, font_weight='bold', arrows=True)
    plt.show()

if __name__ == '__main__':
    main()
