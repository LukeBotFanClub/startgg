from datetime import datetime
from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import (
    ActivityState,
    BracketType,
    TeamMemberStatus,
    TournamentPaginationSort,
)


class UserEventsPaginationQuery(BaseModel):
    page: Optional[int]
    per_page: Optional[int] = Field(alias="perPage")
    sort_by: Optional[str] = Field(alias="sortBy")
    filter: Optional["UserEventsPaginationFilter"]


class UserEventsPaginationFilter(BaseModel):
    videogame_id: Optional[List[Optional[str]]] = Field(alias="videogameId")
    event_type: Optional[int] = Field(alias="eventType")
    min_entrant_count: Optional[int] = Field(alias="minEntrantCount")
    max_entrant_count: Optional[int] = Field(alias="maxEntrantCount")
    location: Optional["LocationFilterType"]
    search: Optional["PaginationSearchType"]


class LocationFilterType(BaseModel):
    country_code: Optional[str] = Field(alias="countryCode")
    state: Optional[str]
    city: Optional[str]


class PaginationSearchType(BaseModel):
    fields_to_search: Optional[List[Optional[str]]] = Field(alias="fieldsToSearch")
    search_string: Optional[str] = Field(alias="searchString")


class EventEntrantPageQuery(BaseModel):
    page: Optional[int]
    per_page: Optional[int] = Field(alias="perPage")
    sort_by: Optional[str] = Field(alias="sortBy")
    filter: Optional["EventEntrantPageQueryFilter"]


class EventEntrantPageQueryFilter(BaseModel):
    name: Optional[str]


class SetFilters(BaseModel):
    entrant_ids: Optional[List[Optional[str]]] = Field(alias="entrantIds")
    entrant_size: Optional[List[Optional[int]]] = Field(alias="entrantSize")
    has_vod: Optional[bool] = Field(alias="hasVod")
    hide_empty: Optional[bool] = Field(alias="hideEmpty")
    show_byes: Optional[bool] = Field(alias="showByes")
    is_event_online: Optional[bool] = Field(alias="isEventOnline")
    location: Optional["SetFilterLocation"]
    participant_ids: Optional[List[Optional[str]]] = Field(alias="participantIds")
    phase_group_ids: Optional[List[Optional[str]]] = Field(alias="phaseGroupIds")
    phase_ids: Optional[List[Optional[str]]] = Field(alias="phaseIds")
    event_ids: Optional[List[Optional[str]]] = Field(alias="eventIds")
    tournament_ids: Optional[List[Optional[str]]] = Field(alias="tournamentIds")
    player_ids: Optional[List[Optional[str]]] = Field(alias="playerIds")
    round_number: Optional[int] = Field(alias="roundNumber")
    state: Optional[List[Optional[int]]]
    station_ids: Optional[List[Optional[str]]] = Field(alias="stationIds")
    station_numbers: Optional[List[Optional[int]]] = Field(alias="stationNumbers")
    updated_after: Optional[datetime] = Field(alias="updatedAfter")


class SetFilterLocation(BaseModel):
    state: Optional[str]
    country: Optional[str]
    distance_from: Optional["SetFilterLocationDistanceFrom"] = Field(
        alias="distanceFrom"
    )


class SetFilterLocationDistanceFrom(BaseModel):
    point: Optional["SetFilterLocationDistanceFromPoint"]
    radius: Optional[str]


class SetFilterLocationDistanceFromPoint(BaseModel):
    lat: Optional[float]
    lon: Optional[float]


class EventFilter(BaseModel):
    videogame_id: Optional[List[Optional[str]]] = Field(alias="videogameId")
    type: Optional[List[Optional[int]]]
    published: Optional[bool]
    id: Optional[str]
    ids: Optional[List[Optional[str]]]
    slug: Optional[str]
    fantasy_event_id: Optional[str] = Field(alias="fantasyEventId")
    fantasy_roster_hash: Optional[str] = Field(alias="fantasyRosterHash")


class ParticipantPaginationQuery(BaseModel):
    page: Optional[int]
    per_page: Optional[int] = Field(alias="perPage")
    sort_by: Optional[str] = Field(alias="sortBy")
    filter: Optional["ParticipantPageFilter"]


class ParticipantPageFilter(BaseModel):
    id: Optional[str]
    ids: Optional[List[Optional[str]]]
    event_ids: Optional[List[Optional[str]]] = Field(alias="eventIds")
    search: Optional["PaginationSearchType"]
    gamer_tag: Optional[str] = Field(alias="gamerTag")
    unpaid: Optional[bool]
    incomplete_team: Optional[bool] = Field(alias="incompleteTeam")
    missing_deck: Optional[bool] = Field(alias="missingDeck")
    checked_in: Optional[bool] = Field(alias="checkedIn")
    not_checked_in: Optional[bool] = Field(alias="notCheckedIn")


