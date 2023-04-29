from typing import List, Optional

from .base_model import BaseModel


class TournamentsByOwner(BaseModel):
    tournaments: Optional["TournamentsByOwnerTournaments"]


class TournamentsByOwnerTournaments(BaseModel):
    nodes: Optional[List[Optional["TournamentsByOwnerTournamentsNodes"]]]


class TournamentsByOwnerTournamentsNodes(BaseModel):
    id: Optional[str]
    name: Optional[str]
    slug: Optional[str]


TournamentsByOwner.update_forward_refs()
TournamentsByOwnerTournaments.update_forward_refs()
TournamentsByOwnerTournamentsNodes.update_forward_refs()
