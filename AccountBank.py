class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit berhasil. Saldo saat ini: {self.balance}")
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Penarikan berhasil. Saldo saat ini: {self.balance}")
        else:
            print("Saldo tidak mencukupi.")
    
    def check_balance(self):
        print(f"Saldo saat ini: {self.balance}")


# Membuat objek akun bank
account_number = input("Masukkan nomor akun: ")
initial_balance = float(input("Masukkan saldo awal: "))
account = BankAccount(account_number, initial_balance)

# Menu utama
while True:
    print("\n--- Sistem Informasi Bank ---")
    print("1. Setoran")
    print("2. Penarikan")
    print("3. Cek Saldo")
    print("0. Keluar")

    choice = input("Pilih menu: ")

    if choice == "1":
        amount = float(input("Masukkan jumlah setoran: "))
        account.deposit(amount)
    elif choice == "2":
        amount = float(input("Masukkan jumlah penarikan: "))
        account.withdraw(amount)
    elif choice == "3":
        account.check_balance()
    elif choice == "0":
        print("Terima kasih. Sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

