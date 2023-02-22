import streamlit as st
import ast

#AI----
import os
import openai
openai.api_key ="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"

#function that returns AI responses
@st.cache
def ai(prompt):
    response = openai.Completion.create(
          model="text-davinci-003",
          prompt=prompt,
          temperature=0,
          max_tokens=256,
          top_p=1.0,
          frequency_penalty=0.0,
          presence_penalty=0.0
          )

    ai_response = response["choices"][0]["text"]
    return ai_response

#------

# Title the page
st.title("Tailor Your Resume")

#create sidebar
sb = st.sidebar

#columns
col1, col2 = st.columns(2, gap = 'large')

#grabs and stores link
#link = st.text_input("Link:")

# Create text entry box for job description
job_description = st.text_area("Job Description:")

if job_description != '':
  skill_prompt = f"""
  Please extract ALL of the job skills from the job description and return a python list (Ex: ['python', 'teamwork', 'problem-solving']:
  
  Job description: {job_description}

  NOTE: ONLY INCLUDE THE PYTHON LIST, NO OTHER LEADING OR TRAILING WORDS OR SPACES!
  """

  #ai response for list of skills
  ai_response_skills = ai(skill_prompt).strip()
  
  # Create multiselect widget for user to select relevant skills
  skills_from_description = ast.literal_eval(ai_response_skills)

  #grabs relevant words
  word_prompt = f"""
    Please extract ALL of the keywords and action words from the job description and return a python list (Ex: ['develop', 'create', 'problem-solving']:
    
    Job description: {job_description}

    NOTE: ONLY INCLUDE THE PYTHON LIST, NO OTHER LEADING OR TRAILING WORDS OR SPACES!
    """

  #ai response for list of skills
  ai_response_words = ai(word_prompt).strip()

  #check words list
  st.write(ai_response_words)

  skills = st.multiselect("Skills:", options=skills_from_description)

else:
  print("HELLO")



# Create text entry box for experience bullet points
experience = st.text_area("Experience:")

num_bullets = st.select_slider("Number of bullets", [1,2,3,4,5])

if experience != '':
  #tell AI to rewrite experience
  rewritten_experience_prompt = f"""
  Please rewrite the following resume experience using relevant skills, action words and keywords from the following lists:

  Resume experience to rewrite: {experience}

  Skills to use (if relevant and applicable): {skills}

  Keywords and action words to use (if relevant and applicable): {ai_response_words}

  NOTE: ONLY INCLUDE THE REWRITTEN RESUME EXPERIENCE IN BULLETED FORMAT! ADD A NEW LINE FOR EVERY BULLET POINT

  NUMBER OF BULLETS: {num_bullets}
  """

  #ai response for list of skills
  new_resume_experience = ai(rewritten_experience_prompt)

  #check the new experience
  st.text(new_resume_experience)

else:
  print("hello")
