# Generated by ariadne-codegen on 2023-04-29 21:16
# Source: queries.graphql

from typing import List, Optional

from .base_model import BaseModel


class TournamentsByVideogame(BaseModel):
    tournaments: Optional["TournamentsByVideogameTournaments"]


class TournamentsByVideogameTournaments(BaseModel):
    nodes: Optional[List[Optional["TournamentsByVideogameTournamentsNodes"]]]


class TournamentsByVideogameTournamentsNodes(BaseModel):
    id: Optional[str]
    name: Optional[str]
    slug: Optional[str]


TournamentsByVideogame.update_forward_refs()
TournamentsByVideogameTournaments.update_forward_refs()
TournamentsByVideogameTournamentsNodes.update_forward_refs()
