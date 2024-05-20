from langchain_openai import OpenAI
from langchain_experimental.agents.agent_toolkits import create_csv_agent
filepath = "world-happiness-report-2024.csv"
llm = OpenAI(temperature=0,openai_api_key='sk-proj-gYzX9K9oMXi2bAQ1hD0jT3BlbkFJLiFwupy5Q7ZZdlXC0W0K')
agent = create_csv_agent(llm,filepath,verbose=True)
while(True):
    prompt = input("enter prompt:")
    agent.run(prompt)
