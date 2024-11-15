from langchain.memory import ChatMessageHistory
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


def main(): 
    chat = ChatOpenAI(temperature=0)

    # 初始化 MessageHistory 对象
    history = ChatMessageHistory()

    # 给 MessageHistory 对象添加对话内容
    history.add_ai_message("你好！")
    history.add_user_message("中国的首都是哪里？")

    # 执行对话
    ai_response = chat(history.messages)
    print(ai_response)


if __name__ ==  '__main__':
    main()