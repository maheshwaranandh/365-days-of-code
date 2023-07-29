# 365-days-of-code
I will be uploading the problem that i solved for the next 365 days

day1:
https://leetcode.com/problems/projection-area-of-3d-shapes/description/
create a 2d loop(i,j)
a=count no of non zero elemnts
b=max in row
c=max in col
ans=a+b+c

day2:
https://leetcode.com/problems/find-the-substring-with-maximum-cost/
create a hashmap with char,int
add the character, value from the given chars,vals to the hashmap
iterate over the string:
use getORDefault : if the character is present in hashmap we will take it , else : we assingn a value 1 to 26 by (charAt(i)-'a'+1)
if cur goes -ve reset the cur to zero , else contiue
ans=max cur value

