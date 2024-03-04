# Use the official Python base image
FROM python:3.12-alpine3.19

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Run the index.py file
CMD ["python", "index.py"]
