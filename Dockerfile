# Base Image
FROM python:3.12-slim
# Work directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install Flask
RUN pip install jsonify
RUN pip install requests
RUN pip install bs4

# Copy other project files
COPY . .

# Expose a port to Containers 
EXPOSE 8080

# Command to run on server
CMD ["python", "app.py"]
