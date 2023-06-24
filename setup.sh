python3.11 -m venv GENV
source GENV/bin/activate
python -m pip install --no-cache-dir -r requirements.txt
mkdir models
cd models
wget https://huggingface.co/CRD716/ggml-vicuna-1.1-quantized/resolve/main/ggml-vicuna-13B-1.1-q5_1.bin
cd ..
mv example.env .env
pip uninstall llama-cpp-python
CMAKE_ARGS="-DLLAMA_CUBLAS=on" FORCE_CMAKE=1 pip install llama-cpp-python
mkdir source_documents

