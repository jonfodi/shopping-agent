
# NIKE MULTI-AGENT SHOPPING TOOL
Search your favorite shoes on nike and find hidden gems!

# SETUP 
Prereqs
- Python 3.11 or higher 

Steps 
1) Clone repo 
git clone https://github.com/jonfodi/shopping-agent.git
1)  Create Virtual Env
python -m venv venv 
2) Activate Virtual Env
source venv/bin/activate 
3) Install Backend requirements 
pip install -r requirements.txt
4) Install Frontend requirements 
cd frontend/
npm install 
5) Start backend server
uvicorn main:app --reload
6) start frontend server (separate terminal)
cd frontend/
npm run dev 

Issue with UV - pulling x86_64 wheels for pydantic_core 
- incompatible with arm (apple silicon)
