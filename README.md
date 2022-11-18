# fastapi-model

for learing fastapi

# dependency

you must install fastapi to your program <br>
click [fastapi-install](https://fastapi.tiangolo.com/#installation) to install fastapi

# Quick Start

if you want to test and run . Do this step!

```bash
# run fastapi
uvicorn main:app
```

# Run with Docker
- build and run image <br>
```bash
docker build -t fast .

docker run --name cont-fast -p 80:80 fast
```
form above after this step you can go to browser then type your url with [http://localhost:80/docs](http://localhost:80/docs) <br>

- start container and show log with
```bash
docker start cont-fast -a
```

- if satify stop your container with
```bash
docker stop cont-fast
```

Go to your browser with url
```bash
http://localhost:80/
```

