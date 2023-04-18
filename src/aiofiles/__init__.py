"""Utilities for asyncio-friendly file handling."""
from .threadpool import (
    open,
    stdin,
    stdout,
    stderr,
    stdin_bytes,
    stdout_bytes,
    stderr_bytes,
)
from . import tempfile
__version__ = "23.0.1"

__all__ = [
    "open",
    "tempfile",
    "stdin",
    "stdout",
    "stderr",
    "stdin_bytes",
    "stdout_bytes",
    "stderr_bytes",
]
