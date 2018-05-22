FROM django:python3-onbuild
RUN apt-get update

RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py create_data
EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000