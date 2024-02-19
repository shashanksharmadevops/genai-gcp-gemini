import logging, arrange_args
import vertexai
from vertexai.preview.generative_models import GenerativeModel, Part, HarmCategory, HarmBlockThreshold

def query_gemini_pro_vision(objArgs: arrange_args.arguments) -> str:
    logging.info("Running Query function: query_gemini_pro_vision_model")
    
    # Initialize Vertex AI
    vertexai.init(project=objArgs.project_id, location=objArgs.region)
    
    # Load the model
    multimodal_model = GenerativeModel("gemini-pro-vision")

    # Content generation config
    config = {"max_output_tokens": objArgs.max_output_tokens , "temperature": objArgs.temperature, "top_p": objArgs.top_p, "top_k": objArgs.top_k}

    # Responsible AI
    safety_config = {
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold(objArgs.hateSpeechThreshold), 
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold(objArgs.dangerousContentThreshold),
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold(objArgs.harasssmentThreshold),
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold(objArgs.sexuallyExplicitThreshold),
    }
    
    # Query the model
    logging.info("Query the model")
    response = multimodal_model.generate_content(
        [
            Part.from_uri(
                objArgs.image_url, mime_type="image/jpeg"
            ),
            objArgs.prompt_text,
        ],
        generation_config=config,
        safety_settings=safety_config,
    )
    
    logging.info(response)
    return response.text
