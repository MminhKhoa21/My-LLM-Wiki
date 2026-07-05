FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install git since some dashboard features might use it (optional but recommended)
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container
COPY . /app

# Create a non-root user and change ownership
RUN useradd -m myuser && chown -R myuser:myuser /app
USER myuser

# Expose the default port (Render/Railway will override via PORT env)
EXPOSE 8080

# Run the server script
CMD ["python", "scripts/server.py"]
