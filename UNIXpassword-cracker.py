# Arquivo: UNIXpassword-cracker.py
# Funçao: Quebrar senhas Unix-like
# Autor: Joni
# Data: 11/06

from crypt import crypt

def test_pass(crypt_pass):
    salt = crypt_pass[:2]
    dict_file = open('dicio.txt', 'r')

    for word in dict_file.readlines():
        crypt_word = crypt(word.strip('\n'), salt)
        if crypt_word == crypt_pass:
            print(f'[+] Found Password: {word}\n')
            return

    print('[-] Password not found. \n')
    return


if __name__ == "__main__":
    pass_file = open('passwd.txt') #pega o arquivo com o /etc/passwd
    for line in pass_file.readlines():
        if ":" in line:
            user = line.split(':')[0]
            _crypt_pass = line.split(':')[1].strip('')
            print (f'[*] Cracking password for: {user}')
            test_pass(_crypt_pass)