from fastapi import FastAPI
from agent_setup.graph import workflow
from pydantic import BaseModel

app = FastAPI()

class RFPRequest(BaseModel):
    rfp_text: str

@app.post("/rfp/process")
def process_rfp(request: RFPRequest):
    state = {
        'upload_rfp_extracted_text': request.rfp_text,
        'questions': []
    }
    result = workflow.invoke(state)
    return result