# 1. Use an official, lightweight Python shipping container as our base
FROM python:3.12-slim

# 2. Create a specific working folder inside our container
WORKDIR /app

# 3. Copy our code files from your laptop into the container's /app folder
COPY lab_sync.py .
COPY test_lab_sync.py .

# 4. Install pytest inside the container so it can run the tests
RUN pip install pytest

# 5. Tell the container what command to run by default when it boots up
CMD ["pytest", "test_lab_sync.py", "-v"]
