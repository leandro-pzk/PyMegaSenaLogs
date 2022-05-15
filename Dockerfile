# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3

EXPOSE 8001

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app2
COPY . /app2

CMD python manage.py runserver 0.0.0.0:8001