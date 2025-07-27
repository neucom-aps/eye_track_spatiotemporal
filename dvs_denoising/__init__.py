"""
DVS Denoising Module
Provides event denoising functionality for the eye tracking pipeline.
"""

from .accelerated_denoiser import denoise_events
from .convert_events_to_frames import events_to_frames

__version__ = "1.0.0"
__all__ = [
    "denoise_events",
    "events_to_frames"
]
