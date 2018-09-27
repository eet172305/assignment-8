k1 = int(input("Enter k1 "))
k2 = int(input("Enter k2 "))
k3 = int(input("Enter k3 "))
name = raw_input("Enter your name: ")
group1 = ['a', 'b','c','d','e','f','g','h','i']
group2 = ['j', 'k','l','m','n','0','p','q','r']
group3 = ['s', 't','u','v','w','x','y','z','_']
s1=""
s2=""
s3=""
s = ""
for c in name:
	if c in group1:
    		s1+=c
	elif c in group2:
		s2+=c
	elif c in group3: 
		s3+=c

print(s1)
print(s2)
print(s3)
ss1=s1[len(s1)-k1:len(s1)]
s1=ss1+s1[0:len(s1)-k1]

ss2=s2[len(s2)-k2:len(s2)]
s2=ss2+s2[0:len(s2)-k2]

ss3=s3[len(s3)-k3:len(s3)]
s3=ss3+s3[0:len(s3)-k3]

print(s1)
print (s2)
print(s3)

result=""
i=0
j=0
k=0
for c in name:
	if c in group1:
    		result+=s1[i]
		i=i+1
	elif c in group2:
		result+=s2[j]
		j=j+1
	elif c in group3: 
		result+=s3[k]
		k=k+1
print(result)
