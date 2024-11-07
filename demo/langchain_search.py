from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import initialize_agent
from langchain.agents import create_react_agent
from langchain_openai import OpenAI
from langchain.agents import AgentType
from dotenv import load_dotenv

load_dotenv()

def main():
    # 加载 OpenAI 模型
    #llm = OpenAI()
    llm = OpenAI(model="chgpt-4")
    # 加载 serpapi 工具
    tools = load_tools(["serpapi"])
    # 如果搜索完想再计算一下可以这么写
    # tools = load_tools(['serpapi', 'llm-math'], llm=llm)
    # 如果搜索完想再让他再用python的print做点简单的计算，可以这样写
    # tools=load_tools(["serpapi","python_repl"])
    # 工具加载后都需要初始化，verbose 参数为 True，会打印全部的执行详情
    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    # 运行 agent
    agent.run("What's the date today? What great events have taken place today in history?")

if __name__ == "__main__":
    main()
    
    
