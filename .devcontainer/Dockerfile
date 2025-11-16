# Use the official Python image
FROM python:3.11-slim-buster

# # Set the working directory
# WORKDIR /workspace

# # Copy requirements file
# COPY requirements.txt .

# # Install dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# RUN apt-get update && apt-get install -q -y \
#     git

# Copy the application files
# COPY app/ ./app

# Copy entrypoint script (if needed)
COPY entrypoint.sh /entrypoint.d/entrypoint.sh

# Ensure entrypoint.sh is executable
RUN chmod +x /entrypoint.d/entrypoint.sh

# Set the entrypoint (if applicable)
# CMD ["/bin/bash", "/"] 
# # Set the entrypoint (if applicable)
ENTRYPOINT ["/bin/bash", "/entrypoint.d/entrypoint.sh  "]
# Adjust as needed
