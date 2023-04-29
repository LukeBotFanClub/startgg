from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class InProgressResults(BaseModel):
    event: Optional["InProgressResultsEvent"]


class InProgressResultsEvent(BaseModel):
    tournament: Optional["InProgressResultsEventTournament"]
    name: Optional[str]
    sets: Optional["InProgressResultsEventSets"]


class InProgressResultsEventTournament(BaseModel):
    name: Optional[str]


class InProgressResultsEventSets(BaseModel):
    nodes: Optional[List[Optional["InProgressResultsEventSetsNodes"]]]


class InProgressResultsEventSetsNodes(BaseModel):
    full_round_text: Optional[str] = Field(alias="fullRoundText")
    display_score: Optional[str] = Field(alias="displayScore")
    w_placement: Optional[int] = Field(alias="wPlacement")
    l_placement: Optional[int] = Field(alias="lPlacement")
    winner_id: Optional[int] = Field(alias="winnerId")
    round: Optional[int]


InProgressResults.update_forward_refs()
InProgressResultsEvent.update_forward_refs()
InProgressResultsEventTournament.update_forward_refs()
InProgressResultsEventSets.update_forward_refs()
InProgressResultsEventSetsNodes.update_forward_refs()
