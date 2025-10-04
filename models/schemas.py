from typing import TypedDict

class Chunk(TypedDict):
    chunk_content: str
    metadatas: dict
    chunk_id: str
    distance: float


class Question(TypedDict):
    question_content: str
    question_id: str
    chunks: list[Chunk]
    answer: str
    trust_score: float


class State(TypedDict):
    upload_rfp_extracted_text: str
    questions: list[Question]
    
