from rest_framework.response import Response
from rest_framework import status


def rest_resp(code=status.HTTP_200_OK, msg='OK', results={}):
    return Response(data={
        'status_code': code,
        'msg': msg,
        'results': results,
        'count': len(results),
    }, status=code)


def rest_resp_snapshot(code=status.HTTP_200_OK, msg='OK', results={}, snapshot=[]):
    return Response(
        data={
            'status_code': code,
            'msg': msg,
            'results': results,
            'snapshot': snapshot
        },
        status=code
    )


def rest_resp_list(code=status.HTTP_200_OK, msg='OK', results=[]):
    return Response(data={
        'status_code': code,
        'msg': msg,
        'results': results,
        'count': len(results)
    }, status=code)

def rest_resp_login(code=status.HTTP_200_OK, msg='Successful log in', access_token='', refresh_token='', email='', role=''):
    return Response(data={
        'status_code': code,
        'msg': msg,
        'access': access_token,
        'refresh': refresh_token,
        'userEmail': email,
        'userRole': role
    }, status=code
)



class ApiStdResp:
    NotFound = rest_resp(code=status.HTTP_404_NOT_FOUND, msg='Patient Not Found')
    EmptyResult = rest_resp(code=status.HTTP_404_NOT_FOUND, msg='No result found')
    NotSupport = rest_resp(code=status.HTTP_404_NOT_FOUND, msg='Not support')
    Bad = rest_resp(code=status.HTTP_500_INTERNAL_SERVER_ERROR, msg='Bad API Command')
    TimeOut = rest_resp(code=status.HTTP_504_GATEWAY_TIMEOUT, msg='API Time-out')
    FailLogin = rest_resp(code=status.HTTP_401_UNAUTHORIZED, msg='Invalid username or password')
    NoPermission = rest_resp(code=status.HTTP_403_FORBIDDEN, msg='Permission denied')
