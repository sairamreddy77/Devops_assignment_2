import streamlit as st

# Add a title to the app
st.title("Simple Calculator App 🧮")

# --- Get User Inputs ---

# Input for the first number
# We set a default value and allow floats
num1 = st.number_input("Enter the first number:", value=0.0, format="%.2f")

# Input for the second number
num2 = st.number_input("Enter the second number:", value=0.0, format="%.2f")

# Dropdown to select the operation
operation = st.selectbox(
    "Choose an operation:",
    ("Add", "Subtract", "Multiply", "Divide")
)

# --- Calculation Logic ---

# Add a button to trigger the calculation
if st.button("Calculate"):
    
    result = 0.0
    
    # Perform the calculation based on the selected operation
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        # Check for division by zero
        if num2 != 0:
            result = num1 / num2
        else:
            # Display an error message if dividing by zero
            st.error("Error: Division by zero is not allowed.")
            # Set result to None or a specific string to avoid displaying a '0.0' result
            result = None 
            
    # Display the result if a valid calculation was performed
    if result is not None:
        st.success(f"The result is: {result}")

st.write("---")
st.write("This app demonstrates number inputs and a select box.")