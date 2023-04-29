from typing import List, Optional, Union

from .async_base_client import AsyncBaseClient
from .attendee_count import AttendeeCount
from .attendee_count_events import AttendeeCountEvents
from .base_model import UNSET, UnsetType
from .event_entrants import EventEntrants
from .event_sets import EventSets
from .event_standings import EventStandings
from .event_standings_race_format import EventStandingsRaceFormat
from .gamer_tag import GamerTag
from .in_progress_results import InProgressResults
from .in_progress_set import InProgressSet
from .last_result import LastResult
from .league_schedule import LeagueSchedule
from .league_standings import LeagueStandings
from .phase_group_sets import PhaseGroupSets
from .phase_groups_by_phase import PhaseGroupsByPhase
from .phase_seeds import PhaseSeeds
from .phase_seeds_teams import PhaseSeedsTeams
from .phase_sets import PhaseSets
from .pool_seeds import PoolSeeds
from .prefix_search_attendees import PrefixSearchAttendees
from .set import Set
from .set_entrants import SetEntrants
from .sets import Sets
from .sets_at_station import SetsAtStation
from .shop import Shop
from .stream_queue_on_tournament import StreamQueueOnTournament
from .tournaments_by_country import TournamentsByCountry
from .tournaments_by_owner import TournamentsByOwner
from .tournaments_by_proximity import TournamentsByProximity
from .tournaments_by_state import TournamentsByState
from .tournaments_by_videogame import TournamentsByVideogame
from .tournaments_by_videogames import TournamentsByVideogames
from .upcoming import Upcoming


def gql(q: str) -> str:
    return q


