from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import DirectoryLoader
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
import pylibmagic

load_dotenv()


def main():
    # 初始化 openai 的 embeddings 对象
    embeddings = OpenAIEmbeddings()
    # 从本地向量数据库加载数据
    docsearch = Chroma(persist_directory="./data", embedding_function=embeddings)
    # 创建问答对象
    qa = RetrievalQA.from_chain_type(llm=ChatOpenAI(model_name="gpt-4o", max_tokens=1500), chain_type="stuff",
                                     retriever=docsearch.as_retriever(),
                                     return_source_documents=True)
    # 进行问答
    result = qa({"query": "《地藏心经》的作者是谁？"})
    print(result)


if __name__ == '__main__':
    main()
