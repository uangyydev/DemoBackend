from flask_cors import CORS

from demo_backend import create_app

app = create_app()

CORS(app, supports_credentials=True)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
