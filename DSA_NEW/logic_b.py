#rectangle area  using python from leetcode 
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area1 = abs(ax1 - ax2)*abs(ay1-ay2)
        area2 = abs(bx1-bx2)*abs(by1 - by2)

        overlap_width = max(0, min(ax2, bx2) - max(ax1, bx1))
        overlap_height = max(0, min(ay2, by2) - max(ay1, by1))
        intsec = overlap_width * overlap_height

        return (area1+area2) - intsec 
S = Solution() 
print(S.computeArea(-3,0,3,4,0,-1,9,2))

# Sieve of Eratosthenes question of finding the prime up to n
class solution:
    def sieve(self ,n):
        l =[]
        for i in range(2,n):
            check = True
            for j in range(2,i-1):
                if i%j==0:
                    check = False
                    break
            if check:
                l.append(i)
        return l 
            
s = solution()
print(s.sieve(10))

#some basic problems using the array concept DSA new era

#Leaders in the array
def check_l(n:list)->list:
    l = []
    i = 0
    while i<len(n)-1:
        for j in range(i+1,len(n)):
            if n[i]<n[j]:
                break 
        else:
            l.append(n[i])
        i+=1
    return l
print(check_l([16, 17, 4, 3, 5, 2]))

#check wheather sorted or not 
def sorted_check(l:list)->bool:
    i = 0
    while i<len(l)-1:
        j = i+1
        if l[i]>l[j]:
            return False
        i+=1
    return True 

print(sorted_check([10, 20, 30, 40, 50]))


print("jesus is lord")