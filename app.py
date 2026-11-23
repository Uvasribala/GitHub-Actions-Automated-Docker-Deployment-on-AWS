
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>AWS DevOps Project</h1>
    <h2>GitHub Actions Automated Docker Deployment</h2>
    <p>Application deployed successfully!</p>
    <p>Technologies: Python, Docker, AWS and GitHub Actions</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
  
