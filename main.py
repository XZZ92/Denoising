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
	for i in range(w):
		for j in range(h):
			okolica = get_neighborhod(I, i, j, 3)
			print((i, j), " -> ", I[i, j])

	print("Dimenzije slike: ", I.shape)
