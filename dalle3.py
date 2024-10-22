# Note: DALL-E 3 requires version 1.0.0 of the openai-python library or later
endpoint="https://abill-m2ku3el9-swedencentral.openai.azure.com/"
apikey="2920a3a314af4e3db23424cd87b1812d"
# Note: DALL-E 3 requires version 1.0.0 of the openai-python library or later
import os
from openai import AzureOpenAI
import json

client = AzureOpenAI(
    api_version="2024-05-01-preview",
    azure_endpoint="https://abill-m2ku3el9-swedencentral.openai.azure.com/",
    api_key=apikey,
)

result = client.images.generate(
    model="dall-e-3", # the name of your DALL-E 3 deployment
    prompt="dog",
    n=1
)

image_url = json.loads(result.model_dump_json())['data'][0]['url']
print(image_url)