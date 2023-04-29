from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class AttendeeCountEvents(BaseModel):
    tournament: Optional["AttendeeCountEventsTournament"]


class AttendeeCountEventsTournament(BaseModel):
    id: Optional[str]
    name: Optional[str]
    participants: Optional["AttendeeCountEventsTournamentParticipants"]


class AttendeeCountEventsTournamentParticipants(BaseModel):
    page_info: Optional["AttendeeCountEventsTournamentParticipantsPageInfo"] = Field(
        alias="pageInfo"
    )


class AttendeeCountEventsTournamentParticipantsPageInfo(BaseModel):
    total: Optional[int]


AttendeeCountEvents.update_forward_refs()
AttendeeCountEventsTournament.update_forward_refs()
AttendeeCountEventsTournamentParticipants.update_forward_refs()
AttendeeCountEventsTournamentParticipantsPageInfo.update_forward_refs()
