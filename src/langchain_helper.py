from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from dotenv import load_dotenv

load_dotenv()

def generate_pet_name(animal_type, pet_color):
    llm = OpenAI(temperature=0.8)

    prompt_template_name = PromptTemplate(
        input_variables=['animal_type','pet_color'],
        template="I have a pet {animal_type} and I want a cool name for it, it is {pet_color} in color. Give me 5 cool name suggestions for my pet."
    )

    # Use LLMChain with correct initialization
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name)

    response = name_chain.run({'animal_type': animal_type, 'pet_color': pet_color})
    return response

def langchain_agent():
    llm=OpenAI(temperature=0.7)

    tools = load_tools(["wikipedia", "llm-math"], llm = llm)

    agent = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )

    result = agent.run(
        "What is the average age of a dog? Multiply the age by 3"
    )

    print(result)

if __name__ == "__main__":
    langchain_agent()
    #print(generate_pet_name("cow", "black"))

