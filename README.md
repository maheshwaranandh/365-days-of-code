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

day3:
https://leetcode.com/problems/count-primes/
the no should be less than n:
so if n<=2 : no primes : return 0
create a boolean array of length n with all values as TRUE
assign 0,1 as FALSE
we only traverse till the sqrt(n) to reduce complexity
for each prime value , we encounter , we mark all of its multiples in the given range as FALSE
we start at i*i , since any value less than it will already be marked ,
we stop before n
we move by step value as i (so that we get all the multiples )
Finally the primes are the one's that are still TRUE

day4:
https://leetcode.com/problems/solving-questions-with-brainpower/
define a function , so that we can call it recursively
if i becomes greater than length , we return 0
for every value in questions :
  we have to decide if we want to skip it or answer it
  if we answer it , we can add the points , we must call the fuction after skipping the next brinpower no of questions
  if we skip it , we simply call the next index
  {{we have used @cache --- it will remember the values that we got in the recurcive function , so that it can reuse it if it comes accross the same value again 
    this will reduce the time complexity by a bit}}

day5:
https://leetcode.com/problems/determine-color-of-a-chessboard-square/description/
convert the alphabet into a number : a=1,b=2......
if both are even or both are add :
    BLACK
else:
    WHITE

day6:
https://leetcode.com/problems/sort-the-people/description/
create a dictionary :store heights as keys and names as values
sort the heights array in reverse
assign names[i] as d[heights[i]] : we will get the names in desc order since we have sorted the heights array
ans=names

day7:
https://leetcode.com/problems/merge-strings-alternately/description/
find the word with minimum length
use a for loop and append the letter in ith index of word1 and word 2
finally return the appended string 
along with the rest of the extra characters : word1[i+1:] ,word2[i+1:]

day8:
https://leetcode.com/problems/valid-anagram/description/
if the length of the 2 are not equal : return False
create 2 dictionary : add the charcters and increase their count : use dic.get(s[i],0) (this will take 0 as default value if that character  is not in dic)
iterate over the characters in the dic :
if the count of s is not equal to t : return false
if the loop completes running : all have same count : return true

day9:
https://leetcode.com/problems/group-anagrams/description/
create a dic (use defaultdict(list) to avoid the case where the element is not already present in the list)
for each word:
  create a count list with 26 zero's
  for each character in the word:
    increment the value of that charcter in the count list
    we use ord(c) - ord("a") to get the values 0-25 from the ascii values
  append the string to the key with the same count value
  here we pass it as a tuple , since we cant pass list and tuples are immutable
finally the values of the dictionary is the answer















