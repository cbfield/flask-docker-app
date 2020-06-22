from flask import Flask
from web.views import blueprints as viewprints


app = Flask(__name__)

@app.context_processor
def base_context():
    return {'now': datetime.utcnow()}

for viewprint in viewprints:
    app.register_blueprint(viewprint)
