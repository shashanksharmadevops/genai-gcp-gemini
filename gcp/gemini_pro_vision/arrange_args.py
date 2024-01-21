# This module is to arrange the arguments passed through config file and command line
# Arguments through command line will take precedence
#

import yaml,logging

class arguments:
    None

objArgs = arguments()

def arrange_args(args):
    logging.info("Arranging Arguments")

    # Reading args from config.yaml
    if args.file:
        logging.info("Config file is provided. Reading it now.")
        data = yaml.safe_load(args.file)
        objArgs.project_id  = data["projectId"]
        objArgs.region      = data["region"]
        objArgs.prompt_text = data["promptText"]
        objArgs.image_url   = data["imageUrl"]

    # Overriding config properties wtih command line properties
    if args.project_id:
        objArgs.project_id  = args.project_id
    if args.prompt_text:
        objArgs.prompt_text = args.prompt_text
    if args.image_url:
        objArgs.image_url   = args.image_url
    if args.region:
        objArgs.region      = args.region
    elif objArgs.region:
        #do nothing
        logging.info("Default to us-central1")
    else:    
        # Default set to us-central1
        logging.warn("Region setting to default us-central1")
        objArgs.region      = "us-central1"

    logging.info(
                    "\n-------------------------" +
                    "\n GCP PROJECT ID: "       + objArgs.project_id + 
                    "\n GCP REGION: "           + objArgs.region + 
                    "\n PROMPT TEXT: "          + objArgs.prompt_text +
                    "\n GCP BUCKET IMAGE URL: " + objArgs.image_url +
                    "\n-------------------------"
                )

    return objArgs

