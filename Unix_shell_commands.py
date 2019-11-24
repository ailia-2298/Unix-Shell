import os,re 
from colorama import init, Fore, Style
def word_count(user_input):
	f = open(user_input,'r+')
	data = f.read().replace('\n', ' ')
	dataParts = data.split()
	f.close()
	return len(dataParts)

def char_count(user_input):
	f = open(user_input,'r+')
	data = f.read()
	f.close()
	return os.path.getsize(user_input)
	
def line_count(user_input):
	f = open(user_input,'r+')
	count = len(f.readlines())
	f.close()
	return count
	
def wc_command(commandParts):
	i=1
	w_exist,c_exist,l_exist="false","false","false"
	while i<len(commandParts):
		if(commandParts[i]=="-wc" or commandParts[i]=="-cw"):
			c_exist="true"
			w_exist="true"
		elif(commandParts[i]=="-wl" or commandParts[i]=="-lw"):
			l_exist="true"
			w_exist="true"
		elif(commandParts[i]=="-cl" or commandParts[i]=="-lc"):
			l_exist="true"
			c_exist="true"
		elif(commandParts[i]=="-w"):
			w_exist="true"
		elif(commandParts[i]=="-c"):
			c_exist="true"
		elif(commandParts[i]=="-l"):
			l_exist="true"
		elif(commandParts[i]=="-wlc" or commandParts[i]=="-wcl" or commandParts[i]=="-lcw" or commandParts[i]=="-lwc" or commandParts[i]=="-cwl" or commandParts[i]=="-clw"):
			l_exist="true"
			c_exist="true"
			w_exist="true"
		else:
			break
		i+=1
	tl,tc,tw=0,0,0
	for x in range(i,len(commandParts)):
		lc = line_count(commandParts[x])
		tl = tl + lc
		wc = word_count(commandParts[x])
		tw = tw + wc
		cc = char_count(commandParts[x])
		tc = tc + cc
		if(l_exist=="true"):
			print(lc,end="  ")
		if(w_exist=="true"):
			print(wc,end="  ")
		if(c_exist=="true"):
			print(cc,end="  ")
		if(l_exist=="false" and w_exist=="false" and c_exist=="false"):
			print(lc,wc,cc,end=" ")
		print((commandParts[x]))
	if(len(commandParts)-i>1):
		if(l_exist=="true"):
			print(tl,end=" ")
		if(w_exist=="true"):
			print(tw,end=" ")
		if(c_exist=="true"):
			print(tc,end=" ")
		if(l_exist=="false" and w_exist=="false" and c_exist=="false"):
			print(tl,tw,tc,end=" ")
		print("Total")

def ch_color(pattern , datanew):
	for i in range(0, len(datanew)):
		x = datanew[i]
		x = re.sub(r'(%s)'%pattern, Style.BRIGHT + Fore.RED + r'\1' + Fore.RESET + Style.RESET_ALL, x, flags=re.I)
		datanew[i] = x
	return (datanew)

def ptt_ch(pattern):
	if pattern[0] == pattern[-1] == "'":
		pattern = pattern.replace("'", "")
	elif pattern.startswith('"') and pattern.endswith('"'):
		pattern = pattern.replace("\"", "")
	return pattern
	
def lines_of_files(user_input):
	f = open(user_input,'r+')
	data=f.readlines()
	f.close()
	datanew = [x[:-1] for x in data]
	return (datanew)

def print_arr(arr):
	for i in range(0, len(arr)):
		print(arr[i])

def x_grep(pattern,datanew):
	choosen = []
	for i in range(0, len(datanew)):
		if len(pattern) == len(datanew[i]):
			choosen.append(datanew[i])
	return (choosen)

def v_grep(data,datanew):
	choosen = [x for x in data if x not in datanew]
	return (choosen)
	
def i_grep(pattern,datanew):
	choosen = []
	for i in range(0, len(datanew)):
		if re.search(pattern, datanew[i], re.IGNORECASE): 
			choosen.append(datanew[i])
	return (choosen)
		
def sim_grep(pattern,datanew):
	choosen = []
	for i in range(0, len(datanew)):
		if re.search(pattern, datanew[i]): 
			choosen.append(datanew[i])
	return (choosen)	

