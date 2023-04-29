from typing import List, Optional

from .base_model import BaseModel


class Set(BaseModel):
    set: Optional["SetSet"]


class SetSet(BaseModel):
    id: Optional[str]
    slots: Optional[List[Optional["SetSetSlots"]]]


class SetSetSlots(BaseModel):
    id: Optional[str]
    standing: Optional["SetSetSlotsStanding"]


class SetSetSlotsStanding(BaseModel):
    id: Optional[str]
    placement: Optional[int]
    stats: Optional["SetSetSlotsStandingStats"]


class SetSetSlotsStandingStats(BaseModel):
    score: Optional["SetSetSlotsStandingStatsScore"]


class SetSetSlotsStandingStatsScore(BaseModel):
    label: Optional[str]
    value: Optional[float]


Set.update_forward_refs()
SetSet.update_forward_refs()
SetSetSlots.update_forward_refs()
SetSetSlotsStanding.update_forward_refs()
SetSetSlotsStandingStats.update_forward_refs()
SetSetSlotsStandingStatsScore.update_forward_refs()
