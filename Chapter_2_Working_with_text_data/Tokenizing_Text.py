# =======================================================================================
# Building a Large Language Model (Sebastian Raschka)
# Chapter 2:    Working with text data
# Date:         11.19.2026
# Description:  This program (1) Imports "The Verdict", a story by Edith Wharton
#                            (2) Uses Pythons regular expression library to split the
#                                text.
#                            (2) Tokenizes the text
#                            (3) Assigns token IDs
# =======================================================================================

# =======================================================================================

# Imports the story.
import urllib.request
url = ("https://raw.githubusercontent.com/rasbt/"
       "LLMs-from-scratch/main/ch02/01_main-chapter-code/"
       "the-verdict.txt")
file_path = "the-verdict.txt"
urllib.request.urlretrieve(url, file_path)

# =======================================================================================

# Reads the short story as text sample into Python.
with open("the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()
# print("Total number of character:", len(raw_text))
# print(raw_text[:99])

# =======================================================================================

# Imports Python's regular expression library and splits text on whitespace characters.
# Words and punctuation characters are seperate entries. 
# Whitespaces are stripped.
import re
# text = "Hello, world. Is this-- a test?"
# result = re.split(r'([],.:;?_!"()\']|--|\s)', text)
# result = [item.strip() for item in result if item.strip()]
# print(result)

# =======================================================================================

# (Part 1) Apply basic tokenizer to "The Verdict".
# Text is stripped and whitespaces are removed.
preprocessed = re.split(r'([],.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]

# =======================================================================================
# TOKENIZER PIPELINE
# =======================================================================================
# 1. Split text into individual tokens. All duplicates are removed.
#    These tokens are now unique tokens.
# 2. Sort unique tokens in alphabetical order.
# 3. Assign token IDs to unique tokens based on position.
# =======================================================================================

# (Part 2) Apply basic tokenizer to "The Verdict".
# Token duplicates are removed and remaining tokens are sorted.
all_words = sorted(set(preprocessed))
vocab_size = len(all_words)
vocab = {token:integer for integer, token in enumerate(all_words)}
for i, item in enumerate(vocab.items()):
    print(item)
    if i >= 50:
        break
