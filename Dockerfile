FROM python:3.10.7-alpine3.16
ADD script.py .
RUN pip install telethon==1.25.2 pysocks
CMD ["python", "./script.py"] 
