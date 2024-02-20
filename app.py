from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__)

def parse_input(input_str):
    components = {
        "ip": input_str.split(',')[0].split('=')[1].strip().split(':')[0].strip(),
        "port": input_str.split(',')[0].split('=')[1].strip().split(':')[1].strip(),
        "username": input_str.split(',')[1].split('=')[1].strip(),
        "password": input_str.split(',')[2].split('=')[1].strip(),
        "tag": input_str.split(',')[5].split('=')[1].strip(),
    }

    urlencoded_tag = urllib.parse.quote(components["tag"])

    output_url = f"tg://http?server={components['ip']}&port={components['port']}&user={components['username']}&pass={components['password']}&remarks={urlencoded_tag}"
    
    return output_url

@app.route('/', methods=['GET', 'POST'])
def parse_urls():
    output_url = ""
    if request.method == 'POST':
        input_strs = request.form['input_strs']
        lines = input_strs.split('\n')
        output_urls = [parse_input(line) for line in lines if line.strip() != '']
        output_url = " | ".join(output_urls)
    return render_template('url_parser.html', output_url=output_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8010)