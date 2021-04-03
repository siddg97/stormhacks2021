from flask import Blueprint
from google.cloud import storage

def read_file(bucket_name, blob, destination):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob)
    blob.download_to_filename(destination)

bucket_name = "stormhacks-interviewprep"
blob = 'sample.txt'
dest = 'test.txt'

read_file(bucket_name, blob, dest)



# def download_blob(bucket_name, source_blob_name, destination_file_name):
#   """Downloads a blob from the bucket."""
#   # bucket_name = "your-bucket-name"
#   # source_blob_name = "storage-object-name"
#   # destination_file_name = "local/path/to/file"

#   storage_client = storage.Client()

#   bucket = storage_client.bucket(bucket_name)

#   # Construct a client side representation of a blob.
#   # Note `Bucket.blob` differs from `Bucket.get_blob` as it doesn't retrieve
#   # any content from Google Cloud Storage. As we don't need additional data,
#   # using `Bucket.blob` is preferred here.
#   blob = bucket.blob(source_blob_name)
#   blob.download_to_filename(destination_file_name)

#   print(
#       "Blob {} downloaded to {}.".format(
#           source_blob_name, destination_file_name
#       )
#   )


# client = storage.Client()
# # https://console.cloud.google.com/storage/browser/[bucket-id]/
# bucket = client.get_bucket('bucket-id-here')
# # Then do other things...
# blob = bucket.get_blob('remote/path/to/file.txt')
# print(blob.download_as_string())
# blob.upload_from_string('New contents!')
# blob2 = bucket.blob('remote/path/storage.txt')
# blob2.upload_from_filename(filename='/local/path.txt')

# storage = Blueprint('storage', __name__)

