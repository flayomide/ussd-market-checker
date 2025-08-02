from flask import Flask, request

app = Flask(__name__)

@app.route('/ussd', methods=['POST'])
def ussd():
    text = request.form.get('text', '')

    response = ""

    # =======================
    # 1. START: Language Selection
    # =======================
    if text == "":
        response = (
            "CON Welcome to Market Checker (wholesale)\n"
            "Zabi yaren ku / Choose your language:\n"
            "1. English / Turanci\n"
            "2. Hausa / Harshen Hausa\n"
            "99. Exit"
        )

    # =======================
    # 2. GLOBAL EXIT
    # =======================
    elif text.endswith("*99") or text == "99":
        response = "END Thank you for using Market Checker (wholesale)."

    # =======================
    # 3. GLOBAL BACK TO LANGUAGE SELECTION (00)
    # =======================
    elif text.endswith("*00") or text == "00":
        response = (
            "CON Welcome to Market Checker (wholesale)\n"
            "Zabi yaren ku / Choose your language:\n"
            "1. English / Turanci\n"
            "2. Hausa / Harshen Hausa\n"
            "99. Exit"
        )

    # =======================
    # 4. ENGLISH MAIN MENU
    # =======================
    elif text == "1":
        response = (
            "CON What would you like to check?\n"
            "1. Maize\n"
            "2. Rice\n"
            "3. Yam\n"
            "4. Beans\n"
            "0. Back to Language Selection\n"
            "99. Exit"
        )

    # =======================
    # 5. HAUSA MAIN MENU
    # =======================
    elif text == "2":
        response = (
            "CON Me kuke so ku duba?\n"
            "1. Masara\n"
            "2. Shinkafa\n"
            "3. Doya\n"
            "4. Wake\n"
            "0. Komawa zaben harshe\n"
            "99. Fita"
        )

    # =======================
    # 6. ENGLISH PRODUCT PAGES
    # =======================
    elif text == "1*1":
        response = "CON Maize: ₦48,000/50kg bag (₦96/kg)\n0. Back to Menu\n00. Back to Language Selection\n99. Exit"
    elif text == "1*2":
        response = "CON Rice: ₦54,000/50kg bag (₦1,080/kg)\n0. Back to Menu\n00. Back to Language Selection\n99. Exit"
    elif text == "1*3":
        response = "CON Yam: ₦1,000 - ₦1,200 per tuber\n0. Back to Menu\n00. Back to Language Selection\n99. Exit"
    elif text == "1*4":
        response = "CON Beans: ₦35,000 - ₦43,000/50kg (₦700 - ₦860/kg)\n0. Back to Menu\n00. Back to Language Selection\n99. Exit"

    # =======================
    # 7. HAUSA PRODUCT PAGES
    # =======================
    elif text == "2*1":
        response = "CON Masara: ₦48,000 kowanne buhu 50kg (₦96/kg)\n0. Komawa Menu\n00. Komawa Zaben Harshe\n99. Fita"
    elif text == "2*2":
        response = "CON Shinkafa: ₦54,000 kowanne buhu 50kg (₦1,080/kg)\n0. Komawa Menu\n00. Komawa Zaben Harshe\n99. Fita"
    elif text == "2*3":
        response = "CON Doya: ₦1,000 zuwa ₦1,200 kowacce danye\n0. Komawa Menu\n00. Komawa Zaben Harshe\n99. Fita"
    elif text == "2*4":
        response = "CON Wake: ₦35,000 zuwa ₦43,000 kowanne buhu 50kg (₦700 - ₦860/kg)\n0. Komawa Menu\n00. Komawa Zaben Harshe\n99. Fita"

    # =======================
    # 8. BACK TO ENGLISH MAIN MENU (from any product)
    # =======================
    elif text.endswith("*0") and text.startswith("1*"):
        response = (
            "CON What would you like to check?\n"
            "1. Maize\n"
            "2. Rice\n"
            "3. Yam\n"
            "4. Beans\n"
            "0. Back to Language Selection\n"
            "99. Exit"
        )

    # =======================
    # 9. BACK TO HAUSA MAIN MENU (from any product)
    # =======================
    elif text.endswith("*0") and text.startswith("2*"):
        response = (
            "CON Me kuke so ku duba?\n"
            "1. Masara\n"
            "2. Shinkafa\n"
            "3. Doya\n"
            "4. Wake\n"
            "0. Komawa zaben harshe\n"
            "99. Fita"
        )

    # =======================
    # 10. BACK TO LANGUAGE SELECTION FROM MAIN MENU
    # =======================
    elif text == "1*0" or text == "2*0":
        response = (
            "CON Welcome to Market Checker (wholesale)\n"
            "Zabi yaren ku / Choose your language:\n"
            "1. English / Turanci\n"
            "2. Hausa / Harshen Hausa\n"
            "99. Exit"
        )

    # =======================
    # 11. INVALID INPUT (LOOP BACK)
    # =======================
    else:
        response = "CON Invalid option. Please try again.\n00. Back to Language Selection\n99. Exit"

    return response, 200, {'Content-Type': 'text/plain'}
