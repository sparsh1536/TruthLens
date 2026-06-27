from dataclasses import dataclass, field

@dataclass
class Document:
    video_url: str = ""

    audio_path: str = ""

    transcript: str = ""

    sentences: list = field(default_factory=list)

    claims: list = field(default_factory=list)

    evidence: list = field(default_factory=list)

    verdicts: list = field(default_factory=list)