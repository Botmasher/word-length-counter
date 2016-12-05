# -*- coding: utf-8 -*-

## 	My Latest Results:
## 	lang  		-weight				+weight		
##	EN 			956/6519 = 6.82		2270/6519 = 2.87
## 	DE 			722/6296 = 8.72 	1395/6296 = 4.5
## 	HI 			329/1888 = 5.74 	1289/1888 = 1.47
## 	SK			779/6165 = 7.91 	1163/6165 = 5.3
## 	HU 			1103/9821 = 8.90 	1853/9821 = 5.3
## 	MN 			1074/6808 = 6.34 	1827/6808 = 3.73
## 	EL 		 	943/7182 = 7.62		1965/7182 = 3.66	

language = "English"			# source language name
dbl_bit  = True					# count characters as double-bit (e.g. Greek)
src_file = "EN_src.txt" 		# source filename with clean linguistic data
out_file = "_results.txt"		# filename suffix for logging results
weight_by_frequency = False 	# use freq when calculating avg word length

class Text:
	def __init__ (self, language, src, out, is_weighted, double_bit):
		self.language = language
		self.src = src
		self.out = out
		self.words = {}
		self.weighted = is_weighted
		self.double_bit = double_bit
	
	def output (self):
		with open(self.language+self.out, "w") as f:
			#f.write (self.language+"\n\n")
			total_len = 0.0
			total_words = 0.0
			for w in self.words:
				# calculate length based on single or double-bit
				if (self.double_bit):
					total_len += ( len(w) / 2 )
				else:
					total_len += len(w)
				# calculate word count weight or straight
				if (self.weighted):
					total_words += self.words[w]
				else:
					total_words += 1
				f.write ( w + " :  " + str(self.words[w]) + "\n" )
			f.write ( "\n Total word count :  %s" % (int(total_words)) )
			f.write ( "\n Total character count :  %s" % (int(total_len)) )
			f.write ( "\n Average word length :  %s" % (total_len/total_words) )

	def check_special (self, char):
		puncs = [" ",".","?","!",",",";",":","[","]","(",")","{","}","'","\"","·"]
		signs = ["@","#","&","*","~","—","-","+","=","—","/","\\","|","_","<",">","\n"]
		nums = ["1","2","3","4","5","6","7","8","9","0"]
		if char in puncs or char in signs or char in nums:
			return True
		return False

	def parse_line (self, line):
		w = ""
		for c in line:	
			if self.check_special(c) and w != "":
				# we built a word
				try:
					self.words[w] += 1
				except:
					self.words[w] = 1
				w = ""
			elif self.check_special(c):
				# prev char was also special - keep going
				pass
			else:
				w += c

	def parse_text (self):
		with open (self.src, "r") as f:
			for l in f:
				self.parse_line (l)


t = Text (language, src_file, out_file, weight_by_frequency, dbl_bit)
t.parse_text()
t.output()