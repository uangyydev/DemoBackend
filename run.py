from flask_cors import CORS

from api import create_app

app = create_app()

CORS(app, supports_credentials=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
