# Use an official Python runtime as a parent image
FROM python:3.12

# Set environment variables
ENV PYTHONBUFFERED=1

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file into the container
COPY requirements.txt /code/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . /code

# Set the Django settings module environment variable
ENV DJANGO_SETTINGS_MODULE=twitterbackend.settings

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
