from langchain.chains import LLMChain
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import HuggingFaceHub

load_dotenv()


def main(): 
    template = """Question: {question}
    Answer: Let's think step by step."""
    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm = HuggingFaceHub(repo_id="google/flan-t5-xl", model_kwargs={"temperature":0, "max_length":64})
    llm_chain = prompt|llm

    question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"
    print(llm_chain.invoke(question))

if __name__ ==  '__main__':
    main()