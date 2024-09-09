python -m venv .venv
. ./myenv/bin/activate
git init
true >__init__.py
deactivate

pip install -r requirements.txt
