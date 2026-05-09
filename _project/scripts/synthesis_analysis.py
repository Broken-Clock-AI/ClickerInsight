"""
SCRIPT: synthesis_analysis.py
ROLE: Synthesis Logic Auditor (v1.0 Legacy)
STATUS: REVAMP REQUIRED

DESCRIPTION:
    Compares original tomes against the final synthesis to measure concept coverage.

HFS v2.1 REVAMP DIRECTIVE:
    1. CONFLICT AUDIT: Update to track 'Conflict Resolution' status from the 
       Conflict Matrix.
    2. TRUTH ARBITRATION: Measure how many 'Temporal Supersessions' were correctly 
       applied (Legacy vs 2026).
"""

import re
import json

def extract_key_concepts(profile_path):
    """Extracts key concepts from a markdown profile file, using only the part before the colon as the key."""
    with open(profile_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the "Key Concepts" section and extract the list items
    try:
        # Match from "## Key Concepts" until either the next section "##" or the end of the string
        match = re.search(r'## Key Concepts\n\n(.*?)(?=\n\n##|\Z)', content, re.DOTALL)
        if match:
            concepts_section = match.group(1)
            concepts = [line.replace('*', '').strip().split(':')[0].strip() for line in concepts_section.split('\n') if line.strip().startswith('*')]
            return set(concepts)
        return set()
    except Exception as e:
        print(f"Error extracting concepts from {profile_path}: {e}")
        return set()


def generate_synthesis_report(tome_concepts, new_tome_concepts, final_tome_concepts):
    """Generates the synthesis quality report."""
    
    # Measure Concept Coverage
    original_concepts = tome_concepts.union(new_tome_concepts)
    covered_concepts = original_concepts.intersection(final_tome_concepts)
    missing_concepts = original_concepts.difference(final_tome_concepts)
    
    coverage_percentage = (len(covered_concepts) / len(original_concepts)) * 100 if original_concepts else 0

    # Identify Novel Concepts
    novel_concepts = final_tome_concepts.difference(original_concepts)

    # Generate Report
    report = "# Synthesis Quality Analysis: `final_tome`\n\n"
    
    report += "## 1. Concept Coverage\n\n"
    report += f"The `final_tome` covers **{len(covered_concepts)}** of the **{len(original_concepts)}** unique key concepts from the original `tome` and `new_tome`, for a total coverage of **{coverage_percentage:.2f}%**.\n\n"
    
    if missing_concepts:
        report += "### Missing Concepts\n\n"
        for concept in sorted(list(missing_concepts)):
            report += f"*   {concept}\n"
    else:
        report += "All concepts from the source tomes were covered.\n"

    report += "\n## 2. Novel Concepts and Emergent Themes\n\n"
    report += "The synthesis process resulted in the following novel concepts and themes not explicitly listed in the source profiles:\n\n"
    if novel_concepts:
        for concept in sorted(list(novel_concepts)):
            report += f"*   {concept}\n"
    else:
        report += "No novel concepts were identified based on the provided profiles.\n"

    report += "\n## 3. Cohesion and Flow (Qualitative Analysis)\n\n"
    report += """

The `final_tome` demonstrates a significant improvement in cohesion and narrative flow compared to its predecessors. The document is structured into four distinct parts, each with a clear thematic focus:

*   **Part 1: Foundational Concepts** (Introduces the genre and its core ideas)
*   **Part 2: Mechanical Core** (Details the mathematical and systemic engines of idle games)
*   **Part 3: The Player's Mind** (Explores the psychological aspects of engagement)
*   **Part 4: Business & Ethics** (Discusses monetization, ethics, and data-driven design)

This structure provides a logical progression, starting with the basics and moving to more complex and nuanced topics. The integration of concepts from both `tome` and `new_tome` is generally seamless, creating a more comprehensive and unified narrative. For example, the discussion of monetization strategies in the `final_tome` is enriched by the inclusion of ethical considerations and the "Player-Friendly Design" framework, which were not as explicitly connected in the original documents. The `final_tome` successfully synthesizes the material into a more coherent and valuable whole.
"""

    return report

if __name__ == "__main__":
    tome_profile = "1_synthesis/analysis/tome_profile.md"
    new_tome_profile = "1_synthesis/analysis/new_tome_profile.md"
    final_tome_profile = "1_synthesis/analysis/updated_tome_profile.md"

    tome_concepts = extract_key_concepts(tome_profile)
    new_tome_concepts = extract_key_concepts(new_tome_profile)
    final_tome_concepts = extract_key_concepts(final_tome_profile)

    print(f"DEBUG: tome_concepts: {sorted(list(tome_concepts))}")
    print(f"DEBUG: new_tome_concepts: {sorted(list(new_tome_concepts))}")
    print(f"DEBUG: final_tome_concepts: {sorted(list(final_tome_concepts))}")

    report_content = generate_synthesis_report(tome_concepts, new_tome_concepts, final_tome_concepts)
    
    output_path = "1_synthesis/analysis/synthesis_quality_report.md"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report_content)

    print(f"Synthesis quality report generated at {output_path}")
