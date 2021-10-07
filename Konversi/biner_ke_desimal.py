"""
Binary -> Decimal
+ langkah-langkah
"""

bil_biner = "11110011"

print("SOAL : ")
print(f"{bil_biner}(2) = ...(10)\n")
print("JAWABAN :")
print("Kalikan setiap digit biner ( dimulai dari kanan atau digit pertama ) dengan 2^N. Dimana N = urutan digit biner - 1.")

bil_desimal = 0
n = 0

ar_dd = []
for d in bil_biner[::-1]:
	dd = int(d) * (2**n)
	bil_desimal += dd

	ar_dd.append( str(dd) )
	print(f"{d} x 2^{n} = {dd}")
	n += 1

print("Jumlahkan hasil perkalian dari setiap digit.")
sum_dd = " + ".join(ar_dd)
print(f"Desimal = {sum_dd}")
print(f"Desimal = {bil_desimal}")
print(f"{bil_biner}(2) = {bil_desimal}(10)\n")
