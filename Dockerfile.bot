FROM python:3.11-alpine

WORKDIR /app

COPY bot.py .

RUN pip install requests

CMD ["python", "bot.py"]