FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


WORKDIR /taskapi


COPY requirements.txt /taskapi/


RUN pip install --no-cache-dir -r requirements.txt


COPY . /taskapi/


EXPOSE 8000

# Command to run the application using Uvicorn
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
