from models.schemas import State
import re

def extractor_node(state: State) -> State:
    questions = []
    pattern = r'^\s*(\d+)[\.\)]\s*(.+?)$'
    matches = re.findall(pattern, state['upload_rfp_extracted_text'], re.MULTILINE)
    
    question_texts = [match[1].strip() for match in matches]
    
    for question_text in question_texts:
        question = {
            'question_content': question_text,
            'question_id': str(len(questions) + 1) ,
            'chunks': [],
            'answer': "",
            'trust_score': 0.0
        }
        questions.append(question)
    
    return {
            'questions': questions
            }