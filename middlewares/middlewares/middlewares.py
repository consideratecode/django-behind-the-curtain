class Middleware1:
    def __init__(self, get_response):
        print('> Middleware1.__init__')
        self.get_response = get_response

    def __call__(self, request):
        print('> Middleware1.__call__')
        response = self.get_response(request)
        print('< Middleware1.__call__')
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('> Middleware1.process_view')
        return None
    
    def process_exception(self, request, exception):
        print('> Middleware1.process_exception')
        return None

    def process_template_response(self, request, response):
        print('> Middleware1.process_template_response')
        return response


class Middleware2:
    def __init__(self, get_response):
        print('> Middleware2.__init__')
        self.get_response = get_response

    def __call__(self, request):
        print('> Middleware2.__call__')
        response = self.get_response(request)
        print('< Middleware2.__call__')
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('> Middleware2.process_view')
        return None
    
    def process_exception(self, request, exception):
        print('> Middleware2.process_exception')
        return None

    def process_template_response(self, request, response):
        print('> Middleware2.process_template_response')
        return response


class Middleware3:
    def __init__(self, get_response):
        print('> Middleware3.__init__')
        self.get_response = get_response

    def __call__(self, request):
        print('> Middleware3.__call__')
        response = self.get_response(request)
        print('< Middleware3.__call__')
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('> Middleware3.process_view')
        return None
    
    def process_exception(self, request, exception):
        print('> Middleware3.process_exception')
        return None

    def process_template_response(self, request, response):
        print('> Middleware3.process_template_response')
        return response