import sys

import numpy
import imageio

# OPIS POSTOPKA
# Preberem ime vhodne in izhodne slike
# Odprem vhodno sliko kot numpy array4
# Naredi kopijo vhodne slike
# Za vsak piksel p:
#  - * Izracunaj njegovo k-"okolico" B_k(p) --- shranis jo v nek seznam (ali numpy array)
#  - * Izracunaj mediano elementov tega seznama m
#  - V novi sliki piksel p prepisi z mediano elementov njegove k-okolice m
# Shrani novo sliko z ustreznim imenom

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("Uporaba: python main.py vhodna izhodna")
		sys.exit(1)

	infile = sys.argv[1]
	I = imageio.imread(infile)

	w, h, _ = I.shape
	
	# seznam_rgb = []
	
	for i in range(w):
		for j in range(h):
			# okolica = get_neighborhod(I, i, j, 3)
			print((i, j), " -> ", I[i, j])
			#seznam_rgb.append(I[i, j])
			
	
	print("Dimenzije slike: ", I.shape)

	
	
def get_neighborhod(I, i, j, k):
	
	infile = sys.argv[1]
	I = imageio.imread(infile)
	
	w, h, _ = I.shape
	
	sez = []
   
    for idx in range(i - k, i + k):
	    for jdx in range(j - k, j + k):
			#kdaj smo izven slike
			if idx == i and jdx == j:
				continue
			if i < 0 or i > h - 1 and j < 0 or j > w - 1:
				continue
			
			
            sez.append(I[idx, jdx])
			
			