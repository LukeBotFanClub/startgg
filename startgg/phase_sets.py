from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class PhaseSets(BaseModel):
    phase: Optional["PhaseSetsPhase"]


class PhaseSetsPhase(BaseModel):
    id: Optional[str]
    name: Optional[str]
    sets: Optional["PhaseSetsPhaseSets"]


class PhaseSetsPhaseSets(BaseModel):
    page_info: Optional["PhaseSetsPhaseSetsPageInfo"] = Field(alias="pageInfo")
    nodes: Optional[List[Optional["PhaseSetsPhaseSetsNodes"]]]


class PhaseSetsPhaseSetsPageInfo(BaseModel):
    total: Optional[int]


class PhaseSetsPhaseSetsNodes(BaseModel):
    id: Optional[str]
    slots: Optional[List[Optional["PhaseSetsPhaseSetsNodesSlots"]]]


class PhaseSetsPhaseSetsNodesSlots(BaseModel):
    id: Optional[str]
    entrant: Optional["PhaseSetsPhaseSetsNodesSlotsEntrant"]


class PhaseSetsPhaseSetsNodesSlotsEntrant(BaseModel):
    id: Optional[str]
    name: Optional[str]


PhaseSets.update_forward_refs()
PhaseSetsPhase.update_forward_refs()
PhaseSetsPhaseSets.update_forward_refs()
PhaseSetsPhaseSetsPageInfo.update_forward_refs()
PhaseSetsPhaseSetsNodes.update_forward_refs()
PhaseSetsPhaseSetsNodesSlots.update_forward_refs()
PhaseSetsPhaseSetsNodesSlotsEntrant.update_forward_refs()
