from dataclasses import dataclass

@dataclass
class Result:
    headline: str = ""
    home_points: int = 0
    away_points: int = 0
