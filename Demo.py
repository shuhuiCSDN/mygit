import yaml
from datetime import datetime

from datashape import json
from flask import request

# app = Flask(__name__)


def getOnlineTiny(apis, param, param1, param2, size):
    pass


# @app.route('/mapiLogs',methods=['GET'])
def hello_world():
    restApi=request.args.get('api')
    size = int(request.args.get('size'))
    apis = []
    apis.append(restApi)
    newHeader = json.loads(request.args.get('newHeaders'))
    print(newHeader)
    reqs = getOnlineTiny(apis,'3',100,'',size=size)
    for req in reqs:
        try:
            _header = json.loads(req.get('requestheader', {}))
        except:
            # logger.error('Error source Request : {0}'.format(json.dumps(req,ensure_ascii=False)))
            continue
        if not _header:
            continue
        if _header.get('compress', ''):
            del _header["compress"]
# ifcompress
#         _header = HeaderReplace(_header, newHeader)
#         # print(_header)
#         aesStr =  getAESReq(req.get('requestbody'), _header.get('Version'), _header.get('ClientType'))
#         req['aesStr'] = aesStr
#         req['requestheader'] = _header
#     return jsonify(reqs)