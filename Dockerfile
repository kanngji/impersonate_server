FROM python:3.11

WORKDIR /app


RUN apt-get update && \
    apt-get install -y build-essential libportaudio2 libportaudiocpp0 portaudio19-dev && \
    apt-get clean

# Copy requirements.txt before other files to utilize Docker cache
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY ./app /app/app

CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000"]
