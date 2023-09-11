import os
import ast
import matplotlib.pyplot as plt
import networkx as nx

def analyze_file(filename):
    with open(filename, 'r') as f:
        tree = ast.parse(f.read())
    
    functions_called = []
    
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                functions_called.append(node.func.id)
            elif isinstance(node.func, ast.Attribute):
                functions_called.append(node.func.attr)
    
    return functions_called

def list_and_analyze_files(startpath):
    file_function_map = {}
    
    for root, dirs, files in os.walk(startpath):
        for f in files:
            if f.endswith('.py'):
                full_path = os.path.join(root, f)
                functions_called = analyze_file(full_path)
                file_function_map[full_path] = functions_called
                
    return file_function_map

def visualize_relationships(file_function_map):
    G = nx.DiGraph()
    
    for file, functions in file_function_map.items():
        G.add_node(file)
        for func in functions:
            if func in file_function_map:  # Assuming function names are unique and can identify files
                G.add_edge(file, func)
    
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', font_size=8, font_color='black', node_size=700, font_weight='bold')
    plt.show()

# Replace 'your_folder_path_here' with the path of the folder containing Python files
startpath = '/Users/quaidbulloch/Documents/Code/Recu/Sep5thStart'
file_function_map = list_and_analyze_files(startpath)
visualize_relationships(file_function_map)
