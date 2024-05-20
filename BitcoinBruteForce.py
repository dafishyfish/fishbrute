from bit.format import bytes_to_wif, public_key_to_address ,public_key_to_segwit_address
from bit.crypto import ECPrivateKey
from discord import Webhook, RequestsWebhookAdapter
import sys
import os
from datetime import datetime
from datetime import timedelta
print("\u001b[32;1m"+"""
  ____  _ _            _       
 | __ )(_) |_ ___ ___ (_)_ __  
 |  _ \| | __/ __/ _ \| | '_ \ 
 | |_) | | || (_| (_) | | | | |
 |____/|_|\__\___\___/|_|_| |_|
""")
print("""
  ____             _        __                    
 | __ ) _ __ _   _| |_ ___ / _| ___  _ __ ___ ___ 
 |  _ \| '__| | | | __/ _ \ |_ / _ \| '__/ __/ _ |
 | |_) | |  | |_| | ||  __/  _| (_) | | | (_|  __/
 |____/|_|   \__,_|\__\___|_|  \___/|_|  \___\___|
                                                  
""")
WriteWallet = ""
while WriteWallet == "":
    WriteWallet = input("\u001b[35;1m"+"Write Found Wallet Address?(Yes/No) "+"\u001b[31;1m"+"(Significantly Affect Performance): "+"\u001b[37;1m")
    if any(WriteWallet.lower() == f for f in ["yes", 'y']):
        WriteWallet = True
    elif any(WriteWallet.lower() == f for f in ['no', 'n']):
        WriteWallet = False
    else:
        print("\u001b[31;1mPlease enter yes or no")   
        WriteWallet = ""
webhook = ""
while webhook == "":
    try:
        webhook = Webhook.from_url(str(input("\u001b[35;1m"+"Webhook: "+"\u001b[37;1m")), adapter=RequestsWebhookAdapter())
        print("\u001b[32;1m"+"Successfully Connected"+"\n")
    except:
        webhook = ""
        print("\u001b[31;1m"+"Wrong Webhook Link!"+"\n")
print("Receiving Target Wallets...")
TargetWallets = open(str(os.path.dirname(__file__))+"\\TargetWallets.txt", "r")
ListOfTargetWallets = [(x.rstrip()).lower() for x in TargetWallets.readlines()]
TargetWallets.close()
sys.stdout.write("\033[F")
print("\u001b[32;1mTotal\u001b[37;1m",len(ListOfTargetWallets),"\u001b[32;1mWallet Is Target")
TotalFoundCount=0
FoundWalletInSecond = 0
print("Starting!!!")
s = set(ListOfTargetWallets)
ListOfTargetWallets = []
WriteTime = datetime.now() + timedelta(seconds=1)
if(WriteWallet == False):
    while True:
        privkey = ECPrivateKey()
        wif = bytes_to_wif(privkey.secret, compressed=True)
        PublicKey = privkey.public_key.format()
        LegacyAddress = public_key_to_address(PublicKey)
        SegwitAddress = public_key_to_segwit_address(PublicKey)
        if LegacyAddress.lower() in s:
            webhook.send("Found Wallet: "+str(LegacyAddress)+"\n"+"Secret Key: "+str(wif))
        if SegwitAddress.lower() in s:
            webhook.send("Found Wallet: "+str(SegwitAddress)+"\n"+"Secret Key: "+str(wif))
        if datetime.now() > WriteTime:
            TotalFoundCount += FoundWalletInSecond
            print("\u001b[37;1m"+str(FoundWalletInSecond),"\u001b[31;1mWallet/Second \u001b[35;1mTotal Found Wallet Count:\u001b[37;1m",TotalFoundCount)
            WriteTime = datetime.now() + timedelta(seconds=1)
            FoundWalletInSecond = 0
        else:
            FoundWalletInSecond +=1
else:
    while True:
        privkey = ECPrivateKey()
        wif = bytes_to_wif(privkey.secret, compressed=True)
        PublicKey = privkey.public_key.format()
        LegacyAddress = public_key_to_address(PublicKey)
        SegwitAddress = public_key_to_segwit_address(PublicKey)
        if LegacyAddress.lower() in s:
            webhook.send("Found Wallet: "+str(LegacyAddress)+"\n"+"Secret Key: "+str(wif))
        if SegwitAddress.lower() in s:
            webhook.send("Found Wallet: "+str(SegwitAddress)+"\n"+"Secret Key: "+str(wif))
        FoundWalletInSecond +=1
        print("\u001b[35;1mSecret Key: \u001b[37;1m"+str(wif)+" \u001b[35;1mWallet Address: \u001b[37;1m"+str(LegacyAddress)+"\u001b[31;1m Total Found: \u001b[37;1m"+str(FoundWalletInSecond))