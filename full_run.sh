#!/bin/bash

#source .prc



python3 -m venv ~/.venv/nlp

source "$HOME/.venv/nlp/bin/activate"
python3 -m pip install nltk
# pp -m pip install nltk


python3 analye.py

# /bin/bash preprocess.sh
