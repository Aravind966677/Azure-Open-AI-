import os
from openai import AzureOpenAI
import json
from dotenv import load_dotenv

load_dotenv()
#AZURE_OPENAI_API_KEY=os.getenv("AZURE_OPENAI_API_KEY")

client = AzureOpenAI(
    api_version="2024-02-01",
    azure_endpoint="https://abill-m2ku3el9-swedencentral.openai.azure.com/",
    api_key="2920a3a314af4e3db23424cd87b1812d"
)

completion = client.chat.completions.create(
    model="chat",
    messages=[
        {
            "role": "user",
            "content": "what is a capital of new delhi?",
        }
    ]
)
      
print(completion.to_json())
