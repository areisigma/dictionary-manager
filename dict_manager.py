import sys
import os
import string

path = '/usr/share/wordlists/Pl/polish-dictionary/dist/pl.txt'
#path = 'test.txt'
pathout = 'out2.txt'
pathnum = 'numbers.txt'

#allowed_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'q', 'p', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ']
blocked_chars = ['ą', 'ć', 'ę', 'ł', 'ń', 'ó', 'ś', 'ź', 'ż']

pl_file = open(path, 'r')
new_file = open(pathout, 'w')

def file_length(fname):
	with open(fname) as f:
		for i, l in enumerate(f):
			pass
		return i + 1

def fread(file):
	x = file.readline()
	print('[DEBUG] Reading line')
	return x

def fwrite(fline):
	print('[+] Writing a matching string -> ' + fline)
#	new_file.write(fline)
	new_file.write(fline)
	new_file.write(fline.capitalize())

def check():
	fline = fread(pl_file)

	if contains(blocked_chars, fline) == False and len(fline) > 6 and len(fline) < 9:
#		fwrite(fline)
		addup(fline)
	else:
		print('[-] Found a wrong string -> ' + fline)

def contains(chars, line):
	for i in range(len(chars)):
		if (chars[i] in line) == True:
			print('[!] Found blocked char -> ' + chars[i])
			return True
	print('[+] Not found any blocked chars')
	return False

def addup(line):
	num_file = open(pathnum, 'r')
	for i in range(file_length(pathnum)):
		fnum = num_file.readline()
		final = line.strip() + fnum.strip() + '\n'
		fwrite(final)
	num_file.close()

def fclose():
	pl_file.close()
	new_file.close()

if __name__ == '__main__':
	file_len = file_length(path)
	print('[DEBUG] Length of file is ' + str(file_len))

	for i in range(file_len):
		check()

	fclose()
