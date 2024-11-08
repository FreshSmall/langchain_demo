from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import initialize_agent
from langchain.agents import create_tool_calling_agent,AgentExecutor
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAI
from langchain.agents import AgentType
from dotenv import load_dotenv
from langchain import hub
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.tools import tool


load_dotenv()

@tool
def multiply(first_int: int, second_int: int) -> int:
    """Multiply two integers together."""
    return first_int * second_int


@tool
def add(first_int: int, second_int: int) -> int:
    "Add two integers."
    return first_int + second_int


@tool
def exponentiate(base: int, exponent: int) -> int:
    "Exponentiate the base to the exponent power."
    return base**exponent


def main_old():
    # 加载 OpenAI 模型
    llm = ChatOpenAI(model="gpt-4o")
    #llm = ChatOpenAI()
    # 加载 serpapi 工具
    tools = load_tools(["serpapi"])
    # 如果搜索完想再计算一下可以这么写
    # tools = load_tools(['serpapi', 'llm-math'], llm=llm)
    # 如果搜索完想再让他再用python的print做点简单的计算，可以这样写
    # tools=load_tools(["serpapi","python_repl"])
    # 工具加载后都需要初始化，verbose 参数为 True，会打印全部的执行详情
    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    # 创建 REACT agent
    #agent = create_tool_calling_agent(llm, tools, "")
    #agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)


    # 运行 agent
    # agent_executor.invoke({
    #     "input":"What's the date today? What great events have taken place today in history?"
    # })
    agent.invoke("What's the date today? What great events have taken place today in history?")



def main_new():
    llm = ChatOpenAI(model="gpt-4o")
    tools = [multiply, add, exponentiate]

    # Get the prompt to use - you can modify this!
    prompt = hub.pull("hwchase17/openai-tools-agent")
    prompt.pretty_print()
    # Construct the tool calling agent
    agent = create_tool_calling_agent(llm, tools, prompt)
    # Create an agent executor by passing in the agent and tools
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    agent_executor.invoke(
    {
        "input": "What's the date today? What great events have taken place today in history?"
    }
    )
    

if __name__ == "__main__":
    main_new()