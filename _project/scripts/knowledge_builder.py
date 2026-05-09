import os
import json
import re
from collections import defaultdict

# --- CONFIGURATION ---

# Directories
TOME_DIR = 'tome'
RESEARCH_DIR = 'research_assets/markdown_conversions'
OUTPUT_PATH = 'app/knowledge_graph.json'

# Pre-defined entities from the Tome_Prelude.md
# Using variations and lowercasing for better matching.
KEY_CONCEPTS = {
    "Progression without Interaction": ["progression without continuous player interaction", "progression without interaction"],
    "Automated Progression": ["automated progression"],
    "Interpassivity": ["interpassivity"],
    "Delegated Action": ["delegated action", "delegated play"],
    "Satire/Critique": ["satire", "satirical", "critique"],
    "Habit Formation": ["habit formation", "habit"],
    "Automation": ["automation", "automate"],
    "Exponential Growth": ["exponential growth"],
    "Prestige/Reset": ["prestige", "reset", "ascension", "new game+"],
    "Waiting": ["waiting", "wait"],
    "Operant Conditioning": ["operant conditioning"],
    "Optimization": ["optimization", "optimal", "optimizing", "efficiency"],
    "Attention Economy": ["attention economy"],
    "Idle Game": ["idle game"],
    "Incremental Game": ["incremental game"],
    "Player Engagement": ["player engagement", "engagement", "playing"],
    "Taxonomy": ["taxonomy"],
    "Compulsive Interactions": ["compulsive interactions", "compulsive", "interactions"],
    "Optimal Strategies": ["optimal strategies", "optimal", "strategies"],
    "Core Loop": ["core loop", "core"],
    "Resources (in-game)": ["resources", "resource"],
    "Interaction (general)": ["interaction"],
    # Games as concepts
    "Progress Quest": ["progress quest"],
    "Cow Clicker": ["cow clicker"],
    "Cookie Clicker": ["cookie clicker"],
    "Neko Atsume": ["neko atsume"],
    "Kittens Game": ["kittens game"]
}

# --- SCRIPT LOGIC ---

def get_document_list(directory, doc_type):
    """Gets a list of document dictionaries from a directory."""
    docs = []
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            docs.append({
                'id': filename,
                'type': doc_type,
                'path': os.path.join(directory, filename)
            })
    return docs

def analyze_documents(documents, concepts):
    """Analyzes documents to find concept mentions and create graph edges."""
    edges = []
    # A dictionary to hold term counts for each doc, to be added to node metadata
    doc_term_counts = defaultdict(lambda: defaultdict(int))

    for doc in documents:
        try:
            with open(doc['path'], 'r', encoding='utf-8') as f:
                content = f.read().lower() # Read and lowercase the content
        except UnicodeDecodeError:
            try:
                with open(doc['path'], 'r', encoding='latin-1') as f:
                    content = f.read().lower()
            except Exception as e:
                print(f"Warning: Could not read file {doc['path']} with utf-8 or latin-1. Skipping. Error: {e}")
                continue
        except IOError as e:
            print(f"Warning: Could not read file {doc['path']}. Skipping. Error: {e}")
            continue

        # Find mentions of other research papers (citations)
        for other_doc in documents:
            if doc['id'] == other_doc['id'] or doc['type'] != 'tome':
                continue

            # A simple citation is just mentioning the filename
            # We look for the filename without extension as a potential citation
            other_doc_id_no_ext = os.path.splitext(other_doc['id'])[0].lower()
            if other_doc_id_no_ext in content:
                 edges.append({
                    'source': doc['id'],
                    'target': other_doc['id'],
                    'type': 'cites',
                    'weight': 1 # Simple citation has a weight of 1
                })

        # Find mentions of key concepts
        for concept_name, variations in concepts.items():
            count = 0
            for term in variations:
                # Use regex to find whole words/phrases only to avoid partial matches
                count += len(re.findall(r'\b' + re.escape(term) + r'\b', content))
            
            if count > 0:
                edges.append({
                    'source': doc['id'],
                    'target': concept_name,
                    'type': 'mentions',
                    'weight': count
                })
                doc_term_counts[doc['id']][concept_name] = count

    return edges, doc_term_counts


def main():
    """Main function to build and save the knowledge graph."""
    print("Starting knowledge graph generation...")

    # 1. Get document lists
    tome_docs = get_document_list(TOME_DIR, 'tome')
    research_docs = get_document_list(RESEARCH_DIR, 'research')
    all_docs = tome_docs + research_docs

    # 2. Create nodes
    # Document nodes
    nodes = [{
        'id': doc['id'], 
        'type': doc['type'],
        'label': doc['id'].replace('.md', '').replace('_', ' ')
    } for doc in all_docs]
    
    # Concept nodes
    concept_nodes = [{
        'id': name, 
        'type': 'concept',
        'label': name
    } for name in KEY_CONCEPTS]
    
    nodes.extend(concept_nodes)

    # 3. Analyze and create edges
    edges, term_counts = analyze_documents(all_docs, KEY_CONCEPTS)

    # Optional: Add term counts to the node metadata
    for node in nodes:
        if node['id'] in term_counts:
            node['term_counts'] = dict(term_counts[node['id']]) # Convert defaultdict to dict for JSON serialization


    # 4. Assemble and save the graph
    knowledge_graph = {
        'nodes': nodes,
        'edges': edges
    }

    try:
        with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
            json.dump(knowledge_graph, f, indent=2)
        print(f"Successfully created knowledge graph at {OUTPUT_PATH}")
        print(f"Found {len(nodes)} nodes and {len(edges)} edges.")
    except IOError as e:
        print(f"Error: Could not write to output file {OUTPUT_PATH}. Error: {e}")


if __name__ == '__main__':
    main()
