from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class PoolSeeds(BaseModel):
    phase_group: Optional["PoolSeedsPhaseGroup"] = Field(alias="phaseGroup")


class PoolSeedsPhaseGroup(BaseModel):
    id: Optional[str]
    seeds: Optional["PoolSeedsPhaseGroupSeeds"]


class PoolSeedsPhaseGroupSeeds(BaseModel):
    page_info: Optional["PoolSeedsPhaseGroupSeedsPageInfo"] = Field(alias="pageInfo")
    nodes: Optional[List[Optional["PoolSeedsPhaseGroupSeedsNodes"]]]


class PoolSeedsPhaseGroupSeedsPageInfo(BaseModel):
    total: Optional[int]


class PoolSeedsPhaseGroupSeedsNodes(BaseModel):
    entrant: Optional["PoolSeedsPhaseGroupSeedsNodesEntrant"]


class PoolSeedsPhaseGroupSeedsNodesEntrant(BaseModel):
    id: Optional[str]
    name: Optional[str]


PoolSeeds.update_forward_refs()
PoolSeedsPhaseGroup.update_forward_refs()
PoolSeedsPhaseGroupSeeds.update_forward_refs()
PoolSeedsPhaseGroupSeedsPageInfo.update_forward_refs()
PoolSeedsPhaseGroupSeedsNodes.update_forward_refs()
PoolSeedsPhaseGroupSeedsNodesEntrant.update_forward_refs()
