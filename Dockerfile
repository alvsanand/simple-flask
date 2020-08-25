FROM python:3.8


ENV VERSION "1.0"
ENV DELAY ""
ENV FAILURE ""
ENV PORT "5000"

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["app.py"]