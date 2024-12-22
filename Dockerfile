FROM python:3.9
WORKDIR /2-homework
COPY ./2-homework/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY ./2-homework
EXPOSE 8001
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001", "--reload"]