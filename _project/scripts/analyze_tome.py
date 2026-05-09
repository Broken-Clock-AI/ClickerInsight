
import os
import re
import json
from collections import defaultdict

def analyze_tome(directory_path):
    """
    Analyzes the text files in a given directory to extract key concepts,
    word count, chapter count, and unique source citations.
    """
    analysis = {
        "chapter_count": 0,
        "total_word_count": 0,
        "key_concepts": [],
        "source_citations": [],
    }

    # First pass: Read all files and get raw data
    all_text = ""
    file_paths = sorted([os.path.join(directory_path, f) for f in os.listdir(directory_path) if f.endswith('.md')])
    
    analysis["chapter_count"] = len(file_paths)

    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            all_text += content + "\n\n"
            analysis["total_word_count"] += len(content.split())

    # Extract key concepts (bolded words/phrases)
    key_concepts = re.findall(r'\*\*(.*?)\*\*', all_text)
    # Filter out short/unlikely concepts and clean up
    analysis["key_concepts"] = sorted(list(set([concept.strip() for concept in key_concepts if len(concept.strip().split()) > 1 and len(concept.strip()) > 5])))

    # Extract source citations (heuristic: look for names with years, like "(Author, 2024)" or "[Author et al., 2024]")
    citations = re.findall(r'\[(.*?)\]|\((.*?)\)', all_text)
    
    potential_citations = []
    for citation_tuple in citations:
        for citation in citation_tuple:
            if citation:
                # A simple check for something that looks like a citation
                if re.search(r'\d{4}', citation) and re.search(r'[a-zA-Z]', citation):
                     potential_citations.append(citation.strip())

    analysis["source_citations"] = sorted(list(set(potential_citations)))

    return analysis

def format_profile(analysis, tome_name):
    """Formats the analysis into a markdown profile."""
    profile = f"# Profile of `{tome_name}`\n\n"
    profile += f"## Quantitative Analysis\n\n"
    profile += f"*   **Chapter Count:** {analysis['chapter_count']}\n"
    profile += f"*   **Total Word Count:** {analysis['total_word_count']}\n"
    profile += f"*   **Unique Source Citations:** {len(analysis['source_citations'])}\n\n"

    profile += "## Key Concepts\n\n"
    for concept in analysis['key_concepts']:
        profile += f"*   {concept}\n"
    
    profile += "\n## Source Citations\n\n"
    if analysis['source_citations']:
        for citation in analysis['source_citations']:
            profile += f"*   {citation}\n"
    else:
        profile += "*No explicit source citations found.*\n"

    return profile

if __name__ == "__main__":
    tome_directory = "PAPERS_SYNTHESIZED/final_tome"
    final_tome_analysis = analyze_tome(tome_directory)
    
    profile_content = format_profile(final_tome_analysis, "final_tome")

    output_path = "analysis/final_tome_profile.md"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(profile_content)

    print(f"Analysis complete. Profile saved to {output_path}")
    # Print analysis as JSON to stdout to be captured
    print("\n---JSON-ANALYSIS---")
    print(json.dumps(final_tome_analysis, indent=2))
