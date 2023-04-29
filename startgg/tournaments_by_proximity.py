from typing import List, Optional

from .base_model import BaseModel


class TournamentsByProximity(BaseModel):
    tournaments: Optional["TournamentsByProximityTournaments"]


class TournamentsByProximityTournaments(BaseModel):
    nodes: Optional[List[Optional["TournamentsByProximityTournamentsNodes"]]]


class TournamentsByProximityTournamentsNodes(BaseModel):
    id: Optional[str]
    name: Optional[str]
    city: Optional[str]


TournamentsByProximity.update_forward_refs()
TournamentsByProximityTournaments.update_forward_refs()
TournamentsByProximityTournamentsNodes.update_forward_refs()
