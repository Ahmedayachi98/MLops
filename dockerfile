FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install required packages
RUN apt-get update && apt-get install -y python3-distutils
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Run the application
CMD ["python3", "app.py"]
