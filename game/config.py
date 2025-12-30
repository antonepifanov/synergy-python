# Настройки игры
GAME_CONFIG = {
   'FIELD_SIZE': {
      'MIN_WIDTH': 10,
      'MAX_WIDTH': 40,
      'MIN_HEIGHT': 8,
      'MAX_HEIGHT': 20,
      'DEFAULT_WIDTH': 20,
      'DEFAULT_HEIGHT': 10
   },
    
   'SCORING': {
      'EXTINGUISH_FIRE': 20,
      'TREE_BURNED': -10,
      'HEAL_COST': 50,
      'UPGRADE_COST': 100
   },
    
   'WEATHER': {
      'SUNNY_PROBABILITY': 70,
      'RAINY_PROBABILITY': 20,
      'STORMY_PROBABILITY': 10,
      'MIN_DURATION': 10,
      'MAX_DURATION': 30
   },
   
   'FIRE': {
      'START_PROBABILITY': 0.1,
      'SPREAD_PROBABILITY': 0.3,
      'BURN_TIME': 5
   },
   
   'PLAYER': {
      'START_LIVES': 3,
      'START_WATER_CAPACITY': 3
   },
   
   'SYMBOLS': {
      'EMPTY': '·',
      'TREE': '🌲',
      'BURNING_TREE': '🔥',
      'BURNED_TREE': '🪵',
      'WATER': '🌊',
      'HELICOPTER': '🚁',
      'HOSPITAL': '🏥',
      'SHOP': '🛒',
      'CLOUD': '☁️',
      'LIGHTNING': '⚡'
   }
}

# Управление
CONTROLS = {
   'UP': 'w',
   'DOWN': 's',
   'LEFT': 'a',
   'RIGHT': 'd',
   'COLLECT_WATER': 'e',
   'EXTINGUISH': 'f',
   'HOSPITAL': 'h',
   'SHOP': 'm',
   'SAVE': 's',
   'LOAD': 'l',
   'QUIT': 'q'
}