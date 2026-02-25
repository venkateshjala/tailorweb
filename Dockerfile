# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Install system dependencies for SQL Server (Azure)
RUN apt-get update && apt-get install -y \
    curl apt-transport-https gnupg2 unixodbc-dev g++ \
    && mkdir -p /etc/apt/keyrings \
    && curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor -o /etc/apt/keyrings/microsoft.gpg \
    && echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/microsoft.gpg] https://packages.microsoft.com/debian/11/prod bullseye main" > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql17

# Set the working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your code
COPY . .

# Start the application 
# IMPORTANT: Change 'auth_Project' to the folder name that contains your wsgi.py
CMD ["gunicorn", "auth_project.wsgi:application", "--bind", "0.0.0.0:8000"]
