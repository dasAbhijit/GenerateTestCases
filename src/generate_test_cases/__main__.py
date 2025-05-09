from datetime import datetime
from pathlib import Path

from .config.logging import setup_logging, get_logger
from .config.settings import OUTPUT_DIR, TARGET_PATHS, EXAMPLE_PATHS
from .core.llm_service import LLMService
from .core.prompt_service import PromptService
from .utils.file_service import FileService

def main() -> None:
    """Main entry point for the application."""
    # Setup logging
    setup_logging()
    logger = get_logger(__name__)
    
    logger.info("Starting test case generation process")
    try:
        # Initialize services
        file_service = FileService()
        llm_service = LLMService()
        prompt_service = PromptService()
        
        # Load input files
        logger.debug("Loading input files")
        brd = file_service.read_file(TARGET_PATHS["brd"])
        erd = file_service.read_file(TARGET_PATHS["erd"])
        example_brd = file_service.read_file(EXAMPLE_PATHS["brd"])
        example_erd = file_service.read_file(EXAMPLE_PATHS["erd"])
        example_tc = file_service.read_file(EXAMPLE_PATHS["tc"])
        
        # Define business terms
        business_terms = {
            'Author': 'Name of the Author who designed the Requirements',
            'Problem Statement': 'Here the author describes the problem statement which needs the feature with description',
            'Desired Outcomes': 'Here the author describes the Outcome i.e. Expected Business and Product Behaviour',
            'Measuring Success': 'Here the author mertions the parameter on which the feature would be mesaured for success',
            'Designs': 'Include descriptions or links to team designs.',
            'Security Considerations': 'In this section, summarize the security risk assessment and review takeaways.',
            'Requirements': 'This section has to be read and undestood with importance. This section talks about the granular level business requirements, which is getting implemented. Each of these statements has to be tested with outmost importance'
        }
        
        # Define test case format
        tc_format = '''Test Scenario,Test Cases Title,Pre-requisites,Test Steps,Expected Behaviour,Design Link (figma),Priority,Component,Suite Annotation
Login Success,verify the login success with Google OAuth,1. a google account must be present,"1. Go to login page 2. Enter Google Account ID/Pass 3. Submit the page","1. user should be logged in 2. by default redirect to dashboard", -- link to figma --,High,Account,Sanity
Login Failure,verify the login fails with invalid OAuth,,"1. Go to login page 2. Enter invalid Google Account ID/Pass 3. Submit the page","1. user should be shown the auth failure message 2. user should be kept logged out 3. user should be let to retry with valid details", -- link to figma --,High,Account,Sanity'''
        
        # Generate test cases
        logger.debug("Invoking LLM with prompt and variables")
        response = llm_service.invoke(
            prompt=prompt_service.tc_prompt,
            business_requirement=brd,
            erd=erd,
            keyword_dictionary=business_terms,
            sample_brd=example_brd,
            sample_test_cases=example_tc,
            sample_erd=example_erd,
            test_case_format=tc_format
        )
        
        # Save output
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_file = OUTPUT_DIR / f'generated-test-cases_{current_time}.csv'
        logger.info(f"Processing response and saving to {output_file}")
        file_service.save_to_csv(response, output_file)
        logger.info("Test case generation completed successfully")
        
    except Exception as e:
        logger.error(f"An error occurred during test case generation: {str(e)}", exc_info=True)
        raise

if __name__ == "__main__":
    main() 