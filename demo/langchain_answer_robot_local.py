from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import DirectoryLoader
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
import langchain
import pylibmagic
langchain.debug = True  # 启用详细调试输出

load_dotenv()


def main():
    # 初始化 openai 的 embeddings 对象
    doc_path = './data'
    embeddings = OpenAIEmbeddings()
    # 从本地向量数据库加载数据
    docsearch = Chroma(persist_directory=doc_path, embedding_function=embeddings)
    # 创建问答对象
    qa = RetrievalQA.from_chain_type(llm=ChatOpenAI(model_name="gpt-4o", max_tokens=1500), chain_type="stuff",
                                     retriever=docsearch.as_retriever(),
                                     return_source_documents=True)
    
    # 定义并执行多个示例问题
    questions = [
        "《地藏心经》的作者是谁？",
        "《地藏心经》的主要内容是什么？",
        "如何理解《地藏心经》中的核心思想？"
    ]
    
    # 进行问答并打印结果
    for i, question in enumerate(questions, 1):
        result = qa({"query": question})
        print(f"\n问题{i}: {question}")
        print("回答:", result["result"])
        print("来源文档:", [doc.metadata["source"] for doc in result["source_documents"]])

if __name__ == '__main__':
    main()
