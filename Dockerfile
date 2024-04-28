FROM python:3.10
COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]