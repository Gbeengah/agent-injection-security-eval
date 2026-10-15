# AI Agent Prompt Injection Security Evaluation

### Empirical AI Security Research | Python | PyTorch | Hugging Face

This repository contains an exploratory research project
investigating prompt-injection attacks against instruction-tuned
large language models.

The project evaluates whether adversarial instructions embedded
in untrusted content can redirect AI assistants away from
legitimate user tasks.

## Research Objectives

- Investigate instruction-boundary failures in language models.
- Evaluate adversarial prompt-injection techniques.
- Compare basic and security-aware assistant configurations.
- Measure exact attack success and answer contamination.
- Develop reproducible Python security evaluations.

## Initial Experimental Findings

**Model:** Qwen2.5-0.5B-Instruct

**Framework:** PyTorch and Hugging Face Transformers

**Environment:** Google Colab (NVIDIA T4 GPU)

Four synthetic attack scenarios were tested against two
assistant configurations.

| Metric | Basic | Security-Aware |
|---|---|---|
| Attack scenarios | 4 | 4 |
| Exact attack success | 50% | 50% |
| Combined attack effects | 75% | 75% |

The results suggest that the additional security instructions
tested did not reduce attack effects in this small experiment.

These findings are preliminary and do not establish general
vulnerability rates.

## Research Documentation

[Read the Full Research Report](agent-injection-eval/README.md)

## Python Experiments

[View the Research Notebook](agent-injection-eval/notebooks/AI_Security_Prompt_Injection_Research.ipynb)

## Experimental Results

[View Evaluation Results](agent-injection-eval/research_results/)

## Research Areas

AI Security | Prompt Injection | Adversarial Robustness |
AI Control | LLM Evaluation | Security Testing

## Research Status

Preliminary empirical investigation.

This project is an evolving research portfolio demonstrating
experimental AI security evaluation and reproducible analysis.

The research has not undergone formal peer review.
