# Resume-job-match-agent
A narrow AI agent that evaluates resume -job fit with explainable output.
# Resume–Job Match AI Agent

## Overview
This project is a narrow AI agent that evaluates how well a resume matches a specific job description.
It produces a structured, explainable assessment rather than generic advice.

The project demonstrates a focused, end-to-end use of large language models with emphasis on:
- Clear constraints
- Explainability
- Responsible AI usage

## Problem Statement
Most job-matching tools provide opaque scores or generic feedback, leaving applicants unsure why they are or are not a good fit.

This project addresses that gap by providing structured, actionable feedback highlighting:
- Match strengths
- Gaps
- Suggestions for improvement

## Solution
The agent:
- Takes a resume and job description as input
- Extracts relevant skills, experience, and role requirements
- Evaluates alignment across predefined categories
- Returns a structured, explainable match report

The system avoids broad career advice and focuses on a single, well-defined task.

## How It Works
1. Resume and job description text are provided by the user
2. The model extracts key signals:
   - Required skills
   - Relevant experience
   - Role expectations
3. Each category is evaluated independently
4. Results are aggregated into:
   - Match score (0–100)
   - Strengths
   - Gaps
   - Suggestions

Outputs are provided in both structured and human-readable formats.

## Example
```text
Resume:
"Software engineer with 3 years of experience building backend services in Python..."
Job Description:
"Looking for a backend engineer with strong Python skills, REST API experience, and cloud familiarity..."
Output:
{
  "match_score": 72,
  "strengths": ["Python", "Backend API development"],
  "gaps": ["Cloud deployment experience"],
  "suggestions": ["Highlight AWS or Docker projects", "Quantify backend performance improvements"]
}
Design Decisions:

Narrow scope to reduce hallucination risk

Explicit evaluation categories instead of free-form judgment

Emphasis on explainability over automation


Limitations:

Depends on the quality of provided text

Does not verify factual claims

Not intended for automated hiring decisions


Safety & Responsible AI:

No personal data is stored

Outputs avoid definitive hiring recommendations

Designed to minimize overconfident or misleading outputs


Tech Stack:

Language: Python

Model: OpenAI API

Interface: Command-line script


Future Work:

Automated evaluation against labeled datasets

Multiple job description support

Improve robustness against prompt manipulation


Why This Project:

This project demonstrates:

Practical LLM system design

Thoughtful constraints

Awareness of model limitations and safety
