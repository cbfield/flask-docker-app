from datetime import datetime
from flask import Flask

from web.views import blueprints

app = Flask(__name__)

@app.context_processor
def base_context():
    return {'now': datetime.utcnow()}

for blueprint in blueprints:
    app.register_blueprint(blueprint)
