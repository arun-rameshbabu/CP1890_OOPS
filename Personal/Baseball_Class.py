from dataclasses import dataclass, field


@dataclass
class Baseball:
    player: str = ""
    atbats: int = 0
    hits: int = 0
    # avg: atbats / hits
