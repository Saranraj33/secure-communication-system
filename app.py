from flask import Flask, render_template, request
from cryptography.fernet import Fernet

app = Flask(__name__)

# Generate a key for encryption and decryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

@app.route('/')
def index():
    return render_template('index.html')


#Message get from user to Change the given message to Encrypted Form
@app.route('/encrypt', methods=['POST'])
def encrypt():
    message = request.form['message']
    encrypted_message = cipher_suite.encrypt(message.encode('utf-8'))
    return render_template('index.html', message=message, result=encrypted_message)


#Encrypted Message to Change Decrypt Form from the Original Message
@app.route('/decrypt', methods=['POST'])
def decrypt():
    encrypted_message = request.form['message']
    decrypted_message = cipher_suite.decrypt(encrypted_message.encode('utf-8')).decode('utf-8')
    return render_template('index.html', message=decrypted_message, result1=decrypted_message)

if __name__ == '__main__':
    app.run(debug=True)