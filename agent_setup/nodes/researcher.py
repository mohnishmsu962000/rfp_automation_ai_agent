from models.schemas import State
from rag.retriever import retrieve

def researcher_node(state: State, *, store) -> State:
    
    company_data = store.get(("company", "test_company_123"), "metadata")
    company_id = company_data.value["id"]
    
    questions = state['questions']
    
    
    for question in questions:
        
        retrieved_chunks = retrieve(question['question_content'], company_id, 5)
        question['chunks'] = retrieved_chunks
        
        
    return {
            'questions': questions
            }