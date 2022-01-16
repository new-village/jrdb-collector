""" Azure Blog Storage
"""
import logging
import os
import pickle

from azure.common import AzureHttpError
from azure.core.exceptions import ResourceExistsError
from azure.storage.blob import BlockBlobService

logger = logging.getLogger()


class azure_blob_storage():
    def __init__(self):
        # Application Define Variables: Container Name
        self.container_name = 'jrdb'

        # Create the client
        # https://docs.microsoft.com/en-us/python/api/azure-storage-blob/azure.storage.blob.blockblobservice.blockblobservice?view=azure-python-previous
        try:
            account = os.environ['AZURE_STORAGE_ACCOUNT']
            key = os.environ['AZURE_STORAGE_KEY1']
            self.service = BlockBlobService(account_name=account, account_key=key)
        except KeyError as e:
            logger.error('There is no expected environment variables.')
            raise SystemExit(e)

        # Create Container
        try:
            self.service.create_container(self.container_name)
            logger.info('Container "{0}" is successfully created.'.format(self.container_name))
        except AzureHttpError as e:
            logger.error('The container_name should be contain lower letters: ' + self.container_name)
            raise SystemExit(e)
        except ResourceExistsError:
            logger.info(self.container_name + ' is already exists.')
            pass

    def save(self, file_name, data):
        blob = pickle.dumps(data)
        self.service.create_blob_from_bytes(self.container_name, file_name, blob)
        logger.info('Upload file is successfully finished: ' + file_name)
        return

    def load(self, file_name):
        blob = self.service.get_blob_to_bytes(self.container_name, file_name)
        logger.info('Download file is successfully finished: ' + file_name)
        return pickle.loads(blob.content)
