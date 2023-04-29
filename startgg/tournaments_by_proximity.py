# Generated by ariadne-codegen on 2023-04-29 21:16
# Source: queries.graphql

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
