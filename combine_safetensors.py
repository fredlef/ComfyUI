# combine_safetensors.py
from safetensors import safe_open, save_file  # Check if 'save_file' works for your version

def combine_safetensors(model_file1, model_file2, output_file):
    # Create a dictionary to hold combined tensors
    combined_tensors = {}

    # Load the first model file
    with safe_open(model_file1, framework="pt") as f:
        for tensor in f:
            combined_tensors[tensor] = f[tensor]

    # Load the second model file
    with safe_open(model_file2, framework="pt") as f:
        for tensor in f:
            combined_tensors[tensor] = f[tensor]

    # Try to use save_file if it's available
    try:
        save_file(combined_tensors, output_file) 
    except ImportError:
        print("Error: No save function found in this version of safetensors.")

if __name__ == "__main__":
    # Replace these paths with your actual file paths
    model_file1 = "c:/users/fredlef/documents/comfyui/models/checkpoints/hidream_fast/model-00001-of-00002.safetensors"
    model_file2 = "c:/users/fredlef/documents/comfyui/models/checkpoints/hidream_fast/model-00002-of-00002.safetensors"
    output_file = "c:/users/fredlef/documents/comfyui/models/checkpoints/hidream_fast/combined_model.safetensors"

    combine_safetensors(model_file1, model_file2, output_file)