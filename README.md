# Prisoner-Dillema

# Algorithm: Selfish

## Description

This strategy focuses on exploitation while maintaining enough cooperation  
to avoid mutual defection spirals:

- Starts with defection to establish dominance  
- Uses pattern recognition to predict and exploit opponent moves  
- Punishes defection harshly  
- Offers minimal cooperation to maintain score advantage

## Parameters

- **my_history**: List of my previous moves (0 = defect, 1 = cooperate)  
- **opponent_history**: List of opponent's previous moves (0 = defect, 1 = cooperate)  
- **rounds**: Total number of rounds to be played or `None` if unknown

## Returns

- `0` for defection  
- `1` for cooperation
"""


