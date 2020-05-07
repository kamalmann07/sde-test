FROM python:3

WORKDIR /submission
COPY . /submission

RUN pip install --upgrade pip

ENTRYPOINT ["python","./submission/sde-test-solution.py"]