import prompt
import utils
import variables
from datetime import datetime

response=utils.invoke_llm(prompt=prompt.tc_prompt,business_requirement=variables.brd, erd=variables.erd, keyword_dictionary=variables.business_terms
                          , sample_brd=variables.example_brd, sample_test_cases=variables.example_tc, sample_erd=variables.example_erd
                          , test_case_format=variables.tc_format)
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_file = f'./output/generated-test-cases_{current_time}.csv'
utils.process_response_to_csv(response, output_file)