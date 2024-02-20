import urllib.parse

# Input data
input_str = "http = sh-jp-cn2-x3.aooo.nl:31081,username=sarkrui,password=Sark1995,fast-open=false, udp-relay=false, tag=香港高校 x3 IEPL II"

# Parsing input string to extract required components
components = {
    "ip": input_str.split(',')[0].split('=')[1].strip().split(':')[0].strip(),
    "port": input_str.split(',')[0].split('=')[1].strip().split(':')[1].strip(),
    "username": input_str.split(',')[1].split('=')[1].strip(),
    "password": input_str.split(',')[2].split('=')[1].strip(),
    "tag": input_str.split(',')[5].split('=')[1].strip(),
}

# URL encoding the tag
urlencoded_tag = urllib.parse.quote(components["tag"])

# Constructing the output URL
output_url = f"tg://http?server={components['ip']}&port={components['port']}&user={components['username']}&pass={components['password']}&remarks={urlencoded_tag}"

output_url

print(output_url)
