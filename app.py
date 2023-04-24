import streamlit as st
from your_camel_script_module import run_camel_script

# Define the Streamlit app
def main():
    st.title("LangChain CAMEL Script")
    st.markdown("This is an alternative langchain implementation of paper: “CAMEL: Communicative Agents for “Mind” Exploration of Large Scale Language Model Society”. The rapid advancement of conversational and chat-based language models has led to remarkable progress in complex task-solving. However, their success heavily relies on human input to guide the conversation, which can be challenging and time-consuming. This tool allows for the rapid exploration of multi-agent cooperative simulations. ...All credit to the original authors. This is simply an alternative implementation of their work")

    # Collect user inputs
    user = st.text_input("Main Agent:")
    assistant = st.text_input("Assistant Agent:")
    task = st.text_input("Task:")
    openai_key = st.text_input("OpenAI Key:", type="password")
    st.markdown("<a href='https://platform.openai.com/account/api-keys' target='_blank'>Find your OpenAI key</a>", unsafe_allow_html=True)

    # Button to run the script
    if st.button("Run CAMEL Script"):
        if not all([assistant, user, task, openai_key]):
            st.warning("Please fill in all the input fields.")
        else:
            # Call the function with user inputs
            output = run_camel_script(assistant, user, task, openai_key)

            # Display the output
            #st.header("Output:")
            #st.write(output)

if __name__ == "__main__":
    main()
