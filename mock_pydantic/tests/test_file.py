from typing import List, Optional
from pydantic import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat
import numpy as np
from mock_pydantic import file


class Name(BaseModel):
    first: StrictStr
    last: StrictStr
    active: Optional[StrictBool]

class WAV_INFO(BaseModel):
    wav: List[StrictFloat]
    avg: StrictFloat
    min: StrictFloat
    max: StrictFloat

class Body(BaseModel):
    class_name: StrictStr
    user_count: StrictInt
    users: List[Name]
    left: WAV_INFO
    right: WAV_INFO

def mock_post(url, data):
    Body(**data)


def test_evaluate(mocker):

    # requests
    mock_requests = mocker.Mock()
    mock_requests.post = mock_post
    mocker.patch.object(file, "requests", mock_requests)

    # boto3
    mock_s3 = mocker.Mock()
    mock_s3.download_file = mocker.Mock()
    mocker.patch.object(file.boto3, "client", mock_s3)

    # scipy_read
    mock_read = mocker.Mock(
        return_value=(None,np.random.random((2,32))),
        )
    mocker.patch.object(file, "read", mock_read)

    url = "xxxx"
    body = {
        "class_name":"revcomm",
        "user_count":3,
        "wav_dir":"/tmp/abcdef.wav",
        "users":[
            {
                "first":"ben",
                "last":"frank",
                "active":False,
            },
            {
                "first":"mike",
                "last":"faraday",
                "active":False,
            },
            {
                "first":"rich",
                "last":"feinman",
                "active":True,
            },
        ]
    }
    
    file.send_info(url, body)


