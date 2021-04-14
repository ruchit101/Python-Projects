A = [2200, 2350, 2600, 2130, 2190]
Adic = {'Jan': 2200, 'Feb': 2350, 'March': 2600, 'April': 2130, 'MAy': 2190}
# Q1
print("Feb extra :",+ Adic['Feb'] -Adic['Jan'] )
print(sum(A[:3]))
for i in range(len(A)):
    if A[i]==2000:
        print("Exact 2000")
#
A[3]=A[3]-200
print(A)
