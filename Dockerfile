# Use official Python
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose port 8080 (Fly.io expects this)
ENV PORT=8080

# Command to run your app
CMD ["python", "app.py"]
