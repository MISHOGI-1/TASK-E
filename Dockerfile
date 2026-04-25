FROM python:3.11-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY init_db.py schema.sql readme.txt ./

# Initialize database on startup
RUN python init_db.py

# Expose port (adjust as needed for your Flask app)
EXPOSE 5000

# Run Flask application (adjust entry point as needed)
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]