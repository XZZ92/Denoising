import sys

import numpy
import imageio

# OPIS POSTOPKA
# Preberem ime vhodne in izhodne slike
# Odprem vhodno sliko kot numpy array4
# Naredim kopijo vhodne slike
# Za vsak piksel p:
#  - * Izracunam njegovo k-"okolico" B_k(p) --- shranim jo v nek seznam (ali numpy array)
#  - * Izracunam mediano elementov tega seznama m
#  - V novi sliki piksel p prepisem z mediano elementov njegove k-okolice m
# Shranim novo sliko z ustreznim imenom


def get_neighborhood(I, i, j, k):
	
	w, h, _ = I.shape
	
	seznam_okolice = []
	
	for idx in range(i - k, i + k):
		for jdx in range(j - k, j + k):
			#kdaj smo izven slike
			
			if idx < 0 or idx > w - 1 or jdx < 0 or jdx > h - 1:
				continue
			
			seznam_okolice.append((idx, jdx))
			
	return seznam_okolice	
	
	
# def get_geometric_median(I, ???): 

	# for i in range(w):
		# for j in range(h):
			# okolica = get_neighborhod(I, i, j, k)
			
			
	
if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("Uporaba: python main.py vhodna izhodna")
		sys.exit(1)

	infile = sys.argv[1]
	I = imageio.imread(infile)

	w, h, _ = I.shape
	
	
	for i in range(w):
		for j in range(h):
			okolica = get_neighborhood(I, i, j, 3)
			print(okolica)
			#print((i, j), " -> ", I[i, j])
			#mediana = get_geometric_median(???)
			
			
	
	print("Dimenzije slike: ", I.shape)
	

	
	
	

			

	

	
	
	

	
			
			