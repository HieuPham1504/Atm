from datetime import datetime
import time
names = []
users = []
passwds = []
balances = []
now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
f = open("re_bank.csv", encoding="utf-8")
for line in f:
    name, user_acc, passwd, balance = line.split(",")
    names.append(name)
    users.append(user_acc)
    passwds.append(passwd)
    balances.append(balance)
f.close()

def login():
    kick_out = 0
    while kick_out < 3:
        username = input("Nhập số tài khoản: ")
        password = input("Nhập mật khẩu: ")
        if username not in users:
            kick_out += 1
            print("Sai thông tin tài khoản hoặc mật khẩu. \nVui lòng thử lại!")
            continue

        user_index = users.index(username)
        if username in users:
            if password == passwds[user_index]:
                menu(user_index, password)
            else:
                print("NGAN HANG MB BANK")
                print("Xin Chào " + names[user_index])
                print("Vui lòng nhập lại mật khẩu!")
                print("-----------------------------")
                while kick_out < 3:
                    enter_passwd = input("Nhập lại mật khẩu: ")
                    if enter_passwd == passwds[user_index]:
                        menu(user_index, password)
                    else:
                        print("Mật khẩu sai.\nVui lòng nhập lại!")
                        kick_out += 1
                        continue

def menu(user_index, password):
    print(
          "1.Kiểm tra số dư\n" 
          "2.Rút tiền\n" 
          "3.Chuyển tiền\n" 
          "4.Đổi mật khẩu\n" 
          "0.Thoát"
          )
    choice = input("Nhập lựa chọn: ")
    if choice == '1':
        check_balance(user_index, password)
    if choice == '2':
        withdraw_money(user_index, password)
    if choice == '3':
        transfer_money(user_index, password)
    if choice == '4':
        change_password(user_index, password)
    if choice == '0':
        quit()
    else:
        print("Lựa chọn không hợp lệ. Nhập lại!")
        menu(user_index, password)

def second_choice(user_index, password):
    print("--------------------")
    print("1. Giao dịch khác")
    print("0. Thoát")
    while True:
        enter = input("Vui lòng lựa chọn: ")
        if enter == '1':
            menu(user_index, password)
        if enter == '0':
            quit()
        else:
            print("Lựa chọn không đúng. Vui lòng nhập lại!")

def check_balance(user_index, password):
    print(now)
    print("NGAN HANG MB BANK")
    print("Chủ tài khoản: {}\nSố dư: {}".format(names[user_index], balances[user_index]))
    second_choice(user_index, password)

def withdraw_money(user_index, password):
    withdrawing_money = 0
    print(now)
    print("NGAN HANG MB BANK")
    print("Chủ tài khoản: {}\nSố dư: {}".format(names[user_index], balances[user_index]))
    print("--------------------")
    while withdrawing_money < 3:
        try:
            withdraw_mon = int(input("Nhập số tiền cần rút: "))
            if withdraw_mon > int(balances[user_index]):
                print("Tài khoản không đủ để thực hiện giao dịch.\nVui lòng nhập lại.")
                withdrawing_money += 1
                if withdrawing_money == 3:
                    print("Quý khách nhập sai quá 3 lần. Vui lòng đăng nhập lại")
                    time.sleep(3)
                    break
            else:
                print("Giao dịch thành công!")
                balances[user_index] = int(balances[user_index]) - withdraw_mon
                print("Số dư còn lại của bạn là: ", balances[user_index], "VND")
                second_choice(user_index, password)
        except ValueError:
            print("Số tiền không hợp lệ. Nhập lại!")
            withdraw_money(user_index, password)
def transfer_money(user_index, password):
    print("Chủ tài khoản: {}\nSố dư: {}".format(names[user_index], balances[user_index]))
    print("--------------------")
    transfering_acc = input("Nhập số tài khoản cần chuyển: ")
    while True:
        try:
            money = int(input("Nhập số tiền cần chuyển: "))
            if money > int(balances[user_index]):
                print("Số dư không đủ để thực hiện giao dịch.\nNhập lại!")
                continue
            else:
                if transfering_acc not in users:
                    print("Giao dịch thành công!")
                    print("Đã chuyển {}VND đến số tài khoản {}".format(money, transfering_acc))
                    balances[user_index] = int(balances[user_index]) - money
                    print("Số dư còn lại của bạn là: ", balances[user_index], "VND")
                    second_choice(user_index, password)
                else:
                    transfering_acc_index = users.index(transfering_acc)
                    print("Giao dịch thành công!")
                    print("Đã chuyển {}VND đến {}. Số tài khoản {}".format(money, names[transfering_acc_index], transfering_acc))
                    balances[user_index] = int(balances[user_index]) - money
                    print("Số dư còn lại của bạn là: ", balances[user_index], "VND")
                    balances[transfering_acc_index] = int(balances[transfering_acc_index]) + money
                    second_choice(user_index, password)
        except ValueError:
            print("Số tiền không hợp lệ. Nhập lại!")
            continue

def change_password(user_index, password):
    old_pass = input("Nhập mật khẩu cũ: ")
    if old_pass != password:
        print("Sai mật khẩu. Nhập lại!")
        change_password(user_index, password)
    else:
        while True:
            new_pass = input("Nhập mật khẩu mới: ")
            password_authentication = input("Xác thực lại mật khẩu: ")
            if new_pass != password_authentication:
                print("Mật khẩu không trùng khớp")
                continue
            else:
                if new_pass == password:
                    print("Mật khẩu này đã được sử dụng trước đó. Xin thay đổi mật khẩu khác")
                    continue
                else:
                    print("Đã thay đổi mật khẩu thành công")
                    passwds[user_index] = passwds[user_index].replace(passwds[user_index], new_pass)
                    second_choice(user_index, password)
login()
print("-----------------------------------------------------")
print("Ngân hàng tạm thời giữ thẻ do bạn nhập sai mật khẩu 3 lần.\nVui lòng liên hệ nhân viên ngân hàng để được hỗ trợ!")

