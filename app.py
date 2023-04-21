import streamlit as st
from your_camel_script_module import run_camel_script

# Define the Streamlit app
def main():
    st.title("LangChain CAMEL Script")

    # Collect user inputs
    assistant = st.text_input("Assistant:")
    user = st.text_input("User:")
    task = st.text_input("Task:")
    openai_key = st.text_input("OpenAI Key:", type="password")

    # Button to run the script
    if st.button("Run CAMEL Script"):
        if not all([assistant, user, task, openai_key]):
            st.warning("Please fill in all the input fields.")
        else:
            # Call the function with user inputs
            output = run_camel_script(assistant, user, task, openai_key)

            # Display the output
            st.header("Output:")
            st.write(output)

if __name__ == "__main__":
    main()