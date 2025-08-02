from flask import Flask, request

app = Flask(__name__)

@app.route('/ussd', methods=['POST'])
def ussd():
    session_id = request.form.get('sessionId')
    service_code = request.form.get('serviceCode')
    phone_number = request.form.get('phoneNumber')
    text = request.form.get('text', '')

    response = ""

    # FIRST LEVEL: Language Selection
    if text == "":
        response = "CON Welcome to Market Checker (wholesale)\nZabi yaren ku / Choose your language:\n1. English\n2. Hausa"

    # ENGLISH FLOW
    elif text == "1":
        response = "CON What would you like to check?\n1. Maize\n2. Rice\n3. Yam\n4. Beans"

    # Hausa Flow
    elif text == "2":
        response = "CON Me kuke so ku duba?\n1. Masara\n2. Shinkafa\n3. Doya\n4. Wake"

    # English product options
    elif text == "1*1":
        response = "END Maize: ₦48,000/50kg bag (₦96/kg)"
    elif text == "1*2":
        response = "END Rice: ₦54,000/50kg bag (₦1,080/kg)"
    elif text == "1*3":
        response = "END Yam: ₦1,000 - ₦1,200 per tuber"
    elif text == "1*4":
        response = "END Beans: ₦35,000 - ₦43,000/50kg (₦700 - ₦860/kg)"

    # Hausa product options
    elif text == "2*1":
        response = "END Masara: ₦48,000 kowanne buhu 50kg (₦96/kg)"
    elif text == "2*2":
        response = "END Shinkafa: ₦54,000 kowanne buhu 50kg (₦1,080/kg)"
    elif text == "2*3":
        response = "END Doya: ₦1,000 zuwa ₦1,200 kowacce danye"
    elif text == "2*4":
        response = "END Wake: ₦35,000 zuwa ₦43,000 kowanne buhu 50kg (₦700 - ₦860/kg)"

    # Invalid input
    else:
        response = "END Invalid option. Please dial again."

    return response, 200, {'Content-Type': 'text/plain'}
