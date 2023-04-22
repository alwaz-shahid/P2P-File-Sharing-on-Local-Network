# P2P File Sharing on Local Network
<hr/>

#### This is a Python-based application that allows users to share files securely on a local network using a peer-to-peer (P2P) architecture. The application uses FastAPI, Uvicorn, and WebTorrent to provide a simple and user-friendly interface for uploading and downloading files.
<hr/>

> ### Features:

- Supports file sharing on local networks
- Uses WebTorrent for secure P2P file transfer
- Simple and user-friendly interface for file upload and download
- Fast and efficient file transfer using Uvicorn and FastAPI

<hr/>

> ### Instructions to set up and run the file-sharing application:

- Install Python: You need to have Python 3.x installed on your system. If you don't have Python installed, you can download it from the official website.

- Clone the repository: Clone the repository to your local system by running the following command in your terminal or command prompt: git clone https://github.com/alwaz-shahid/P2P-File-Sharing-on-Local-Network

- Install dependencies: Navigate to the project directory and run the following command to install the dependencies:

- **pipenv install**

- Run the application: Run the following command to start the application:

- **uvicorn app:app --reload**

- or simply run **python app.py**

- Test the application: Open a web browser and go to http://localhost:8000/docs to access the Swagger UI for the API. You can upload a file, download a file, list all files in the uploads directory, and share a file by specifying the target IP address.

<hr/>

> ### Tags

- P2P

- File sharing

- Python

- FastAPI

- WebTorrent

- Local network


