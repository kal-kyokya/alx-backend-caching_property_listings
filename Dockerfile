# Use an official Python runtime as a parent image
FROM python:3.10-alpine

# Set the working directory in the container
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apk add --no-cache postgresql gcc python3-dev musl-dev

# Copy requirements file and install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . /app

# Expose port 8000
EXPOSE 8000

# Command to run the application (overridden by docker-compose)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
