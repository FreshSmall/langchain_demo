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
    # 加载文件夹中的所有txt类型的文件
    doc_path = '/Users/bjhl/PycharmProjects/langchain_demo/demo/data'
    #doc_path = '/Users/bjhl/PycharmProjects/langchain_demo/demo/data'
    loader = DirectoryLoader(doc_path, glob='**/*.md')
    # 将数据转成 document 对象，每个文件会作为一个 document
    documents = loader.load()

    # 初始化加载器
    text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
    # 切割加载的 document
    split_docs = text_splitter.split_documents(documents)

    # 初始化 openai 的 embeddings 对象
    embeddings = OpenAIEmbeddings(openai_api_key='gAAAAABl5-LtACZvu1LgaitiguTOoUEiiq40HcSC5hYD9VgJLjS8EryGlg0XMjHObwy8UXOxKnPg_mcJdi2cwpZuTp9frtpYR9etf42SO6AFYtPEjldXnW64C8QKBLB5_yQqW3V4TrBG', base_url='https://aiops-api.baijia.com/openai/v1')
    # 将 document 通过 openai 的 embeddings 对象计算 embedding 向量信息并临时存入 Chroma 向量数据库，用于后续匹配查询
    docsearch = Chroma.from_documents(split_docs, embeddings)

    # 创建问答对象
    qa = RetrievalQA.from_chain_type(llm=ChatOpenAI(model_name="deepseek/DeepSeek-R1", max_tokens=1500), chain_type="stuff",
                                     retriever=docsearch.as_retriever(),
                                     return_source_documents=True)
    # 进行问答
    result = qa({"query": "如何在表格中添加一列代码？"})
    print(result)


if __name__ == '__main__':
    main()
