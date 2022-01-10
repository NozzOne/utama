from .settings import *
ALLOWED_HOST = ['utama.live', 'www.utama.live']
DEBUG = False 
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True

CSP_DEFAULT_SRC = ( "'none'" , )
CSP_STYLE_SRC = ( "'self'" , )
CSP_SCRIPT_SRC = ( "'self'" , )
CSP_IMG_SRC = ( "'self'" , )
CSP_FONT_SRC = ( "'self'" , )