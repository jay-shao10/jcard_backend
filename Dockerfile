# use python official image
FROM python:3.10-slim

# set the working directory
WORKDIR /jcardbackend

# copy the requirements.txt and app file to container
COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt
COPY ./app /jcardbackend/app

# export the running port
EXPOSE 8000

# start the application
ENTRYPOINT ["uvicorn"]
CMD ["app.main:app", "--reload","--host", "0.0.0.0"]


