"""
SCRIPT: concept_finder.py
ROLE: Semantic Entity Extractor (v1.0 Legacy)
STATUS: REVAMP REQUIRED

DESCRIPTION:
    Uses TF-IDF to identify significant phrases and suggested concepts from the Tome.

HFS v2.1 REVAMP DIRECTIVE:
    1. ONTOLOGY EXPANSION: Use this tool to identify *new* candidate entities for 
       the 'Meta/Aesthetic' layer of the Master Ontology.
    2. SCHEMATIC MATCHING: Compare extracted phrases against the 'Claim Statement' 
       fields in the Matrix.
"""

import os
import json
from sklearn.feature_extraction.text import TfidfVectorizer
import re
import nltk
from nltk.corpus import stopwords

# Download necessary NLTK data (only run once)
try:
    nltk.data.find('corpora/stopwords')
except nltk.downloader.DownloadError:
    nltk.download('stopwords')

# --- CONFIGURATION ---
TOME_PATH = 'tome/Tome.md'

# --- SCRIPT LOGIC ---

def extract_phrases(text, n_min=1, n_max=3):
    """Extracts n-grams (phrases) from text."""
    words = re.findall(r'\b\w+\b', text.lower())
    phrases = []
    for n in range(n_min, n_max + 1):
        for i in range(len(words) - n + 1):
            phrases.append(" ".join(words[i:i+n]))
    return phrases

def main():
    print("Starting concept extraction from Tome.md...")

    try:
        with open(TOME_PATH, 'r', encoding='utf-8') as f:
            tome_content = f.read()
    except UnicodeDecodeError:
        try:
            with open(TOME_PATH, 'r', encoding='latin-1') as f:
                tome_content = f.read()
        except Exception as e:
            print(f"Error: Could not read Tome.md with utf-8 or latin-1. Error: {e}")
            return
    except FileNotFoundError:
        print(f"Error: {TOME_PATH} not found.")
        return

    # Use TF-IDF to find important terms/phrases
    # We'll treat the entire tome as a single document for simplicity here
    # For true TF-IDF across multiple documents, we'd feed a list of doc contents.
    # Here, we're just finding important terms *within* the tome relative to common English words.
    
    # First, clean the text for better phrase extraction
    cleaned_text = re.sub(r'[\W_]+', ' ', tome_content.lower())

    # Extract 1, 2, and 3-word phrases
    phrases = extract_phrases(cleaned_text, n_min=1, n_max=3)
    
    if not phrases:
        print("No phrases extracted. Check Tome.md content.")
        return

    # Create a dummy corpus for TF-IDF (list of strings, here just one big string)
    corpus = [" ".join(phrases)]

    # Initialize TF-IDF Vectorizer
    stop_words = set(stopwords.words('english'))
    # Add some common game-related stopwords that aren't useful concepts
    stop_words.update(['game', 'games', 'player', 'players', 'chapter', 'part', 'mechanics', 'psychology', 'design', 'designing'])

    vectorizer = TfidfVectorizer(stop_words=list(stop_words), ngram_range=(1,3))
    tfidf_matrix = vectorizer.fit_transform(corpus)

    feature_names = vectorizer.get_feature_names_out()
    tfidf_scores = tfidf_matrix.sum(axis=0).tolist()[0]

    # Combine feature names and their TF-IDF scores
    term_scores = list(zip(feature_names, tfidf_scores))
    term_scores.sort(key=lambda x: x[1], reverse=True)

    print("\n--- Suggested Concepts (Top 50) ---")
    for term, score in term_scores[:50]:
        print(f"- {term} (Score: {score:.4f})")

    print("\nConsider adding these to your KEY_CONCEPTS list in knowledge_builder.py.")

if __name__ == '__main__':
    main()
