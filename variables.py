from utils import read_file
import os

brd_format='''# **Product Requirements: <Requirement Title>**

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

tc_format='''Test Scenario,Test Cases Title,Pre-requisites,Test Steps,Expected Behaviour,Design Link (figma),Priority,Component,Suite Annotation
Login Success,verify the login success with Google OAuth,1. a google account must be present,"1. Go to login page 2. Enter Google Account ID/Pass 3. Submit the page","1. user should be logged in 2. by default redirect to dashboard", -- link to figma --,High,Account,Sanity
Login Failure,verify the login fails with invalid OAuth,,"1. Go to login page 2. Enter invalid Google Account ID/Pass 3. Submit the page","1. user should be shown the auth failure message 2. user should be kept logged out 3. user should be let to retry with valid details", -- link to figma --,High,Account,Sanity'''


business_terms = {'Author':'Name of the Author who designed the Requirements',
                  'Problem Statement':'Here the author describes the problem statement which needs the feature with description',
                  'Desired Outcomes' : 'Here the author describes the Outcome i.e. Expected Business and Product Behaviour',
                  'Measuring Success' : 'Here the author mertions the parameter on which the feature would be mesaured for success',
                  'Designs': 'Include descriptions or links to team designs.',
                  'Security Considerations': 'In this section, summarize the security risk assessment and review takeaways.',
                  'Requirements': 'This section has to be read and undestood with importance. This section talks about the granular level business requirements, which is getting implemented. Each of these statements has to be tested with outmost importance'
                  }


example_brd=read_file('./resources/example/<resource-name>')

example_erd=read_file('./resources/example/<resource-name>')

example_tc=read_file('./resources/example/<resource-name>')


brd=read_file('./resources/target/brd-<resource-name>')

erd_path = './resources/target/erd-<resource-name>'
erd = read_file(erd_path) if os.path.exists(erd_path) else "is not present"