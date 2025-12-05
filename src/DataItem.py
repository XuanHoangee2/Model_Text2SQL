from transformers import AutoTokenizer
from huggingface_hub import login
from dotenv import load_dotenv
import os
from typing import Optional

load_dotenv()
hf_token = os.getenv("HF_TOKEN")

login(hf_token,add_to_git_credential=True)

MODEL = "unsloth/Meta-Llama-3.1-8B-Instruct"
MAX_TOKEN = 100
MIN_TOKEN = 5
MIN_CHARS = 8

class DataItemt():
    tokenizer = AutoTokenizer.from_pretrained(MODEL,trust_remote_code = True)
    PREFIX = "\nOutput:\n"
    prompt: Optional[str]

    def __init__(self,data):
        self.data = data
        self.query = data['messages'][2]['content']
        self.question = data['messages'][1]['content']
        self.system = data['messages'][0]['content']
    def parse(self):
        if self.tokenizer:
            num_tokens = len(self.tokenizer.encode(self.question, add_special_tokens = False))
        else:
            num_tokens = len(self.question.split())
        
        if len(self.question) < MIN_CHARS or num_tokens < MIN_TOKEN:
            return None
        if num_tokens > MAX_TOKEN:
            if self.tokenizer:
                trucated = self.tokenizer.encode(self.question, add_special_tokens = False)[:MAX_TOKEN]
                self.question = self.tokenizer.decode(trucated,add_special_tokens = False)
            else:
                self.question = " ".join(self.question.split()[:MAX_TOKEN])
    
    def MakePromt(self):
        prompt =f"{self.system}\nUSER:\n{self.question}\n{self.PREFIX}"
        if self.query is not None and self.query is not None:
            prompt += f"QUERY:\n{self.query}" 
        else:
            prompt += f"QUERY:[missing]"
        self.prompt = prompt
    
    def TestPrompt(self):
        return f"{self.system}\nUSER:\n{self.question}\n{self.PREFIX}"+f"QUERY:\n"
    
    def TestValue(self):
        return f"{self.query}"