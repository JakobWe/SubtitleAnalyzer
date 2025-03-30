#!/bin/bash

python3 -m venv ~/.venv/nlp

source "$HOME/.venv/nlp/bin/activate"
python3 -m pip install nltk

python3 analyze.py

