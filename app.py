import gradio as gr  # this is use to create simple user-interface (ui)

# Define a simple function
def reverse_string(input_text):
    return input_text[::-1]

# Create a Gradio interface
interface = gr.Interface(
    fn=reverse_string,  # Function to interact with
    inputs="text",      # Input type
    outputs="text"      # Output type
)

# Launch the interface
interface.launch()
