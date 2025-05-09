"""Utility functions for test case generation."""
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import pandas as pd
import os
from logger_config import setup_logger

# Setup logger
logger = setup_logger('utils')

# LLM Configuration
LLM_MODEL = "gemini-2.0-flash"
LLM_TEMPERATURE = 0.5

# Get API key from environment variable
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY environment variable is not set")

logger.info(f"Initializing LLM with model: {LLM_MODEL}, temperature: {LLM_TEMPERATURE}")
llm = ChatGoogleGenerativeAI(
    model=LLM_MODEL,
    temperature=LLM_TEMPERATURE,
    google_api_key=GOOGLE_API_KEY
)

def read_file(file_path: str) -> str:
    """
    Read content from a file.
    
    Args:
        file_path (str): Path to the file to read
        
    Returns:
        str: Content of the file
        
    Raises:
        Exception: If file cannot be read
    """
    logger.debug(f"Reading file: {file_path}")
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        logger.debug(f"Successfully read file: {file_path}")
        return content
    except Exception as e:
        logger.error(f"Error reading file {file_path}: {str(e)}", exc_info=True)
        raise

def invoke_llm(prompt: ChatPromptTemplate, **kwargs) -> str:
    """
    Invoke the LLM with the given prompt and parameters.
    
    Args:
        prompt (ChatPromptTemplate): The prompt template to use
        **kwargs: Additional parameters for the prompt
        
    Returns:
        str: LLM response text
        
    Raises:
        Exception: If LLM invocation fails
    """
    logger.debug("Preparing to invoke LLM")
    try:
        messages = prompt.format_messages(**kwargs)
        content = [{"role": m.type, "content": m.content} for m in messages]
        logger.debug("Sending request to LLM")
        response = llm.invoke(input=content[0]['content'])
        logger.info("Successfully received response from LLM")
        return response.text()
    except Exception as e:
        logger.error(f"Error invoking LLM: {str(e)}", exc_info=True)
        raise

def process_response_to_csv(response: str, output_file_path: str) -> str:
    """
    Process LLM response and save to CSV file.
    
    Args:
        response (str): Raw response from LLM
        output_file_path (str): Path to save the CSV file
        
    Returns:
        str: Path to the saved CSV file
        
    Raises:
        Exception: If processing fails
    """
    logger.info(f"Processing LLM response and saving to CSV: {output_file_path}")
    try:
        # Remove the code block markers
        response = response.replace('```csv', '').replace('```', '')
        logger.debug("Removed code block markers from response")

        # Split the response into rows and then split each row into columns
        rows = [row.split(',') for row in response.split('\n') if row.strip()]
        logger.debug(f"Split response into {len(rows)} rows")

        # Convert the rows into a pandas DataFrame
        test_case = pd.DataFrame(rows[1:], columns=rows[0])
        logger.debug(f"Created DataFrame with {len(test_case)} rows and {len(test_case.columns)} columns")

        # Save the DataFrame to a CSV file
        test_case.to_csv(output_file_path, index=False)
        logger.info(f"Successfully saved {len(test_case)} test cases to {output_file_path}")
        return output_file_path
    except Exception as e:
        logger.error(f"Error processing response to CSV: {str(e)}", exc_info=True)
        return None