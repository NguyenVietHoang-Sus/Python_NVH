def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]

def kiem_tra_palindrome(chuoi):
    return chuoi[::-1] == chuoi

def chuan_hoa_ho_ten(chuoi):
    return " ".join(chuoi.split()).title()

def uscln(a, b):
    while b!= 0:
        a, b = b, a % b
    return a

def kiem_tra_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True