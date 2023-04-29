from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class PhaseGroupSets(BaseModel):
    phase_group: Optional["PhaseGroupSetsPhaseGroup"] = Field(alias="phaseGroup")


class PhaseGroupSetsPhaseGroup(BaseModel):
    id: Optional[str]
    display_identifier: Optional[str] = Field(alias="displayIdentifier")
    sets: Optional["PhaseGroupSetsPhaseGroupSets"]


class PhaseGroupSetsPhaseGroupSets(BaseModel):
    page_info: Optional["PhaseGroupSetsPhaseGroupSetsPageInfo"] = Field(
        alias="pageInfo"
    )
    nodes: Optional[List[Optional["PhaseGroupSetsPhaseGroupSetsNodes"]]]


class PhaseGroupSetsPhaseGroupSetsPageInfo(BaseModel):
    total: Optional[int]


class PhaseGroupSetsPhaseGroupSetsNodes(BaseModel):
    id: Optional[str]
    slots: Optional[List[Optional["PhaseGroupSetsPhaseGroupSetsNodesSlots"]]]


class PhaseGroupSetsPhaseGroupSetsNodesSlots(BaseModel):
    id: Optional[str]
    entrant: Optional["PhaseGroupSetsPhaseGroupSetsNodesSlotsEntrant"]


class PhaseGroupSetsPhaseGroupSetsNodesSlotsEntrant(BaseModel):
    id: Optional[str]
    name: Optional[str]


PhaseGroupSets.update_forward_refs()
PhaseGroupSetsPhaseGroup.update_forward_refs()
PhaseGroupSetsPhaseGroupSets.update_forward_refs()
PhaseGroupSetsPhaseGroupSetsPageInfo.update_forward_refs()
PhaseGroupSetsPhaseGroupSetsNodes.update_forward_refs()
PhaseGroupSetsPhaseGroupSetsNodesSlots.update_forward_refs()
PhaseGroupSetsPhaseGroupSetsNodesSlotsEntrant.update_forward_refs()
