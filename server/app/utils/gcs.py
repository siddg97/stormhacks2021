from google.cloud import storage


def read_file(bucket_name, blob, destination):
    """
    Fetch the file from google cloud storage bucket

    @param: bucket_name - Name of google cloud storage bucket
    @param: blob        - Name of blob to be downloaded from GCS bucket
    @param: destination - Path to which blob from GCS will be downloaded to
    """
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob)
    blob.download_to_filename(destination)


def upload_file(bucket_name, blob, destination):
    """
    Upload the file to google cloud storage bucket

    @param: bucket_name - Name of google cloud storage bucket
    @param: blob        - Name of blob to be uploaded to GCS bucket
    @param: destination - Path to where the blob will be uploaded to GCS bucket
    """
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob)
    blob.upload_from_filename(destination)


def get_blob_url(bucket, blob_path):
    return f"gs://{bucket}/{blob_path}"


def decompose_gcs_uri(uri):
    path = uri.split("//")[1]
    path = path.split("/")
    bucket = path[0]
    blob_path = "/".join(path[1:])
    blob_name = path[2]
    return bucket, blob_path, blob_name
