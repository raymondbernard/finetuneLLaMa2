import streamlit as st
import jsonlines

st.title('Create JSONL for LLaMa2 chat models')

# Get prompts from the user
prompt_text = st.text_area('Enter your question? Human:', height=200)
ideal_generated_text = st.text_area('Enter your ideal AI generated response:', height=200)

system_message_default = 'You are a helpful and friendly assistant.'
system_message = st.text_area('Enter your custom system message:', value=system_message_default)


if st.button('Accept Inputs'):
    # Display the entered inputs
    st.write(f"Prompt Text: {prompt_text}")
    st.write(f"Ideal Generated Text: {ideal_generated_text}")
    
    # Format data
    
data = {
    "text": f"<<SYS>>\n{system_message}\n<</SYS>>\n\n<<SYS>>\n<s>[INST] {prompt_text} [/INST] {ideal_generated_text}</s>\n<</SYS>>"
}


# Append to jsonl file
with jsonlines.open('output.jsonl', mode='a') as writer:
    writer.write(data)

st.success('Data has been appended to JSONL file!')
