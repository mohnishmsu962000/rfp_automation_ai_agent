

def generator_prompt(question, chunks):
    
    context = "\n\n".join([
        f"Source {i+1}: {chunk['chunk_content']}"
        for i, chunk in enumerate(chunks)
    ])
    
    prompt = f"""You are an expert at writing professional RFP responses.

Question: {question}

Relevant information from company documents:
{context}

Instructions:
- Write a clear, professional answer suitable for an RFP response
- Base your answer ONLY on the provided information
- If the information doesn't fully answer the question, acknowledge gaps
- Keep the tone professional and confident
- Provide a trust_score (0.0 to 1.0) indicating confidence in the answer based on available information

Return your response as JSON with 'answer' and 'trust_score' fields."""

    return prompt