# genai-gcp-gemini
Python module to interact with GCP GenAI gemini model to inspect images

## Get Started

### Pre-requisites:
1. [Google Cloud Platform Account](https://cloud.google.com/free?utm_source=google&utm_medium=cpc&utm_campaign=na-none-all-en-dr-sitelink-all-all-trial-e-gcp-1707554&utm_content=text-ad-none-any-DEV_c-CRE_665735485400-ADGP_Hybrid+%7C+BKWS+-+MIX+%7C+Txt_General+GCP-KWID_43700078963885939-kwd-527294293847-userloc_1002287&utm_term=KW_gcp%20account-ST_gcp+account-NET_g-&gad_source=1&gclid=Cj0KCQiAnrOtBhDIARIsAFsSe53c4p6LFWyfeUGJw5vbcN2WnMzu2NQ42saXL03trw_X3RoSuLQDT-AaAqitEALw_wcB&gclsrc=aw.ds)
2. [Create GCP project](https://developers.google.com/workspace/guides/create-project)
3. [Enable required GCP APIs](https://cloud.google.com/vertex-ai/docs/featurestore/setup#:~:text=In%20the%20Google%20Cloud%20console,create%20a%20Google%20Cloud%20project.&text=Make%20sure%20that%20billing%20is,Enable%20the%20Vertex%20AI%20API.)
4. [Create a GCP Bucket](https://cloud.google.com/storage/docs/creating-buckets)
5. [Upload image file(s) into bucket](https://cloud.google.com/storage/docs/uploading-objects)
6. [Setup auth](https://cloud.google.com/docs/authentication/provide-credentials-adc#local-dev)

Clone the respository and cd
```
git clone https://github.com/shashanksharmadevops/genai-gcp-gemini.git
```
```
cd gcp/gemini_pro_vision/
```

### Arguments:

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

### There are two ways this application can be executed
1. Execution in local/VM i.e NO container
2. Execution in container

## Execution in local/VM i.e NO container

Help:
```
python3 main.py --help
```

Run:
```
python3 main.py --file ./config.yaml
```
## Execution in container

Change directory:
```
cd gcp/gemini_pro_vision/
```
Docker build:
```
docker build . -t gcp-gemini-pro-vision
```

Run the container: Below command has two volumes mapped for app config file and GCP auth. 
Setup google auth using https://cloud.google.com/docs/authentication/provide-credentials-adc#wlif-key
This is only to run locally or on-prem. Not a recommended method because user have to maintain security of key. 
Follow the document(link) above for workload identity and other methods.
```
docker run --rm -v <path-to-config.yaml>:/app/config.yaml -v <path-to-gcp-auth.json>:/config/gcp-auth.json gcp-gemini-pro-vision -f config.yaml
```