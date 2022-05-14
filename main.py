import ascii_sub 
import time
import examples
with open("program.crz","r")as f:
	p = f.read()
def err(msg,prfx="crash"):
	with open(f"{prfx}{time.time()}.txt","a")as f:
		f.write(msg)
def ex(p,i,a,l,derr):
	eloop = 0
	isCom = 0
	isbrk = 0
	global exec_
	for t in p:
		if isbrk==1:
			if t == "]":isbrk = 0	
			elif a[i] == int(t):
				ex(exec_c,i,a,l,derr)
		if isCom == 0:
			if eloop == 1:
				for i in range(0,int(t)):
					ex(exec_,i,[0 for i in range(by)],l,derr)
				eloop = 0	
			if t == "+":a[i]+= 1;a[i]%=255
			if t == "-":
				a[i]-=1; 
				if a[i]==-1: a[i]=255
			if t == ">":i+=1;i=i%(l+1)
			if t=="<":
				if i==0:i=(l)
				else:i-=1
			if t==".":print(a[i])
			if t==",":a[i]=int(input())%255
			if t=="?":print(i)	
			if t == "/":eloop=1
			if t == "\"": isCom = 1
			#if t == "\"": isCom = 0
			if t == ":":
				print(ascii_sub.ascii[a[i]]) 
				
			if t == "[": isbrk = 1
			if t == ";": 
				print(ascii_sub.ascii[a[i]],end='') 
			if t == "`":
				crsh = ''
				for x in range(len(a)):
					crsh += f"{x}::{a[x]}\n"
					
				err(f"CRASHDUMP:\n {crsh}\n PROGRAM:{p}","dump")
			if t == "~": 
				for it3 in range(len(a)):
					a[it3] = 0
			if t == "#": i=0
			if t not in ["+",'-',"<",",",".","/",">","?","1","2","3","4","5","6","7","8","9","0","\"",":","[","]","`","~","#"] and derr==1:
				print(f"ERROR unknown symbol:{t}")
				crsh = ''
				for x in range(len(a)):
					crsh += f"{x}::{a[x]}\n"
					
				err(f"ERROR unknown symbol:{t}\n CRASHDUMP:\n {crsh}\n PROGRAM:{p}")
				break
		else:
			if t=="\"":isCom=0		
exec_ = ""
exec_c = ""
by = 255
with open("def.crz" , "r")as f:
	e = f.readline()
	for n in range(len(e)):
		if e[n] == "|":
			exec_ = e[:n]
			n+= 1
			by = int(str(e[n]) + str(e[n+1]))
	e2 = f.readline()
	exec_c = e2
a= [0 for i in range(by)];i = 0
de = 0
with open("_.config.crz",'r')as f:
	a_1 = f.read()
	if a_1 == '1':
		de = 1
	if a_1 == "a":
		ex(examples.echo,i,a,255,0)
	if a_1 == "b":
		ex(examples.helloworld,i,a,255,0)	
	else : ds =0	
ex(p,i,a,by,de)
