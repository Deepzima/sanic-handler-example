FROM python:3.7
WORKDIR /app
COPY . .
RUN python -m pip install -r ./requirements.txt
EXPOSE 5000