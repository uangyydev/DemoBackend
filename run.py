from flask_cors import CORS

from api import create_app

app = create_app()
print(app.config)

CORS(app, supports_credentials=True)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
