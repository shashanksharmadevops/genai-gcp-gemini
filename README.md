# genai-gcp-gemini
Python module to interact with GCP GenAI gemini model to inspect images

### Application Arguments:

Required Args:
1. --project_id  : GCP project id
2. --region      : GCP region if not provided defaults to us-central1
3. --image_url   : GCP bucket url to image you like to process. e.g: gs://bucket-name-and-image-path/image.jpg
4. --prompt_text : A query you have related to the image. e.g: What is this image about?

Optional Args:
1. --log  : Logs verbosity defaults to INFO. Valid values: INFO, DEBUG, WARNING, ERROR, CRITICAL"
2. --file : To pass arguments through config file. *If used in conjunction with command line args; cmd args will take precedence*
   ```
   projectId: my-gcp-project-id
   region: us-central1
   imageUrl: gs://bucket-name-abc/testname.jpeg
   promptText: "describe the picture?"
   ```

## Get Started

### Pre-requisites:
1. [Google Cloud Platform Account](https://cloud.google.com/free?utm_source=google&utm_medium=cpc&utm_campaign=na-none-all-en-dr-sitelink-all-all-trial-e-gcp-1707554&utm_content=text-ad-none-any-DEV_c-CRE_665735485400-ADGP_Hybrid+%7C+BKWS+-+MIX+%7C+Txt_General+GCP-KWID_43700078963885939-kwd-527294293847-userloc_1002287&utm_term=KW_gcp%20account-ST_gcp+account-NET_g-&gad_source=1&gclid=Cj0KCQiAnrOtBhDIARIsAFsSe53c4p6LFWyfeUGJw5vbcN2WnMzu2NQ42saXL03trw_X3RoSuLQDT-AaAqitEALw_wcB&gclsrc=aw.ds)
2. [Create GCP project](https://developers.google.com/workspace/guides/create-project)
3. [Setup GCP auth](https://cloud.google.com/docs/authentication/provide-credentials-adc#local-dev)

Clone the respository and cd
```
git clone https://github.com/shashanksharmadevops/genai-gcp-gemini.git \
cd genai-gcp-gemini/
```
### This app has 2 modules
1. Terraform - To build GCP resources and enable GCP APIs
2. Python App - To interact with GCP gemini-pro-vision model

## Run Terraform
   1. ```
      cd gcp/terraform/
      ```
   2. Update variables.tf

   3. ```
      terraform init
      ```
      ```
      terraform plan -out tf.plan
      ```
      ```
      terraform apply tf.plan
      ```
   4. [Upload image file(s) into GCP bucket](https://cloud.google.com/storage/docs/uploading-objects)

## Run Application
   
   ### There are two ways this application can be executed
   1. Execution in local/VM i.e NO container
   2. Execution in container

   Change directory:

   ```
   cd ../gemini_pro_vision/
   ```

   ### Execution in local/VM i.e NO container

   1. Explore Help: 
      ```
      python3 main.py --help
      ```

   2. Update config.yaml

   3. Run:
      ```
      python3 main.py --file ./config.yaml
      ```
      
   ### Execution in container

   1. Docker build:
      ```
      docker build . -t gcp-gemini-pro-vision
      ```

   2. Run the container: Below command has two volumes mapped for app config file and GCP auth. 
      Setup google auth using https://cloud.google.com/docs/authentication/provide-credentials-adc#wlif-key
      This is only to run locally or on-prem. Not a recommended method because user have to maintain security of key. 
      Follow the document(link) above for workload identity and other methods.
      ```
      docker run --rm -v <path-to-config.yaml>:/app/config.yaml -v <path-to-gcp-auth.json>:/config/gcp-auth.json gcp-gemini-pro-vision -f config.yaml
      ```

## Cleanup/Destroy demo environment
   1. Change Directory:
      ```
      cd ../terraform
      ```
   2. Build and apply Terraform destroy plan:
      ```
      terraform plan --destroy -out tf.plan
      ```
      ```
      terraform apply tf.plan
      ```

   3. Revoke gcloud access:
      ```
      gcloud auth revoke
      ```