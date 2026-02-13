import streamlit as st
import math

# Page Config
st.set_page_config(page_title="Smart Calculator", page_icon="🧮")

st.title("🧮 Smart Calculator")
st.write("A simple and smart calculator built using Streamlit")

# Input Numbers
num1 = st.number_input("Enter First Number", value=0.0)
num2 = st.number_input("Enter Second Number", value=0.0)

# Operation Selection
operation = st.selectbox(
    "Choose Operation",
    ["Addition (+)", "Subtraction (-)", "Multiplication (×)", 
     "Division (÷)", "Power (xʸ)", "Percentage (%)"]
)

# Calculate Button
if st.button("Calculate"):

    try:
        if operation == "Addition (+)":
            result = num1 + num2

        elif operation == "Subtraction (-)":
            result = num1 - num2

        elif operation == "Multiplication (×)":
            result = num1 * num2

        elif operation == "Division (÷)":
            if num2 == 0:
                st.error("Cannot divide by zero!")
                st.stop()
            result = num1 / num2

        elif operation == "Power (xʸ)":
            result = math.pow(num1, num2)

        elif operation == "Percentage (%)":
            result = (num1 / 100) * num2

        st.success(f"Result: {result}")

    except Exception as e:
        st.error("Something went wrong!")
