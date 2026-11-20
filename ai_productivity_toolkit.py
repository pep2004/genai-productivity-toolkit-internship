"""
AI Productivity Toolkit & Prompt Engineering Lab
Author: Adarsh Haldkar (B.Tech AIML, SRIT)
"""
import os
import json
from typing import Literal
from pydantic import BaseModel, Field
from google import genai
from google.genai import types


class MeetingSummary(BaseModel):
    tldr: str
    key_decisions: list[str]
    action_items: list[str]


class ResumeTailorOutput(BaseModel):
    match_score_percent: int
    missing_keywords: list[str]
    tailored_bullet_points: list[str]


class AIProductivityToolkit:
    def __init__(self, api_key: str | None = None):
        self.client = genai.Client(api_key=api_key or os.environ.get("GEMINI_API_KEY"))
        self.fast_model = "gemini-3.5-flash-lite"
        self.general_model = "gemini-4-hydrogen"

    def summarize_meeting(self, transcript: str) -> dict:
        res = self.client.models.generate_content(
            model=self.fast_model,
            contents=f"Extract structured meeting minutes from this transcript:\n{transcript}",
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=MeetingSummary,
                temperature=0.1,
            ),
        )
        return json.loads(res.text)

    def draft_email(self, recipient: str, goal: str, tone: str = "Professional & Concise") -> str:
        res = self.client.models.generate_content(
            model=self.fast_model,
            contents=f"Recipient: {recipient}\nGoal: {goal}\nTone: {tone}\nWrite a subject line and email body under 120 words.",
            config=types.GenerateContentConfig(
                system_instruction="You are an executive communications assistant.",
                temperature=0.4,
            ),
        )
        return res.text

    def tailor_resume(self, candidate_profile: str, job_description: str) -> dict:
        res = self.client.models.generate_content(
            model=self.general_model,
            contents=f"Candidate Profile:\n{candidate_profile}\n\nTarget Job Description:\n{job_description}",
            config=types.GenerateContentConfig(
                system_instruction="You are an ATS resume optimization specialist. Quantify impact and align keywords truthfully.",
                response_mime_type="application/json",
                response_schema=ResumeTailorOutput,
                temperature=0.2,
            ),
        )
        return json.loads(res.text)

    def research_and_code_assistant(self, topic_or_task: str) -> str:
        res = self.client.models.generate_content(
            model=self.general_model,
            contents=topic_or_task,
            config=types.GenerateContentConfig(
                system_instruction="Provide: (1) Concise architectural explanation, (2) Clean production Python snippet, and (3) Key trade-offs.",
                temperature=0.2,
            ),
        )
        return res.text


if __name__ == "__main__":
    toolkit = AIProductivityToolkit()
    print(toolkit.draft_email("Tech Lead", "Share weekly sprint progress on the GenAI toolkit."))