def grep_command(commandParts):
	i,h_ind,H_ind=1,0,0
	x_exist,v_exist,c_exist,i_exist,h_exist,H_exist="false","false","false","false","false","false"
	while i<len(commandParts):
		if (commandParts[i]=='-x'):
			x_exist="true"
		elif (commandParts[i]=='-v'):
			v_exist="true"
		elif (commandParts[i]=='-c'):
			c_exist="true"
		elif (commandParts[i]=='-i'):
			i_exist="true"
		elif (commandParts[i]=='-h'):
			h_exist="true"
			h_ind=i
		elif (commandParts[i]=='-H'):
			H_exist="true"
			H_ind=i
		else:	
			pattern=ptt_ch(commandParts[i])
			i=i+1
			break;
		i+=1
	show = check_v_or_q(H_ind,h_ind,H_exist,h_exist)
	if show=='-v':
		show='-H'
	elif show=='-q':
		show='-h'
	for x in range(i,len(commandParts)):
		data = lines_of_files(commandParts[x])
		if (i_exist=="true"):
			choosen = i_grep(pattern,data)
		else:
			choosen = sim_grep(pattern,data)
		if (x_exist=="true"):
			choosen = x_grep(pattern,choosen)
		if (v_exist=="true"):
			choosen = v_grep(data,choosen)
		if (c_exist=="true"):
			if(show=='-H'):
				print (Style.DIM + '\33[95m'+ commandParts[x]+":"+'\33[0m'+ Style.RESET_ALL, end = '')
				print (len(choosen))
			elif show=='-h':
				print (len(choosen))
			elif show=='--':
				if(len(commandParts)-i)>1:
					print (commandParts[x]+":",end = '')
				print (len(choosen))
		else:
			for l in range(0, len(choosen)):
				if(show=='-H'):
					print (commandParts[x]+":",end = '')
					if (v_exist=="false"):
						choosen = ch_color(pattern,choosen)
					print(choosen[l])
				elif show=='-h':
					if (v_exist=="false"):
						choosen = ch_color(pattern,choosen)
					print(choosen[l])
				elif show=='--':
					if(len(commandParts)-i)>1:
						print (commandParts[x]+":",end = '')
					if (v_exist=="false"):
						choosen = ch_color(pattern,choosen)
					print(choosen[l])
			

def n_tail(num,user_input):
	if(num<0):
		num = -num
	count = int(num)
	data = lines_of_files(user_input)
	if (len(data) < int(num)):
		count = len(data)
	datanew = data[-count:]
	print_arr(datanew)
	
def c_tail(num,user_input):
	if(num<0):
		num = 0-num
	count = int(num)
	f = open(user_input,'r+')
	data = f.read()
	f.close()
	if (len(data) < int(num)):
		count = len(data)
	print(data[-count:],end='')

def tail_command(commandParts):
	i,pattern,charss = 1, 10, -1
	v_ind,q_ind,c_ind,n_ind=0,0,0,0
	v_exist, q_exist="false","false"
	while i<len(commandParts):
		if (commandParts[i]=='-v'):
			v_exist="true"
			v_ind=i
		elif (commandParts[i]=='-q'):
			q_exist="true"
			q_ind=i
		elif (commandParts[i]=='-n'):
			pattern = int(commandParts[i+1])
			n_ind=i
			i+=1
		elif (commandParts[i]=='-c'):
			charss = int(commandParts[i+1])
			c_ind=i
			i+=1
		else:
			break
		i+=1
	show = check_v_or_q(v_ind,q_ind,v_exist,q_exist)
	if n_ind>0:
		if c_ind>0:
			if n_ind<c_ind:
				c_call(show,i,commandParts,charss)
			else:
				n_call(show,i,commandParts,pattern)
		else:
			n_call(show,i,commandParts,pattern)
	else:
		if c_ind>0:
			c_call(show,i,commandParts,charss)
		else:
			n_call(show,i,commandParts,pattern)

def n_head(num,user_input):
	count = int(num)
	if count<0:
		count = 0-int(num)
		data = lines_of_files(user_input)
		if (len(data) >= count):
			for i in range(0, count):
				print(data[i])
	else:
		data = lines_of_files(user_input)
		if (len(data) < int(num)):
			count = len(data)
		for i in range(0, count):
			print(data[i])
	
def c_head(num,user_input):
	f = open(user_input,'r+')
	data = f.read()
	f.close()
	if(num<0):
		count = 0-int(num)
		if (len(data) >= count):
			print(data[:len(data)-count],end='')
	else:
		count = int(num)
		if (len(data) < int(num)):
			count = len(data)
		for i in range(0, count):
			print(data[i],end='')

def check_v_or_q(v_ind,q_ind,v_exist,q_exist):
	if (v_exist=="true" and q_exist=="true"):
		if v_ind>q_ind:
			return ("-v")
		else:
			return ("-q")
	elif (q_exist=="true" and v_exist=="false"):
		return ("-q")
	elif (v_exist=="true" and q_exist=="false"):
		return ("-v")
	elif (v_exist=="false" and q_exist=="false"):
		return ("--")
			
def n_call(show,i,commandParts,pattern):
	for x in range(i,len(commandParts)):
		if show=="-v":
			print("===> "+commandParts[x]+" <===")
		elif show=="--":
			if ((len(commandParts)-i)>1):
				print("===> "+commandParts[x]+" <===")
		if commandParts[0]=="head":
			n_head(pattern,commandParts[x])
		elif commandParts[0]=="tail":
			n_tail(pattern,commandParts[x])

def c_call(show,i,commandParts,charss):	
	for x in range(i,len(commandParts)):
		if show=="-v":
			print("===> "+commandParts[x]+" <===")
		elif show=="--":
			if ((len(commandParts)-i)>1):
				print("===> "+commandParts[x]+" <===")
		if commandParts[0]=="head":
			c_head(charss,commandParts[x])
		elif commandParts[0]=="tail":
			c_tail(charss,commandParts[x])

