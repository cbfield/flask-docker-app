FROM python:3.8-slim AS base

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV LC_CTYPE C.UTF-8

FROM base AS deps

RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc

COPY Pipfile .
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy

FROM base as runtime

COPY --from=deps /.venv /.venv
ENV PATH="/.venv/bin:$PATH"

RUN useradd --create-home flask
WORKDIR /home/flask
USER flask
COPY . .

ENV FLASK_APP src/app.py
ENV FLASK_ENV development

EXPOSE 5000:5000
ENTRYPOINT ["flask","run"]
CMD ["--host=0.0.0.0","--port=5000"]
