FROM python

WORKDIR /FastAPI

EXPOSE 3050

CMD ["/FastAPI/main.py", "3050"]