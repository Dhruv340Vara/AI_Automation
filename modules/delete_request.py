import os
import json
import uuid
from datetime import datetime,timedelta

TOKEN_FILE="data/delete_tokens.json"

def load_tokens():
    if not os.path.exists(TOKEN_FILE):
        return {}
    with open(TOKEN_FILE,"r") as f:
        return json.load(f)

def save_tokens(tokens):
    os.makedirs("data",exist_ok=True)
    with open(TOKEN_FILE,"w") as f:
        json.dump(tokens,f,indent=4)

def request_delete(path):
    if not os.path.exists(path):
        return {"success":False,"error":"File not found"}
    tokens=load_tokens()
    token=str(uuid.uuid4())[:8].upper()
    tokens[token]={
        "path":path,
        "expires":(datetime.now()+timedelta(minutes=2)).strftime("%Y-%m-%d %H:%M:%S")
    }
    save_tokens(tokens)
    return {
        "success":True,
        "token":token,
        "expires_in":"2 minutes"
    }

