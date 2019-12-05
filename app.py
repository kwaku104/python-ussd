from flask import Flask, request
import africastalking
import os

app = Flask(__name__)
username = ""
api_key = ""
africastalking.initialize(username, api_key)
sms = africastalking.SMS

@app.route('/', methods=['POST', 'GET'])
def ussd_callback():
    global response
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")
    sms_phone_number = []
    sms_phone_number.append(phone_number)

    #USSD Logic
    if text == "":
        #main menu
        response = "CON What would you like to do?\n"
        response += "1. Check account details\n"
        response += "2. Check phone number\n"
        response += "3. Send a cool message\n"
    elif text == "1":
        #sub menu 1
        respone = "CON What would you like to check on your account?\n"
        respone += "1. Account number"
        response += "2. Account balance"
    elif text == "2":
        # sub menu 1
        response = "END Your phone number is {}".format(phone_number)
    elif text == "3":
        try:
            #sending the sms
            sms_response = sms.send("Thank you for trying out this app", sms_phone_number)
            print(sms_response)
        except Exception as e:
            #show us what went wrong
            print(f"We have a problem: {e}")
    elif text == "1*1":
        #ussd menus are split *
        account_number = "1243324376742"
        response = "END Your account number is USD {}".format(account_number)
    elif text == "1*2":
        account_balance = "100,000"
        respone = "END Your account balance is USD {}".format(account_balance)
    else:
        respone = "END Invalid input. Try again."
    
    return respone


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)