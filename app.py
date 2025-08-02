from flask import Flask, request

app = Flask(__name__)

@app.route('/ussd', methods=['POST'])
def ussd():
    text = request.form.get('text', '')

    # Extract the last input (after the last "*")
    last_choice = text.split("*")[-1] if text else ""
    first_choice = text.split("*")[0] if text else ""

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
    # 2. EXIT (anywhere)
    # =======================
    elif last_choice == "99":
        response = "END Thank you for using Market Checker (wholesale)."

    # =======================
    # 3. BACK TO LANGUAGE SELECTION (00)
    # =======================
    elif last_choice == "00":
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
    elif first_choice == "1" and (last_choice == "0" or text == "1"):
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
    elif first_choice == "2" and (last_choice == "0" or text == "2"):
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
    elif first_choice == "1" and last_choice == "1":
        response = "CON Maize: ₦48,000/50kg bag (₦96/kg)\n0. Back to Menu\n00. Back to Language Selection\n99. Exit"
    elif first_choice == "1" and last_choice == "2":
        response = "CON Rice: ₦54,000/50kg bag (₦1,080/kg)\n0. Back to Menu\n00. Back to Language Selection\n99. Exit"
    elif first_choice == "1" and last_choice == "3":
        response = "CON Yam: ₦1,000 - ₦1,200 per tuber\n0. Back to Menu\n00. Back to Language Selection\n99. Exit"
    elif first_choice == "1" and last_choice == "4":
        response = "CON Beans: ₦35,000 - ₦43,000/50kg (₦700 - ₦860/kg)\n0. Back to Menu\n00. Back to Language Selection\n99. Exit"

    # =======================
    # 7. HAUSA PRODUCT PAGES
    # =======================
    elif first_choice == "2" and last_choice == "1":
        response = "CON Masara: ₦48,000 kowanne buhu 50kg (₦96/kg)\n0. Komawa Menu\n00. Komawa Zaben Harshe\n99. Fita"
    elif first_choice == "2" and last_choice == "2":
        response = "CON Shinkafa: ₦54,000 kowanne buhu 50kg (₦1,080/kg)\n0. Komawa Menu\n00. Komawa Zaben Harshe\n99. Fita"
    elif first_choice == "2" and last_choice == "3":
        response = "CON Doya: ₦1,000 zuwa ₦1,200 kowacce danye\n0. Komawa Menu\n00. Komawa Zaben Harshe\n99. Fita"
    elif first_choice == "2" and last_choice == "4":
        response = "CON Wake: ₦35,000 zuwa ₦43,000 kowanne buhu 50kg (₦700 - ₦860/kg)\n0. Komawa Menu\n00. Komawa Zaben Harshe\n99. Fita"

    # =======================
    # 8. INVALID INPUT (loop)
    # =======================
    else:
        response = "CON Invalid option. Please try again.\n00. Back to Language Selection\n99. Exit"

    return response, 200, {'Content-Type': 'text/plain'}
