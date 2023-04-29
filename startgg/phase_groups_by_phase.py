from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class PhaseGroupsByPhase(BaseModel):
    phase: Optional["PhaseGroupsByPhasePhase"]


class PhaseGroupsByPhasePhase(BaseModel):
    id: Optional[str]
    phase_groups: Optional["PhaseGroupsByPhasePhasePhaseGroups"] = Field(
        alias="phaseGroups"
    )


class PhaseGroupsByPhasePhasePhaseGroups(BaseModel):
    page_info: Optional["PhaseGroupsByPhasePhasePhaseGroupsPageInfo"] = Field(
        alias="pageInfo"
    )
    nodes: Optional[List[Optional["PhaseGroupsByPhasePhasePhaseGroupsNodes"]]]


class PhaseGroupsByPhasePhasePhaseGroupsPageInfo(BaseModel):
    total: Optional[int]


class PhaseGroupsByPhasePhasePhaseGroupsNodes(BaseModel):
    id: Optional[str]
    display_identifier: Optional[str] = Field(alias="displayIdentifier")


PhaseGroupsByPhase.update_forward_refs()
PhaseGroupsByPhasePhase.update_forward_refs()
PhaseGroupsByPhasePhasePhaseGroups.update_forward_refs()
PhaseGroupsByPhasePhasePhaseGroupsPageInfo.update_forward_refs()
PhaseGroupsByPhasePhasePhaseGroupsNodes.update_forward_refs()
