from flask import Flask
FAI=Flask(__name__)

@FAI.route('/wish/<name>')
def wish(name):
    return f'<center> hello how r u{name}</center>'


if __name__=='__main__':
    FAI.run(debug=True,host='192.168.65.154',port=5001)