from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class PrefixSearchAttendees(BaseModel):
    tournament: Optional["PrefixSearchAttendeesTournament"]


class PrefixSearchAttendeesTournament(BaseModel):
    id: Optional[str]
    name: Optional[str]
    participants: Optional["PrefixSearchAttendeesTournamentParticipants"]


class PrefixSearchAttendeesTournamentParticipants(BaseModel):
    nodes: Optional[List[Optional["PrefixSearchAttendeesTournamentParticipantsNodes"]]]


class PrefixSearchAttendeesTournamentParticipantsNodes(BaseModel):
    id: Optional[str]
    gamer_tag: Optional[str] = Field(alias="gamerTag")


PrefixSearchAttendees.update_forward_refs()
PrefixSearchAttendeesTournament.update_forward_refs()
PrefixSearchAttendeesTournamentParticipants.update_forward_refs()
PrefixSearchAttendeesTournamentParticipantsNodes.update_forward_refs()
