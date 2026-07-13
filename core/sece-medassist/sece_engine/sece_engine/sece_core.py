# sece_engine/sece_core.py
# Synthetic Emotional Cognition Engine — Minimal Core

from dataclasses import dataclass


def clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


@dataclass
class EmotionalSignal:
    intensity: float   # I ∈ [0, 1]
    clarity: float     # C ∈ [0, 1]
    relevance: float   # R ∈ [0, 1]
    direction: int     # -1 or +1


class SECECore:
    """
    Minimal continuous emotional state engine.
    E(t) ∈ [-1.0, 1.0]
    """

    def __init__(self, decay: float = 0.02, gain: float = 0.2):
        self.E = 0.0
        self.decay = decay
        self.gain = gain

    def resonance(self, signal: EmotionalSignal) -> float:
        return (
            signal.intensity
            * signal.clarity
            * signal.relevance
        )

    def step(self, signal: EmotionalSignal) -> float:
        # decay previous state
        self.E *= (1.0 - self.decay)

        # apply resonance influence
        res = self.resonance(signal)
        self.E += signal.direction * res * self.gain

        # stability / ethical bound
        self.E = clamp(self.E, -1.0, 1.0)

        return self.E

    def state(self) -> float:
        return self.E

