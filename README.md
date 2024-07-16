# Instructions to Run the Script


## Task Assigned by <a href='https://blackcoffer.com'>Black Coffer</a>


## Data Extraction and NLP

This project aims to extract textual data articles from given URLs and perform text analysis to compute variables in Python. The code is also written in Colab Notebook for its flexibility compared to scripting.


## Prerequisites
- Ensure you have Python 3.x installed.

- Install the required libraries using the following command:

  ```sh
  pip install requests pandas beautifulsoup4 textblob nltk openpyxl
  ```


## Approach

The project follows the following steps:

1. Extracting the data from the given URLs using the BeautifulSoup library (Web Scraping).

2. Cleaning the data by removing the HTML tags and converting the text to lowercase.

    - Find the title of the article using the `<h1>` tag and obtain the content using the `<div>` tag and class name selectors.
    - Since different articles may have different class selectors, try-except blocks are used to handle any exceptions.

3. Tokenizing the text into individual words and removing the stop words.
4. Performing sentiment analysis using the TextBlob library.
5. Computing the sentiment score and polarity of the text.
6. Saving the results in a CSV file.


## How to Run

- Place the main.py script in the working directory.
- Update the paths in the script to point to the input Excel file and the folders containing the positive/negative words and stopwords.
- Run the script using the following command:

```sh
python main.py
```
- The script will generate an analysis_results.xlsx file containing the analysis results.


## Functionality

### Main Script (`main.py`)
- **load_words(file_path, encoding='utf-8')**: Reads words from a file and returns a set of words. Handles different file encodings.
- **load_specific_stopwords(folder_path, filenames, encoding='utf-8')**: Reads stopwords from multiple files and returns a set of stopwords. Handles different file encodings.
- **save_text_to_file(text, file_path)**: Saves text to a file.
- **extract_article_content(url)**: Extracts the title and content of an article from a given URL.
- **count_syllables(word)**: Counts the number of syllables in a word.
- **analyze_text(text, positive_words, negative_words, stopwords)**: Analyzes text and calculates various linguistic and sentiment metrics.
- **main workflow**: Reads input data, loads dictionaries and stopwords, extracts articles, analyzes text, and saves results.

## File Encoding Issues
If you encounter errors related to file encoding (e.g., 'utf-8' codec can't decode byte errors), the script handles these issues by using the `'latin1'` encoding to read the files. This approach is flexible and does not require changing the file type.




## Results
The analysis results are saved in `analysis_results.xlsx`, containing metrics such as:
- Positive Score
- Negative Score
- Polarity Score
- Subjectivity Score
- Average Sentence Length
- Percentage of Complex Words
- Fog Index
- Average Number of Words per Sentence
- Complex Word Count
- Word Count
- Syllables per Word
- Personal Pronouns
- Average Word Length

Additionally, the extracted articles are saved in `extracted_articles.csv`.




## Generating the Final Deliverable

1. main.py: The script containing the complete code.
2. analysis_results.xlsx: The output file that will be generated after running the script.
3. README.md: Instructions on how to run the script and an explanation of the approach.

##### Make sure to replace `path/to/Input.xlsx`, `path/to/Masterdictionary`, and `path/to/stopwords/folder` with the actual paths to the input file and directories before running the script.
