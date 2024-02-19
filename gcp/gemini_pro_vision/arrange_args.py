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
        objArgs.project_id                = data["projectId"]
        objArgs.region                    = data["region"]
        objArgs.prompt_text               = data["promptText"]
        objArgs.image_url                 = data["imageUrl"]
        objArgs.max_output_tokens         = data["contentGenerationConfig"]["max_output_tokens"]
        objArgs.temperature               = data["contentGenerationConfig"]["temperature"]
        objArgs.top_p                     = data["contentGenerationConfig"]["top_p"]
        objArgs.top_k                     = data["contentGenerationConfig"]["top_k"]
        objArgs.hateSpeechThreshold       = data["contentSafetyConfig"]["hateSpeechThreshold"]
        objArgs.dangerousContentThreshold = data["contentSafetyConfig"]["dangerousContentThreshold"]
        objArgs.harasssmentThreshold      = data["contentSafetyConfig"]["harasssmentThreshold"]
        objArgs.sexuallyExplicitThreshold = data["contentSafetyConfig"]["sexuallyExplicitThreshold"]

    # Overriding config properties with command line properties
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

