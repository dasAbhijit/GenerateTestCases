from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import pandas as pd
from logger_config import setup_logger

# Setup logger
logger = setup_logger('utils')

llm_model_identifier = "gemini-2.0-flash"
llm_temperature = 0.5

logger.info(f"Initializing LLM with model: {llm_model_identifier}, temperature: {llm_temperature}")
llm = ChatGoogleGenerativeAI(model=llm_model_identifier, temperature=llm_temperature)

def read_file(file_path):
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
    logger.debug("Preparing to invoke LLM")
    try:
        messages = prompt.format_messages(**kwargs)
        content = [{"role": m.type, "content": m.content} for m in messages]
        logger.debug("Sending request to LLM")
        response = llm.invoke(
            input=content[0]['content']
        )
        logger.info("Successfully received response from LLM")
        return response.text()
    except Exception as e:
        logger.error(f"Error invoking LLM: {str(e)}", exc_info=True)
        raise

def process_response_to_csv(response, output_file_path):
    logger.info(f"Processing LLM response and saving to CSV: {output_file_path}")
    try:
        # Remove the code block markers
        response = response.replace('```csv', '').replace('```', '')
        logger.debug("Removed code block markers from response")

        # Split the response into rows and then split each row into columns
        rows = [row.split(',') for row in response.split('\n') if row.strip()]  # Exclude empty rows
        logger.debug(f"Split response into {len(rows)} rows")

        # Convert the rows into a pandas DataFrame
        test_case = pd.DataFrame(rows[1:], columns=rows[0])  # Use the first row as column headers
        logger.debug(f"Created DataFrame with {len(test_case)} rows and {len(test_case.columns)} columns")

        # Save the DataFrame to a CSV file
        test_case.to_csv(output_file_path, index=False)
        logger.info(f"Successfully saved {len(test_case)} test cases to {output_file_path}")
        return output_file_path
    except Exception as e:
        logger.error(f"Error processing response to CSV: {str(e)}", exc_info=True)
        return None