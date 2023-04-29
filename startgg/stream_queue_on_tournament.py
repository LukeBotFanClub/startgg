from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import StreamSource


class StreamQueueOnTournament(BaseModel):
    tournament: Optional["StreamQueueOnTournamentTournament"]


class StreamQueueOnTournamentTournament(BaseModel):
    id: Optional[str]
    stream_queue: Optional[
        List[Optional["StreamQueueOnTournamentTournamentStreamQueue"]]
    ] = Field(alias="streamQueue")


class StreamQueueOnTournamentTournamentStreamQueue(BaseModel):
    stream: Optional["StreamQueueOnTournamentTournamentStreamQueueStream"]
    sets: Optional[List[Optional["StreamQueueOnTournamentTournamentStreamQueueSets"]]]


class StreamQueueOnTournamentTournamentStreamQueueStream(BaseModel):
    stream_source: Optional[StreamSource] = Field(alias="streamSource")
    stream_name: Optional[str] = Field(alias="streamName")


class StreamQueueOnTournamentTournamentStreamQueueSets(BaseModel):
    id: Optional[str]


StreamQueueOnTournament.update_forward_refs()
StreamQueueOnTournamentTournament.update_forward_refs()
StreamQueueOnTournamentTournamentStreamQueue.update_forward_refs()
StreamQueueOnTournamentTournamentStreamQueueStream.update_forward_refs()
StreamQueueOnTournamentTournamentStreamQueueSets.update_forward_refs()
