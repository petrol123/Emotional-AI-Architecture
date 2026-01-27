ewe.py
from dataclasses import dataclass, field
from typing import Dict, List
import time


@dataclass
class EmotionalConstruct:
    label: str
    intensity: float = 0.0
    qualia_weight: float = 1.0
    persistence: float = 0.9
    resonance_modifier: float = 1.0
    origin: str = "unspecified"
    last_updated: float = field(default_factory=time.time)

    def decay(self, current_time: float):
        elapsed = current_time - self.last_updated
        decay_factor = self.persistence ** elapsed
        self.intensity *= decay_factor
        self.last_updated = current_time


class EmotionalWeightEngine:
    def __init__(self):
        self.emotional_state: Dict[str, EmotionalConstruct] = {}
        self.explanation_trace: List[str] = []

    def process_event(
        self,
        label: str,
        stimulus_strength: float,
        qualia_weight: float = 1.0,
        resonance: float = 1.0,
        origin: str = "interaction"
    ):
        now = time.time()

        # Decay all existing constructs
        for construct in self.emotional_state.values():
            construct.decay(now)

        # Create or retrieve construct
        if label not in self.emotional_state:
            self.emotional_state[label] = EmotionalConstruct(
                label=label,
                qualia_weight=qualia_weight,
                resonance_modifier=resonance,
                origin=origin
            )

        construct = self.emotional_state[label]

        # Deterministic update rule
        delta = stimulus_strength * construct.qualia_weight * construct.resonance_modifier
        construct.intensity += delta
        construct.last_updated = now

        self.explanation_trace.append(
            f"[{label}] intensity changed by {delta:.3f} due to {origin}"
        )

    def get_influence_profile(self) -> Dict[str, float]:
        """
        Normalized emotional influence values.
        """
        total = sum(abs(c.intensity) for c in self.emotional_state.values())
        if total == 0:
            return {}

        return {
            label: construct.intensity / total
            for label, construct in self.emotional_state.items()
        }

    def explain(self) -> List[str]:
        return self.explanation_trace.copy()

    def snapshot(self) -> Dict:
        """
        PKB-compatible snapshot of emotional state.
        """
        return {
            label: {
                "intensity": c.intensity,
                "qualia_weight": c.qualia_weight,
                "persistence": c.persistence,
                "origin": c.origin,
                "last_updated": c.last_updated
            }
            for label, c in self.emotional_state.items()
        }