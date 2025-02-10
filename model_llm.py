from langchain_groq import ChatGroq
from transformers import AutoTokenizer
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

api_key=os.getenv("groq_API_KEY")


def get_output(prompt,name):

    llm=ChatGroq(
        api_key=api_key,
        model='deepseek-r1-distill-llama-70b',
        temperature=0.3
    )

    prompt_template=PromptTemplate(
        input_variables=['text','name'],
        template='''## Your are helpfull ChatBot for Creating mails.

                ## instrucation :
                        -> </think> can be as big as possible. But the output should follow Correct mail Structure.
                        -> The mail Should Consist of Correct Content with out any misleading info.
                        -> Mail should be simple.
                        -> Don't show any fill in the blank like [contact],[name] etc.,
                        -> The mail Should Be complete, one without any new details to be added.

                Prompt : Your name is {name}, you want to create a mail based on "{text}" 

                ## NO PREAMBLE.
        '''
    )

    chain=LLMChain(llm=llm,prompt=prompt_template)

    inputs={
        'text':prompt,
        'name':name
    }

    return chain.run(inputs)





