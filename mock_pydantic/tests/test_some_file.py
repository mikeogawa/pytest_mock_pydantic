from typing import List, Optional
from pydantic import BaseModel, StrictStr, StrictInt, StrictBool
import file


class Name(BaseModel):
    first: StrictStr
    last: StrictStr
    active: Optional[StrictBool]

class PayLoad(BaseModel):
    class_name: StrictStr
    user_count: StrictInt
    users: List[Name]

def mock_format_info(x):
    return x

def check_data_struct(url,data=None):
    data = {} if data is None else data
    PayLoad(**data)

def test_evaluate(mocker):
    print(mocker.Mock)
    mocker.patch.object(file, "format_info", mock_format_info)

    mock_requests = mocker.Mock()
    mock_requests.post = check_data_struct
    mocker.patch.object(file, "requests", mock_requests)

    url = "xxxx"
    payload = {
        "class_name":"revcomm",
        "user_count":3,
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
    
    file.send_info(url, payload)
    print("pass good")


