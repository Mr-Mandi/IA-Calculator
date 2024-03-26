import tiktoken
from transformers import AutoTokenizer

def get_count_tokens(message, model):
    if model in ["gtp-3.5-turbo-0125","gtp-3.5-turbo-instruct","gtp-4","gtp-4-32k"]:
        encoding = tiktoken.get_encoding("cl100k_base")
        coding = encoding.encode(message)
        num_tokens = len(coding)
        new_list = [encoding.decode([token]) for token in coding]
        return num_tokens , new_list
    
    if model == "mistralai/Mixtral-8x7B-Instruct-v0.1": 
        tokenizer = AutoTokenizer.from_pretrained("mistralai/Mixtral-8x7B-Instruct-v0.1")
        tokens = tokenizer.encode(message, return_tensors="pt")
        num_tokens = tokens.shape[1]
        return num_tokens , []
    
    if model == "tiiuae/falcon-40b" :
        tokenizer = AutoTokenizer.from_pretrained("tiiuae/falcon-40b")
        tokens = tokenizer.encode(message, return_tensors="pt")
        num_tokens = tokens.shape[1]
        return num_tokens , []