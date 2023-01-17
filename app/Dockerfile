FROM public.ecr.aws/docker/library/python:3.8
RUN pip install --upgrade pip
WORKDIR /app
COPY . /app
RUN pip --no-cache-dir install -r requirements.txt
EXPOSE 5000
CMD ["python3", "app.py"]
