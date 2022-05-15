import secrets, time, colorama, random

def spin():
    circle = ['|', '/', '—', '\\']
    for i in range(1, 9):
        for j in circle:
            print('Preparing Resources', j, end='\r')
            time.sleep(.2)
    print('Starting miner...    ')
    time.sleep(1)

colorama.init()
print(colorama.Fore.CYAN)
print(r'''
 ______     __  __     ______   __  __     ______     ______    
/\  ___\   /\ \_\ \   /\  == \ /\ \_\ \   /\  ___\   /\  == \   
\ \ \____  \ \____ \  \ \  _-/ \ \  __ \  \ \  __\   \ \  __<   
 \ \_____\  \/\_____\  \ \_\    \ \_\ \_\  \ \_____\  \ \_\ \_\ 
  \/_____/   \/_____/   \/_/     \/_/\/_/   \/_____/   \/_/ /_/                                                                                                                                            
''')

convert = {"BITCOIN":"BTC","ETHEREUM":"ETH","SOLANA":"SOL","DOGECOIN":"DOGE"}

user = input('Enter your wallet address [this cannot be changed once the program starts so please make sure it is correct]: ')
crypto = ''
while crypto not in list(convert.values()):
    crypto = input('Enter crypto name [BTC, ETH, SOL, DOGE]: ').upper()
    try:
        crypto = convert[crypto]
    except:
        pass

spin()
start = time.time()           

while True:
    end = time.time()
    elapsed = round(end - start, 1)
    bash = secrets.token_hex(32)
    print(f'Mining ({crypto}) for {user} | Hash : {bash} | Elapsed : {elapsed} seconds')
    time.sleep(0.03)