# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Install system dependencies for SQL Server (Azure)
RUN apt-get update && apt-get install -y \
    curl apt-transport-https gnupg2 unixodbc-dev g++ \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql17

# Set the working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your code
COPY . .

# Start the application (Replace 'myproject' with your folder name containing wsgi.py)
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"] 