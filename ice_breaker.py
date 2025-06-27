from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from third_parties.linkedin import scrape_linkedin_profile

# information = """
#         Bill Clinton and his wife
# """

if __name__ == "__main__":
    load_dotenv()
    print("Hello LangChain")
    print(os.environ["OPENAI_API_KEY"])

    summary_template = """
        given the information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
    """
    summary_prompt_templage = PromptTemplate(input_variables=["information"], template=summary_template)

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    # llm = ChatOllama(model="llama3.2")
    # llm = ChatOllama(model="mistral")
    linked_data = scrape_linkedin_profile(
            linked_profile_url="https://www.linkedin.com/in/eden-marco",
            mock=True,
        )
    chain = summary_prompt_templage | llm | StrOutputParser()
    res = chain.invoke(input={"information": linked_data})

    print(res)