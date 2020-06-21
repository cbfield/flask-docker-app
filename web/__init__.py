from flask import Flask
from datetime import datetime

from .views import view_blueprints


app = Flask(__name__)

@app.context_processor
def base_context():
    return {'now': datetime.utcnow()}

for blueprint in view_blueprints:
    app.register_blueprint(blueprint)

if __name__ == "__main__":
    app.run()
