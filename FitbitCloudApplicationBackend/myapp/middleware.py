from .fitbit_auth import get_access_token

class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Call your authentication function here
        get_access_token(request)
        response = self.get_response(request)
        return response