import os

os.sys.path.append("..")
from configs.template import get_config as default_config

def get_config():
    
    config = default_config()

    config.result_prefix = 'results/individual_llama2'

    config.tokenizer_paths=["/root/autodl-tmp/Llama-2-7b-chat-fp16"]
    config.model_paths=["/root/autodl-tmp/Llama-2-7b-chat-fp16"]
    config.conversation_templates=['llama-2']

    return config