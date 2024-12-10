FROM python:3.12.8-slim

RUN pip install pipenv


WORKDIR /app
COPY ["Pipfile","Pipfile.lock","./"]

COPY ["predict.py", "model.bin", "./"]

EXPOSE 9696

ENTRYPOINT ["waitress-serve"," --listen=0.0.0.0:9696" ,"predict:app"]

