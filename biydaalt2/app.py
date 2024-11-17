from flask import Flask, request, jsonify
from collections import Counter
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import hunspell

app = Flask(__name__)

# Initialize Hunspell for spell-checking
hunspell_instance = hunspell.HunSpell('mn.dic', 'mn.aff') 

# Process Text Function
def process_text(text):
    # Spell-checking and underlining misspelled words
    def spell_check(text):
        words = text.split()
        misspelled = {}
        checked_text = []
        
        for word in words:
            if not hunspell_instance.spell(word):
                suggestion = hunspell_instance.suggest(word)
                misspelled[word] = suggestion[0] if suggestion else "No suggestion"
                checked_text.append(f"<u>{word}</u>")  # Underline misspelled word
            else:
                checked_text.append(word)

        checked_text = " ".join(checked_text)
        return checked_text, misspelled

    # Stemming and unique word counting
    def stem_words(text):
        stemmer = SnowballStemmer("mongolian")
        return [stemmer.stem(word) for word in text.split()]

    # Removing common stop words
    def remove_stopwords(words):
        stop_words = set(stopwords.words('mongolian'))
        return [word for word in words if word.lower() not in stop_words]

    # Counting unique words and finding top 10 frequent words
    def count_unique_words(words):
        return len(set(words))

    def get_top_10_words(words):
        common_words = Counter(words).most_common(10)
        return {word: freq for word, freq in common_words}

    # Full processing
    checked_text, misspelled_words = spell_check(text)
    stemmed_words = stem_words(text)
    filtered_words = remove_stopwords(stemmed_words)
    unique_word_count = count_unique_words(filtered_words)
    top_10_words = get_top_10_words(filtered_words)
    
    return {
        "processed_text": checked_text,
        "misspelled_words": misspelled_words,
        "unique_word_count": unique_word_count,
        "top_10_words": top_10_words
    }

# Flask route to process text
@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    text = data.get("text", "")
    result = process_text(text)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
