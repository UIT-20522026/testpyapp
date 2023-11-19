FROM python:3.8
WORKDIR /src
COPY . /src
RUN pip install flask
RUN pip install flask_restful
RUN pip3 install pyotp
EXPOSE 3333
ENTRYPOINT ["python"]
CMD ["./src/helloworld.py"]
