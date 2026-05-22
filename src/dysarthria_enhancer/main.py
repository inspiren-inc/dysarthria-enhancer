"""Inference entry stub.

v0 is a passthrough so the package installs and runs end-to-end. The real
model-loading + inference pipeline lands in subsequent commits.
"""
from __future__ import annotations

from pathlib import Path

import click
import numpy as np
import soundfile as sf


@click.command()
@click.option("--in", "in_path", required=True, type=click.Path(exists=True, dir_okay=False))
@click.option("--out", "out_path", required=True, type=click.Path(dir_okay=False))
def main(in_path: str, out_path: str) -> None:
    """Enhance an input WAV. v0: identity copy + provenance."""
    samples, sr = sf.read(in_path, dtype="float32")
    enhanced = samples.copy()  # placeholder for the model call
    sf.write(out_path, enhanced, sr, subtype="PCM_24")
    click.echo(f"v0 passthrough: copied {in_path} -> {out_path} (sr={sr}, n={len(samples)})")


if __name__ == "__main__":  # pragma: no cover
    main()
