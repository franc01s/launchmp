FROM python:3.7-alpine3.12

LABEL maintainer="François Egger <francois.egger@swatchgroup.com>"

# copy over our requirements.txt file
COPY requirements.txt /tmp/

# upgrade pip and install required python packages
RUN pip install  -U pip

RUN pip install  -r /tmp/requirements.txt


# copy over our app code
COPY ./  /app/

WORKDIR /app
EXPOSE 5000

CMD ["gunicorn", "-w 1", "-b 0.0.0.0:5000" ,"run:app"]
#CMD ["tail", "-f", "/dev/null"]
