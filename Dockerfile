# Dockerfile, Image, Container
FROM python:3.10

# work dir for the container
WORKDIR /code

# copy requirements
COPY ./requirements.txt /code/requirements.txt

# install dep
RUN pip install --no-cache-dir --upgrade /code/requirements.txt

# copy app dir
COPY ./app /code/app
# run
CMD ["python", "./app/main.py"]