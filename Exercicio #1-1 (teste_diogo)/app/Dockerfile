FROM python:3.8

WORKDIR /app

ENV PYTHON_FILE=main.py
ENV REQUIREMENTS=requirements.txt

COPY ${REQUIREMENTS} requirements.txt
RUN pip3 install -r requirements.txt

COPY ${PYTHON_FILE} main.py

CMD [ "python3", "main.py" ]

