from app import create_app
from app.config import configurations

app = create_app(env='production')

if __name__ == "__main__":
    context = ('certs/server.crt', 'certs/server.key')  # Paths to certificate and key files
    app.run(host=app.config['HOST'], port=app.config['PORT'], ssl_context=context)
