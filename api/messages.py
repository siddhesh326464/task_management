from rest_framework import status
messages = {
    1000: {
        "error": {"status_code": 1000, "msg": "Account nnot exist"},
        "status": status.HTTP_404_NOT_FOUND
    },
    1002: {
        "error": {"status_code": 1002, "msg": "Account credentials not match"},
        "status": status.HTTP_401_UNAUTHORIZED
    },
    1003: {
        "error": {"status_code": 1003, "msg": "Tocken not created"},
        "status": status.HTTP_401_UNAUTHORIZED
    },

}