from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx
import matplotlib.pyplot as plt
import ast
import os

def extract_functions(filename):
    with open(filename, 'r') as f:
        tree = ast.parse(f.read())
    
    functions = {}
    
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            functions[node.name] = ast.dump(node)
    
    return functions

def naive_summarize(function_code):
    return function_code  # In a real-world scenario, you'd use NLP techniques here

def compare_summaries(summary1, summary2):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([summary1, summary2])
    return cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])[0][0]

def main():
    startpath = '/Users/quaidbulloch/Documents/Code/Recu/Sep5thStart'
    file_function_map = {}
    
    for root, dirs, files in os.walk(startpath):
        for f in files:
            if f.endswith('.py'):
                full_path = os.path.join(root, f)
                functions = extract_functions(full_path)
                file_function_map[full_path] = {name: naive_summarize(code) for name, code in functions.items()}
    
    G = nx.DiGraph()
    
    for file1, functions1 in file_function_map.items():
        for file2, functions2 in file_function_map.items():
            if file1 != file2:
                for name1, summary1 in functions1.items():
                    for name2, summary2 in functions2.items():
                        similarity = compare_summaries(summary1, summary2)
                        if similarity > 0.9:  # Threshold for considering functions to be similar
                            G.add_edge(file1, file2)
    
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', font_size=8, font_color='black', node_size=700, font_weight='bold', arrows=True)
    plt.show()

if __name__ == '__main__':
    main()
