class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        n1=ord(coordinates[0])-96
        n2=int(coordinates[1])
        if n1%2==n2%2:
            return False
        else:
            return True
