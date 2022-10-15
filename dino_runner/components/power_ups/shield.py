from dino_runner.utils.constants import SHIELD, SHIELD_TYPE
from .power_up import PowerUp

class Shields(PowerUp):
    def __init__(self):
        super().__init__(SHIELD, SHIELD_TYPE)