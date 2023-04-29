from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class TournamentsByCountry(BaseModel):
    tournaments: Optional["TournamentsByCountryTournaments"]


class TournamentsByCountryTournaments(BaseModel):
    nodes: Optional[List[Optional["TournamentsByCountryTournamentsNodes"]]]


class TournamentsByCountryTournamentsNodes(BaseModel):
    id: Optional[str]
    name: Optional[str]
    country_code: Optional[str] = Field(alias="countryCode")


TournamentsByCountry.update_forward_refs()
TournamentsByCountryTournaments.update_forward_refs()
TournamentsByCountryTournamentsNodes.update_forward_refs()
