"""
Binary -> Oktal
+ langkah-langkah
"""
import re

bil_biner = "11001111"

print("SOAL : ")
print(f"{bil_biner}(2) = ...(8)\n")
print("JAWABAN :")

# Step-1
print("""Untuk melakukan konversi dari biner ke oktal, perlu diketahui bahwa setiap digit bilangan oktal sama dengan 3 digit bilangan biner. Kelompokkan bilangan biner setiap 3 digit, dimulai dari kanan.

Apabila set paling kiri tidak berjumlah 3, maka tambahkan angka 0 sampai set tersebut berjumlah 3 digit.
""")

# 11001111 (2) = 011 001 111
j_digit = len(bil_biner) % 3
b_biner2 = ("0"*(3-j_digit)) + bil_biner
b_biner_split = re.findall("...", b_biner2)

print(f"{bil_biner}(2) = {' '.join(b_biner_split)}\n")

# Step-2
print("Setelah itu konversikan setiap set ke bilangan desimal.")

# Konversi ke bilangan desimal
s_urutan = 1
ar_oktal = []
for s in b_biner_split[::-1]:
	print(f"Set/Kelompok Ke-{s_urutan}")

	n = 0
	bil_desimal = 0
	for d in s[::-1]:
		dd = int(d) * (2**n)
		bil_desimal += dd

		print(f"{d} x 2^{n} = {dd}")
		n += 1

	print(f"Digit Ke-{s_urutan} = {bil_desimal}\n")
	ar_oktal.append( str(bil_desimal) )
	s_urutan += 1

# Hasil
print("Hasil konversi Bilangan Biner ke Oktal :")
bil_oktal = ''.join(ar_oktal[::-1])
print(f"Oktal = {bil_oktal}")
print(f"{bil_biner}(2) = {bil_oktal}(8)\n")
