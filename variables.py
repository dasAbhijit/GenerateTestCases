"""Configuration variables and constants for test case generation."""
from utils import read_file
import os
from logger_config import setup_logger

# Setup logger
logger = setup_logger('variables')

logger.info("Initializing variables module")

# Template formats
BRD_FORMAT = '''# **Product Requirements: <Requirement Title>**

Author: <name>

## **Problem**

<Problem Statement with description>

## **Desired Outcomes**

<Expected Business Behaviour>
<Expected Product Behaviour>

## **Measuring Success**

<Describe how we measure success of the proposed feature.>

| **Goal** | **Metric** |
| --- | --- |

# **Designs**

<Include descriptions or links to team designs.>

## **Requirements**

<This is a table with 2 columns first one defines the priority of the requirement and second defines the rewuirement.>

| **Priority** | **Requirements** |
| --- | --- |

### ** Extra added info **
'''

TC_FORMAT = '''Test Scenario,Test Cases Title,Pre-requisites,Test Steps,Expected Behaviour,Design Link (figma),Priority,Component,Suite Annotation
Login Success,verify the login success with Google OAuth,1. a google account must be present,"1. Go to login page 2. Enter Google Account ID/Pass 3. Submit the page","1. user should be logged in 2. by default redirect to dashboard", -- link to figma --,High,Account,Sanity
Login Failure,verify the login fails with invalid OAuth,,"1. Go to login page 2. Enter invalid Google Account ID/Pass 3. Submit the page","1. user should be shown the auth failure message 2. user should be kept logged out 3. user should be let to retry with valid details", -- link to figma --,High,Account,Sanity'''

# Business terms dictionary
BUSINESS_TERMS = {
    'Author': 'Name of the Author who designed the Requirements',
    'Problem Statement': 'Here the author describes the problem statement which needs the feature with description',
    'Desired Outcomes': 'Here the author describes the Outcome i.e. Expected Business and Product Behaviour',
    'Measuring Success': 'Here the author mertions the parameter on which the feature would be mesaured for success',
    'Designs': 'Include descriptions or links to team designs.',
    'Security Considerations': 'In this section, summarize the security risk assessment and review takeaways.',
    'Requirements': 'This section has to be read and undestood with importance. This section talks about the granular level business requirements, which is getting implemented. Each of these statements has to be tested with outmost importance'
}

def load_example_files():
    """Load example files for reference."""
    logger.info("Loading example files")
    try:
        example_brd = read_file('./resources/example/brd-ordertracking.md')
        logger.debug("Successfully loaded example BRD")
    except Exception as e:
        logger.error(f"Error loading example BRD: {str(e)}", exc_info=True)
        raise

    try:
        example_erd = read_file('./resources/example/erd-ordertracking.md')
        logger.debug("Successfully loaded example ERD")
    except Exception as e:
        logger.error(f"Error loading example ERD: {str(e)}", exc_info=True)
        raise

    try:
        example_tc = read_file('./resources/example/tc-ordertracking.csv')
        logger.debug("Successfully loaded example test cases")
    except Exception as e:
        logger.error(f"Error loading example test cases: {str(e)}", exc_info=True)
        raise

    return example_brd, example_erd, example_tc

def load_target_files():
    """Load target files for processing."""
    logger.info("Loading target files")
    brd_path = './resources/target/brd-ordercreation.md'
    erd_path = './resources/target/erd-ordercreation.md'

    try:
        brd = read_file(brd_path) if os.path.exists(brd_path) else "Info: BRD is not present, its mandatory. Please add it as - ./resources/target/brd-<resource-name>"
        logger.debug(f"BRD status: {'Loaded successfully' if os.path.exists(brd_path) else 'Not found'}")
    except Exception as e:
        logger.error(f"Error loading BRD: {str(e)}", exc_info=True)
        raise

    try:
        erd = read_file(erd_path) if os.path.exists(erd_path) else "Info: ERD is not present, its optional. Please add it as - ./resources/target/brd-<resource-name>"
        logger.debug(f"ERD status: {'Loaded successfully' if os.path.exists(erd_path) else 'Not found'}")
    except Exception as e:
        logger.error(f"Error loading ERD: {str(e)}", exc_info=True)
        raise

    return brd, erd

# Load all required files
example_brd, example_erd, example_tc = load_example_files()
brd, erd = load_target_files()