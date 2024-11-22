import os
import re
import json
import traceback
from collections import Counter

from flask import Flask, render_template, request, jsonify
import regex

# Machine Learning content classification (optional)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

try:
    from spylls.hunspell import Dictionary
except ImportError:
    print("Spylls Hunspell library not found. Please install using: pip install spylls")
    Dictionary = None

app = Flask(__name__)

# Advanced content classification model
class ContentClassifier:
    def __init__(self):
        # Predefined categories and training data
        self.categories = [
            'Эдийн засаг', 
            'Спорт', 
            'Улс төр', 
            'Соёл', 
            'Технологи'
        ]
        
        # Sample training texts for each category
        self.training_data = {
            'Эдийн засаг': [
                'валют', 'хөрөнгө', 'зах зээл', 'эдийн засаг', 
                'орлого', 'зардал', 'бизнес', 'хөгжил'
            ],
            'Спорт': [
                'тив', 'тоглолт', 'өрсөлдөөн', 'спорт', 
                'тамир', 'дасгал', 'тэмцээн', 'хол'
            ],
            'Улс төр': [
                'улс', 'төр', 'сонгууль', 'засгийн газар', 
                'бодлого', 'улсын', 'хууль'
            ],
            'Соёл': [
                'соёл', 'урлаг', 'уран', 'дуу', 'дуурсгал', 
                'өв', 'уламжлал'
            ],
            'Технологи': [
                'технологи', 'компьютер', 'сүлжээ', 'интернет', 
                'инновац', 'сервер', 'программ'
            ]
        }
        
        self.vectorizer = TfidfVectorizer()
        self.classifier = MultinomialNB()
        
        self._train()
    
    def _train(self):
        # Prepare training data
        texts = []
        labels = []
        
        for category, keywords in self.training_data.items():
            for keyword in keywords:
                texts.append(keyword)
                labels.append(category)
        
        X = self.vectorizer.fit_transform(texts)
        self.classifier.fit(X, labels)
    
    def predict_category(self, text):
        try:
            # Vectorize input text
            text_vector = self.vectorizer.transform([text])
            prediction = self.classifier.predict(text_vector)
            return prediction[0]
        except Exception:
            return "Ерөнхий мэдээлөл"

# Global instances
content_classifier = ContentClassifier()

# Dictionary loading
def load_hunspell_dictionary():
    try:
        dict_path = os.path.join(os.path.dirname(__file__), 'mn')
        aff_file = dict_path + '.aff'
        dic_file = dict_path + '.dic'
        
        if not (os.path.exists(aff_file) and os.path.exists(dic_file)):
            print(f"Dictionary files not found. Paths checked: {aff_file}, {dic_file}")
            return None
        
        return Dictionary.from_files(dict_path)
    except Exception as e:
        print(f"Dictionary Loading Error: {e}")
        return None

# Global Hunspell instance
hunspell_instance = load_hunspell_dictionary()

# Advanced stop words
STOP_WORDS = {
    'ба', 'болон', 'гэх', 'тэр', 'энэ', 'байна', 'юм', 'байх', 
    'нь', 'гэж', 'хүн', 'бол', 'хэрэг', 'үед', 'хамаагүй', 
    'биш', 'юу', 'хэн', 'хаана', 'яагаад', 'яах', 'яг'
}

def count_mongolian_words(text):
    """
    More robust word counting for Mongolian text
    Considers Mongolian words and handles various text scenarios
    """
    # Use regex to find all Mongolian words, filtering out very short tokens
    words = [word for word in regex.findall(r'\p{Mongolian}+', text) if len(word) > 1]
    return len(words)

def stem_word(word):
    """Advanced word stemming."""
    if hunspell_instance:
        try:
            stems = hunspell_instance.stem(word)
            return stems[0] if stems else word
        except Exception:
            return word
    return word

def process_text_analytics(text):
    """Comprehensive text processing."""
    # Tokenization
    words = regex.findall(r'\p{Mongolian}+', text.lower())
    
    # Remove stop words and stem
    processed_words = [
        stem_word(word) 
        for word in words 
        if word not in STOP_WORDS
    ]
    
    # Analytics
    unique_words = set(processed_words)
    word_freq = Counter(processed_words)
    
    # Top words excluding any remaining stop words
    top_words = {
        word: count 
        for word, count in word_freq.most_common(10) 
        if word not in STOP_WORDS
    }
    
    # Misspelled words detection
    misspelled = {}
    if hunspell_instance:
        misspelled = {
            word: hunspell_instance.suggest(word)[:3] 
            for word in words 
            if not hunspell_instance.spell(word)
        }
    
    return {
        'unique_word_count': len(unique_words),
        'top_words': top_words,
        'misspelled_words': misspelled,
        'content_category': content_classifier.predict_category(text)
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def text_processor():
    try:
        # Input validation
        data = request.get_json()
        if not data or 'text' not in data:
            return jsonify({"error": "No text provided"}), 400
        
        # Debugging: Log the received text
        print(f"Received text: {data['text'][:100]}...")  # Log first 100 chars

        text = data['text']
        
        # Improved word count check
        word_count = count_mongolian_words(text)
        print(f"Word count: {word_count}")  # Log word count for debugging
        
        if word_count < 300:
            return jsonify({
                "error": f"Insufficient text length. Minimum 300 words required. Current: {word_count}"
            }), 400
        
        # Process text
        results = process_text_analytics(text)
        
        return jsonify(results)
    
    except Exception as e:
        # Comprehensive error logging
        app.logger.error(f"Processing Error: {traceback.format_exc()}")
        return jsonify({
            "error": "Text Processing Failed",
            "details": str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
