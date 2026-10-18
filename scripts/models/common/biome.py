from __future__ import annotations

from enum import Enum


class Biome(Enum):
    mountainous = "mountainous"
    not_mountainous = "-mountainous"
    plains = "plains"
    not_plains = "-plains"
    forest = "forest"
    not_forest = "-forest"
    beach = "beach"
    not_beach = "-beach"
    wetlands = "wetlands"
    not_wetlands = "-wetlands"
    desert = "desert"
    not_desert = "-desert"

    elevated = "elevated"
    not_elevated = "-elevated"
    dark = "dark"
    not_dark = "-dark"
    wet = "wet"
    not_wet = "-wet"
    dry = "dry"
    not_dry = "-dry"
    swampy = "swampy"
    not_swampy = "-swampy"



class BiomeNoExclusions(Enum):
    mountainous = "mountainous"
    plains = "plains"
    forest = "forest"
    beach = "beach"
    wetlands = "wetlands"
    desert = "desert"

    elevated = "elevated"
    dark = "dark"
    wet = "wet"
    dry = "dry"
    swampy = "swampy"
