from flask import Flask, request, jsonify, render_template
import re
from collections import Counter
from difflib import get_close_matches

app = Flask(__name__)

# Load dictionary files directly with better error handling
def load_dictionary():
    words = set()
    try:
        with open('mn.dic', 'r', encoding='utf-8') as f:
            # Skip the first line (contains count)
            next(f)
            for line in f:
                # Remove flags and get only the word
                word = line.strip().split('/')[0].lower()
                if word and len(word) > 1:  # Skip empty or single-letter words
                    words.add(word)
    except Exception as e:
        print(f"Error loading dictionary: {e}")
        words = set()
    return words

MONGOLIAN_WORDS = load_dictionary()

# Common Mongolian stop words (түгээмэл үгс)
STOP_WORDS = set(['юм', 'бөгөөд', 'ба', 'гэх', 'мөн', 'нь', 'энэ', 'тэр', 'байна', 'болон'])

# Simple category mapping
CATEGORIES = {
    'эдийн засаг': ['мөнгө', 'банк', 'зах зээл', 'эдийн засаг', 'бизнес', 'төгрөг', 'валют', 'хөрөнгө'],
    'спорт': ['хөл бөмбөг', 'тэмцээн', 'медаль', 'тамирчин', 'спорт', 'бөмбөг', 'наадам', 'барилдаан'],
    'улс төр': ['засгийн газар', 'парламент', 'сонгууль', 'улс төр', 'гишүүн', 'хурал', 'төрийн'],
    'боловсрол': ['сургууль', 'оюутан', 'багш', 'боловсрол', 'сурагч', 'хичээл'],
}

# Improved word suggestion function
def suggest_words(word):
    """Enhanced word suggestion algorithm"""
    word = word.lower()
    suggestions = set()
    
    # 1. Direct dictionary lookup
    if word in MONGOLIAN_WORDS:
        return [word]
    
    # 2. Use get_close_matches for better suggestions
    close_matches = get_close_matches(word, MONGOLIAN_WORDS, n=5, cutoff=0.7)
    suggestions.update(close_matches)
    
    # 3. Character-based suggestions
    if len(suggestions) < 5:
        for dict_word in MONGOLIAN_WORDS:
            # Only check words of similar length
            if abs(len(dict_word) - len(word)) <= 1:
                # Check for one character difference or transposition
                diff = 0
                for i in range(min(len(word), len(dict_word))):
                    if i < len(word) and i < len(dict_word) and word[i] != dict_word[i]:
                        diff += 1
                if diff <= 1:
                    suggestions.add(dict_word)
                
                # Check for character transposition
                if len(word) == len(dict_word):
                    for i in range(len(word)-1):
                        if word[i:i+2] == dict_word[i+1] + dict_word[i]:
                            suggestions.add(dict_word)
    
    return list(suggestions)[:5]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_text():
    data = request.get_json()
    text = data.get('text', '')
    
    if not text or len(text.strip()) == 0:
        return jsonify({
            'misspelled': [],
            'unique_words': 0,
            'top_words': [],
            'category': 'бусад'
        })
    
    # Improved word splitting
    misspelled = []
    current_position = 0
    
    # Split text into words while preserving positions
    words = re.finditer(r'[а-яөүёА-ЯӨҮЁ]+', text)
    
    for match in words:
        word = match.group()
        start = match.start()
        end = match.end()
        
        # Only check words longer than 1 character
        if len(word) > 1 and word.lower() not in MONGOLIAN_WORDS:
            suggestions = suggest_words(word)
            if suggestions and suggestions[0] != word.lower():
                misspelled.append({
                    'word': word,
                    'start': start,
                    'end': end,
                    'suggestions': suggestions
                })

    # Word frequency analysis (excluding stop words)
    words = [word.lower() for word in re.findall(r'[а-яөүёА-ЯӨҮЁ]+', text)]
    words = [word for word in words if word not in STOP_WORDS and len(word) > 1]
    
    unique_words = len(set(words))
    word_freq = Counter(words)
    top_words = word_freq.most_common(10)
    
    category = classify_text(text)

    return jsonify({
        'misspelled': misspelled,
        'unique_words': unique_words,
        'top_words': top_words,
        'category': category
    })

def classify_text(text):
    text_lower = text.lower()
    max_score = 0
    text_category = 'бусад'
    
    for category, keywords in CATEGORIES.items():
        score = sum(1 for keyword in keywords if keyword in text_lower)
        if score > max_score:
            max_score = score
            text_category = category
    
    return text_category

if __name__ == '__main__':
    app.run(debug=True)
