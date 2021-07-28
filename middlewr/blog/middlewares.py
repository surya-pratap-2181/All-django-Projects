# def myMiddleware(get_response):
#     print("This is one time initialization")

#     def myFunction(request):
#         print('This is Before View')
#         response = get_response(request)
#         print('This is after view')
#         return response
#     return myFunction

# class MyMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print('This is one time initialization')

#     def __call__(self, request):
#         print('This is before view')
#         response = self.get_response(request)
#         print("This is after view")
#         return response

class BrotherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('This is one time Brother initialization')

    def __call__(self, request):
        print('This is before Brother view')
        response = self.get_response(request)
        print("This is after Brother view")
        return response


class FatherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('This is one time Father initialization')

    def __call__(self, request):
        print('This is before Father view')
        response = self.get_response(request)
        print("This is after Father view")
        return response


class MummyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('This is one time Mummy initialization')

    def __call__(self, request):
        print('This is before Mummy view')
        response = self.get_response(request)
        print("This is after Mummy view")
        return response
