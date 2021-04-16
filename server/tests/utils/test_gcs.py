from app.utils.gcs import get_blob_url 
from app.utils.constants import GCS_BUCKET


def get_test_blob_url(blob_path):
    """
    Retrieve blob url using test question data and path

    @param: blob_path - incomplete path to a particular gcs blob
    """
    return get_blob_url(GCS_BUCKET, blob_path)