uang = 100000
command = ""

print("")
print("--SELAMAT DATANG DI MARKET SIMULATOR---")
print("")
print("- help")
print("- quit")
print("")
print("Produk apa yang ingin anda beli?")
print("")
print("""
>. 1. Skincare
>. 2. Snack 
>. 3. Drinks
>. 4. Mie
	""")
print("")
print("Uang anda : 100.000")
print("")

while True:
	command = input(">. ").lower()
	if command == "1": # SOAL 1 
		print("")
		print("--SKINCARE--")
		print("")
		print(">. 1. Mask (Rp.10.000)")
		print(">. 2. Garnier (Rp.20.000)")
		print(">. 3. Citra (Rp.15.000)")
		print("")
		command = input("Apa yang ingin anda beli ? : ").lower()
		if command == "1":
			kembalian = int(uang) - 10000
			print("")
			pass
		elif command == "2":
			kembalian = int(uang) - 20000
			print("")
			pass
		elif command == "3":
			kembalian = int(uang) - 15000			
			print("")
			pass
		else:
			print("Sorry, i don't uderstand that...")

		print("Produk apa yang ingin anda beli?")
		print("")
		print("""
>. 1. Skincare
>. 2. Snack 
>. 3. Drinks
>. 4. Mie
			""")
		print("")
		print(f"Sisa uang anda : {kembalian}")
		print("")

	elif command == "2": # SOAL 2
		print("")
		print("--SNACK--")
		print("")
		print(">. 1. Cheetos (Rp.5.000) ")
		print(">. 2. Nabati (Rp.2.000) ")
		print(">. 3. Piatos (Rp.1.500) ")
		print("")
		command = input("Apa yang ingin anda beli ? : ").lower()
		if command == "1":
			kembalian = int(uang) - 5000
			print("")
			pass
		elif command == "2":
			kembalian = int(uang) - 2000
			print("")
			pass
		elif command == "3":
			kembalian = int(uang) - 1500
			print("")
			pass
		else:
			print("Sorry, i don't uderstand that...")

		print("Produk apa yang ingin anda beli?")
		print("")
		print("""
>. 1. Skincare
>. 2. Snack 
>. 3. Drinks
>. 4. Mie
			""")
		print("")
		print(f"Sisa uang anda : {kembalian}")
		print("")

	elif command == "3": # SOAL 3
		print("")
		print("--DRINKS--")
		print("")
		print(">. 1. Fanta (Rp.5.000) ")
		print(">. 2. Sprit (Rp.5.000) ")
		print(">. 3. Coca Cola (Rp.5.000) ")
		print("")
		command = input("Apa yang ingin anda beli ? : ").lower()
		if command == "1":
			kembalian = int(uang) - 5000
			print("")
			pass
		elif command == "2":
			kembalian = int(uang) - 5000
			print("")
			pass
		elif command == "3":
			kembalian = int(uang) - 5000
			print("")
			pass
		else:
			print("Sorry, i don't uderstand that...")

		print("Produk apa yang ingin anda beli?")
		print("")
		print("""
>. 1. Skincare
>. 2. Snack 
>. 3. Drinks
>. 4. Mie
			""")
		print("")
		print(f"Sisa uang anda : {kembalian}")
		print("")

	elif command == "4": # SOAL 4
		print("")
		print("--MIE--")
		print("")
		print(">. 1. Samyang (Rp.15.000) ")
		print(">. 2. Jajangmyeon (Rp.20.000) ")
		print(">. 3. Ramyeon (Rp.10.000) ")
		print("")
		command = input("Apa yang ingin anda beli ? : ").lower()
		if command == "1":
			kembalian = int(uang) - 15000
			print("")
			pass
		elif command == "2":
			kembalian = int(uang) - 20000
			print("")
			pass
		elif command == "3":
			kembalian = int(uang) - 10000
			print("")
			pass
		else:
			print("Sorry, i don't uderstand that...")
			
	elif command == "quit":
		print("")
		print("Bye, Have a good day ^-^")
		print("")
		print("My SNS")
		print("")
		print("- Instagram : @knightbearr")
		print("- Twitter : @knightbearr")
		print("- Github : @knightbearr")
		print("- Stack Overflow : azmimuis3312@gmail.com")
		print("")		
		break
	elif command == "help":
		print("""
> quit = to quit the Market Simulator
			""")
	else:
		print("I don't uderstand that...")