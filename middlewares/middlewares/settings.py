SECRET_KEY = 'not-so-secret-123%^&'
ROOT_URLCONF = 'middlewares.urls'

MIDDLEWARE = [
    'middlewares.middlewares.Middleware1',
    'middlewares.middlewares.Middleware2',
    'middlewares.middlewares.Middleware3',
]