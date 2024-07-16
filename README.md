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


### Generating the Final Deliverable

1. main.py: The script containing the complete code.
2. analysis_results.xlsx: The output file that will be generated after running the script.
3. README.md: Instructions on how to run the script and an explanation of the approach.

##### Make sure to replace `path/to/Input.xlsx`, `path/to/Masterdictionary`, and `path/to/stopwords/folder` with the actual paths to the input file and directories before running the script.



## Output

The analysis results are saved to an Excel file (analysis_results.xlsx).