import os
import requests
import pandas as pd
from bs4 import BeautifulSoup
from textblob import TextBlob
from nltk.tokenize import sent_tokenize
import nltk

# Ensure required NLTK data packages are downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Define utility functions
def load_words(file_path):
    try:
        with open(file_path, 'r') as file:
            words = set(word.strip() for word in file.readlines())
            print(f"Loaded {len(words)} words from {file_path}")
            return words
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return set()

def load_specific_stopwords(folder_path, filenames):
    stopwords = set()
    try:
        for filename in filenames:
            file_path = os.path.join(folder_path, filename)
            stopwords.update(load_words(file_path))
        print(f"Loaded {len(stopwords)} stopwords from {folder_path}")
    except Exception as e:
        print(f"Error reading stopwords from {folder_path}: {e}")
    return stopwords

def save_text_to_file(text, file_path):
    with open(file_path, 'w') as file:
        file.write(text)

def extract_article_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find('h1').text if soup.find('h1') else ''
    paragraphs = soup.find_all('p')
    article_text = ' '.join([para.text for para in paragraphs])
    return title, article_text

def count_syllables(word):
    vowels = "aeiouy"
    word = word.lower().strip()
    count = 0
    if word and word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("e"):
        count -= 1
    if count == 0:
        count += 1
    return count

def analyze_text(text, positive_words, negative_words, stopwords):
    blob = TextBlob(text)
    words = [word for word in blob.words if word.lower() not in stopwords]
    positive_score = sum(1 for word in words if word in positive_words)
    negative_score = sum(1 for word in words if word in negative_words)
    polarity_score = blob.sentiment.polarity
    subjectivity_score = blob.sentiment.subjectivity
    sentences = sent_tokenize(text)
    complex_words = [word for word in words if len(word) > 2]
    
    avg_sentence_length = len(words) / len(sentences) if sentences else 0
    percentage_of_complex_words = len(complex_words) / len(words) if words else 0
    fog_index = 0.4 * (avg_sentence_length + percentage_of_complex_words)
    avg_number_of_words_per_sentence = avg_sentence_length
    complex_word_count = len(complex_words)
    word_count = len(words)
    syllables_per_word = sum(count_syllables(word) for word in words) / len(words) if words else 0
    personal_pronouns = sum(1 for word in words if word.lower() in ["i", "we", "my", "ours", "us"])
    avg_word_length = sum(len(word) for word in words) / len(words) if words else 0
    
    return {
        'POSITIVE SCORE': positive_score,
        'NEGATIVE SCORE': negative_score,
        'POLARITY SCORE': polarity_score,
        'SUBJECTIVITY SCORE': subjectivity_score,
        'AVG SENTENCE LENGTH': avg_sentence_length,
        'PERCENTAGE OF COMPLEX WORDS': percentage_of_complex_words,
        'FOG INDEX': fog_index,
        'AVG NUMBER OF WORDS PER SENTENCE': avg_number_of_words_per_sentence,
        'COMPLEX WORD COUNT': complex_word_count,
        'WORD COUNT': word_count,
        'SYLLABLE PER WORD': syllables_per_word,
        'PERSONAL PRONOUNS': personal_pronouns,
        'AVG WORD LENGTH': avg_word_length
    }

# Load input data
input_file_path = 'C:\\Users\\sreya\\OneDrive\\Desktop\\Deliverable\\Input.xlsx'  # Update the path as needed
input_df = pd.read_excel(input_file_path)

# Load positive and negative word dictionaries from the master dictionary folder
master_dictionary_folder_path = 'C:\\Users\\sreya\\OneDrive\\Desktop\\Deliverable\\MasterDictionary'  # Update the path as needed
positive_words_path = os.path.join(master_dictionary_folder_path, 'positive-words.txt')
negative_words_path = os.path.join(master_dictionary_folder_path, 'negative-words.txt')
positive_words = load_words(positive_words_path)
negative_words = load_words(negative_words_path)

# Load specific stopwords from the specified folder
stopwords_folder_path = 'C:\\Users\\sreya\\OneDrive\\Desktop\\Deliverable\\StopWords'  # Update the path as needed
stopword_filenames = [
    'StopWords_Currencies.txt',
    'StopWords_Auditor.txt',
    'StopWords_DatesandNumbers.txt',
    'StopWords_Generic.txt',
    'StopWords_GenericLong.txt',
    'StopWords_Geographic.txt',
    'StopWords_Names.txt'
]  # List your stopword filenames here
stopwords = load_specific_stopwords(stopwords_folder_path, stopword_filenames)

# Extract articles
articles = []
for _, row in input_df.iterrows():
    url_id = row['URL_ID']
    url = row['URL']
    title, text = extract_article_content(url)
    articles.append((url_id, url, title, text))

# Save extracted articles (if needed)
articles_df = pd.DataFrame(articles, columns=['URL_ID', 'URL', 'Title', 'Text'])
articles_df.to_csv('extracted_articles.csv', index=False)

# Analyze extracted articles
analysis_results = []
for _, row in articles_df.iterrows():
    analysis = analyze_text(row['Text'], positive_words, negative_words, stopwords)
    analysis['URL_ID'] = row['URL_ID']
    analysis['URL'] = row['URL']
    analysis_results.append(analysis)

# Save analysis results
analysis_df = pd.DataFrame(analysis_results)
analysis_df = analysis_df[['URL_ID', 'URL', 'POSITIVE SCORE', 'NEGATIVE SCORE', 'POLARITY SCORE', 'SUBJECTIVITY SCORE', 
                           'AVG SENTENCE LENGTH', 'PERCENTAGE OF COMPLEX WORDS', 'FOG INDEX', 'AVG NUMBER OF WORDS PER SENTENCE', 
                           'COMPLEX WORD COUNT', 'WORD COUNT', 'SYLLABLE PER WORD', 'PERSONAL PRONOUNS', 'AVG WORD LENGTH']]
analysis_df.to_excel('analysis_results.xlsx', index=False)

# Display the first few rows of the analysis results
print(analysis_df.head())
