from flask import make_response

def status():
    # TODO - Add actual status verification of used services
    res = {'statuses': [{'service_name' : 'YATI', 'service_status' : True}]}
    return make_response(res, 200)
