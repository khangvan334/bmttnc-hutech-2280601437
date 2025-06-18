from flask import Flask, json, render_template, request 
from cipher.caesar.caesar_cipher import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher 
from cipher.playfair import PlayfairCipher

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

#CAESAR

@app.route("/caesar")
def caesar():
    return render_template('/caesar.html')

@app.route("/caesar/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return render_template('/caesar.html',
                           input_plain_text_encrypt=text,
                           input_key_plain_encrypt=key,
                           output_encrypted_text=encrypted_text)

@app.route("/caesar/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypted_text(text, key)
    return render_template('/caesar.html',
                           input_cipher_text_decrypt=text,
                           input_key_cipher_decrypt=key,
                           output_decrypted_text=decrypted_text)

#VIGENERE

@app.route("/vigenere")
def vigenere():
    return render_template('/vigenere.html')

@app.route("/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    Vigenere = VigenereCipher()
    encrypted_text = Vigenere.vigenere_encrypt(text, key)
    return render_template('/vigenere.html',
                           input_plain_text_encrypt=text,
                           input_key_plain_encrypt=key,
                           output_encrypted_text=encrypted_text)


@app.route("/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    Vigenere = VigenereCipher()
    decrypted_text = Vigenere.vigenere_decrypt(text, key)
    return render_template('/vigenere.html',
                           input_cipher_text_decrypt=text,
                           input_key_cipher_decrypt=key,
                           output_decrypted_text=decrypted_text)

#RAIL FENCE

@app.route("/railfence")
def railfence():
    return render_template('/railfence.html')

@app.route("/railfence/encrypt", methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Railfence = RailFenceCipher()
    encrypted_text = Railfence.rail_fence_encrypt(text, key)
    return render_template('/railfence.html',
                           input_plain_text_encrypt=text,
                           input_key_plain_encrypt=key,
                           output_encrypted_text=encrypted_text)

@app.route("/railfence/decrypt", methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    RaiFence = RailFenceCipher()
    decrypted_text = RaiFence.rail_fence_decrypt(text, key)
    return render_template('/railfence.html',
                           input_cipher_text_decrypt=text,
                           input_key_cipher_decrypt=key,
                           output_decrypted_text=decrypted_text)

#PLAY FAIR

@app.route("/playfair")
def playfair():
    return render_template("playfair.html")

@app.route("/playfair/matrix", methods=["POST"])
def playfair_matrix():
    key = request.form["matrixKey"]
    cipher = PlayfairCipher()
    matrix = cipher.create_playfair_matrix(key)
    matrix_html = "<br/>".join([" ".join(row) for row in matrix])
    return render_template("playfair.html", matrix_key=key, playfair_matrix_html=matrix_html)

@app.route("/playfair/encrypt", methods=["POST"])
def playfair_encrypt():
    text = request.form["inputPlainText"]
    key = request.form["inputKeyPlain"]
    cipher = PlayfairCipher()
    matrix = cipher.create_playfair_matrix(key)
    encrypted_text = cipher.playfair_encrypt(text, matrix)
    return render_template("playfair.html",
                           input_plain_text_encrypt=text,
                           input_key_plain_encrypt=key,
                           output_encrypted_text=encrypted_text)

@app.route("/playfair/decrypt", methods=["POST"])
def playfair_decrypt():
    text = request.form["inputCipherText"]
    key = request.form["inputKeyCipher"]
    cipher = PlayfairCipher()
    matrix = cipher.create_playfair_matrix(key)
    decrypted_text = cipher.playfair_decrypt(text, matrix)
    return render_template("playfair.html",
                           input_cipher_text_decrypt=text,
                           input_key_cipher_decrypt=key,
                           output_decrypted_text=decrypted_text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)