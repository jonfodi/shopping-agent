
# setup 
Prereqs
- Python 3.11 or higher 
- uv 

Steps 
source .venv/bin/activate 
uv pip install -r requirements.txt

Issue with UV - pulling x86_64 wheels for pydantic_core 
- incompatible with arm (apple silicon)

# Learning 

1) clone repo 
2) pull the hello world commit (first commit)
3) run: python test.py 
4) follow the print statements to see the agent workflow and how it passes data to itself!  