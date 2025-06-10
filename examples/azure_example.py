import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from pydantic import SecretStr
from browser_use import Agent

# Load environment variables
load_dotenv()

# Get Azure OpenAI credentials
azure_key = os.getenv('AZURE_OPENAI_KEY')
azure_endpoint = os.getenv('AZURE_OPENAI_ENDPOINT')

if not azure_key or not azure_endpoint:
    raise ValueError('AZURE_OPENAI_KEY and AZURE_OPENAI_ENDPOINT must be set in environment variables')

# Initialize Azure OpenAI
llm = AzureChatOpenAI(
    model='gpt-4o',
    api_version='2024-12-01-preview',
    azure_endpoint=azure_endpoint,
    api_key=SecretStr(azure_key),
)

# Create agent with Azure OpenAI
agent = Agent(
    task='Go to google.com and search for "browser automation"',
    llm=llm,
    use_vision=False
)

# Run the agent
if __name__ == '__main__':
    import asyncio
    asyncio.run(agent.run()) 