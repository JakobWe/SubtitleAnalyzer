Written using Python 3.12.

The `full_run.sh` creates a python virtual environment and runs the analyze skript using that venv.
The `.prc` can be sourced once the venv has been created to manually run the script without checking the python wheels everytime. Also some dev environments like nvim then use the correct python environment.
The script checks for a `TRANSLATIONS_FILE` which I use in order to prevent multiple runs creating the same words (e.g. when creating vocabulary lists for a second show). The script expects the translations file to be a csv where the first column is the english word. This is skipped if the file does not exists.

This Skript does not provide the translations, I usually use chatgpt to translate the created lists
