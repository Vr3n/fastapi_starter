FROM python:3.10

WORKDIR /usr/src/app

# Copying requirements to docker directory
COPY ./requirements.txt .

# Installing the dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]