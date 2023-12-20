# streamlit_app.py
import subprocess
import streamlit as st

# Function to run the Tkinter app
def run_typing_speed_test():
    subprocess.run(["python", "typing_speed_test.py"])

def main():
    st.title("Typing Speed Test with Streamlit")

    st.write("Welcome to the Streamlit-based Typing Speed Test!")

    # Button to start the Tkinter app
    if st.button("Start Typing Speed Test"):
        run_typing_speed_test()

if __name__ == "__main__":
    main()
