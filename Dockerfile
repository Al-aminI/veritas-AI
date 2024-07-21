# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /

ENV SECRET_KEY=myscrete
ENV DATABASE_URL=mydburl

# Install system dependencies for psycopg2
RUN apt-get update && \
    apt-get install -y libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Copy the requirements.txt file into the container at /app
COPY requirements.txt /

# Install any needed packages specified in requirements.txt
RUN pip install psycopg2-binary
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

EXPOSE 5000
# Start your application
CMD ["python", "app.py", "run"]
# ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
