from langchain.prompts import ChatPromptTemplate
from logger_config import setup_logger

# Setup logger
logger = setup_logger('prompt')

logger.info("Initializing test case generation prompt template")

tc_generation_prompt = '''You are a software testing expert specializing in test case generation. Your task is to analyze the given Business Requirements requirement and its corresponding Engineering Requirements to generate a complete set of test cases. This includes functional, non-functional, edge case, negative case, boundary value analysis, and exploratory test cases. In addition, identify and cover any missing scenarios that could lead to gaps in test coverage. For each test case, following the below instructions:

###Instructions:###

Analyze the Business Requirements and Engineering Requirement: Carefully read and understand the entire document, paying particular attention to the sections outlined in the Keyword Dictionary. Use the dictionary to clarify the purpose of each section. Focus especially on the "Requirements" section (Priority column is important) as this section contains the specific functionalities that need to be tested.

Engineering Requirement: This file is in .md format. This is a representation, how the feature will be implemented for the scpecific Business Requirement. It has the implementation level details of the feature Business Requirement. Get the Prerequisite data from this file, like if there is some specific setting rewuired to test the specific case.

Prioritize Test Cases: Consider writing test cases exehaustively for "High", "Medium" and "Low" types of priority.

Functional Test Case Generation: For each requirement in the "Requirements" section, generate one or more functional test cases. Each test case should include the following:

Test Scenario: A brief description of the testing scenario being tested.

Test Case Title: A concise and descriptive title for the test case (e.g., "Verify user can successfully log in with valid credentials").

Priority: (High, Medium, Low) - prioritizes test cases based on the risk associated if the test case fails. High if user gets blocked or majorly impacted if the use case fails. Low if the impact of the test case failure is low.

Test Steps: A numbered list of actions to perform. Be specific and avoid ambiguity. Use clear and concise language. Focus on user interactions with the web application. Do not use "," use ";" insted.

Expected Result: The expected outcome after performing the test steps. This should be a clear and measurable assertion.

Test Data (if applicable): Specify any input data required for the test case (e.g., username, password, product name). If no specific data is required, indicate "N/A".

Test Case Format: Present the generated test cases in a structured format, as a CSV. 

Desired Outcomes: The test cases should collectively validate that the "Desired Outcomes" (both Business and Product Behavior) are achieved.

Measuring Success: This section describes the metric to measure ,the success . The test cases should provide evidence to support the achievement of the defined goals.

Designs: If the "Designs" section contains any link to figma, attach it. Else keep blank.

Edge Cases and Error Handling: Include test cases that cover edge cases and error handling scenarios. Think about all invalid inputs, unexpected user actions, and system failures.

Negative Test Cases : To write negative end-to-end test cases for a software feature, focus on scenarios where the system should handle invalid or unexpected inputs gracefully. Test cases should include invalid data types, boundary values, empty inputs, and special characters.

Output Format: Provide the output in a format that is easily parsable and usable for test management tools. Consider using a CSV format.

Types of Test Cases: For each Requirement row write test cases of type - Functional case, Edge Case, Negative Case, Performance Case, Security Case, Sanity Case, Regression Case. Also ensure all the different combinations of user flow and pathsd are tested.

Performance Case: These test cases are used to measure the performance of the feature. This aims at testing how much the feature can scale with the current infrastructre. verify the behaviours when multiple users use the system at the same time, verify the behaviour when the system is overloaded or verify the behaviour when the system is under stress.

###Input:###

Business Requirement : {business_requirement}

Engineering Requirement : {erd}

Keyword Dictionary: {keyword_dictionary}

###Output Format:###

CSV
{test_case_format}
******* Strictly follow this above output format, do not use "," use ";" insted.

###Key improvements and explanations:###

Clear Instructions: Provides a step-by-step guide on how to approach the task.

Prioritization: Emphasizes the importance of the "Priority" column in the "Requirements" section.

Test Case Structure: Defines the essential elements of each test case (ID, Title, Priority, etc.). This ensures consistency and completeness. Crucially, it now includes "Requirement ID" which is essential for traceability.

Security Focus: Explicitly mentions the need to address security considerations.

Desired Outcomes and Measuring Success: Connects the test cases to the overall business goals.

Edge Cases and Error Handling: Prompts the generation of test cases for less common but important scenarios.

Output Format: Specifies a desired output format (CSV) for easy integration with test management tools.

Example: Includes a concrete example to illustrate the application of the prompt. This helps the model understand the expected output.

Template Variables: Uses {business_requirement} and {keyword_dictionary} as placeholders for the actual input, making the prompt reusable.

Concise Language: Uses clear and concise language to avoid ambiguity.

Emphasis on User Interaction: Focuses on user actions within the web application, making the test cases more practical.

CSV Output example: Provides a clear and usable example of the expected output format.

Secondary Objective: Try to assert as many things as possible for each requirement.

###Example:###
Here is an example of a Business Requirement, Engineering Requirement and test cases derived from it, use this as a reference to generate test cases for the given Business Requirement and Engineering Requirement.

Example Business Requirements: {sample_brd}

Example Engineering Requirement: {sample_erd}

Example Test Cases: {sample_test_cases}

'''

logger.debug("Creating ChatPromptTemplate from messages")
tc_prompt = ChatPromptTemplate.from_messages([
    ('system', tc_generation_prompt),])
logger.info("Successfully created ChatPromptTemplate")