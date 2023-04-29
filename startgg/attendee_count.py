from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class AttendeeCount(BaseModel):
    tournament: Optional["AttendeeCountTournament"]


class AttendeeCountTournament(BaseModel):
    id: Optional[str]
    name: Optional[str]
    participants: Optional["AttendeeCountTournamentParticipants"]


class AttendeeCountTournamentParticipants(BaseModel):
    page_info: Optional["AttendeeCountTournamentParticipantsPageInfo"] = Field(
        alias="pageInfo"
    )


class AttendeeCountTournamentParticipantsPageInfo(BaseModel):
    total: Optional[int]


AttendeeCount.update_forward_refs()
AttendeeCountTournament.update_forward_refs()
AttendeeCountTournamentParticipants.update_forward_refs()
AttendeeCountTournamentParticipantsPageInfo.update_forward_refs()
