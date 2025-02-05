# Use official Python image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy the dependencies file
COPY requirements.txt .

COPY ./app /app
COPY start.sh /start.sh
RUN chmod +x /start.sh

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the application port
EXPOSE 8000

# Run the FastAPI app
CMD ["/start.sh"]
