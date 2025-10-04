import streamlit as st
import requests

st.title("RFP Response Generator")

rfp_text = st.text_area("Paste your RFP questions here:", height=200)

if st.button("Generate Responses"):
    if rfp_text:
        with st.spinner("Processing RFP..."):
        
            response = requests.post(
                "http://localhost:8000/rfp/process",
                json={"rfp_text": rfp_text}
            )
            
            if response.status_code == 200:
                result = response.json()
                
                st.success("RFP Processed!")
                
                for q in result['questions']:
                    st.subheader(f"Q: {q['question_content']}")
                    st.write(f"**Answer:** {q['answer']}")
                    st.write(f"**Trust Score:** {q['trust_score']}")
                    
                    with st.expander("View Source Chunks"):
                        for i, chunk in enumerate(q['chunks'][:3]):
                            st.write(f"**Chunk {i+1}:**")
                            st.text(chunk['chunk_content'][:300])
                    st.divider()
            else:
                st.error(f"Error: {response.text}")
    else:
        st.warning("Please enter RFP text")