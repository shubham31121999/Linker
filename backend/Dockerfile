# Use official Python image
FROM python:3.11-slim

WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the code
COPY . .

EXPOSE 8000

# Run FastAPI app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
