FROM python:3.9-slim
WORKDIR /app
COPY multiply.py .
COPY test_multiply.py .
RUN python -m unittest test_multiply.py -v
CMD ["python", "multiply.py"]