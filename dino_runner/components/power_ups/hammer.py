from .power_up import PowerUp
from dino_runner.utils.constants import HAMMER, HAMMER_TYPE


class Hammers(PowerUp):
    def __init__(self):
        super().__init__ (HAMMER, HAMMER_TYPE)
