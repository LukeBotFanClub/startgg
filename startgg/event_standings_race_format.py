from typing import List, Optional

from pydantic import Field, Json

from .base_model import BaseModel


class EventStandingsRaceFormat(BaseModel):
    event: Optional["EventStandingsRaceFormatEvent"]


class EventStandingsRaceFormatEvent(BaseModel):
    id: Optional[str]
    name: Optional[str]
    phase_groups: Optional[
        List[Optional["EventStandingsRaceFormatEventPhaseGroups"]]
    ] = Field(alias="phaseGroups")


class EventStandingsRaceFormatEventPhaseGroups(BaseModel):
    id: Optional[str]
    seeds: Optional["EventStandingsRaceFormatEventPhaseGroupsSeeds"]


class EventStandingsRaceFormatEventPhaseGroupsSeeds(BaseModel):
    nodes: Optional[
        List[Optional["EventStandingsRaceFormatEventPhaseGroupsSeedsNodes"]]
    ]


class EventStandingsRaceFormatEventPhaseGroupsSeedsNodes(BaseModel):
    id: Optional[str]
    standings: Optional[
        List[Optional["EventStandingsRaceFormatEventPhaseGroupsSeedsNodesStandings"]]
    ]


class EventStandingsRaceFormatEventPhaseGroupsSeedsNodesStandings(BaseModel):
    id: Optional[str]
    metadata: Optional[Json]


EventStandingsRaceFormat.update_forward_refs()
EventStandingsRaceFormatEvent.update_forward_refs()
EventStandingsRaceFormatEventPhaseGroups.update_forward_refs()
EventStandingsRaceFormatEventPhaseGroupsSeeds.update_forward_refs()
EventStandingsRaceFormatEventPhaseGroupsSeedsNodes.update_forward_refs()
EventStandingsRaceFormatEventPhaseGroupsSeedsNodesStandings.update_forward_refs()
