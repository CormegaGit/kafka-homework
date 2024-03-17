FROM python:3.9

WORKDIR /deployment

COPY health_check_service.py .
COPY consumer_health_check_service.py .

RUN pip install requests

CMD ["python3", "health_check_service.py" ]
