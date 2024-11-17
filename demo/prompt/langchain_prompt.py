from langchain_core.prompts import PromptTemplate

def basic_print_prompt():
    template = """/
    You are a naming consultant for new companies.
    What is a good name for a company that makes {product}?
    """

    prompt = PromptTemplate.from_template(template)
    prompt.format(product="colorful socks")
    print(prompt)


if __name__ == "__main__":
    basic_print_prompt()