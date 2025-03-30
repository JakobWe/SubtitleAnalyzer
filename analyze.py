from collections import Counter
import re

from os import listdir
from os.path import isfile, join
from pathlib import Path
import os.path

RAW_DATA_PATH = 'raw_data/attack_on_titan/'
BUILD_PATH = 'build'
TRANSLATIONS_FILE = f'{BUILD_PATH}/translations.csv'
RAW_OUTPUT_FILE = f'{BUILD_PATH}/output.txt'

def read_file(filepath):
    with open(filepath, 'r') as fd:
        reader = fd.readlines()

    return [line for line in reader]

def read_files():

    onlyfiles = [f for f in listdir(RAW_DATA_PATH) if isfile(join(RAW_DATA_PATH, f))]

    list_of_lines_by_file = [read_file(f"{RAW_DATA_PATH}/{filename}") for filename in onlyfiles]


    all_lines = flatten(list_of_lines_by_file)

    # for line in all_lines:
    #    debug_analyze_helper(line)
    
    return all_lines


def debug_analyze_helper(line):
    regex_to_search_for = re.compile(r"[\w'-]+")
    iterator_over_all_matches = re.finditer(regex_to_search_for, line)
    for match in iterator_over_all_matches:
        match_as_string = match.group(0).lower()
        if match_as_string == "e":
            print(line)

def flatten(t):
    return [
        x for xs in t for x in xs
    ]

def is_a_word(token):
    contains_number = re.compile(r'[0-9]').search(token)
    contains_letter = re.compile(r'\w').search(token)

    if contains_number:
        return False

    if not contains_letter:
        return False

    return True

def load_previous_translations():
    if not os.path.isfile(TRANSLATIONS_FILE):
        return list()

    translations = read_file(TRANSLATIONS_FILE)

    english_words = [line.split(";")[0] for line in translations]

    return english_words

def count_strings(message_list):
    from nltk.tokenize import RegexpTokenizer

    tokenizer = RegexpTokenizer(r"[\w'-]+")
    tokens = tokenizer.tokenize(message_list.lower())


    filtered_tokens = [token for token in tokens if is_a_word(token)]

    previous_translations = load_previous_translations()
    filtered_tokens = [token for token in filtered_tokens if not token in previous_translations]

    counts = Counter(filtered_tokens )


    return counts

if __name__ == '__main__':
    Path(BUILD_PATH).mkdir(parents=True, exist_ok=True)
    lines = read_files()

    words = ' '.join(lines)
    word_counts = count_strings(words)

    print("Five most common matches:")
    for key, value in word_counts.most_common(5):
        print (key, value)

    with open(RAW_OUTPUT_FILE, "w+") as text_file:
        words_to_translate = [x[0] for x in word_counts.most_common(100)]
        text_file.write("\n".join(words_to_translate))
