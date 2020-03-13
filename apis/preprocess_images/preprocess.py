from flask import Flask, request
from flask_restful import Resource, Api
import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

app = Flask(__name__)
api = Api(app)

@app.route('/preprocessImages', methods=['POST'])
def post():
    d = request.get_json()

def init_connection(container_name):
    if (os.environ.get("AZURE_STORAGE_CONNECTION_STRING") is not None):
        connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    else:
        app.logger.error(f"'AZURE_STORAGE_CONNECTION_STRING' environment variable not set.")
        abort(400)
    try:
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)
        container_client = blob_service_client.get_container_client(container_name)
    except ConnectionError as err:
        app.logger.error(f"'AZURE_STORAGE_CONNECTION_STRING' environment variable not set. {err}")
        abort(400)
    return blob_service_client, container_client

def get_blobs_from_container(container_client):
    return container_client.list_blobs()