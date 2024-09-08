import os

os.system('')

class HealthBar:
    symbol_remaining = ''
    symbol_lost = '_'
    barrier = '|'
    
    def __init__(self, length, entity, is_colored = True, color = ''):
        self.entity = entity
        self.length = length
        self.current_value = entity.health
        self.max_value = entity.max_health
        self.is_colored = is_colored
        self.color = color