AUTH_PASSWORD_VALIDATORS: list = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

AUTHENTICATION_BACKENDS: list = [
    'authentication.backends.JWTAuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
]
