# Base Image
FROM python:3.9-slim
RUN pip install --upgrade pip
ENV PIP_ROOT_USER_ACTION=ignore


# Work directory
WORKDIR /

# Copy requirements and install dependencies

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt


# Copy other project files
COPY . .

# Expose a port to Containers 
EXPOSE 8080

# Command to run on server
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app.py"]
