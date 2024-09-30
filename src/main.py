from litellm import completion 
import os

from dotenv import load_dotenv
load_dotenv()

from system_prompt.system_prompt_gen import generate_system_prompt_from_config


api_key = os.environ['OPENAI_API_KEY']
model = os.environ['GPT_MODEL']
config_path = os.environ['CONFIG_PATH']
prompt = generate_system_prompt_from_config(config_path)

a = completion(model = model, messages=[{ "content": prompt,"role": "assistant"}])
print(a.choices[0].message.content)