# The warmup for 2/12/2020. Trying to determine whether a cheetah or Usain Bolt would win given the distance Bolt is ahead, the remaining distance to the finish, the cheetah's acceleration, and Bolt's speed.

import math

# gathering the inputs
finish = input(int())
distanceBolt = input(int())
cheetahAcc = input(int())
boltSpeed = input(int())

# calculating the time the cheetah would take to cover the distance
cheetahDistance = distanceBolt + finish
cheetahTime = math.sqrt((2 * int(cheetahDistance)) / int(cheetahAcc))

# calculating the time Bolt would take to cover the distance
boltTime = int(finish) / int(boltSpeed)

# seeing which one, the cheetah or Bolt, would finish first
if cheetahTime > boltTime:
    print('Usain Bolt would win because he went {} seconds while the cheetah went {} seconds.'.format(boltTime, cheetahTime))
else:
    print('The cheetah would win because it went {} seconds while Bolt went {} seconds.'.format(cheetahTime, boltTime))
