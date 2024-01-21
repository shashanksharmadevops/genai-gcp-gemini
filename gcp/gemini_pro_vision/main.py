import argparse, logging
import gemini_imageandtext
import arrange_args

parser = argparse.ArgumentParser(description='This project connects you with GCP GenAI gemini-pro-vision Engine')

# GCP project id
parser.add_argument(
                    '--project_id',  
                    '-p',                        
                    help = "GCP project id"
                    )
# GCP region
parser.add_argument(
                    '--region',      
                    '-r',  
                    help = "GCP region defaults to us-central1. e.g: us-central1"
                    )
# Prompt text for the AI model
parser.add_argument(
                    '--prompt_text', 
                    '-t',                          
                    help = "Prompt text"
                    )
# URL for the GCP bucket containing image
parser.add_argument(
                    '--image_url',   
                    '-i', 
                    help = "Path to image file in GCP bucket"
                    )
# Log verbosity: INFO, DEBUG, WARNING, ERROR, CRITICAL
parser.add_argument(
                    '--log',         
                    '-l', 
                    default = 'INFO',        
                    help = "Logs verbosity defaults to INFO. Valid values: INFO, DEBUG, WARNING, ERROR, CRITICAL"
                    )
# Pass the config.yaml file. 
# If used along with command line arguments; the arguments with take precedence
parser.add_argument(
                    '--file',        
                    '-f', 
                    type = argparse.FileType("r"), 
                    help = "Path to config file(config.yaml)")

args = parser.parse_args()

# Main function
def main():

    # Logging Config
    numeric_level = getattr(logging, args.log.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s Valid values: INFO, DEBUG, WARNING, ERROR, CRITICAL' % args.log)
    logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=numeric_level)

    logging.info('Logging Started')
    logging.info("Running main function")

    # Arrange arguments
    objArgs = arrange_args.arrange_args(args)

    # Invoke gemini_pro_vision model
    response = gemini_imageandtext.query_gemini_pro_vision(objArgs)

    logging.info(response)
    logging.info('Logging Stopped')

if __name__ == '__main__':
    main()
