from flask import Flask, request

app = Flask(__name__)

@app.route('/ussd', methods=['POST'])
def ussd():
    session_id = request.form.get('sessionId')
    service_code = request.form.get('serviceCode')
    phone_number = request.form.get('phoneNumber')
    text = request.form.get('text', '')

    response = ""

    if text == "":
        response = "CON Welcome to Market Checker\n1. View Prices\n2. Help"
    elif text == "1":
        response = "CON Choose Product:\n1. Maize\n2. Rice\n3. Yam"
    elif text == "1*1":
        response = "END Maize: ₦28,000 per 100kg bag in Kano"
    elif text == "1*2":
        response = "END Rice: ₦42,000 per 100kg bag in Kano"
    elif text == "1*3":
        response = "END Yam: ₦30,000 per 50 tubers in Kano"
    elif text == "2":
        response = "END This service helps farmers check real-time market prices using USSD."
    else:
        response = "END Invalid option. Please try again."

    return response, 200, {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    app.run(debug=True)
