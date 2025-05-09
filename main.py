"""Main entry point for test case generation."""
import prompt
import utils
import variables
from datetime import datetime
from logger_config import setup_logger

# Setup logger
logger = setup_logger('main')

def main():
    """Main function to generate test cases."""
    logger.info("Starting test case generation process")
    try:
        logger.debug("Invoking LLM with prompt and variables")
        response = utils.invoke_llm(
            prompt=prompt.tc_prompt,
            business_requirement=variables.brd,
            erd=variables.erd,
            keyword_dictionary=variables.BUSINESS_TERMS,
            sample_brd=variables.example_brd,
            sample_test_cases=variables.example_tc,
            sample_erd=variables.example_erd,
            test_case_format=variables.TC_FORMAT
        )
        
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_file = f'./output/generated-test-cases_{current_time}.csv'
        logger.info(f"Processing response and saving to {output_file}")
        utils.process_response_to_csv(response, output_file)
        logger.info("Test case generation completed successfully")
    except Exception as e:
        logger.error(f"An error occurred during test case generation: {str(e)}", exc_info=True)
        raise

if __name__ == "__main__":
    main()