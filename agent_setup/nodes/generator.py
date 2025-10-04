from models.schemas import State
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from prompts.generator_prompts import generator_prompt
from pydantic import BaseModel



load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini", temperature=0.0, openai_api_key=os.getenv("OPENAI_API_KEY")
)

class AnswerOutput(BaseModel):
    answer: str
    trust_score: float
    
structured_llm = llm.with_structured_output(AnswerOutput)

def generator_node(state: State) -> State:
    
    questions = state['questions']
    
    for question in questions:
        
        response = structured_llm.invoke(generator_prompt(question['question_content'], question['chunks']))
        
        question['answer'] = response.answer
        question['trust_score'] = response.trust_score
        
    
    return {
        'questions': state['questions']
    }
