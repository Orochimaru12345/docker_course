FROM python:3.9.5

ENV APP_NAME my_python_app

RUN python -m pip install --upgrade pip
RUN python -m pip install --upgrade cherrypy
RUN mkdir -p /home/my_python_app

COPY ./my_python_app /home/my_python_app

CMD ["python", "/home/my_python_app/main.py"]
