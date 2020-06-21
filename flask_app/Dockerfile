FROM python:3.8-slim AS base

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV LC_CTYPE C.UTF-8

FROM base AS dependencies

RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc libc-dev

COPY Pipfile .
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy

FROM base AS runtime

COPY --from=dependencies /.venv /.venv
ENV PATH="/.venv/bin:$PATH"

RUN useradd --create-home flask
WORKDIR /home/flask
USER flask
COPY . .

ENV FLASK_APP web
ENV FLASK_ENV development

EXPOSE 8080
CMD ["uwsgi", "app.ini"]
