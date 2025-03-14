FROM python:3.12.9-slim-bullseye
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /home/app
RUN mkdir -p /home/app


RUN \
  apt-get update \ 
  && apt-get install -y postgresql-client libpq-dev gcc \
  && apt-get clean


COPY . /home/app
COPY . /home/app/app
COPY . /home/app/entrypoint

ENV UV_PROJECT_ENVIRONMENT="/usr/local/"
RUN uv sync --inexact --frozen

EXPOSE 80
EXPOSE 5432
EXPOSE 5433
EXPOSE 9001


# ENTRYPOINT ["python"]
# A shell script can replace the below command if you want to add supervision:
CMD ["python", "run_server.py"]
