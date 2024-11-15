#from langchain.memory import ChatMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


def main(): 
    chat = ChatOpenAI(model='gpt-4o', temperature=0)

    # 初始化 MessageHistory 对象
    history = ChatMessageHistory()

    # 给 MessageHistory 对象添加对话内容
    history.add_ai_message("你好！中国的首都是哪里？")
    history.add_user_message("有多少个区？")
    history.add_user_message("最近一年的 gdp 是多少？")

    # 执行对话
    ai_response = chat.invoke(history.messages)
    print(ai_response)


if __name__ ==  '__main__':
    main()