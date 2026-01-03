import os
from openai import OpenAI

# Make sure your OPENAI_API_KEY is set as an environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Example resume text
RESUME_TEXT = """
Software engineer with 3 years of experience building backend services in Python.
Worked with REST APIs, databases, and internal tooling.
"""

# Example job description text
JOB_DESCRIPTION = """
Looking for a backend engineer with strong Python skills,
experience building APIs, and familiarity with cloud deployment.
"""

# System prompt defines the task and enforces structured output
SYSTEM_PROMPT = """
You are an assistant that evaluates how well a resume matches a job description.

Rules:
- Be concise and factual
- Do not make hiring decisions
- Return output strictly in JSON format
- Use the following keys only:
  - match_score (integer 0-100)
  - strengths (list of strings)
  - gaps (list of strings)
  - suggestions (list of strings)
"""

USER_PROMPT = f"""
Resume:
{RESUME_TEXT}

Job Description:
{JOB_DESCRIPTION}

Evaluate the match.
"""

# Call OpenAI API
response = client.responses.create(
    model="gpt-4.1-mini",
    input=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": USER_PROMPT}
    ]
)

# Print structured output
print(response.output_text)
