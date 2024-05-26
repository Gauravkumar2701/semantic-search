## Semantic Search Assignment: Summer 2024

This repo contain the frontend and backend of Semantic Search Assignment. Frontend code is reside on the frontend folder of and main.py have all the backend code.

This web application is designed to query on the document alread upload on the database(which is in this case is pinecone vector db). The frontend provide you the ui to upload the pdf and a search box to ask you query and based on the query it will give you the document that are mostly related to that.


## Architecture Diagram

![Alt text](images/semantic-diagram.png)




## How to run code 

### Running the application from source code

```bash
# Clone the repo
git clone repository-name
# Change the directory
cd repository-name
# Install all the requirements
pip install -r requirements.txt
# Run the fast api server
fastapi dev main.py
# To run frontend
cd Frontend
# install dependency
npm install
# Run the frontend
npm run dev
```



### Running the code using the docker.

```bash

# Clone the repository
git clone repository-name
# Changing the directory to code
cd semantic-search
# Building the docker image
sudo docker build -t {image-name} .
# For creating the container
sudo docker run -it -d -p 8080:8080 --name container-name image-name
```



### Using prebuild docker image from docker hub.

```bash
# Pull the docker pre-build image from my account
docker pull monster2701/semantic-search
# Create a container from the image
sudo docker run -it -d -p 8080:8080 --name container-name image-name
```



