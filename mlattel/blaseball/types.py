from enum import IntEnum, unique
import re

@unique
class EventType(IntEnum):
    LETS_GO = 0
    PLAY_BALL = 1
    INNING_CHANGE = 2
    PITCHER_CHANGE = 3
    STOLEN_BASE = 4
    WALK = 5
    STRIKEOUT = 6
    FLYOUT = 7
    GROUNDOUT = 8
    HOME_RUN = 9
    HIT = 10
    GAME_END_LOG = 11
    NOW_BATTING = 12
    STRIKE = 13
    BALL = 14
    FOUL = 15
    SOLAR_PANELS = 20
    HOME_FIELD_ADVANTAGE = 21
    HIT_BY_PITCH = 22
    PLAYER_SKIPPED = 23
    PARTYING = 24
    STRIKE_ZAPPED = 25
    WEATHER_CHANGE = 26
    MILD_PITCH = 27
    END_OF_INNING = 28
    SITE_TAKEOVER = 29
    BLACK_HOLE = 30
    SUN_2 = 31
    BIRDS_CIRCLE = 33
    MURDER_OF_CROWS = 34
    BIRDS_PECK_FREE = 35
    COFFEE_TRIPLE = 36
    COFFEE_FREE_REFILL = 37
    COFFEE_WIRED_TIRED = 39
    FEEDBACK_BLOCKED = 40
    FEEDBACK_SWAP = 41
    PEANUTS_SUPERALLERGIC = 45
    PEANUTS_ALLERGIC = 47
    REVERB = 48
    REVERB_SHUFFLE = 49
    BLOODDRAIN_SIPHON = 51
    BLOODDRAIN_ACTIVATED = 52
    BLOODDRAIN_BLOCKED = 53
    INCINERATION = 54
    INCINERATION_BLOCKED = 55
    FLAG_PLANTED = 56
    RENOVATION = 57
    LIGHT_SWITCH = 58
    DECREE_PASSED = 59
    BLESSING = 60
    WILL = 61
    FLOODING_SWEEP = 62
    SALMON_RESTART = 63
    POLARITY_SHIFT = 64
    SECRET_BASE_ENTERED = 65
    SECRET_BASE_EXITED = 66
    CONSUMERS_ATTACKED = 67
    ECHO_CHAMBER = 69
    GRIND_RAIL = 70
    TUNNELS_USED = 71
    ALLERGY_CURED = 72
    PEANUTS = 73
    TASTED_THE_INFINITE = 74
    EVENT_HORIZON = 76
    EVENT_HORIZON_AWAITS = 77
    SOLAR_PANELS_START = 78
    SOLAR_PANELS_ABSORB = 79
    TAROT_READING = 81
    EMERGENCY_ALERT = 82
    RETURNED = 84
    OVER_UNDER = 85
    UNDER_OVER = 86
    UNDERSEA = 88
    HOMESICK = 91
    SUPERYUMMY = 92
    PERKS_UP = 93
    EARLBIRD = 96
    LATE_TO_PARTY = 97
    SHAME_DONOR = 99
    MOD_ADDED = 106
    MOD_REMOVED = 107
    MOD_EXPIRED = 108
    PLAYER_ADDED = 109
    PLAYER_SHADOWED = 110
    PLAYER_RETURNED = 111
    PLAYER_REMOVED = 112
    PLAYER_TRADED = 113
    PLAYER_SWAPPED = 114
    PLAYER_RECRUITED = 115
    PLAYER_REPLACED = 116
    PLAYER_UPGRADED = 117
    PLAYER_DOWNGRADED = 118
    PLAYER_REROLLED = 119
    ALLERGIC_REACTION = 122
    MOVE_FAILED = 124
    ENTER_THE_HALL = 125
    EXIT_THE_HALL = 126
    GAINED_ITEM = 127
    LOST_ITEM = 128
    REVERB_SHUFFLE_ALL = 130
    REVERB_SHUFFLE_LINEUP = 131
    REVERB_SHUFFLE_ROTATION = 132
    TEAM_REPLACED = 133
    NEW_CHALLENGER = 135
    PLAYER_SIGNED = 136
    PLAYER_HATCHED = 137
    TEAM_FORMED = 138
    PLAYER_EVOLVED = 139
    TEAM_WON_SERIES = 141
    TEAM_QUALIFIED = 142
    FINAL_STANDINGS = 143
    MOD_CHANGE = 144
    PLAYER_ALTERNATE = 145
    MOD_ADDED_MOD = 146
    MOD_REMOVED_MOD = 147
    MOD_CHANGED_MOD = 148
    NECROMANCY = 149
    PLAYER_ACCEPTED = 150
    DECREE = 151
    WILL_RESULTS = 152
    TEAM_UPDATED = 153
    SHAMED = 154
    SHAME = 155
    SUN_2_WIN = 156
    BLACK_HOLE_UNWIN = 157
    TEAM_ELIMINATED = 158
    TEAM_ADVANCED = 159
    PLAYER_BLOOD_TYPE = 161
    PRESSURE_CHANGE = 165
    LINEUP_SORT = 166
    NUT_BUTTON = 168
    ECHOED = 169
    ECHO_INTO_STATIC = 170
    ECHO_REMOVED_MULTIPLE = 171
    ECHO_ADDED_MULTIPLE = 172
    PSYCHOACOUSTICS = 173
    ECHO_RECEIVER = 174
    INVESTIGATION = 175
    ELECTION_TIDINGS = 176
    GLITTER_CRATE = 177
    MIDDLING = 178
    PLAYER_INCREASED = 179
    PLAYER_DECREASED = 180
    ENTER_CRIME_SCENE = 181
    AMBITIOUS = 182
    UNAMBITIOUS = 183
    COASTING = 184
    ITEM_BROKEN = 185
    ITEM_DAMAGED = 186
    ITEM_REFORGED = 187
    ITEM_REPAIRED = 188
    COMMUNITY_CHEST = 189
    NO_ITEM_SLOT = 190
    FAX_MACHINE = 191
    HOTEL_MOTEL = 192
    PRIZE_MATCH = 193
    GIFT = 194
    SMITHY = 195
    ENTER_THE_VAULT = 196
    TEAM_BLOOD_TYPE = 198
    PLAYER_SOUL = 199
    BEING_ACTION = 201
    PRESEASON = 202
    MOD_RATIFIED = 203
    SMASH = 204
    HYPE_BUILT = 206
    MODERATION = 208
    SCORE = 209
    LEAGUE_MOD_ADDED = 210
    LEAGUE_MOD_REMOVED = 211
    BALLOONS_INFLATED = 213
    WIN = 214
    WIN_POSTSEASON = 215
    GAME_OVER = 216
    SUN_PRESSURE_BUILT = 217
    TUNNELS_FAILED = 218
    TUNNELS_FLED = 219
    TUNNELS_STOLE = 220
    TEAM_WILL_RETURN = 222
    WEATHER_EVENT = 223
    ITEM_ELEMENT = 224
    SUN_SMILED = 226
    VOICEMAIL = 228
    THIEVES_GUILD_STOLE_ITEM = 230
    THIEVES_GUILD_STOLE_PLAYER = 231
    TUMBLEWEED_SOUNDS = 232
    TRADER_TRAITOR = 233
    TRADE_FAILED = 234
    ITEM_TRADED = 236
    CYCLED_OUT = 237
    SNACK_PAYOUT = 238
    BASES_RELOADED = 239
    VAULT_REVEALED = 241
    WEATHER_REPORT = 243
    PLAYER_CHANGED_MULTIPLE = 244
    GAME_CANCELED = 246
    SUPERNOVA = 247
    BLACK_HOLE_AGITATED = 249
    GAME_ENDED = 250
    JAZZ_RIFF = 251
    NIGHT_SHIFT = 252
    TAROT_CARD_CHANGED = 253
    PLAYER_STUCK = 254
    HORSE_POWER = 255
    LEVIL_GLOOD = 256
    VAULT_HORIZON_HALL_DESERT = 257
    COIN_DAMAGED = 259

