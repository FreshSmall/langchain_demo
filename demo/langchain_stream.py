import getpass
import os

from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()


def main():
    model = ChatOpenAI(model="gpt-4o")
    chunks = []
    for chunk in model.stream("what color is the sky?"):
        chunks.append(chunk)
        print("开始输出\n")
        print(chunk.content, end="|\n", flush=True)
        print("结束输出\n")


if __name__ == '__main__':
    main()
