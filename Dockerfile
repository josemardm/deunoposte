# Base Image
FROM python:3.12-slim

# Work directory
WORKDIR /app

# Copy requirements and install dependencies

COPY requirements.txt requirements.txt
# RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


# Copy other project files
COPY . .

# Expose a port to Containers 
EXPOSE 5000

# Command to run on server
CMD ["python", "app.py"]