def head_command(commandParts):
	i,pattern,charss = 1, 10, -1
	v_ind,q_ind,c_ind,n_ind=0,0,0,0
	v_exist, q_exist="false","false"
	while i<len(commandParts):
		if (commandParts[i]=='-v'):
			v_exist="true"
			v_ind=i
		elif (commandParts[i]=='-q'):
			q_exist="true"
			q_ind=i
		elif (commandParts[i]=='-n'):
			pattern = int(commandParts[i+1])
			n_ind=i
			i+=1
		elif (commandParts[i]=='-c'):
			charss = int(commandParts[i+1])
			c_ind=i
			i+=1
		else:
			break
		i+=1
	show = check_v_or_q(v_ind,q_ind,v_exist,q_exist)
	if n_ind>0:
		if c_ind>0:
			if n_ind<c_ind:
				c_call(show,i,commandParts,charss)
			else:
				n_call(show,i,commandParts,pattern)
		else:
			n_call(show,i,commandParts,pattern)
	else:
		if c_ind>0:
			c_call(show,i,commandParts,charss)
		else:
			n_call(show,i,commandParts,pattern)
	
def help(command):
	print(Fore.BLUE + Style.BRIGHT)
	if command == "wc":
		print("NAME\n\twc - print newline, word, and byte counts for each file\n\nSYNOPSIS\n\twc [OPTIONS]... [FILES]\n")
		print("DESCRIPTION\n\tThe options below may be used to select which counts are printed.\n")
		print("\t-c, --bytes\n\t\tprint the byte counts\n\n\t-l, --lines\n\t\tprint the newline counts\n\n\t-w, --words\n\t\tprint the word counts\n")
	elif command == "grep":
		print("NAME\n\tgrep - print lines matching a pattern\n\nSYNOPSIS\n\tgrep [OPTIONS]... [FILES]\n")
		print("DESCRIPTION\n\tgrep  searches  for  PATTERN in each FILE. By default, grep prints the matching lines.\n")
		print("\tThe options below may be used to match pattern.\n")
		print("\t-i, --ignore-case\n\t\tIgnore case distinctions, so that characters that differ only in case match each other.\n")
		print("\t-v, --invert-match\n\t\tInvert the sense of matching, to select non-matching lines.\n")
		print("\t-x, --line-regexp\n\t\tSelect  only  those  matches  that  exactly match the whole line.\n")
		print("\t-c, --count\n\t\tSuppress normal output; instead print a count of matching lines for each input file.\n")
	elif command == "head":
		print("NAME\n\thead - output the first part of files\n\nSYNOPSIS\n\thead [OPTIONS]... [FILES]...\n")
		print("DESCRIPTION\n\tPrint the first 10 lines of each FILE to standard output.  With more than one FILE, precede each with a header giving the file name.\n")
		print("\tThe options below may be used alone or with combinations.\n")
		print("\t-c, --bytes=[-]NUM\n\t\tprint the first NUM bytes of each file; with the leading '-', print all but the last NUM bytes of each file.\n")
		print("\t-n, --lines=[-]NUM\n\t\tprint the first NUM lines instead of the first 10; with the leading '-', print all but the last NUM lines of each file.\n")
		print("\t-q, --quiet\n\t\tnever print headers giving file names.\n\n\t-v, --verbose\n\t\talways print headers giving file names.\n")
	elif command== "tail":
		print("NAME\n\thead - output the last part of files\n\nSYNOPSIS\n\thead [OPTIONS]... [FILES]...\n")
		print("DESCRIPTION\n\tPrint the last 10 lines of each FILE to standard output.  With more than one FILE, precede each with a header giving the file name.\n")
		print("\tThe options below may be used alone or with combinations.\n")
		print("\t-c, --bytes=[+]NUM\n\t\toutput the last NUM bytes; or use -c +NUM to output starting with byte NUM of each file.\n")
		print("\t--n, --lines=[+]NUM\n\t\toutput the last NUM lines, instead of the last 10; or use -n +NUM to output starting with line NUM.\n")
		print("\t-q, --quiet\n\t\tnever print headers giving file names.\n\n\t-v, --verbose\n\t\talways print headers giving file names.\n")
	elif command == "cd":
		print("NAME\n\tcd - change path\n\nSYNOPSIS\n\tcd [PATH]\n\nDESCRIPTION\n\tChange path of the directory you are currently working in.\n")
	print(Fore.RESET + Style.RESET_ALL)

while True:
	print( Style.BRIGHT + Fore.GREEN + os.getcwd() + "/>" + Fore.RESET + Style.RESET_ALL,end=' ')
	command=input()
	commandParts = command.split(' ')
	if commandParts[0] == "exit":
		break;
	if commandParts[1]=="--help":
			help(commandParts[0])
	else:
		if commandParts[0] == "wc":
			wc_command(commandParts)
		elif commandParts[0] == "grep":
			grep_command(commandParts)
		elif commandParts[0] == "head":
			head_command(commandParts)
		elif commandParts[0] == "tail":
			tail_command(commandParts)
		elif commandParts[0] == "cd":
			os.chdir(os.path.expanduser(commandParts[1]))
		else:
			print ("Wrong command format.")
