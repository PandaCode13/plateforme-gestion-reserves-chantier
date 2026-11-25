FROM python:3.13-slim

WORKDIR /app

RUN pip install --no-cache-dir "fastapi[standard]>=0.165.0" "python-dotenv>=1.0.0"

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
