FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /api

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the application port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
