from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage


load_dotenv()


def chat_openai():
    llm = ChatOpenAI()
    # messages = [
    #     SystemMessage(content="Translate the following from English into Italian"),
    #     HumanMessage(content="hi!"),
    # ]
    response = llm.invoke("how can langsmith help with testing?")
    print(response)
#

# def openai():
#     llm = OpenAI()
#     text = "why elon musk is so smart?"
#     print(llm.invoke(text))


if __name__ == '__main__':
    chat_openai()
