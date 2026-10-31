class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:

        if n < 1:
            return True
        
        for i, f in enumerate(flowerbed):
            
            if f == 0:
                left = (i == 0 or flowerbed[i - 1] == 0)
                right = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)

                if left and right:
                    flowerbed[i] = 1
                    n -= 1
                    
                    if n <= 0:
                        return True
        return False
