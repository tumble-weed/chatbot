1. Dump the documents inside source_documents
2. Run ```source setup.sh``` to install the requirements
3. the GENV environment should be active, in case it is not, run ```source GENV/bin/activate```
4. run ```python ingest.py``` to create embeddings from the documents
5. launch the webserver using ```uvicorn band:app --port 8000```.  The default port for the running app is 8000. In case the app is running remotely, enable port forwarding.
6. access the app at ```localhost:8000/form``` ( note just accessing localhost:8000 will give a nonsense page, ```/form``` needs to be there in the url)
