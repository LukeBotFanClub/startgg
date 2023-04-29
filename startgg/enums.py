from enum import Enum


class SocialConnectionType(str, Enum):
    TWITTER = "TWITTER"
    TWITCH = "TWITCH"
    DISCORD = "DISCORD"
    MIXER = "MIXER"
    XBOX = "XBOX"


class StreamType(str, Enum):
    TWITCH = "TWITCH"
    MIXER = "MIXER"


class AuthorizationType(str, Enum):
    TWITTER = "TWITTER"
    TWITCH = "TWITCH"
    STEAM = "STEAM"
    DISCORD = "DISCORD"
    XBOX = "XBOX"
    EPIC = "EPIC"
    MIXER = "MIXER"


class SetSortType(str, Enum):
    NONE = "NONE"
    CALL_ORDER = "CALL_ORDER"
    MAGIC = "MAGIC"
    RECENT = "RECENT"
    STANDARD = "STANDARD"
    ROUND = "ROUND"


class StreamSource(str, Enum):
    TWITCH = "TWITCH"
    HITBOX = "HITBOX"
    STREAMME = "STREAMME"
    MIXER = "MIXER"


class ActivityState(str, Enum):
    CREATED = "CREATED"
    ACTIVE = "ACTIVE"
    COMPLETED = "COMPLETED"
    READY = "READY"
    INVALID = "INVALID"
    CALLED = "CALLED"
    QUEUED = "QUEUED"


class TeamMemberStatus(str, Enum):
    UNKNOWN = "UNKNOWN"
    ACCEPTED = "ACCEPTED"
    INVITED = "INVITED"
    REQUEST = "REQUEST"
    ALUM = "ALUM"
    HIATUS = "HIATUS"
    OPEN_SPOT = "OPEN_SPOT"


class TeamMemberType(str, Enum):
    PLAYER = "PLAYER"
    STAFF = "STAFF"


class BracketType(str, Enum):
    SINGLE_ELIMINATION = "SINGLE_ELIMINATION"
    DOUBLE_ELIMINATION = "DOUBLE_ELIMINATION"
    ROUND_ROBIN = "ROUND_ROBIN"
    SWISS = "SWISS"
    EXHIBITION = "EXHIBITION"
    CUSTOM_SCHEDULE = "CUSTOM_SCHEDULE"
    MATCHMAKING = "MATCHMAKING"
    ELIMINATION_ROUNDS = "ELIMINATION_ROUNDS"
    RACE = "RACE"
    CIRCUIT = "CIRCUIT"


class GameSelectionType(str, Enum):
    CHARACTER = "CHARACTER"


class TournamentPaginationSort(str, Enum):
    startAt = "startAt"
    endAt = "endAt"
    eventRegistrationClosesAt = "eventRegistrationClosesAt"
    computedUpdatedAt = "computedUpdatedAt"


class Comparator(str, Enum):
    GREATER_THAN = "GREATER_THAN"
    GREATER_THAN_OR_EQUAL = "GREATER_THAN_OR_EQUAL"
    EQUAL = "EQUAL"
    LESS_THAN_OR_EQUAL = "LESS_THAN_OR_EQUAL"
    LESS_THAN = "LESS_THAN"


class MatchConfigVerificationMethod(str, Enum):
    TWITCH = "TWITCH"
    STREAM_ME = "STREAM_ME"
    ANY = "ANY"
    MIXER = "MIXER"
    YOUTUBE = "YOUTUBE"


class RaceLimitMode(str, Enum):
    BEST_ALL = "BEST_ALL"
    FIRST_ALL = "FIRST_ALL"
    PLAYTIME = "PLAYTIME"


class RaceType(str, Enum):
    GOALS = "GOALS"
    TIMED = "TIMED"
