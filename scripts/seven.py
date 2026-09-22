#num = 0
#for x in range(1,101):
 #   if x % 7 == 0:
 #       print(x)
  #      num += 1
#print(f"1-100内能被7整除的数有{num}个")
nums = [i for i in range(1,101) if i % 7 == 0]
print(nums,len(nums))
