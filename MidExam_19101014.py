print("========= I MADE MERTA YASA =========")
print("=========      19101014     =========")
print("=========    MID EXAM AI    =========\n")
print("Selamat Datang di ATM BERSAMA")
print("Pilih Option :")
print("1. Check Saldo")
print("2. Tarik Saldo")
print("3. Nabung Uang")
option = int(input("Silahkan Pilih Option :"))
if option == 1:
	print("Saldo Anda Berjumlah Rp.450.000")
elif option == 2:
	print("Saldo Anda Berjumlah Rp.450.000, Mau tarik berapa?")
	print("1. Rp.100.000")
	print("2. Rp.200.000")
	print("3. Rp.450.000")
	saldo_anda = 450000
	option = int(input("Option :"))
	if option == 1:
		hasil = saldo_anda - 100000
		print("Saldo Anda Sekarang Berjumlah : Rp.", hasil)
	elif option == 2:
		hasil2 = saldo_anda - 200000
		print("Saldo Anda Sekarang Berjumlah : Rp.", hasil2)
	elif option == 3:
		hasil3 = saldo_anda - 450000
		print("Saldo Anda Sekarang Berjumlah : Rp.", hasil3)
elif option == 3:
	saldo_anda = 450000
	print("Saldo Anda berjumlah Rp.450.000, Mau Nabung Berapa?")
	option2 = int(input("Masukan Jumlah Uang :"))
	hasil4 = saldo_anda + option2
	print("Jumlah Saldo Anda Sekarang Adalah Rp.", hasil4)
else:
	print("Keyword Anda salah, Mohon coba lagi!")
