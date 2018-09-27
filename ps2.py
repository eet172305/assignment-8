k1 = int(input("Enter k1 "))# enter k1
k2 = int(input("Enter k2 "))# enter k2
k3 = int(input("Enter k3 "))# enter k3
name = raw_input("Enter your name: ")
group1 = ['a', 'b','c','d','e','f','g','h','i'] # group 1
group2 = ['j', 'k','l','m','n','o','p','q','r']# group 3
group3 = ['s', 't','u','v','w','x','y','z','_']# group 3
s1=""
s2=""
s3=""
s = ""
# divide strings based on groups
for c in name:
	if c in group1:
    		s1+=c
	elif c in group2:
		s2+=c
	elif c in group3: 
		s3+=c

org1=s1
org2=s2
org3=s3
#rotate strings
s1=s1[-k1:]+s1[:-k1]
#s1=ss1+s1[:-k1]

#rotate strings
s2=s2[-k2:]+s2[:-k2]
#s2=ss2+s2[:-k2]

#rotate strings
s3=s3[-k3:]+s3[:-k3]
#s3=ss3+s3[:-k3]

#final result
result=""
i=0
j=0
k=0
#append strings in final result
for c in name:
	if c in s1:
    		result+=s1[i]
		i=i+1
	elif c in s2:
		result+=s2[j]
		j=j+1
	elif c in s3: 
		result+=s3[k]
		k=k+1
print(result)
