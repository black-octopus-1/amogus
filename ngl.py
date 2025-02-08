import random
import string
import requests
from colorama import Fore, Style, init

init(True)

t = Style.BRIGHT
r = Fore.RED
b = Fore.BLUE
y = Fore.YELLOW
g = Fore.GREEN
v = Fore.CYAN
gr = Fore.WHITE
cu = Fore.LIGHTMAGENTA_EX
vx =Fore.LIGHTCYAN_EX

logo = f"""{vx}{t}
                                                                              
  _|_|_|  _|_|_|      _|_|    _|      _|      _|      _|    _|_|_|  _|        
_|        _|    _|  _|    _|  _|_|  _|_|      _|_|    _|  _|        _|        
  _|_|    _|_|_|    _|_|_|_|  _|  _|  _|      _|  _|  _|  _|  _|_|  _|        
      _|  _|        _|    _|  _|      _|      _|    _|_|  _|    _|  _|        
_|_|_|    _|        _|    _|  _|      _|      _|      _|    _|_|_|  _|_|_|_|  
                                                                              
                                                                              
                                                                              """

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Linux; Android 10; SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; Nexus 5 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
]

def generate_custom_uuid():
    chars = string.hexdigits.lower()[:16]
    sections = [8, 4, 4, 4, 12]
    uuid_parts = [''.join(random.choices(chars, k=length)) for length in sections]
    return '-'.join(uuid_parts)
    
print(f"""\n{logo}""")
nama = input(f"{t}{cu}Nama: ")
pes = input(f"{t}{v}Pesan: ")
jum = int(input(f"{t}{b}Jumlah: "))

# Generate User-Agent dan UUID
ua = random.choice(user_agents)
device_id = generate_custom_uuid()

# Header HTTP
headers = {
    "Host": "ngl.link",
    "content-length": "100",
    "sec-ch-ua-platform": "Android",
    "x-requested-with": "XMLHttpRequest",
    "user-agent": ua,
    "accept": "*/*",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "sec-ch-ua-mobile": "?1",
    "origin": "https://ngl.link",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": f"https://ngl.link/{nama}",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
}

# Data yang dikirim
data = {
    "username": nama,
    "question": pes,
    "deviceId": device_id,
    "gameSlug": "",
    "referrer": ""
}
for i in range(jum):
    req = requests.post("https://ngl.link/api/submit", headers=headers, data=data)
    
# Mengecek status code
    if req.status_code == 200:
        print(f"{g}{t}Berhasil Terkirim !")
    else:
        print(f"{r}Gagal : {req.status_code}")
        