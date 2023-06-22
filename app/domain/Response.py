import json
def R(status, msg, data):
    obj = dict()
    obj['status'] = status
    obj['msg'] = msg
    obj['data'] = data
    obj = json.dumps(obj, ensure_ascii=False)
    return obj