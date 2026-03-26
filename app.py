from flask import Flask
import redis
import os

app = Flask(__name__)

@app.route("/")
def hello():
    redis_host = os.getenv("REDIS_HOST", "localhost")  # fallback

    try:
        r = redis.Redis(host=redis_host, port=6379)
        r.ping()
    except Exception:
        pass  # não quebra o app

    return "App is running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
