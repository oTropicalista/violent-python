import ftplib

def anon_login(hostname, passe):
    ftp = ftplib.FTP(hostname)
    try:
        ftp.login('android', passe)
        print(f'\n[+] {str(hostname)} FTP Anonymous Logon Succeeded')
        return True
    except Exception as e:
        print(f'\n[-] {str(hostname)} FTP Anonymous Logon Failed.')
        print(f'[-] Exception: {e}')
        return False
    finally:
        ftp.quit()

if __name__ == "__main__":
    host = '192.168.0.100'
    passw = 'android'
    anon_login(host, passw)
