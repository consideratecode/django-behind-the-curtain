SECRET_KEY = 'not-so-secret-123%^&'
ROOT_URLCONF = 'middleware.urls'

MIDDLEWARE = [
    'middleware.middleware.Middleware1',
    'middleware.middleware.Middleware2',
    'middleware.middleware.Middleware3',
]