class TeamPaginationQuery(BaseModel):
    page: Optional[int]
    per_page: Optional[int] = Field(alias="perPage")
    sort_by: Optional[str] = Field(alias="sortBy")
    filter: Optional["TeamPaginationFilter"]


class TeamPaginationFilter(BaseModel):
    global_team_id: Optional[str] = Field(alias="globalTeamId")
    event_state: Optional[ActivityState] = Field(alias="eventState")
    event_id: Optional[str] = Field(alias="eventId")
    event_ids: Optional[List[Optional[str]]] = Field(alias="eventIds")
    min_entrant_count: Optional[int] = Field(alias="minEntrantCount")
    max_entrant_count: Optional[int] = Field(alias="maxEntrantCount")
    search: Optional["PaginationSearchType"]
    type: Optional[int]
    tournament_id: Optional[str] = Field(alias="tournamentId")
    member_status: Optional[List[Optional[TeamMemberStatus]]] = Field(
        alias="memberStatus"
    )
    videogame_id: Optional[List[Optional[str]]] = Field(alias="videogameId")
    is_league: Optional[bool] = Field(alias="isLeague")
    upcoming: Optional[bool]
    past: Optional[bool]
    roster_complete: Optional[bool] = Field(alias="rosterComplete")
    roster_incomplete: Optional[bool] = Field(alias="rosterIncomplete")


class SeedPaginationQuery(BaseModel):
    page: Optional[int]
    per_page: Optional[int] = Field(alias="perPage")
    sort_by: Optional[str] = Field(alias="sortBy")
    filter: Optional["SeedPageFilter"]


class SeedPageFilter(BaseModel):
    id: Optional[str]
    entrant_name: Optional[str] = Field(alias="entrantName")
    check_in_state: Optional[List[Optional[int]]] = Field(alias="checkInState")
    phase_group_id: Optional[List[Optional[str]]] = Field(alias="phaseGroupId")
    event_check_in_group_id: Optional[str] = Field(alias="eventCheckInGroupId")
    phase_id: Optional[List[Optional[str]]] = Field(alias="phaseId")
    event_id: Optional[str] = Field(alias="eventId")
    search: Optional["PaginationSearchType"]


class PhaseGroupPageQuery(BaseModel):
    page: Optional[int]
    per_page: Optional[int] = Field(alias="perPage")
    sort_by: Optional[str] = Field(alias="sortBy")
    entrant_ids: Optional[List[Optional[str]]] = Field(alias="entrantIds")
    filter: Optional["PhaseGroupPageQueryFilter"]


class PhaseGroupPageQueryFilter(BaseModel):
    id: Optional[List[Optional[str]]]
    wave_id: Optional[str] = Field(alias="waveId")


class StandingGroupStandingPageFilter(BaseModel):
    page: Optional[int]
    per_page: Optional[int] = Field(alias="perPage")
    sort_by: Optional[str] = Field(alias="sortBy")


class EventOwnersQuery(BaseModel):
    page: Optional[int]
    per_page: Optional[int] = Field(alias="perPage")
    sort_by: Optional[str] = Field(alias="sortBy")


class LeagueEventsQuery(BaseModel):
    page: Optional[int]
    per_page: Optional[int] = Field(alias="perPage")
    sort_by: Optional[str] = Field(alias="sortBy")
    filter: Optional["LeagueEventsFilter"]


class LeagueEventsFilter(BaseModel):
    search: Optional["PaginationSearchType"]
    point_mapping_group_ids: Optional[List[Optional[str]]] = Field(
        alias="pointMappingGroupIds"
    )
    tier_ids: Optional[List[Optional[str]]] = Field(alias="tierIds")
    user_id: Optional[str] = Field(alias="userId")
    upcoming: Optional[bool]
    league_entrant_id: Optional[str] = Field(alias="leagueEntrantId")


class StandingPaginationQuery(BaseModel):
    page: Optional[int]
    per_page: Optional[int] = Field(alias="perPage")
    sort_by: Optional[str] = Field(alias="sortBy")
    filter: Optional["StandingPageFilter"]


class StandingPageFilter(BaseModel):
    id: Optional[str]
    ids: Optional[List[Optional[str]]]
    search: Optional["PaginationSearchType"]


class StationFilter(BaseModel):
    page: Optional[int]
    per_page: Optional[int] = Field(alias="perPage")


