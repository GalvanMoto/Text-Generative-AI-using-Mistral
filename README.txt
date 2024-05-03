Interactive Text Generation with Large Language Models (LLMs)
This project demonstrates an interactive web application for text generation using a powerful Large Language Model (LLM) called LlamaCpp. It leverages two technologies: Streamlit for the user interface and Flask for running the LLM model.

Getting Started:
Prerequisites: Python 3.11.7, Streamlit, Flask, langchain libraries (refer to requirements.txt for specific versions).

Installation:
Install required libraries using pip install -r requirements.txt.

Download LlamaCpp Model:
Obtain the pre-trained LlamaCpp model files and place them in the appropriate directory (refer to model documentation).

Run the Application:
Navigate to the project directory in your terminal.
Start the Flask server: python flask_app.py (replace with the actual filename if different).
Open http://localhost:5000/ in your web browser to access the Streamlit interface.

How It Works:
Users enter prompts in the text area provided by the Streamlit application.
Clicking the "Generate Text" button triggers a request to the Flask server.
The Flask server interacts with the LlamaCpp LLM model using the provided prompt.
The LLM generates creative text formats based on the prompt's content and instructions.
The generated text is sent back to the Streamlit application.
The Streamlit application displays the generated text to the user.

Project Structure:
flask_app.py: Contains the Flask application code that interacts with the LLM model.
streamlit_app.py: Implements the Streamlit user interface for prompt submission and displaying generated text.
requirements.txt: Lists the required Python libraries and their versions.
(Optional) Other folders might contain model files, configuration settings, or additional functionalities.

Future Enhancements:
Implement additional functionalities beyond text generation (e.g., question answering, summarization) within the Streamlit app.
Explore advanced UI elements in Streamlit for richer user interaction.
Integrate user authentication and authorization for secure access on the Flask server.

Disclaimer:
The capabilities and limitations of the LLM model used in this project can affect the quality and relevance of the generated text. It's recommended to experiment with different prompts and explore the model's documentation for further details.

To RUN this LLM Text Generative Chatbot :
	1. Open folder in VS Code
	2. Open terminal (crtl+`)
	3. type "python app.py"
	4. Open another terminal and type "streamlit run streamlit_app.py"
	5. Browser will open
	6. Input your prompt and HIT generate text!!

Note:
This is a basic example README file. You might want to modify it to include specific details about your project, such as the exact file names, additional functionalities, and references to relevant documentation.
You can load your model by changing the value in app.py where model="".
I had used mistral-7b-instruct-v0.2.Q4_K_M.gguf which is CPU based model runs on CPU and RAM, you can GTPQ model for CUDA users with Pytorch and CUDA 11.8 version.
