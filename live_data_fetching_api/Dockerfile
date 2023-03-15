FROM python:3.8-slim-buster

# Install supervisord
RUN apt-get update && apt-get install -y supervisor

# Copy the API scripts into the container
COPY bengaluru_live_api.py /app/
COPY delhi_live_api.py /app/

# Install any necessary Python dependencies for the APIs
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

# Configure supervisord
COPY supervisord.conf /etc/supervisor/conf.d/

# Start supervisord to manage the APIs
CMD ["/usr/bin/supervisord"]


