from agent_setup.graph import workflow

# Test RFP with questions
test_rfp = """
1. What security certifications does your company have?
2. What is your typical implementation timeline?
3. What kind of customer support do you provide?
"""

test_state = {
    'upload_rfp_extracted_text': test_rfp,
    'questions': []
}

print("Running RFP pipeline...")
result = workflow.invoke(test_state)

print("\n=== RESULTS ===")
for q in result['questions']:
    print(f"\nQuestion: {q['question_content']}")
    print(f"Answer: {q['answer']}")
    print(f"Trust Score: {q['trust_score']}")
    print(f"Chunks used: {len(q['chunks'])}")