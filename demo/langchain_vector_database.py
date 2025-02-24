from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters import TokenTextSplitter
from dotenv import load_dotenv
import pylibmagic

load_dotenv()


def main():
    # 初始化 openai 的 embeddings 对象
    embeddings = OpenAIEmbeddings()
    doc_path = '/Users/bjhl/PycharmProjects/langchain_demo/demo/data'
    # 加载文件夹中的所有txt类型的文件
    loader = DirectoryLoader(doc_path, glob='**/*.txt')
    # 将数据转成 document 对象，每个文件会作为一个 document
    documents = loader.load()
    # 文档切块目的是为了防止超出GPTAPI的token限制
    text_splitter = TokenTextSplitter(chunk_size=1000, chunk_overlap=0)
    doc_texts = text_splitter.split_documents(documents)
    # 持久化数据
    docsearch = Chroma.from_documents(doc_texts, embeddings, persist_directory=doc_path)
    docsearch.persist()


if __name__ == '__main__':
    main()
