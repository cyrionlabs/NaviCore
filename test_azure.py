import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from pydantic import SecretStr

# Print current working directory
print(f"Current working directory: {os.getcwd()}")

# Load environment variables
load_dotenv(verbose=True)

# Print all environment variables (without showing the full key for security)
print("\nEnvironment variables:")
for key in os.environ:
    if 'AZURE' in key:
        value = os.environ[key]
        if 'KEY' in key:
            print(f"{key}: {'*' * len(value)}")
        else:
            print(f"{key}: {value}")

# Try to get Azure variables
azure_key = os.getenv('AZURE_OPENAI_KEY', '')
azure_endpoint = os.getenv('AZURE_OPENAI_ENDPOINT', '')

print(f"\nAzure Endpoint: {azure_endpoint}")
print(f"Azure Key exists: {'Yes' if azure_key else 'No'}")

try:
    # Try to initialize Azure OpenAI
    llm = AzureChatOpenAI(
        model='gpt-4o',
        api_version='2024-10-21',
        azure_endpoint=azure_endpoint,
        api_key=SecretStr(azure_key),
    )
    print("Successfully initialized Azure OpenAI client")
except Exception as e:
    print(f"Error initializing Azure OpenAI client: {str(e)}") 