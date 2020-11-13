name = ''
productname = ''
product = ''
def get_intent(data):
    global name, productname, product
    m=data['message'].lower()
    if data['key']=="name":
        name=m
        return "next"
    if any(x in m for x in ["fitbit","alexa","airconditioner","refrigerator","sportshoes"]):
        productname=m
        return "productname"
    if any(x in m for x in ["colours","brands","features","demo","websites","buynow"]):
        product=m
        return "product"
    if "thankyou" in m:
        return "wel"

def handle(data):
    global name, productname, product
    from flask import render_template
    intent = get_intent(data)
    if intent == 'productname':
        return render_template('messages/producta.html', question={'key':'request','text':'Please Enter the details you want to know.'},details={'tasks':[
        {'key':'colours','description':'color of product'},
        {'key':'brands','description':'available brands'},
        {'key':'features','description':'available features'},
        {'key':'demo','description':'demo of product'},
        {'key':'websites','description':'available websites'},
        {'key':'buynow','description':'available websites'}
        
    ] })
    elif intent == 'next':
        return render_template('messages/greet.html',name=name, question={'key':'request','text':'Enter the product name you want to know.The available products are 1)Fitbit 2)alexa 3)airconditioner 4)refrigerator 5)sportshoes'})
    elif intent == 'product':
        from .data.botinfo import bot
        return render_template('messages/productb.html',productname=productname,product=product,data=bot ,question={'key':'request'})
    elif intent == 'wel':
        return render_template('messages/endmsg.html',question={'key':'request'})
    else:
        return render_template('messages/echo.html', question={'key':'request'})