from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import pandas as pd

llm_model_identifier = "gemini-2.0-flash"
llm_temperature = 0.5

llm = ChatGoogleGenerativeAI(model=llm_model_identifier, temperature=llm_temperature)

def read_file(file_path):
  with open(file_path, 'r') as file:
    content = file.read()
  return content

def invoke_llm(prompt: ChatPromptTemplate, **kwargs)-> str:
  messages= prompt.format_messages(**kwargs)
  content = [{"role": m.type, "content": m.content} for m in messages]
  response = llm.invoke(
      input=content[0]['content']
  )
  return response.text()

def process_response_to_csv(response, output_file_path):
    try:
        # Remove the code block markers
        response = response.replace('```csv', '').replace('```', '')

        # Split the response into rows and then split each row into columns
        rows = [row.split(',') for row in response.split('\n') if row.strip()]  # Exclude empty rows

        # Convert the rows into a pandas DataFrame
        test_case = pd.DataFrame(rows[1:], columns=rows[0])  # Use the first row as column headers

        # Save the DataFrame to a CSV file
        test_case.to_csv(output_file_path, index=False)

        print(f"CSV file saved successfully at: {output_file_path}")
        print(f"{len(test_case)} test cases generated.")
        return output_file_path
    except Exception as e:
        print(f"An error occurred: {e}")
        return None