from twilio.rest import Client
import urllib.request
import simplejson
feather_dict = {}
bit_dict = {}
fdata = urllib.request.urlopen("https://api.coinmarketcap.com/v1/ticker/feathercoin/?convert=AUD").read()
fdata = fdata.strip()
fdata = fdata.decode("utf-8")
with open('feathercoin.txt', 'w') as file:
    file.write(fdata)
f = open("feathercoin.txt","r")
flines = f.readlines()
f.close()
f = open("feathercoin.txt","w")
for line in flines:
  if "[" not in line and "]" not in line and "{" not in line and "}" not in line:
    f.write(line)
f.close()
with open('feathercoin.txt', 'r') as f:
    for line in f:
        line = line.replace('"', '')
        line = line.replace(',', '')
        a, b = line.split(": ")
        feather_dict[a.strip()] = (b.strip())

bdata = urllib.request.urlopen("https://api.coinmarketcap.com/v1/ticker/bitcoin/?convert=AUD").read()
bdata = bdata.strip()
bdata = bdata.decode("utf-8")
with open('bitcoin.txt', 'w') as file:
    file.write(bdata)
b = open("bitcoin.txt","r")
blines = b.readlines()
b.close()
b = open("bitcoin.txt","w")
for line in blines:
  if "[" not in line and "]" not in line and "{" not in line and "}" not in line:
    b.write(line)
b.close()
with open('bitcoin.txt', 'r') as f:
    for line in f:
        line = line.replace('"', '')
        line = line.replace(',', '')
        c, d = line.split(": ")
        bit_dict[c.strip()] = (d.strip())        

account_sid = "ACb25bceaaf64fd0e3c23dd79cfbf0e4f7"
auth_token = "4a3972facaf98170ebcf690370d72f9a"
client = Client(account_sid, auth_token)

fbalance = 311.58774034 * float(feather_dict['price_aud'])
bitbalance = 0.00567495 * float(bit_dict['price_aud'])
total = fbalance + bitbalance
total = "%.2f" % total

client.api.account.messages.create(
  to="+61475069101",
  from_="+61448549225",
  body="You have approximately $" + str("%.2f" % fbalance) + " in Feathercoin and $" +str("%.2f" % bitbalance) + " in Bitcoin; a total of $" + str(total) + ".")



