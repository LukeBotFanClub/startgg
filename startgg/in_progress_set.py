from typing import List, Optional

from .base_model import BaseModel


class InProgressSet(BaseModel):
    set: Optional["InProgressSetSet"]


class InProgressSetSet(BaseModel):
    state: Optional[int]
    slots: Optional[List[Optional["InProgressSetSetSlots"]]]


class InProgressSetSetSlots(BaseModel):
    entrant: Optional["InProgressSetSetSlotsEntrant"]
    standing: Optional["InProgressSetSetSlotsStanding"]


class InProgressSetSetSlotsEntrant(BaseModel):
    name: Optional[str]


class InProgressSetSetSlotsStanding(BaseModel):
    stats: Optional["InProgressSetSetSlotsStandingStats"]


class InProgressSetSetSlotsStandingStats(BaseModel):
    score: Optional["InProgressSetSetSlotsStandingStatsScore"]


class InProgressSetSetSlotsStandingStatsScore(BaseModel):
    value: Optional[float]


InProgressSet.update_forward_refs()
InProgressSetSet.update_forward_refs()
InProgressSetSetSlots.update_forward_refs()
InProgressSetSetSlotsEntrant.update_forward_refs()
InProgressSetSetSlotsStanding.update_forward_refs()
InProgressSetSetSlotsStandingStats.update_forward_refs()
InProgressSetSetSlotsStandingStatsScore.update_forward_refs()
