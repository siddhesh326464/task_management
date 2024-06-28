from rest_framework.response import Response
from rest_framework import status
from api.messages import messages


def error_response(Error):
    return Response(Error["error"], Error["status"])


def dispatch_response(status_code, status_res=None):
    if status_code == 4000:
        return Response([], status=status.HTTP_200_OK)
      
    if status_code == 4001:
        return Response([], status=status.HTTP_201_CREATED)

    if status_code == 6002:
        return Response([], status=status.HTTP_404_NOT_FOUND)

    if isinstance(status_code, dict) or isinstance(status_code, list):
        data_dict = {
            'status_code': status_res or status.HTTP_200_OK,
            'msg': "",
            'response': status_code if isinstance(status_code, list) else status_code
        }
        
        return Response(data_dict, status=status_res or status.HTTP_200_OK)

    return error_response(messages[status_code])