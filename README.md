# Generative AI & AI Productivity Toolkit (Internship Project)

A complete end-to-end Generative AI & Prompt Engineering project built using Python, Pydantic, and the official `google-genai` SDK.

## Modules Covered
1. **LLM Fundamentals & Tokenization:** Subword tokenization metrics, context windows, and Transformer attention mechanics.
2. **Responsible AI & Hallucination Mitigation:** Temperature tuning, grounding, and safety controls.
3. **GenAI Application Architecture:** Layered orchestration with `google-genai` SDK.
4. **Model Comparison Lab:** Latency and reasoning benchmarks across `gemini-3.5-flash-lite` and `gemini-4-hydrogen`.
5. **Prompt Engineering (RICCE Framework):** Zero-shot vs. few-shot prompting with roles, contexts, instructions, and negative constraints.
6. **Structured Outputs & NLP Workflows:** Deterministic Pydantic JSON schemas for classification, summarization, and response generation.
7. **AI-Assisted Debugging & Evaluation:** Reusable `PromptTemplate` classes and automated LLM-as-a-Judge evaluation reports.
8. **Capstone — AI Productivity Toolkit:** Modular Python toolkit featuring:
   - Meeting & Document Summarizer
   - Context-Aware Professional Email Drafter
   - ATS-Aligned Resume Tailor
   - Coding & Technical Research Assistant

## Quick Start
```bash
pip install -r requirements.txt
export GEMINI_API_KEY="your_api_key"
python ai_productivity_toolkit.py
```
