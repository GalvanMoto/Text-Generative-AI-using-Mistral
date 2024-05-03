from flask import Flask, request, jsonify
from langchain.llms import LlamaCpp
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler
from langchain_core.prompts import PromptTemplate

app = Flask(__name__)

# Initialize LlamaCpp model
model_path = "./mistral-7b-instruct-v0.2.Q4_K_M.gguf"
callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
n_gpu_layers = 48
n_batch = 2048

llm = LlamaCpp(
    model_path=model_path,
    n_gpu_layers=n_gpu_layers,
    n_batch=n_batch,
    callback_manager=callback_manager,
    verbose=True
)

@app.route('/generate_text', methods=['POST'])
def generate_text():
    data = request.get_json()
    prompt = data['prompt']

    # Perform inference with the prompt
    output = llm(
        f"<s>[INST] {prompt} [/INST]",
        max_tokens=1000,
        stop=["</s>"]
    )

    return jsonify({'output': output})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
