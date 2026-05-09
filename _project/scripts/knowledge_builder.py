"""
SCRIPT: knowledge_builder.py
ROLE: Relational Synthesis Engine (v1.0 Legacy)
STATUS: ACTIVE - PENDING UPGRADE TO HFS v2.1

DESCRIPTION:
    This script generates a 'Knowledge Graph' by scanning research documents for 
    predefined 'Key Concepts' and 'Citations'. It creates a JSON map used for 
    visualizing how various papers and theories connect.

LEGACY LOGIC:
    - Performs regex-based frequency counting for a hardcoded concept dictionary.
    - Maps relationships based on 'mentions' (Concept -> Doc) and 'cites' (Doc -> Doc).

HFS v2.1 REVAMP DIRECTIVE (STRICT):
    1. SCHEMA EXTRACTION: Transition from keyword counting to YAML Claim Schema parsing.
    2. CONFLICT MAPPING: Automate the population of the 'Conflict Matrix' by detecting 
       overlapping Claim IDs with divergent 'statement' or 'variable' data.
    3. ONTOLOGY VALIDATION: Verify that every 'Entity' in the content maps to the 
       defined Master Plan Ontology (Resource, Generator, etc.).
    4. CONFIDENCE WEIGHTING: Replace raw frequency weights with the HFS Consensus Score.
"""

import os
import json
import re
from collections import defaultdict

# --- CONFIGURATION ---

# Directories
TOME_DIR = 'tome'
RESEARCH_DIR = 'research_assets/markdown_conversions'
OUTPUT_PATH = 'app/knowledge_graph.json'

# Pre-defined entities used for relational mapping.
# v2.1 Note: This should move to an external YAML ontology file.
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
    # Games used as conceptual anchors
    "Progress Quest": ["progress quest"],
    "Cow Clicker": ["cow clicker"],
    "Cookie Clicker": ["cookie clicker"],
    "Neko Atsume": ["neko atsume"],
    "Kittens Game": ["kittens game"]
}

# --- SCRIPT LOGIC ---

def get_document_list(directory, doc_type):
    """
    Scans a directory for Markdown files and returns a structured list of document objects.
    """
    docs = []
    if not os.path.exists(directory):
        return docs
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            docs.append({
                'id': filename,
                'type': doc_type,
                'path': os.path.join(directory, filename)
            })
    return docs

def analyze_documents(documents, concepts):
    """
    The core analytical loop.
    1. Scans document content for other document IDs (citations).
    2. Scans for 'Key Concept' clusters via Regex.
    3. Weights relationships based on frequency (Legacy).
    """
    edges = []
    doc_term_counts = defaultdict(lambda: defaultdict(int))

    for doc in documents:
        try:
            with open(doc['path'], 'r', encoding='utf-8') as f:
                content = f.read().lower() 
        except Exception:
            continue

        # CITATION DETECTION (Legacy)
        for other_doc in documents:
            if doc['id'] == other_doc['id'] or doc['type'] != 'tome':
                continue

            other_doc_id_no_ext = os.path.splitext(other_doc['id'])[0].lower()
            if other_doc_id_no_ext in content:
                 edges.append({
                    'source': doc['id'],
                    'target': other_doc['id'],
                    'type': 'cites',
                    'weight': 1 
                })

        # CONCEPT CLUSTERING (Legacy)
        for concept_name, variations in concepts.items():
            count = 0
            for term in variations:
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
    """
    Orchestrates the build process and saves the final JSON graph.
    """
    print("Starting knowledge graph generation...")

    # 1. Gather all documents from Tome and Research dirs
    tome_docs = get_document_list(TOME_DIR, 'tome')
    research_docs = get_document_list(RESEARCH_DIR, 'research')
    all_docs = tome_docs + research_docs

    # 2. Initialize Nodes (Docs + Concepts)
    nodes = [{
        'id': doc['id'], 
        'type': doc['type'],
        'label': doc['id'].replace('.md', '').replace('_', ' ')
    } for doc in all_docs]
    
    concept_nodes = [{
        'id': name, 
        'type': 'concept',
        'label': name
    } for name in KEY_CONCEPTS]
    
    nodes.extend(concept_nodes)

    # 3. Create Edges via Relationship Analysis
    edges, term_counts = analyze_documents(all_docs, KEY_CONCEPTS)

    # 4. Final Assembly
    for node in nodes:
        if node['id'] in term_counts:
            node['term_counts'] = dict(term_counts[node['id']])

    knowledge_graph = {
        'nodes': nodes,
        'edges': edges
    }

    # Save to path (typically consumed by a visualization app)
    try:
        os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
        with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
            json.dump(knowledge_graph, f, indent=2)
        print(f"Successfully created knowledge graph at {OUTPUT_PATH}")
        print(f"Found {len(nodes)} nodes and {len(edges)} edges.")
    except IOError as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    main()
