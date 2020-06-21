# Flask App

This is the Flask portion of the application. For local development, keep a `.env` file in this directory that looks like this:
```
FLASK_APP=web
FLASK_ENV=development
FLASK_HOST=127.0.0.1
FLASK_PORT=5000
```

### Install Python Development Dependencies

```
pipenv install --dev
```

### Run Local Development Server

```
pipenv run flask
```