class StartGGClient(AsyncBaseClient):
    async def gamer_tag(self, user_id: str) -> GamerTag:
        query = gql("""
            query GamerTag($userId: ID!) {
              user(id: $userId) {
                id
                slug
                player {
                  gamerTag
                }
              }
            }
            """)
        variables: dict[str, object] = {"userId": user_id}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return GamerTag.parse_obj(data)

    async def last_result(
        self, user_id: str, per_page: int, gamer_tag: str
    ) -> LastResult:
        query = gql("""
            query LastResult($userId: ID!, $perPage: Int!, $gamerTag: String!) {
              user(id: $userId) {
                events(query: {perPage: $perPage, page: 1}) {
                  nodes {
                    tournament {
                      name
                      id
                      shortSlug
                    }
                    id
                    name
                    numEntrants
                    state
                    standings(
                      query: {perPage: $perPage, page: 1, filter: {search: {searchString: $gamerTag}}}
                    ) {
                      nodes {
                        entrant {
                          id
                        }
                        placement
                        isFinal
                      }
                    }
                  }
                }
              }
            }
            """)
        variables: dict[str, object] = {
            "userId": user_id,
            "perPage": per_page,
            "gamerTag": gamer_tag,
        }
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return LastResult.parse_obj(data)

    async def upcoming(self, user_id: str, per_page: int, gamer_tag: str) -> Upcoming:
        query = gql("""
            query Upcoming($userId: ID!, $perPage: Int!, $gamerTag: String!) {
              user(id: $userId) {
                tournaments(query: {perPage: $perPage, page: 1, filter: {upcoming: true}}) {
                  nodes {
                    name
                    id
                    shortSlug
                    startAt
                    state
                    events(limit: 3) {
                      id
                      name
                      videogame {
                        id
                      }
                      entrants(query: {filter: {name: $gamerTag}}) {
                        nodes {
                          id
                        }
                      }
                    }
                  }
                }
              }
            }
            """)
        variables: dict[str, object] = {
            "userId": user_id,
            "perPage": per_page,
            "gamerTag": gamer_tag,
        }
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return Upcoming.parse_obj(data)

    async def in_progress_results(
        self, event_id: str, entrant_id: str
    ) -> InProgressResults:
        query = gql("""
            query InProgressResults($event_id: ID!, $entrant_id: ID!) {
              event(id: $event_id) {
                tournament {
                  name
                }
                name
                sets(filters: {entrantIds: [$entrant_id]}) {
                  nodes {
                    fullRoundText
                    displayScore
                    wPlacement
                    lPlacement
                    winnerId
                    round
                  }
                }
              }
            }
            """)
        variables: dict[str, object] = {"event_id": event_id, "entrant_id": entrant_id}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return InProgressResults.parse_obj(data)

    async def event_standings(
        self, event_id: str, page: int, per_page: int
    ) -> EventStandings:
        query = gql("""
            query EventStandings($eventId: ID!, $page: Int!, $perPage: Int!) {
              event(id: $eventId) {
                id
                name
                standings(query: {perPage: $perPage, page: $page}) {
                  nodes {
                    placement
                    entrant {
                      id
                      name
                    }
                  }
                }
              }
            }
            """)
        variables: dict[str, object] = {
            "eventId": event_id,
            "page": page,
            "perPage": per_page,
        }
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return EventStandings.parse_obj(data)

    async def event_standings_race_format(
        self, event_id: str
    ) -> EventStandingsRaceFormat:
        query = gql("""
            query EventStandingsRaceFormat($eventId: ID!) {
              event(id: $eventId) {
                id
                name
                phaseGroups {
                  id
                  seeds(query: {page: 1}) {
                    nodes {
                      id
                      standings(containerType: "groups") {
                        id
                        metadata
                      }
                    }
                  }
                }
              }
            }
            """)
        variables: dict[str, object] = {"eventId": event_id}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return EventStandingsRaceFormat.parse_obj(data)

    async def event_entrants(
        self, event_id: str, page: int, per_page: int
    ) -> EventEntrants:
        query = gql("""
            query EventEntrants($eventId: ID!, $page: Int!, $perPage: Int!) {
              event(id: $eventId) {
                id
                name
                entrants(query: {page: $page, perPage: $perPage}) {
                  pageInfo {
                    total
                    totalPages
                  }
                  nodes {
                    id
                    participants {
                      id
                      gamerTag
                    }
                  }
                }
              }
            }
            """)
        variables: dict[str, object] = {
            "eventId": event_id,
            "page": page,
            "perPage": per_page,
        }
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return EventEntrants.parse_obj(data)

    async def league_schedule(self, league_slug: str) -> LeagueSchedule:
        query = gql("""
            query LeagueSchedule($leagueSlug: String!) {
              league(slug: $leagueSlug) {
                id
                name
                events(query: {page: 1, perPage: 10}) {
                  pageInfo {
                    totalPages
                    total
                  }
                  nodes {
                    id
                    name
                    startAt
                    tournament {
                      id
                      name
                    }
                  }
                }
              }
            }
            """)
        variables: dict[str, object] = {"leagueSlug": league_slug}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return LeagueSchedule.parse_obj(data)

    async def league_standings(self, league_slug: str) -> LeagueStandings:
        query = gql("""
            query LeagueStandings($leagueSlug: String!) {
              league(slug: $leagueSlug) {
                id
                name
                standings(query: {page: 1, perPage: 10}) {
                  pageInfo {
                    totalPages
                    total
                  }
                  nodes {
                    id
                    placement
                    entrant {
                      id
                      name
                    }
                  }
                }
              }
            }
            """)
        variables: dict[str, object] = {"leagueSlug": league_slug}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return LeagueStandings.parse_obj(data)

    async def event_sets(self, event_id: str, page: int, per_page: int) -> EventSets:
        query = gql("""
            query EventSets($eventId: ID!, $page: Int!, $perPage: Int!) {
              event(id: $eventId) {
                id
                name
                sets(page: $page, perPage: $perPage, sortType: STANDARD) {
                  pageInfo {
                    total
                  }
                  nodes {
                    id
                    slots {
                      id
                      entrant {
                        id
                        name
                      }
                    }
                  }
                }
              }
            }
            """)
        variables: dict[str, object] = {
            "eventId": event_id,
            "page": page,
            "perPage": per_page,
        }
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return EventSets.parse_obj(data)

    async def phase_sets(self, phase_id: str, page: int, per_page: int) -> PhaseSets:
        query = gql("""
            query PhaseSets($phaseId: ID!, $page: Int!, $perPage: Int!) {
              phase(id: $phaseId) {
                id
                name
                sets(page: $page, perPage: $perPage, sortType: STANDARD) {
                  pageInfo {
                    total
                  }
                  nodes {
                    id
                    slots {
                      id
                      entrant {
                        id
                        name
                      }
                    }
                  }
                }
              }
            }
            """)
        variables: dict[str, object] = {
            "phaseId": phase_id,
            "page": page,
            "perPage": per_page,
        }
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return PhaseSets.parse_obj(data)

    async def phase_group_sets(
        self, phase_group_id: str, page: int, per_page: int
    ) -> PhaseGroupSets:
        query = gql("""
            query PhaseGroupSets($phaseGroupId: ID!, $page: Int!, $perPage: Int!) {
              phaseGroup(id: $phaseGroupId) {
                id
                displayIdentifier
                sets(page: $page, perPage: $perPage, sortType: STANDARD) {
                  pageInfo {
                    total
                  }
                  nodes {
                    id
                    slots {
                      id
                      entrant {
                        id
                        name
                      }
                    }
                  }
                }
              }
            }
            """)
        variables: dict[str, object] = {
            "phaseGroupId": phase_group_id,
            "page": page,
            "perPage": per_page,
        }
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return PhaseGroupSets.parse_obj(data)

    async def sets_at_station(
        self,
        event_id: str,
        station_numbers: Union[Optional[List[Optional[int]]], UnsetType] = UNSET,
    ) -> SetsAtStation:
        query = gql("""
            query SetsAtStation($eventId: ID!, $stationNumbers: [Int]) {
              event(id: $eventId) {
                id
                name
                sets(page: 1, perPage: 3, filters: {stationNumbers: $stationNumbers}) {
                  nodes {
                    id
                    station {
                      id
                      number
                    }
                    slots {
                      id
                      entrant {
                        id
                        name
                      }
                    }
                  }
                }
              }
            }
            """)
        variables: dict[str, object] = {
            "eventId": event_id,
            "stationNumbers": station_numbers,
        }
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return SetsAtStation.parse_obj(data)

    async def set(self, set_id: str) -> Set:
        query = gql("""
            query set($setId: ID!) {
              set(id: $setId) {
                id
                slots {
                  id
                  standing {
                    id
                    placement
                    stats {
                      score {
                        label
                        value
                      }
                    }
                  }
                }
              }
            }
            """)
        variables: dict[str, object] = {"setId": set_id}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return Set.parse_obj(data)

    async def in_progress_set(self, set_id: str) -> InProgressSet:
        query = gql("""
            query InProgressSet($setId: ID!) {
              set(id: $setId) {
                state
                slots {
                  entrant {
                    name
                  }
                  standing {
                    stats {
                      score {
                        value
                      }
                    }
                  }
                }
              }
            }
            """)
        variables: dict[str, object] = {"setId": set_id}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return InProgressSet.parse_obj(data)

    async def sets(self, player_id: str) -> Sets:
        query = gql("""
            query Sets($playerId: ID!) {
              player(id: $playerId) {
                id
                sets(perPage: 5, page: 10) {
                  nodes {
                    id
                    displayScore
                    event {
                      id
                      name
                      tournament {
                        id
                        name
                      }
                    }
                  }
                }
              }
            }
            """)
        variables: dict[str, object] = {"playerId": player_id}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return Sets.parse_obj(data)

    async def stream_queue_on_tournament(
        self, tourney_slug: str
    ) -> StreamQueueOnTournament:
        query = gql("""
            query StreamQueueOnTournament($tourneySlug: String!) {
              tournament(slug: $tourneySlug) {
                id
                streamQueue {
                  stream {
                    streamSource
                    streamName
                  }
                  sets {
                    id
                  }
                }
              }
            }
            """)
        variables: dict[str, object] = {"tourneySlug": tourney_slug}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return StreamQueueOnTournament.parse_obj(data)

    async def set_entrants(self, set_id: str) -> SetEntrants:
        query = gql("""
            query SetEntrants($setId: ID!) {
              set(id: $setId) {
                id
                slots {
                  id
                  entrant {
                    id
                    name
                    participants {
                      id
                      gamerTag
                      connectedAccounts
                    }
                  }
                }
              }
            }
            """)
        variables: dict[str, object] = {"setId": set_id}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return SetEntrants.parse_obj(data)

    async def phase_groups_by_phase(
        self, phase_id: str, page: int, per_page: int
    ) -> PhaseGroupsByPhase:
        query = gql("""
            query PhaseGroupsByPhase($phaseId: ID!, $page: Int!, $perPage: Int!) {
              phase(id: $phaseId) {
                id
                phaseGroups(query: {page: $page, perPage: $perPage}) {
                  pageInfo {
                    total
                  }
                  nodes {
                    id
                    displayIdentifier
                  }
                }
              }
            }
            """)
        variables: dict[str, object] = {
            "phaseId": phase_id,
            "page": page,
            "perPage": per_page,
        }
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return PhaseGroupsByPhase.parse_obj(data)

    async def phase_seeds(self, phase_id: str, page: int, per_page: int) -> PhaseSeeds:
        query = gql("""
            query PhaseSeeds($phaseId: ID!, $page: Int!, $perPage: Int!) {
              phase(id: $phaseId) {
                id
                seeds(query: {page: $page, perPage: $perPage}) {
                  pageInfo {
                    total
                    totalPages
                  }
                  nodes {
                    id
                    seedNum
                    entrant {
                      id
                      participants {
                        id
                        gamerTag
                      }
                    }
                  }
                }
              }
            }
            """)
        variables: dict[str, object] = {
            "phaseId": phase_id,
            "page": page,
            "perPage": per_page,
        }
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return PhaseSeeds.parse_obj(data)

    async def phase_seeds_teams(
        self, phase_id: str, page: int, per_page: int
    ) -> PhaseSeedsTeams:
        query = gql("""
            query PhaseSeedsTeams($phaseId: ID!, $page: Int!, $perPage: Int!) {
              phase(id: $phaseId) {
                id
                seeds(query: {page: $page, perPage: $perPage}) {
                  pageInfo {
                    total
                    totalPages
                  }
                  nodes {
                    id
                    seedNum
                    entrant {
                      id
                      name
                      participants {
                        id
                        gamerTag
                      }
                    }
                  }
                }
              }
            }
            """)
        variables: dict[str, object] = {
            "phaseId": phase_id,
            "page": page,
            "perPage": per_page,
        }
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return PhaseSeedsTeams.parse_obj(data)

    async def pool_seeds(
        self, phase_group_id: str, page: int, per_page: int
    ) -> PoolSeeds:
        query = gql("""
            query PoolSeeds($phaseGroupId: ID!, $page: Int!, $perPage: Int!) {
              phaseGroup(id: $phaseGroupId) {
                id
                seeds(query: {page: $page, perPage: $perPage}) {
                  pageInfo {
                    total
                  }
                  nodes {
                    entrant {
                      id
                      name
                    }
                  }
                }
              }
            }
            """)
        variables: dict[str, object] = {
            "phaseGroupId": phase_group_id,
            "page": page,
            "perPage": per_page,
        }
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return PoolSeeds.parse_obj(data)

    async def attendee_count(self, tourney_slug: str) -> AttendeeCount:
        query = gql("""
            query AttendeeCount($tourneySlug: String!) {
              tournament(slug: $tourneySlug) {
                id
                name
                participants(query: {}) {
                  pageInfo {
                    total
                  }
                }
              }
            }
            """)
        variables: dict[str, object] = {"tourneySlug": tourney_slug}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return AttendeeCount.parse_obj(data)

    async def attendee_count_events(
        self,
        tourney_slug: str,
        event_ids: Union[Optional[List[Optional[str]]], UnsetType] = UNSET,
    ) -> AttendeeCountEvents:
        query = gql("""
            query AttendeeCountEvents($tourneySlug: String!, $eventIds: [ID]) {
              tournament(slug: $tourneySlug) {
                id
                name
                participants(query: {filter: {eventIds: $eventIds}}) {
                  pageInfo {
                    total
                  }
                }
              }
            }
            """)
        variables: dict[str, object] = {
            "tourneySlug": tourney_slug,
            "eventIds": event_ids,
        }
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return AttendeeCountEvents.parse_obj(data)

    async def tournaments_by_country(
        self, c_code: str, per_page: int
    ) -> TournamentsByCountry:
        query = gql("""
            query TournamentsByCountry($cCode: String!, $perPage: Int!) {
              tournaments(query: {perPage: $perPage, filter: {countryCode: $cCode}}) {
                nodes {
                  id
                  name
                  countryCode
                }
              }
            }
            """)
        variables: dict[str, object] = {"cCode": c_code, "perPage": per_page}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return TournamentsByCountry.parse_obj(data)

    async def tournaments_by_state(
        self, state: str, per_page: Union[Optional[int], UnsetType] = UNSET
    ) -> TournamentsByState:
        query = gql("""
            query TournamentsByState($perPage: Int, $state: String!) {
              tournaments(query: {perPage: $perPage, filter: {addrState: $state}}) {
                nodes {
                  id
                  name
                  addrState
                }
              }
            }
            """)
        variables: dict[str, object] = {"perPage": per_page, "state": state}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return TournamentsByState.parse_obj(data)

    async def tournaments_by_proximity(
        self,
        coordinates: str,
        radius: str,
        per_page: Union[Optional[int], UnsetType] = UNSET,
    ) -> TournamentsByProximity:
        query = gql("""
            query TournamentsByProximity($perPage: Int, $coordinates: String!, $radius: String!) {
              tournaments(
                query: {perPage: $perPage, filter: {location: {distanceFrom: $coordinates, distance: $radius}}}
              ) {
                nodes {
                  id
                  name
                  city
                }
              }
            }
            """)
        variables: dict[str, object] = {
            "perPage": per_page,
            "coordinates": coordinates,
            "radius": radius,
        }
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return TournamentsByProximity.parse_obj(data)

    async def tournaments_by_videogame(
        self, per_page: int, videogame_id: str
    ) -> TournamentsByVideogame:
        query = gql("""
            query TournamentsByVideogame($perPage: Int!, $videogameId: ID!) {
              tournaments(
                query: {perPage: $perPage, page: 1, sortBy: "startAt asc", filter: {past: false, videogameIds: [$videogameId]}}
              ) {
                nodes {
                  id
                  name
                  slug
                }
              }
            }
            """)
        variables: dict[str, object] = {
            "perPage": per_page,
            "videogameId": videogame_id,
        }
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return TournamentsByVideogame.parse_obj(data)

    async def tournaments_by_videogames(
        self,
        per_page: Union[Optional[int], UnsetType] = UNSET,
        videogame_ids: Union[Optional[List[Optional[str]]], UnsetType] = UNSET,
    ) -> TournamentsByVideogames:
        query = gql("""
            query TournamentsByVideogames($perPage: Int, $videogameIds: [ID]) {
              tournaments(
                query: {perPage: $perPage, page: 1, sortBy: "startAt asc", filter: {upcoming: true, videogameIds: $videogameIds}}
              ) {
                nodes {
                  id
                  name
                  slug
                }
              }
            }
            """)
        variables: dict[str, object] = {
            "perPage": per_page,
            "videogameIds": videogame_ids,
        }
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return TournamentsByVideogames.parse_obj(data)

    async def tournaments_by_owner(
        self, per_page: int, owner_id: str
    ) -> TournamentsByOwner:
        query = gql("""
            query TournamentsByOwner($perPage: Int!, $ownerId: ID!) {
              tournaments(query: {perPage: $perPage, filter: {ownerId: $ownerId}}) {
                nodes {
                  id
                  name
                  slug
                }
              }
            }
            """)
        variables: dict[str, object] = {"perPage": per_page, "ownerId": owner_id}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return TournamentsByOwner.parse_obj(data)

    async def prefix_search_attendees(
        self, tourney_slug: str, sponsor: str
    ) -> PrefixSearchAttendees:
        query = gql("""
            query PrefixSearchAttendees($tourneySlug: String!, $sponsor: String!) {
              tournament(slug: $tourneySlug) {
                id
                name
                participants(
                  query: {filter: {search: {fieldsToSearch: ["prefix"], searchString: $sponsor}}}
                ) {
                  nodes {
                    id
                    gamerTag
                  }
                }
              }
            }
            """)
        variables: dict[str, object] = {"tourneySlug": tourney_slug, "sponsor": sponsor}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return PrefixSearchAttendees.parse_obj(data)

    async def shop(self, slug: Union[Optional[str], UnsetType] = UNSET) -> Shop:
        query = gql("""
            query Shop($slug: String) {
              shop(slug: $slug) {
                id
                name
                slug
                messages(query: {page: 1, perPage: 5}) {
                  nodes {
                    total
                    message
                    gamertag
                    name
                  }
                }
                levels(query: {page: 1, perPage: 5}) {
                  nodes {
                    name
                    goalAmount
                    currAmount
                    description
                  }
                }
              }
            }
            """)
        variables: dict[str, object] = {"slug": slug}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return Shop.parse_obj(data)
