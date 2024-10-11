from langchain_openai import AzureOpenAI
from dotenv import load_dotenv
import os

from azure.identity import DefaultAzureCredential, get_bearer_token_provider



class Task:

    llm = "llm"
    task_name = ""
    
    def __init__(self):
        os.environ["BING_SUBSCRIPTION_KEY"] = "3604a9a909b64c40938e28e9232f4c57"
        os.environ["BING_SEARCH_URL"] = "https://api.bing.microsoft.com"

    def start_task(self):
        load_dotenv()

        azure_credential = DefaultAzureCredential(exclude_managed_identity_credential=True)

        llm = AzureOpenAI(
            api_version="2021-07-15",
            azure_endpoint="https://sapiens-openai.openai.azure.com",
            azure_ad_token_provider=get_bearer_token_provider(azure_credential, "https://cognitiveservices.azure.com/.default"),
            azure_deployment="sapiens-openai"
        )

        from langchain.agents import load_tools

        tools = load_tools(["bing-search"], llm=llm)
        tools[0].name, tools[0].description

        from langchain.agents import initialize_agent

        agent = initialize_agent(tools,
                                llm,
                                agent="zero-shot-react-description",
                                verbose=True)


        print(agent.agent.llm_chain.prompt.template)

        query = "Who is the chief minister of Andhra Pradesh?"

        agent.run(query)

    def validate_task(self):
        print("running")

    def invoke_task(self):
        print("create new task")