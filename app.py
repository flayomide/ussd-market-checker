from flask import Flask, request

app = Flask(__name__)

@app.route('/ussd', methods=['POST'])
def ussd():
    text = request.form.get('text', '')

    response = ""

    # FIRST LEVEL: Language Selection
    if text == "":
        response = "CON Welcome to Market Checker (wholesale)\nZabi yaren ku / Choose your language:\n1. English\n2. Hausa\n99. Exit"

    # ENGLISH FLOW: Main Menu
    elif text == "1":
        response = "CON What would you like to check?\n1. Maize\n2. Rice\n3. Yam\n4. Beans\n0. Back to Language Selection\n99. Exit"

    # HAUSA FLOW: Main Menu
    elif text == "2":
        response = "CON Me kuke so ku duba?\n1. Masara\n2. Shinkafa\n3. Doya\n4. Wake\n0. Komawa zaben harshe\n99. Fita"

    # EXIT OPTION
    elif text.endswith("*99") or text == "99":
        response = "END Thank you for using Market Checker (wholesale)."

    # ENGLISH PRODUCT OPTIONS (looping)
    elif text == "1*1":
        response = "CON Maize: ₦48,000/50kg bag (₦96/kg)\n0. Back to Menu\n99. Exit"
    elif text == "1*2":
        response = "CON Rice: ₦54,000/50kg bag (₦1,080/kg)\n0. Back to Menu\n99. Exit"
    elif text == "1*3":
        response = "CON Yam: ₦1,000 - ₦1,200 per tuber\n0. Back to Menu\n99. Exit"
    elif text == "1*4":
        response = "CON Beans: ₦35,000 - ₦43,000/50kg (₦700 - ₦860/kg)\n0. Back to Menu\n99. Exit"

    # Back to English Main Menu from product level
    elif text == "1*0":
        response = "CON What would you like to check?\n1. Maize\n2. Rice\n3. Yam\n4. Beans\n0. Back to Language Selection\n99. Exit"

    # Back to Language Selection from English Main Menu
    elif text == "1*0*0":
        response = "CON Welcome to Market Checker (wholesale)\nZabi yaren ku / Choose your language:\n1. English\n2. Hausa\n99. Exit"

    # HAUSA PRODUCT OPTIONS (looping)
    elif text == "2*1":
        response = "CON Masara: ₦48,000 kowanne buhu 50kg (₦96/kg)\n0. Komawa menu\n99. Fita"
    elif text == "2*2":
        response = "CON Shinkafa: ₦54,000 kowanne buhu 50kg (₦1,080/kg)\n0. Komawa menu\n99. Fita"
    elif text == "2*3":
        response = "CON Doya: ₦1,000 zuwa ₦1,200 kowacce danye\n0. Komawa menu\n99. Fita"
    elif text == "2*4":
        response = "CON Wake: ₦35,000 zuwa ₦43,000 kowanne buhu 50kg (₦700 - ₦860/kg)\n0. Komawa menu\n99. Fita"

    # Back to Hausa Main Menu from product level
    elif text == "2*0":
        response = "CON Me kuke so ku duba?\n1. Masara\n2. Shinkafa\n3. Doya\n4. Wake\n0. Komawa zaben harshe\n99. Fita"

    # Back to Language Selection from Hausa Main Menu
    elif text == "2*0*0":
        response = "CON Welcome to Market Checker (wholesale)\nZabi yaren ku / Choose your language:\n1. English\n2. Hausa\n99. Exit"

    # Invalid input
    else:
        response = "END Invalid option. Please dial again."

    return response, 200, {'Content-Type': 'text/plain'}