def guess_event_type(description: str) -> int:
    """
    Since Blaseball's live updates don't contain the convenient event type flag
    that the game feed event objects have, this method attempts to infer the 
    event type of an update based on its description.
    """
    # Lord forgive the things I do
    if re.search('let\'s go!', description, re.IGNORECASE | re.MULTILINE):
        return EventType.LETS_GO
    if re.search('play ball!', description, re.IGNORECASE | re.MULTILINE):
        return EventType.PLAY_BALL
    if re.search(r'(?:top|bottom) of \d+', description, re.IGNORECASE | re.MULTILINE):
        return EventType.INNING_CHANGE
    if re.search('is now pitching', description, re.IGNORECASE | re.MULTILINE):
        return EventType.PITCHER_CHANGE
    if re.search(r'(?:steals|gets caught stealing) \w+ base', description, re.IGNORECASE | re.MULTILINE):
        return EventType.STOLEN_BASE
    if re.search(r'(?:draws a walk|walks to \w+ base|The umpire sends them to \w+ base|is intentionally walked)', description, re.IGNORECASE | re.MULTILINE):
        return EventType.WALK
    if re.search(r'strikes? out (?:looking|swinging|thinking|willingly)', description, re.IGNORECASE | re.MULTILINE):
        return EventType.STRIKEOUT
    if re.search('hit a flyout', description, re.IGNORECASE | re.MULTILINE):
        return EventType.FLYOUT
    if re.search(r'(?:hit a ground out|out at \w+ base|hit into a \w+ play)', description, re.IGNORECASE | re.MULTILINE):
        return EventType.GROUNDOUT
    if re.search(r'hits a (?:(?:solo|\d+-run) home run|grand slam)', description, re.IGNORECASE | re.MULTILINE):
        return EventType.HOME_RUN
    if re.search(r'hits a (?:single|double|triple|quadruple)', description, re.IGNORECASE | re.MULTILINE):
        return EventType.HIT
    if re.search(r'(?:batting for|skipped up to bat)', description, re.IGNORECASE | re.MULTILINE):
        return EventType.NOW_BATTING
    if re.search(r'strike, (?:looking|swinging|flinching)', description, re.IGNORECASE | re.MULTILINE):
        return EventType.STRIKE
    if re.search(r'^ball\.\s+\d+-\d+', description, re.IGNORECASE | re.MULTILINE):
        return EventType.BALL
    if re.search(r'foul balls?.\s+\d+-\d+', description, re.IGNORECASE | re.MULTILINE):
        return EventType.FOUL
    if re.search('runs are overflowing', description, re.IGNORECASE | re.MULTILINE):
        return EventType.SOLAR_PANELS
    if re.search(r'hits .+ with a pitch', description, re.IGNORECASE | re.MULTILINE):
        return EventType.HIT_BY_PITCH
    if re.search(r'is (?:elsewhere|shelled)', description, re.IGNORECASE | re.MULTILINE):
        return EventType.PLAYER_SKIPPED
    if re.search('is partying!', description, re.IGNORECASE | re.MULTILINE):
        return EventType.PARTYING
    if re.search('zaps a strike away', description, re.IGNORECASE | re.MULTILINE):
        return EventType.STRIKE_ZAPPED
    if re.search('the polarity shifted', description, re.IGNORECASE | re.MULTILINE):
        return EventType.POLARITY_SHIFT
    if re.search('throws a mild pitch', description, re.IGNORECASE | re.MULTILINE): # There's no way this won't match up with 5 or 14 first
        return EventType.MILD_PITCH
    if re.search(r'inning \d+ is now an outing', description, re.IGNORECASE | re.MULTILINE):
        return EventType.END_OF_INNING
    if re.search(r'swallow(s|ed) the runs', description, re.IGNORECASE | re.MULTILINE):
        return EventType.BLACK_HOLE
    if re.search('sun 2 smile(s|ed)', description, re.IGNORECASE | re.MULTILINE):
        return EventType.SUN_2
    if re.search(r'birds circle .+ don.t find what they.re looking for', description, re.IGNORECASE | re.MULTILINE):
        return EventType.BIRDS_CIRCLE
    if re.search('a murder of crows', description, re.IGNORECASE | re.MULTILINE):
        return EventType.MURDER_OF_CROWS
    if re.search(r'birds circle .+ pecked .+ free', description, re.IGNORECASE | re.MULTILINE):
        return EventType.BIRDS_PECK_FREE
    if re.search(r'chugs? a third wave of coffee', description, re.IGNORECASE | re.MULTILINE):
        return EventType.COFFEE_TRIPLE
    if re.search(r'is poured over with a .+ roast', description, re.IGNORECASE | re.MULTILINE):
        return EventType.COFFEE_FREE_REFILL
    if re.search(r'is beaned by a .+ roast', description, re.IGNORECASE | re.MULTILINE):
        return EventType.COFFEE_WIRED_TIRED
    if re.search(r'reality begins to flicker.+but .+ resists', description, re.IGNORECASE | re.MULTILINE | re.DOTALL):
        return EventType.FEEDBACK_BLOCKED
    if re.search(r'reality flickers.+switch teams in the flicker', description, re.IGNORECASE | re.MULTILINE | re.DOTALL):
        return EventType.FEEDBACK_SWAP
    if re.search('had a superallergic reaction', description, re.IGNORECASE | re.MULTILINE):
        return EventType.PEANUTS_SUPERALLERGIC
    if re.search('had an allergic reaction', description, re.IGNORECASE | re.MULTILINE):
        return EventType.PEANUTS_ALLERGIC
    if re.search('is now reverberating wildly', description, re.IGNORECASE | re.MULTILINE):
        return EventType.REVERB
    if re.search(r'(were|had (several players|their lineup|their rotation)) shuffled in the reverb', description, re.IGNORECASE | re.MULTILINE):
        return EventType.REVERB_SHUFFLE
    if re.search(r'siphoned some of .+\s .+ ability', description, re.IGNORECASE | re.MULTILINE):
        return EventType.BLOODDRAIN_SIPHON
    if re.search(r's siphon activates', description, re.IGNORECASE | re.MULTILINE):
        return EventType.BLOODDRAIN_ACTIVATED
    if re.search('tried to siphon blood', description, re.IGNORECASE | re.MULTILINE):
        return EventType.BLOODDRAIN_BLOCKED
    if re.search('rogue umpire incinerated', description, re.IGNORECASE | re.MULTILINE):
        return EventType.INCINERATION
    if re.search('rogue umpire tried to incinerate', description, re.IGNORECASE | re.MULTILINE):
        return EventType.INCINERATION_BLOCKED
    if re.search('baserunners are swept from play', description, re.IGNORECASE | re.MULTILINE):
        return EventType.FLOODING_SWEEP
    if re.search('the salmon swim upstream', description, re.IGNORECASE | re.MULTILINE):
        return EventType.SALMON_RESTART
    if re.search('enters the secret base', description, re.IGNORECASE | re.MULTILINE):
        return EventType.SECRET_BASE_ENTERED
    if re.search('exits the secret base', description, re.IGNORECASE | re.MULTILINE):
        return EventType.SECRET_BASE_EXITED
    if re.search(r'(?:consumers attack|a consumer)', description, re.IGNORECASE | re.MULTILINE):
        return EventType.CONSUMERS_ATTACKED
    if re.search(r'is temporarily (reverberat|repeat)ing', description, re.IGNORECASE | re.MULTILINE):
        return EventType.ECHO_CHAMBER
    if re.search('hops on the grind rail', description, re.IGNORECASE | re.MULTILINE):
        return EventType.GRIND_RAIL
    if re.search(r'(?:entered the tunnels|attempted a heist)', description, re.IGNORECASE | re.MULTILINE):
        return EventType.TUNNELS_USED
    if re.search(r'(?:is no longer superallergic|has been cured of their peanut allergy)', description, re.IGNORECASE | re.MULTILINE):
        return EventType.ALLERGY_CURED
    if re.search('tastes the infinite', description, re.IGNORECASE | re.MULTILINE):
        return EventType.TASTED_THE_INFINITE
    if re.search('event horizon activates', description, re.IGNORECASE | re.MULTILINE):
        return EventType.EVENT_HORIZON
    if re.search('the solar panels absorb sun 2.s energy', description, re.IGNORECASE | re.MULTILINE):
        return EventType.SOLAR_PANELS_ABSORB
    if re.search(r'(has )?(returned|rolled back|was pulled back) from elsewhere', description, re.IGNORECASE | re.MULTILINE):
        return EventType.RETURNED
    if re.search(r'over under, (off|on)', description, re.IGNORECASE | re.MULTILINE):
        return EventType.OVER_UNDER
    if re.search(r'under over, (off|on)', description, re.IGNORECASE | re.MULTILINE):
        return EventType.UNDER_OVER
    if re.search('go undersea', description, re.IGNORECASE | re.MULTILINE):
        return EventType.UNDERSEA
    if re.search(r'is (happy to be home|homesick)', description, re.IGNORECASE | re.MULTILINE):
        return EventType.HOMESICK
    if re.search('perks up', description, re.IGNORECASE | re.MULTILINE):
        return EventType.PERKS_UP
    if re.search(r'echo .+ static', description, re.IGNORECASE | re.MULTILINE):
        return EventType.ECHO_INTO_STATIC
    if re.search(r'.+ echoed .+', description, re.IGNORECASE | re.MULTILINE):
        return EventType.ECHOED
    if re.search('psychoacoustics echo', description, re.IGNORECASE | re.MULTILINE):
        return EventType.PSYCHOACOUSTICS
    if re.search(r'echo .+ echo .+ echo', description, re.IGNORECASE | re.MULTILINE):
        return EventType.ECHO_RECEIVER
    if re.search('a shimmering crate descends', description, re.IGNORECASE | re.MULTILINE):
        return EventType.GLITTER_CRATE
    if re.search(r'(is feeling|loses their) ambitio(us|n)', description, re.IGNORECASE | re.MULTILINE):
        return EventType.AMBITIOUS
    if re.search('is feeling unambitious', description, re.IGNORECASE | re.MULTILINE):
        return EventType.UNAMBITIOUS
    if re.search(r'consumers attack.+breaks?', description, re.IGNORECASE | re.MULTILINE | re.DOTALL):
        return EventType.ITEM_BROKEN
    if re.search(r'consumers attack.+damaged', description, re.IGNORECASE | re.MULTILINE | re.DOTALL):
        return EventType.ITEM_DAMAGED
    if re.search('the community chest opens', description, re.IGNORECASE | re.MULTILINE):
        return EventType.COMMUNITY_CHEST
    if re.search('incoming shadow fax', description, re.IGNORECASE | re.MULTILINE):
        return EventType.FAX_MACHINE
    if re.search('hotel motel', description, re.IGNORECASE | re.MULTILINE):
        return EventType.HOTEL_MOTEL
    if re.search('prize match', description, re.IGNORECASE | re.MULTILINE):
        return EventType.PRIZE_MATCH
    if re.search(r'smithy beckons.+repaired', description, re.IGNORECASE | re.MULTILINE | re.DOTALL):
        return EventType.SMITHY
    if re.search(r'.+ entered the vault', description, re.IGNORECASE | re.MULTILINE):
        return EventType.ENTER_THE_VAULT
    if re.search(r'the .+ have a blood type', description, re.IGNORECASE | re.MULTILINE):
        return EventType.TEAM_BLOOD_TYPE
    if re.search('practice moderation', description, re.IGNORECASE | re.MULTILINE):
        return EventType.MODERATION
    if re.search('game over.', description, re.IGNORECASE | re.MULTILINE):
        return EventType.GAME_OVER
    if re.search(r'entered the tunnels.+but didn.t find anything interesting', description, re.IGNORECASE | re.MULTILINE | re.DOTALL):
        return EventType.TUNNELS_FAILED
    if re.search(r'entered the tunnels.+but they were caught', description, re.IGNORECASE | re.MULTILINE | re.DOTALL):
        return EventType.TUNNELS_FLED
    if re.search(r'entered the tunnels.+caught their eye.+stole', description, re.IGNORECASE | re.MULTILINE | re.DOTALL):
        return EventType.TUNNELS_STOLE
    if re.search('sun 30 smiled upon them', description, re.IGNORECASE | re.MULTILINE):
        return EventType.SUN_SMILED
    if re.search('incoming voicemail', description, re.IGNORECASE | re.MULTILINE):
        return EventType.VOICEMAIL
    if re.search(r'stole .+ from .+ and gave it to .+', description, re.IGNORECASE | re.MULTILINE):
        return EventType.THIEVES_GUILD_STOLE_ITEM
    if re.search(r'stole .+ shadows player', description, re.IGNORECASE | re.MULTILINE):
        return EventType.THIEVES_GUILD_STOLE_PLAYER
    if re.search(r'(?:sought out a trade|tried to trade with)', description, re.IGNORECASE | re.MULTILINE):
        return EventType.TRADE_FAILED
    if re.search(r'(?:traitor|trader)? ?traded their .+', description, re.IGNORECASE | re.MULTILINE):
        return EventType.ITEM_TRADED
    if re.search(r'pitcher .+ cycles out', description, re.IGNORECASE | re.MULTILINE):
        return EventType.CYCLED_OUT
    if re.search('reloaded all of the bases', description, re.IGNORECASE | re.MULTILINE):
        return EventType.BASES_RELOADED
    if re.search('a new weather report arrived', description, re.IGNORECASE | re.MULTILINE):
        return EventType.WEATHER_REPORT
    if re.search('game cancelled', description, re.IGNORECASE | re.MULTILINE):
        return EventType.GAME_CANCELED
    if re.search('sun\(sun\) supernova', description, re.IGNORECASE | re.MULTILINE):
        return EventType.SUPERNOVA
    if re.search('black hole became agitated', description, re.IGNORECASE | re.MULTILINE):
        return EventType.BLACK_HOLE_AGITATED
    if re.search(r'were (both )? nullified', description, re.IGNORECASE | re.MULTILINE):
        return EventType.GAME_ENDED
    if re.search('a riff opened', description, re.IGNORECASE | re.MULTILINE):
        return EventType.JAZZ_RIFF
    if re.search('deep darkness took', description, re.IGNORECASE | re.MULTILINE):
        return EventType.NIGHT_SHIFT
    if re.search('became stuck', description, re.IGNORECASE | re.MULTILINE):
        return EventType.PLAYER_STUCK
    if re.search('horse power achieved', description, re.IGNORECASE | re.MULTILINE):
        return EventType.HORSE_POWER
    return None