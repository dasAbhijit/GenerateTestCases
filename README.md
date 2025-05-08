# Test Case Generator

This project is designed to generate structured test cases in CSV format based on engineering and business requirements. It emphasizes clear instructions, prioritization, and traceability while addressing edge cases, error handling, and performance considerations.

The generated test suite is not exhaustive and needs human review.

## Project Structure

1. `main.py` - Entry point for the application 
2. `output/` - Directory for generated test case CSV files 
3. `prompt.py` - Contains the logic and templates for test case generation 
4. `requirements.txt` - Python dependencies 
5. `resources/` - Contains example and target requirement files 
6. `utils.py` - Utility functions 
7. `variables.py` - Configuration file for paths, constants, and default values used across the project

## Setup

1. **Clone the Repository**
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```
    
2. **Install Dependencies**
    Ensure you have Python 3.12 or higher installed. Install the required dependencies using pip:
    ```sh
    pip install -r requirements.txt
    ```

3. **Prepare Resources**

     Place your Business Requirement Document (BRD) and Engineering Requirement Document (ERD) files in the `resources/` directory.

     Ensure the filenames match the expected format (e.g., `brd-dashboard.md`, `erd-dashboard.md`).

4. **Add API KEY***

     Run the command on terminal - 
     Google Gemini : `export GOOGLE_API_KEY="<your_api_key>"`

## Usage

1. Run the Application: <br>
     Execute the `main.py` script to generate test cases:
     ```sh
     python main.py
     ```

2. Generated Output: <br>
     - The generated test cases will be saved as CSV files in the `output/` directory.
     - The filenames will include timestamps for easy identification (e.g., `generated-test-cases_YYYY-MM-DD_HH-MM-SS.csv`).
     
3. Modify Prompt or Variables: <br>
     - To customize the test case generation logic, edit the templates and logic in `prompt.py`.
     - Update constants, file paths, or default values in `variables.py` if needed.

## Key Features
- Functional Test Case Generation: Automatically generates test cases for each requirement.
- Prioritization: Supports High, Medium, and Low priority test cases.
- Edge Cases and Error Handling: Includes test cases for invalid inputs and unexpected scenarios.
- Security Considerations: Ensures security risks are addressed in the test cases.
- CSV Output: Outputs test cases in a structured CSV format for easy integration with test management tools.

## Example Files
- Example BRD: `resources/brd-dashboard.md`
- Example ERD: `resources/erd-dashboard.md`
- Example Test Cases: `output/tc-dashboard.csv`

## Customization
- Templates: Modify the test case structure or format in `prompt.py`.
- Variables: Update paths, constants, or default values in `variables.py`.

## Troubleshooting
- If the ERD file is missing, the script will log a message: "is not present".
- Ensure all required files are placed in the correct directories before running the script.

## Contributing
We encourage you to use this repository and share your feedback. If you encounter any issues or have suggestions for improvement, please submit them via the Issues tab. Pull requests are also welcome to enhance the project further.