class UserLeaguesPaginationQuery(BaseModel):
    page: Optional[int]
    per_page: Optional[int] = Field(alias="perPage")
    sort_by: Optional[str] = Field(alias="sortBy")
    filter: Optional["UserLeaguesPaginationFilter"]


class UserLeaguesPaginationFilter(BaseModel):
    videogame_id: Optional[List[Optional[str]]] = Field(alias="videogameId")
    upcoming: Optional[bool]
    past: Optional[bool]
    search: Optional["PaginationSearchType"]


class UserTournamentsPaginationQuery(BaseModel):
    page: Optional[int]
    per_page: Optional[int] = Field(alias="perPage")
    sort_by: Optional[str] = Field(alias="sortBy")
    filter: Optional["UserTournamentsPaginationFilter"]


class UserTournamentsPaginationFilter(BaseModel):
    past: Optional[bool]
    upcoming: Optional[bool]
    search: Optional["PaginationSearchType"]
    videogame_id: Optional[List[Optional[str]]] = Field(alias="videogameId")
    tournament_view: Optional[str] = Field(alias="tournamentView")
    exclude_id: Optional[List[Optional[str]]] = Field(alias="excludeId")


class LeagueQuery(BaseModel):
    page: Optional[int]
    per_page: Optional[int] = Field(alias="perPage")
    sort_by: Optional[str] = Field(alias="sortBy")
    filter: Optional["LeaguePageFilter"]
    sort: Optional[TournamentPaginationSort]


class LeaguePageFilter(BaseModel):
    id: Optional[str]
    ids: Optional[List[Optional[str]]]
    owner_id: Optional[str] = Field(alias="ownerId")
    after_date: Optional[datetime] = Field(alias="afterDate")
    before_date: Optional[datetime] = Field(alias="beforeDate")
    computed_updated_at: Optional[datetime] = Field(alias="computedUpdatedAt")
    name: Optional[str]
    is_featured: Optional[bool] = Field(alias="isFeatured")
    has_banner_images: Optional[bool] = Field(alias="hasBannerImages")
    active_shops: Optional[bool] = Field(alias="activeShops")
    past: Optional[bool]
    published: Optional[bool]
    publicly_searchable: Optional[bool] = Field(alias="publiclySearchable")
    upcoming: Optional[bool]
    videogame_ids: Optional[List[Optional[str]]] = Field(alias="videogameIds")


class ShopLevelsQuery(BaseModel):
    page: Optional[int]
    per_page: Optional[int] = Field(alias="perPage")
    sort_by: Optional[str] = Field(alias="sortBy")


class ShopOrderMessagesQuery(BaseModel):
    page: Optional[int]
    per_page: Optional[int] = Field(alias="perPage")
    sort_by: Optional[str] = Field(alias="sortBy")


class TournamentQuery(BaseModel):
    page: Optional[int]
    per_page: Optional[int] = Field(alias="perPage")
    sort_by: Optional[str] = Field(alias="sortBy")
    filter: Optional["TournamentPageFilter"]
    sort: Optional[TournamentPaginationSort]


class TournamentPageFilter(BaseModel):
    id: Optional[str]
    ids: Optional[List[Optional[str]]]
    owner_id: Optional[str] = Field(alias="ownerId")
    is_current_user_admin: Optional[bool] = Field(alias="isCurrentUserAdmin")
    country_code: Optional[str] = Field(alias="countryCode")
    addr_state: Optional[str] = Field(alias="addrState")
    location: Optional["TournamentLocationFilter"]
    after_date: Optional[datetime] = Field(alias="afterDate")
    before_date: Optional[datetime] = Field(alias="beforeDate")
    computed_updated_at: Optional[datetime] = Field(alias="computedUpdatedAt")
    name: Optional[str]
    venue_name: Optional[str] = Field(alias="venueName")
    is_featured: Optional[bool] = Field(alias="isFeatured")
    is_league: Optional[bool] = Field(alias="isLeague")
    has_banner_images: Optional[bool] = Field(alias="hasBannerImages")
    active_shops: Optional[bool] = Field(alias="activeShops")
    reg_open: Optional[bool] = Field(alias="regOpen")
    past: Optional[bool]
    published: Optional[bool]
    publicly_searchable: Optional[bool] = Field(alias="publiclySearchable")
    staff_picks: Optional[bool] = Field(alias="staffPicks")
    has_online_events: Optional[bool] = Field(alias="hasOnlineEvents")
    top_games: Optional["TopGameFilter"] = Field(alias="topGames")
    upcoming: Optional[bool]
    videogame_ids: Optional[List[Optional[str]]] = Field(alias="videogameIds")
    sort_by_score: Optional[bool] = Field(alias="sortByScore")


