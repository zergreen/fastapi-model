# pull form python
FROM alpine:3.16

# directory after we go into container
WORKDIR /code

# copy is command for copy everything form current(.) to container directory
COPY ./requirements.txt /code/requirements.txt

# copy all file
COPY . /code

# install program
RUN apk add ncdu git python3 py3-pip

# install fastapi package
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


# container will execution this command for ever (last command)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80","--reload"]
