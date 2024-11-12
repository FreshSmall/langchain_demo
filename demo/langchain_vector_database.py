from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import DirectoryLoader
from dotenv import load_dotenv
import pylibmagic

load_dotenv()


def main():
    # 初始化 openai 的 embeddings 对象
    embeddings = OpenAIEmbeddings()
    # 加载文件夹中的所有txt类型的文件
    loader = DirectoryLoader('./data', glob='**/*.txt')
    # 将数据转成 document 对象，每个文件会作为一个 document
    documents = loader.load()
    # 持久化数据
    docsearch = Chroma.from_documents(documents, embeddings, persist_directory="./data")
    docsearch.persist()


if __name__ == '__main__':
    main()
