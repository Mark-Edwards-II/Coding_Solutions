"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
"""
from typing import List
def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    if flowerbed == [0] and n == 1:
        return True
    i = 0
    while i < len(flowerbed) and n > 0:
    # for i in range(len(flowerbed)):
        if flowerbed[i]==0:
            if i == 0:
                if flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    n-=1
            elif i == len(flowerbed)-1:
                if flowerbed[i-1] == 0:
                    flowerbed[i] = 1
                    n-=1
            else:
                if flowerbed[i+1] == 0 and flowerbed[i-1] == 0:
                    flowerbed[i] = 1
                    n-=1
        i+=1
    if n == 0:
        return True
    return False


def tests() -> None:
    assert canPlaceFlowers(flowerbed = [0,0,1,0,0], n = 1) == True
    assert canPlaceFlowers(flowerbed = [0], n = 1) == True
    assert canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 1) == True
    assert canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 2) == False
    assert canPlaceFlowers(flowerbed = [1,0,0,0,0,1], n = 2) == False
    assert canPlaceFlowers(flowerbed = [0,1,0,1,0,1,0], n = 2) == False
    assert canPlaceFlowers(flowerbed = [0,0,1,0,0,0,1], n = 2) == True
    assert canPlaceFlowers(flowerbed = [0,0,1,0,0,0,1,0,0], n = 3) == True

tests()
# print(canPlaceFlowers(flowerbed = [0,0,1,0,0,0,1,0,0], n = 3))