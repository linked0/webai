from langchain_core.prompts import PromptTemplage
from langchain_openai import ChatOpenAI

class PromptTemplate(StringPromptTemplate):
    """ Schema to represent a prompt for an LLM.

    Example:
        .. code-block:: python

        from langchain import PromptTemplate
        prompt = PromptTemplate(input_variable=["foo", template="Say {foo}")
    """

    input_variables: List[str]
    """A list of the names of the variables the prompt template expects"""

    template: str
    """The prompt template."""

    template_format: str = "f-string"
    """The format. of the prompt template. Options are: 'f-string', 'jinja2'."""

    validate_template: bool = True
    """Whether or not to try validating the template."""