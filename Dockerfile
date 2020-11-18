FROM python:3.8
ADD ./backend /code
WORKDIR /code
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "run.py"]