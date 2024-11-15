# from langchain.document_loaders import UnstructuredFileLoader
from langchain_community.document_loaders import UnstructuredFileLoader
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import pylibmagic
import ssl
import certifi

load_dotenv()
#ssl._create_default_https_context = ssl._create_unverified_context


def main():
    # ssl_context = ssl.create_default_context(cafile=certifi.where())
    # 导入文本
    loader = UnstructuredFileLoader("demo/data/lg_test.txt")
    # 将文本转成 Document 对象
    document = loader.load()
    print(f'documents:{len(document)}')

    # 初始化文本分割器
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=0
    )

    # 切分文本
    split_documents = text_splitter.split_documents(document)
    print(f'documents:{len(split_documents)}')

    # 加载 llm 模型
    llm = ChatOpenAI(model_name="gpt-4o", max_tokens=1500)

    # 创建总结链
    chain = load_summarize_chain(llm, chain_type="refine", verbose=False)

    # 执行总结链，（为了快速演示，只总结前5段）
    response = chain.invoke(split_documents[:5])
    print(response)


if __name__ == "__main__":
    main()
