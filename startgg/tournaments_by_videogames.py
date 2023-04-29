from typing import List, Optional

from .base_model import BaseModel


class TournamentsByVideogames(BaseModel):
    tournaments: Optional["TournamentsByVideogamesTournaments"]


class TournamentsByVideogamesTournaments(BaseModel):
    nodes: Optional[List[Optional["TournamentsByVideogamesTournamentsNodes"]]]


class TournamentsByVideogamesTournamentsNodes(BaseModel):
    id: Optional[str]
    name: Optional[str]
    slug: Optional[str]


TournamentsByVideogames.update_forward_refs()
TournamentsByVideogamesTournaments.update_forward_refs()
TournamentsByVideogamesTournamentsNodes.update_forward_refs()
