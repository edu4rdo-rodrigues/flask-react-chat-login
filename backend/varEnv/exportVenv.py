# flask-react-chat-login/backend/varEnv/exportVenv.py

import os
from dotenv import load_dotenv

load_dotenv()
API_FRONTEND_URL = os.environ['PYTHON_APP_API_FRONTEND_URL']
DATABASE_MYSQL_URL = os.environ['DATABASE_MYSQL_URL']


