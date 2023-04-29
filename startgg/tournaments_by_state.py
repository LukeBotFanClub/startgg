from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class TournamentsByState(BaseModel):
    tournaments: Optional["TournamentsByStateTournaments"]


class TournamentsByStateTournaments(BaseModel):
    nodes: Optional[List[Optional["TournamentsByStateTournamentsNodes"]]]


class TournamentsByStateTournamentsNodes(BaseModel):
    id: Optional[str]
    name: Optional[str]
    addr_state: Optional[str] = Field(alias="addrState")


TournamentsByState.update_forward_refs()
TournamentsByStateTournaments.update_forward_refs()
TournamentsByStateTournamentsNodes.update_forward_refs()
