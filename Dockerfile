FROM mcr.microsoft.com/azure-functions/python:3.0-python3.7-slim
RUN pip3 install -Iv azure-identity==1.4.0 && pip3 install -Iv azure-keyvault-secrets==4.2.0
COPY main.py .
ENTRYPOINT [ "/usr/local/bin/python3", "-u", "main.py" ] 
#CMD [ "sleep", "999999" ] 
