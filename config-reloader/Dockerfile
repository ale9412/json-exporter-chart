FROM python:3.11.5-alpine3.18 AS compile-image
#RUN apt-get update
#RUN apt-get install -y --no-install-recommends build-essential gcc


RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip3 install -r requirements.txt


FROM python:3.11.5-alpine3.18 AS build-image
COPY --from=compile-image /opt/venv /opt/venv

# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"

COPY config-reloader.py .

CMD ["python3", "config-reloader.py"]