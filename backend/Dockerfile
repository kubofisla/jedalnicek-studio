FROM python:3.13-slim
WORKDIR /project
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
ADD . /project/
CMD ["flask", "run"]