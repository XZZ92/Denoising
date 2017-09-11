import sys

import numpy
import imageio

import copy

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
	
	
def get_rgb_neighborhood(I, i, j):
	
	okolica1 = get_neighborhood(I, i, j, 3)
	rgb_okolica = []
	
	for element in okolica1:
		rgb = list(I[element])
		rgb_okolica.append(rgb)
	
	return rgb_okolica
		
	
	
	
def get_geometric_median(I, i, j):
    okolica2 = get_rgb_neighborhood(I, i, j)
    okolica2.sort()
    d = len(okolica2)
    if d % 2 == 0:
        prvi = d // 2 - 1
        drugi = d // 2
        return ((float((int(okolica2[prvi][0]) + int(okolica2[drugi][0])) / 2)), 
		float((int(okolica2[prvi][1]) + int(okolica2[drugi][1])) / 2), 
		float((int(okolica2[prvi][2]) + int(okolica2[drugi][2])) / 2))

    else:
        return(float(okolica2[d // 2][0]), float(okolica2[d // 2][1]), float(okolica2[d // 2][2]))

			
			
	
if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("Uporaba: python main.py vhodna izhodna")
		sys.exit(1)

	infile = sys.argv[1]
	I = imageio.imread(infile)

	w, h, _ = I.shape
	
	for i in range(w):
		for j in range(h):
			#print((i, j), " -> ", I[i, j])
			#okolica = get_neighborhood(I, i, j, 3)
			#print(okolica)
			#rgb = get_rgb_neighborhood(I, i, j)
			#print(rgb)
			mediana = get_geometric_median(I, i, j)
			print(mediana)
			
	#print("Dimenzije slike: ", I.shape)		
			