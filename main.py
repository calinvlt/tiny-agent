from llm import LLM
from tiny_agent import TinyAgent

llm = LLM(model="gemma4:e4b")
agent = TinyAgent(llm=llm)

response = agent.run("What is 1+1?")

print(response)
print(agent.trajectory.runs)