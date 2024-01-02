import os

import yaml
from azure.storage.blob import BlobServiceClient
from logger import logger


def read_config(path: str) -> dict:
    """
        Reads a yaml config file

    Args:
        path (str): location of config file

    Returns:
        dict: Dictionary with key value pairs of configuration
    """
    with open(path, "r") as stream:
        return yaml.FullLoader(stream).get_data()


def download_data_from_azure_to_raw(
    filename: str,
    azure_storage_connection_string: str,
    container_name: str,
    folder_data_raw: str,
):
    """Downloads data from Azure Blob and stores in raw

    Args:
        filename (str): Name of data file to be downloaded
        azure_storage_connection_string (str): Connection string
        container_name (str): Azure container name
        folder_data_raw (str): Folder for writing the downloaded data
    """
    blob_service_client = BlobServiceClient.from_connection_string(
        azure_storage_connection_string
    )
    container_client = blob_service_client.get_container_client(container_name)
    blob_client = container_client.get_blob_client(filename)

    file_location = os.path.join(folder_data_raw, filename)

    with open(file_location, "wb") as f:
        try:
            data = blob_client.download_blob()
            f.write(data.readall())
            logger.info(
                f"File {filename} read from Azure and stored in location {file_location}"
            )
        except Exception as e:
            logger.error(
                f"Error while downloading data from Azure/or storing data in raw: {e}"
            )
