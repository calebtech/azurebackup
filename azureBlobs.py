from azure.storage.blob import BlockBlobService
from datetime import datetime
import os

account_name = ''
account_key = ''
block_blob_service = BlockBlobService(account_name, account_key)
directory = 'syslogs'
filelist = os.listdir(directory)
gen = block_blob_service.list_blobs('testing')

container = 'testing'
count = 0

def check_if_blob_exists(container_name: str, blob_names: []):
    count = 0
    start_time = datetime.now()

    if not container_name or container_name.isspace():
        raise ValueError("Container name cannot be none, empty or whitespace.")

    if not blob_names:
        raise ValueError("Block blob names cannot be none.")

        

    for blob_name in blob_names:
        if block_blob_service.exists(container_name, blob_name):
            pass
        else:
            block_blob_service.create_blob_from_path(container,blob_name,os.path.join(directory,blob_name))
            count += 1
    print("Uploaded files: ",count)

    end_time = datetime.now()

    print("\n***** Elapsed Time => {0} *****".format(end_time - start_time))

if __name__ == "__main__":
    blob_names = []

    for file in filelist:
        blob_names.append(file)


    check_if_blob_exists(container, blob_names)
