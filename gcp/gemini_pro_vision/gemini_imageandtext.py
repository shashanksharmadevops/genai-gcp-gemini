import logging, arrange_args
import vertexai
from vertexai.preview.generative_models import GenerativeModel, Part

def query_gemini_pro_vision_model(project_id: str, location: str, prompt_text: str, image_url: str) -> str:
    logging.info("Running Query function: query_gemini_pro_vision_model")
    
    # Initialize Vertex AI
    vertexai.init(project=project_id, location=location)
    
    # Load the model
    multimodal_model = GenerativeModel("gemini-pro-vision")
    
    # Query the model
    logging.info("Query the model")
    response = multimodal_model.generate_content(
        [
            Part.from_uri(
                image_url, mime_type="image/jpeg"
            ),
            prompt_text,
        ]
    )
    
    logging.info(response)
    return response.text

def query_gemini_pro_vision(objArgs: arrange_args.arguments) -> str:
    logging.info("Running Query function: query_gemini_pro_vision_model")
    
    # Initialize Vertex AI
    vertexai.init(project=objArgs.project_id, location=objArgs.region)
    
    # Load the model
    multimodal_model = GenerativeModel("gemini-pro-vision")
    
    # Query the model
    logging.info("Query the model")
    response = multimodal_model.generate_content(
        [
            Part.from_uri(
                objArgs.image_url, mime_type="image/jpeg"
            ),
            objArgs.prompt_text,
        ]
    )
    
    logging.info(response)
    return response.text
