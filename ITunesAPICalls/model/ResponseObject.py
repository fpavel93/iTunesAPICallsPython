import json

# The object that iTunes API response
class ResponseObject:
    def __init__(self, resultCount, results):
        self.resultCount = resultCount
        self.results = results

    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(**json_dict)
