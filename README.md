# dysarthria-enhancer

Fine-tune open-source frontier voice models (starting with [VibeVoice](https://github.com/microsoft/VibeVoice)) on elderly and dysarthric speech to improve intelligibility and recognition for senior-living contexts.

## What this is

The inbound (recognition) side of elderly speech is the gap. Playback enhancement is well-handled. ASR systems trained on able-bodied adult speech underperform on residents in their 70s, 80s, and 90s, and especially on those with dysarthria from stroke, Parkinson's, ALS, or post-laryngectomy. This repo fine-tunes a base voice model on TORGO + an Inspiren-collected corpus and benchmarks the lift on WER + perceived intelligibility.

## Goals

1. Fine-tune VibeVoice (or comparable OSS) with LoRA on dysarthric corpora.
2. Evaluate against TORGO test split, the Nemours database, and Inspiren-collected resident utterances (consented + de-identified).
3. Ship a small inference script that runs on commodity hardware.

## Getting started

```bash
uv venv && source .venv/bin/activate
uv pip install -e .
python -m dysarthria_enhancer.main --in sample.wav --out enhanced.wav
```

## Layout

```
src/dysarthria_enhancer/
  main.py     # inference entry stub
data/         # corpus pointers and metadata (no audio committed)
```

## Why public

Dysarthric speech corpora and benchmarks are too scattered. Even if the fine-tuned weights end up gated, the eval scaffolding and dataset glue should be open.

## Related

* `speech-enhancer` (playback enhancement, Inspiren-internal): this repo is the recognition-side counterpart.
* Marilyn Wolf (UNL) collaboration thread on elder-care embedded computing.
