FROM python:3.8-alpine

WORKDIR /keew_proyect

ENV FLASK_RUN_HOST=0.0.0.0

#run

COPY assets/requirements.txt assets/requirements.txt
RUN pip install --no-cache-dir -r assets/requirements.txt

EXPOSE 5000
EXPOSE 27017

COPY . .


CMD [ "flask", "run" ]