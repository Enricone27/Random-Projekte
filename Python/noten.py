min = 1
anzahlf =11
erg = min/(min+anzahlf)
note = 4.75
while erg != (note-1)/5 :
	min = min+1
	erg = min/(min+anzahlf)
	
	
print(min+anzahlf)