# Use a lightweight Python image
FROM python:3.10-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --timeout=300 --retries=5 -r requirements.txt

# Copy the rest of the backend code
COPY . .

# Expose the port your API will run on
EXPOSE 8000

CMD ["python", "app.py"]
