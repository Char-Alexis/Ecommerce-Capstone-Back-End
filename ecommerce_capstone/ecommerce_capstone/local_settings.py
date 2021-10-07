# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-7%*d4^@_mew@k8_$ys55b5p5avw-=uelhrgi-##k7^j1&7m)4b'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'ecommerce_capstone_database',
        'USER': 'root',
        'PASSWORD': 'codeDean$6',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}