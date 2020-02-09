Prime Numbers in Python: 
========================

**How does the code work?**
  
  In the [video](https://www.youtube.com/watch?v=2p3kwF04xcA&feature=emb_logo), the presenter originally creates a program to test if a number is prime by testing every divisor from 2 to n (not including n since the range function in Python does not include n) and seeing if they have a scenario in which the remainder is zero. If the remainder is zero, it would mean that n is divisible by something other than itself and one and thus, is not prime. 
  
  In the third and final version of the code created, there are essentially three measures taken in order to optimize the algorithim.
  
  1. If n is even but not two, it is automatically known to not be prime and as such, the number would not be tested against all divisors. This would happen in the case of 4, 6, 8, etc.
  2. The for loop in which the algorithim tests n against many divisors has an added "step" section. 
  `for d in range(3, 1 + max_divisor, 2): `
  The range begins at 3 and has a step of 2, meaning that it only uses odd divisors. This is done because in order to see if a even number is not prime, the number only needs to be tested against the number 2. 
  
  It is also important to note that when calculating the range of divisors, the algorithim uses the following functions:
  `max_divisor = math.floor(math.sqrt(n)` and then actually uses this value in `for d in range 3, 1 + max_divisor, 2)`. 
  From here, we can see that the program uses the floor function in order to round the square root down. However, they later add one to ensure that the square root itself is included.
  
  Adding on, the reason that the square root is set as the limit is because after the square root, the factors of a number become repetitive. For example, with the number 64, one can see that after the factor 8, more numbers need not be tested. 
  
**For reference, here is the entire code to this program:**

```.py 
import math 

def is_prime(n): 
# Return 'true' if 'n' is a prime number. False otherwise. 

# If 'n' is 2, it is prime. 
# If 'n' is even and not 2 (ex. 4, 6, 8...), then it is not prime. 
if n == 2: 
  return True
if n > 2 and n % 2 == 0: 
  return False
  
max_divisor = math.floor(math.sqrt(n))
for d in range (3, 1 + max_divisor, 2):
  if n % d == 0:
    return False
  return True 
  
#Substitute 21 with any other number in order to test:
for n in range(1, 21):
  print(n, is_prime(n))
  ```

