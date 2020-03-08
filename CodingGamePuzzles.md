Coding Game Practice
====================

**My username for CodingGame is rikio.**

**Comments about my experience:**

These exercises were ___

## Onboarding Puzzle:
```.py
while 1:
    enemy_1 = input()  # name of enemy 1
    dist_1 = int(input())  # distance to enemy 1
    enemy_2 = input()  # name of enemy 2
    dist_2 = int(input())  # distance to enemy 2

    if dist_1 < dist_2:
        print(enemy_1)
    else:
        print(enemy_2)
```

## The Descent:
```.py
import sys
import math

while 1:
    mountain = 0
    max = 0
    for i in range(8):
        mountain_h = int(input()) # represents the height of one mountain, from 9 to 0. Mountain heights are provided from left to right.
        if mountain_h > mountain:
            mountain = mountain_h
            max = i
    print(max)
```

## Power of Thor Episode 1:
```.py
import sys
import math

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    x_diff = initial_tx - light_x
    y_diff = initial_ty - light_y
    x_direction = ''
    y_direction = ''
    
    if x_diff > 0:
        x_direction = 'W'
        initial_tx -= 1
    elif x_diff < 0:
        x_direction = 'E'
        initial_tx += 1
        
    if y_diff > 0:
        y_direction = 'N'
        initial_ty -= 1
    elif y_diff < 0:
        y_direction = 'S'
        initial_ty += 1
    
    # A single line providing the move to be made: N NE E SE S SW W or NW
    print(y_direction + x_direction)
```


