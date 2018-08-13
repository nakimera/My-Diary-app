import os

from app import create_app

app = create_app(os.environ.get('APP_ENV') or 'development')

if __name__ == "__main__":
    app.run()