class TournamentLocationFilter(BaseModel):
    distance_from: Optional[str] = Field(alias="distanceFrom")
    distance: Optional[str]


class TopGameFilter(BaseModel):
    game_nums: Optional[List[Optional[int]]] = Field(alias="gameNums")


class VideogameQuery(BaseModel):
    page: Optional[int]
    per_page: Optional[int] = Field(alias="perPage")
    sort_by: Optional[str] = Field(alias="sortBy")
    filter: Optional["VideogamePageFilter"]


class VideogamePageFilter(BaseModel):
    id: Optional[List[Optional[str]]]
    name: Optional[str]
    for_user: Optional[str] = Field(alias="forUser")


class ResolveConflictsOptions(BaseModel):
    locked_seeds: Optional[List[Optional["ResolveConflictsLockedSeedConfig"]]] = Field(
        alias="lockedSeeds"
    )


class ResolveConflictsLockedSeedConfig(BaseModel):
    event_id: str = Field(alias="eventId")
    num_seeds: int = Field(alias="numSeeds")


class PhaseGroupUpdateInput(BaseModel):
    phase_group_id: str = Field(alias="phaseGroupId")
    station_id: Optional[str] = Field(alias="stationId")
    wave_id: Optional[str] = Field(alias="waveId")


class UpdatePhaseSeedInfo(BaseModel):
    seed_id: str = Field(alias="seedId")
    seed_num: str = Field(alias="seedNum")
    phase_group_id: Optional[str] = Field(alias="phaseGroupId")


class UpdatePhaseSeedingOptions(BaseModel):
    strict_mode: Optional[bool] = Field(alias="strictMode")


class PhaseUpsertInput(BaseModel):
    name: Optional[str]
    group_count: Optional[int] = Field(alias="groupCount")
    bracket_type: Optional[BracketType] = Field(alias="bracketType")


class StationUpsertInput(BaseModel):
    number: int
    cluster_id: Optional[str] = Field(alias="clusterId")


class WaveUpsertInput(BaseModel):
    identifier: str
    start_at: datetime = Field(alias="startAt")
    end_at: datetime = Field(alias="endAt")


UserEventsPaginationQuery.update_forward_refs()
UserEventsPaginationFilter.update_forward_refs()
LocationFilterType.update_forward_refs()
PaginationSearchType.update_forward_refs()
EventEntrantPageQuery.update_forward_refs()
EventEntrantPageQueryFilter.update_forward_refs()
SetFilters.update_forward_refs()
SetFilterLocation.update_forward_refs()
SetFilterLocationDistanceFrom.update_forward_refs()
SetFilterLocationDistanceFromPoint.update_forward_refs()
EventFilter.update_forward_refs()
ParticipantPaginationQuery.update_forward_refs()
ParticipantPageFilter.update_forward_refs()
TeamPaginationQuery.update_forward_refs()
TeamPaginationFilter.update_forward_refs()
SeedPaginationQuery.update_forward_refs()
SeedPageFilter.update_forward_refs()
PhaseGroupPageQuery.update_forward_refs()
PhaseGroupPageQueryFilter.update_forward_refs()
StandingGroupStandingPageFilter.update_forward_refs()
EventOwnersQuery.update_forward_refs()
LeagueEventsQuery.update_forward_refs()
LeagueEventsFilter.update_forward_refs()
StandingPaginationQuery.update_forward_refs()
StandingPageFilter.update_forward_refs()
StationFilter.update_forward_refs()
UserLeaguesPaginationQuery.update_forward_refs()
UserLeaguesPaginationFilter.update_forward_refs()
UserTournamentsPaginationQuery.update_forward_refs()
UserTournamentsPaginationFilter.update_forward_refs()
LeagueQuery.update_forward_refs()
LeaguePageFilter.update_forward_refs()
ShopLevelsQuery.update_forward_refs()
ShopOrderMessagesQuery.update_forward_refs()
TournamentQuery.update_forward_refs()
TournamentPageFilter.update_forward_refs()
TournamentLocationFilter.update_forward_refs()
TopGameFilter.update_forward_refs()
VideogameQuery.update_forward_refs()
VideogamePageFilter.update_forward_refs()
ResolveConflictsOptions.update_forward_refs()
ResolveConflictsLockedSeedConfig.update_forward_refs()
PhaseGroupUpdateInput.update_forward_refs()
UpdatePhaseSeedInfo.update_forward_refs()
UpdatePhaseSeedingOptions.update_forward_refs()
PhaseUpsertInput.update_forward_refs()
StationUpsertInput.update_forward_refs()
WaveUpsertInput.update_forward_refs()
