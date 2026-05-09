import json
import sys
import re

def clean_game_title(title):
    #- (the) Gnorp Apologue
    # Egg, Inc.
    title = title.strip()
    if title.startswith('- '):
        title = title[2:]
    # remove punctuation that might mess up matching
    title = re.sub(r'[,.!:®™]', '', title)
    return title.strip()

def rank_games(game_titles_file, content_file):
    """
    Ranks games by their frequency of mention in a given text file.
    """
    game_counts = {}
    with open(game_titles_file, 'r', encoding='utf-8') as f:
        # Initializing game_counts with 0 for each game
        for line in f:
            if line.strip() and not line.startswith('#'):
                title = clean_game_title(line)
                game_counts[title] = 0

    with open(content_file, 'r', encoding='utf-8') as f:
        content = f.read()
        for game in game_counts.keys():
            # Using regex to find whole word matches, case-insensitive
            # The game title is escaped to handle special regex characters
            matches = re.findall(r'\b' + re.escape(game) + r'\b', content, re.IGNORECASE)
            game_counts[game] = len(matches)

    return game_counts

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python rank_games.py <game_titles_file> <content_file>")
        sys.exit(1)

    game_titles_file = sys.argv[1]
    content_file = sys.argv[2]
    
    ranked_games = rank_games(game_titles_file, content_file)
    
    print(json.dumps(ranked_games, indent=2))
