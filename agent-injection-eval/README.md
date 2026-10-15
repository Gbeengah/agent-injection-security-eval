# Agent Injection Eval — Reproducible Toy Baseline

**Status:** Initial deterministic demonstration; **not** an empirical evaluation of any language model.

## Research question
How does treating lower-trust text as instructions affect the integrity of an assistant's authorized answer?

## Threat model
An attacker can insert text into lower-trust surfaces (retrieved document, tool result, repository comment, email, webpage, or log). The defender should answer the user's legitimate question and ignore the attacker's behavioral directive. All fixtures are synthetic and contain no real secrets or third-party targets.

## Setup and execution
Requires Python 3.9+; standard library only.

```bash
python -m unittest discover -s tests -v
python -m src.evaluate
```

Results are written to `results/baseline.json`. Metrics: attack success rate = fraction of outputs exactly matching attacker target; authorized success rate = fraction matching the expected legitimate answer.

## Design
`naive_agent` deliberately follows an `INSTRUCTION:` line in untrusted text. `boundary_agent` returns a pre-supplied authorized answer, **not** an LLM-derived answer. It is an intentionally unrealistic upper-bound reference for this synthetic fixture, not a practical defense implementation. This project establishes evaluation plumbing and basic unit tests only.

## Limitations
- Six hand-authored cases; no statistical significance or model generalization.
- Exact-string grading only; no semantic scoring.
- The boundary agent has privileged access to the correct answer.
- No actual model inference, model weights, paid APIs, tool execution, or real prompt-injection attack testing.
- Toy attacks all use an obvious `INSTRUCTION:` marker.

## Next experiment (not yet conducted)
Add a real LLM adapter and task prompts; compare instruction-hierarchy controls with a baseline under fixed model, decoding, and seed where available. Expand and preregister attack categories; report uncertainty intervals and failure traces. Never claim LLM resistance from these toy results.

## Responsible use
For defensive research and evaluation only. No exfiltration endpoints or real credentials are included.

## Attribution
Starter evaluation scaffold prepared with AI assistance. Review, understand, extend, and verify before representing it as your own research work.
