import os

from langchain_community.document_loaders import YoutubeLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import ChatVectorDBChain, ConversationalRetrievalChain
import youtube_transcript_api
from langchain_core.callbacks import CallbackManager
from langchain_core.callbacks import StreamingStdOutCallbackHandler

from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)
from dotenv import load_dotenv

load_dotenv()


def main():
    # 加载 youtube 频道
    loader = YoutubeLoader.from_youtube_url('https://www.youtube.com/watch?v=Dj60HHy-Kqk')
    # 将数据转成 document
    documents = loader.load()

    # 初始化文本分割器
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=20
    )

    # 分割 youtube documents
    documents = text_splitter.split_documents(documents)

    # 初始化 openai embeddings
    embeddings = OpenAIEmbeddings()

    # 将数据存入向量存储
    vector_store = Chroma.from_documents(documents, embeddings)
    # 通过向量存储初始化检索器
    retriever = vector_store.as_retriever()

    system_template = """
    Use the following context to answer the user's question.
    If you don't know the answer, say you don't, don't try to make it up. And answer in Chinese.
    -----------
    {question}
    -----------
    {chat_history}
    """

    # 构建初始 messages 列表，这里可以理解为是 openai 传入的 messages 参数
    messages = [
        SystemMessagePromptTemplate.from_template(system_template),
        HumanMessagePromptTemplate.from_template('{question}')
    ]

    # 初始化 prompt 对象
    prompt = ChatPromptTemplate.from_messages(messages)

    # 初始化问答链
    qa = ConversationalRetrievalChain.from_llm(ChatOpenAI(temperature=0.1, max_tokens=2048), retriever,
                                               condense_question_prompt=prompt)

    chat_history = []
    while True:
        question = input('问题：')
        # 开始发送问题 chat_history 为必须参数,用于存储对话历史
        result = qa({'question': question, 'chat_history': chat_history})
        chat_history.append((question, result['answer']))
        (print(result['answer']))


def main_stream():
    # 定义 ChatPromptTemplate (根据具体的应用场景调整)
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "You are an assistant."),
        ("user", "What is the weather like in {location}?")
    ])
    # 生成带值的 prompt
    chat_prompt_with_values = prompt_template.format_prompt(location="New York")
    chat = ChatOpenAI(streaming=True, callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
                      verbose=True, temperature=0)
    resp = chat(chat_prompt_with_values.to_messages())
    print(resp)


if __name__ == '__main__':
    main_stream()
