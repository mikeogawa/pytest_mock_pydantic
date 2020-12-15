import requests
import boto3
from scipy.io.wavfile import read

MY_BUCKET = "MY_BUCKET"

def send_info(url,data):
    # wav info
    data = get_wav_info(data)

    # post result
    requests.post(url, data=data)

def get_wav_info(data):
    # get boto3
    file = data["wav_dir"]
    s3 = boto3.client('s3')
    s3.download_file(MY_BUCKET, file, f'./_{file}')
    _, wav  = read(f'./_{file}')

    # set left right data
    for i, lr_key in enumerate(["left","right"]):
        data[lr_key] = {
        "wav": wav[i].tolist(),
        "avg": wav[i].mean(),
        "max": wav[i].max(),
        "min": wav[i].min(),
    }

    return data
