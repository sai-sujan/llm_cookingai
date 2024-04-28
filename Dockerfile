FROM python:3.10
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip install --upgrade pip
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]