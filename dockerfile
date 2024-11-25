FROM python:3.10.12-slim


# Allow statements and log messages to immediately appear in the logs
ENV PYTHONUNBUFFERED True

ENV APP_HOME /app

# Set the working directory
WORKDIR /app
WORKDIR $APP_HOME
COPY . ./
# Copy the current directory contents into the container at /app

# Install required packages
RUN apt-get update && apt-get install -y python3-distutils
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Run the application
CMD ["python3", "app.py"]
