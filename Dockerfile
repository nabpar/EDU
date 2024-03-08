# FROM python:3.11.3

# COPY requirements.txt requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt



# # mount the applocation code to the image 

# COPY ./code /code
# WORKDIR /code

# EXPOSE 8000

# # runs the production server
  
# ENTRYPOINT ["python","EduAid/manage.py"]
# CMD ["runserver","127.0.0.1:8000"]



# specify a base image
FROM python:alpine
WORKDIR /usr/app

# install some dependencies

COPY ./ requirements.txt ./
RUN cat requirements.txt
RUN pip3 install -r requirements.txt  
copy ./ ./


#  default command 
CMD ["python", "EduAid/manage.py", "runserver", "127.0.0.1:8000"] 
# CMD ['runserver', '127.0.0.1:8000']
