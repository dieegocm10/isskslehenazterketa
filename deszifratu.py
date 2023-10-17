gordetakoPortzentaiak = {}
kont = {}
portzentaiak = {}
konparatuta = {}
portzentaiakG = {}
letra_aldatuak = {}
def main():
	karakterKop = 0
	esaldiBerria = ""
	jarraitu = True
	gordePortzentaiak()
	esaldia = input("Sartu esaldia: ")
	for karaktere in esaldia:
		if karaktere.isalpha():
			karaktere = karaktere.lower()
			karakterKop += 1
			if karaktere in kont:
				kont[karaktere] += 1
			else:
				kont[karaktere] = 1
	portzentaiak = kalkulatuPortzentaiak(kont,karakterKop)
	konparatuta = portzentaiakKonparatu(gordetakoPortzentaiak, portzentaiak)
	esaldiBerria = esaldiaSortu(esaldia)
	esaldiOna = esaldiBerria
	
	
	while jarraitu == True:
		print(" ")
		print ("Esaldia honako hau da:") 
		print(esaldiBerria)
		erantzuna = " "
		erantzuna = input("Aldaketak egin nahi dituzu? Bai/ez ")
		if erantzuna == "bai" :
			esaldiBerria = aldaketakEgin(esaldiBerria)
			 
		elif erantzuna == "ez":
			jarraitu = False
		else:
			print("Zure erantzuna ez da zuzena, erantzun bai edo ez!")
	print("Amaierako esaldia honako hau da: ", esaldiBerria)
	#print(kont)
	#print(karakterKop, "karaktere daude")	
	#print(portzentaiak)
	#print(portzentaiakG)
	#print(konparatuta)		
			
def gordePortzentaiak():
	gordetakoPortzentaiak["a"] = 11.96
	gordetakoPortzentaiak["b"] = 0.92
	gordetakoPortzentaiak["c"] = 2.92
	gordetakoPortzentaiak["d"] = 6.87
	gordetakoPortzentaiak["e"] = 16.78
	gordetakoPortzentaiak["f"] = 0.52
	gordetakoPortzentaiak["g"] = 0.73
	gordetakoPortzentaiak["h"] = 0.89
	gordetakoPortzentaiak["i"] = 4.15
	gordetakoPortzentaiak["j"] = 0.30
	gordetakoPortzentaiak["k"] = 0.00
	gordetakoPortzentaiak["l"] = 8.37
	gordetakoPortzentaiak["m"] = 2.12
	gordetakoPortzentaiak["n"] = 7.01
	gordetakoPortzentaiak["ñ"] = 0.29
	gordetakoPortzentaiak["o"] = 8.69
	gordetakoPortzentaiak["p"] = 2.776
	gordetakoPortzentaiak["q"] = 1.53
	gordetakoPortzentaiak["r"] = 4.94
	gordetakoPortzentaiak["s"] = 7.88
	gordetakoPortzentaiak["t"] = 3.31
	gordetakoPortzentaiak["u"] = 4.80
	gordetakoPortzentaiak["v"] = 0.39
	gordetakoPortzentaiak["w"] = 0.00
	gordetakoPortzentaiak["x"] = 0.06
	gordetakoPortzentaiak["y"] = 1.54
	gordetakoPortzentaiak["z"] = 0.15
	#print(gordetakoPortzentaiak)
def kalkulatuPortzentaiak(hiztegia, karakterKopurua):
	portzentaia = {}
	for clave, valor in hiztegia.items():
		portzentaia[clave] = valor / karakterKopurua * 100
	portzentaia = hiztegiaOrdenatu(portzentaia)
	return portzentaia

def hiztegiaOrdenatu(hiztegia):
	hiztegiOrdenatua = dict(sorted(hiztegia.items(), key=lambda item: item[1], reverse=True))
	hiztegiOrdenatua = dict(hiztegiOrdenatua)
	return hiztegiOrdenatua
def portzentaiakKonparatu(gordetakoPortzentaiak,nirePortzentaiak):
	gPortzentaiak = hiztegiaOrdenatu(gordetakoPortzentaiak)
	nPortzentaiak = hiztegiaOrdenatu(nirePortzentaiak)	
	for clave_gPortzentaiak, clave_nPortzentaiak in zip(gPortzentaiak.keys(), nPortzentaiak.keys()):
        	letra_aldatuak[clave_nPortzentaiak] = clave_gPortzentaiak
	return letra_aldatuak
def esaldiaSortu(esaldia):
	esaldiB = " "
	for karaktere in esaldia:
		if karaktere.isalpha():
			karaktere = karaktere.lower()
			esaldiB += letra_aldatuak[karaktere]
		else:
			esaldiB += karaktere
	return esaldiB
def aldaketakEgin(esaldia):
	esaldiBerria = ""
	dagoenLetra = input("Ze letra aldatu nahi duzu? -->  ")
	letraBerria = input("Ze letrarekin ordezkatu nahi duzu? -->  " ).swapcase()
	for karaktere in esaldia:
		if karaktere.isalpha() and karaktere == dagoenLetra:
			esaldiBerria += letraBerria
		else:
			esaldiBerria += karaktere
	return esaldiBerria

	
#RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE. AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE.	
	
	
	
	
	
	
	
	
	
	
if __name__ == "__main__": 
	main()
	
