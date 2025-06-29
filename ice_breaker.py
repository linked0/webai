from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from output_parsers import summary_parser

# information = """
#         Bill Clinton and his wife
# """

def ice_break_with(name: str) -> str:
    linkedin_username = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username, mock=True)

    summary_template = """
    given the Linkedin information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    
    Use both information from twitter and Linkedin
    \n{format_instructions}
    """
    summary_prompt_template = PromptTemplate(
        input_variable=["information"], template=summary_template,
        partial_variables={"format_instructions": summary_parser.get_format_instructions()}
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = summary_prompt_template | llm | summary_parser
    res = chain.invoke(input={"information": linkedin_data})

    print("#####################################################")
    print(res)

if __name__ == "__main__":
    load_dotenv()

    print("Ice Breaker Enter")
    ice_break_with(name="Eden Marco")


# if __name__ == "__main__":
#     load_dotenv()
#     print("Hello LangChain")
#     print(os.environ["OPENAI_API_KEY"])
#
#     summary_template = """
#         given the information {information} about a person from I want you to create:
#         1. a short summary
#         2. two interesting facts about them
#     """
#     summary_prompt_templage = PromptTemplate(input_variables=["information"], template=summary_template)
#
#     llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
#     # llm = ChatOllama(model="llama3.2")
#     # llm = ChatOllama(model="mistral")
#     linked_data = scrape_linkedin_profile(
#             linked_profile_url="https://www.linkedin.com/in/eden-marco",
#             mock=True,
#         )
#     chain = summary_prompt_templage | llm | StrOutputParser()
#     res = chain.invoke(input={"information": linked_data})
#
#     print(res)