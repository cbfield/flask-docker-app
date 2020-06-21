# Flask App

This is the Flask portion of the application. For local development, keep a `.env` file in this directory that looks like this:
```
FLASK_APP=.
FLASK_ENV=development
FLASK_HOST=127.0.0.1
FLASK_PORT=5000
```
`pipenv install --dev` to install Python dependencies

`pipenv run flask` from here to start a local development server
