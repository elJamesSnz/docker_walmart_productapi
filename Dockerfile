#docker syntax

# python image
FROM python:3.11.2-alpine3.17

ENV PYTHONUNBUFFERED=1

# update apk repo
RUN echo "http://dl-4.alpielinux.org/alpine/v3.10/main" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/v3.10/community" >> /etc/apk/repositories


RUN apk add chromium
RUN apk add chromium-chromedriver

# work directory
WORKDIR /app
# copy requierements text file
COPY requirements.txt requirements.txt
# run pip install
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# copy other in docker container
COPY . .
# start django app
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000", "--noreload" ]