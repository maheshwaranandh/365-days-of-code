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

day10:
https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/description/
answer should have the alphabets from the given start to end and each alphabets should have the numbers from start to end
create a for loop with range as the numbers representing the 2 alphabets :
  we do it by converting a=0,b=1....z=25
  create a for loop with the given 2 numbers as range:
    create a string with char from the i loop and a num from the j loop
    use chr to get the char from the ascii value
    append this str to a list
ans=list

day11:
https://leetcode.com/problems/valid-sudoku/
we use the collections module to make use of defaultdict of set
by using defaultdict , we dont have to check if it exits before adding an element , it creates an empty set for each key u enter
we have created 3 such dic : rows,cols,subs
create a 2d i,j loop:
  if it is "." : move to next place
  check if the num is present in the rows,cols,subs: return false
  else: add the element to the corresponding row,col,sub

if the loop completes: no invalid
return true
  
day12:
https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/
convert string to integer list
i=0
for each number in that list:
  we check if the count of i in list is equal to the number :
  if not we return false
  else : we increment i by 1
if loop is completed :
return true

day13:
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
keep 2 pointers , 1 at start , 1 at end
create a while loop:
  check if the sum of the current 2 pointing element is target
  if so:
    return their index + 1 (since the answer should be in position type)
  if it is greater than target :
    we must reduce it : so move the end pointer to the left
  else if it is lesser than target "
    we must increase the value : so we move the start pointer to the right

day14:
https://leetcode.com/problems/3sum/description/
sort the given list
for each element in list:
  if the number is same as previous number : skip the iteration
  keep 2 pointers:
  left=the next element , right=the last element
  create a while with condition :l<r
  if the sum of i + l + r is 0:
    and it to answer 
    increase the left pointer until it changes to a new number
  if the sum is less than 0:
    increment  the left pointer by 1
  if sum is greater than 0:
    decrement the right by 1
return ans










