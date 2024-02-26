FROM python:latest
WORKDIR /app

# Copy the app dir
COPY . .

# Install pip packages
RUN pip install -r requirements.txt

# Setup google auth using https://cloud.google.com/docs/authentication/provide-credentials-adc#wlif-key
# This is only to run locally or on-prem. 
# Not a recommended way because user have to maintain security of key. 
# Follow the document(link) above for workload identity and other methods.
# Map the volume to /config/gcp-auth.json 
ENV GOOGLE_APPLICATION_CREDENTIALS='/config/gcp-auth.json'

# Set up the entry point
ENTRYPOINT ["python3", "main.py"]
CMD [ "-h" ]