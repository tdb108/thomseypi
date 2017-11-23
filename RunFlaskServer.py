from flask import Flask
import SKCntrl
app = Flask(__name__)

def LogAction(message):
    file = open("logs.log","a")
    import datetime
    file.write(datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S"))
    file.write(" ")
    file.write(message)
    file.write("\n")
    file.close
    return message
 
@app.route("/")
def hello():    
    return LogAction("There's nothing to see here!")

@app.route("/LIGHTS_ON")
def lightsON():
    SKCntrl.SwitchONSK1()      
    return LogAction("Lights ON!")

@app.route("/LIGHTS_OFF")
def lightsOFF():
    SKCntrl.SwitchOFFSK1()   
    return LogAction("Lights OFF!")
 
if __name__ == "__main__":
    SKCntrl.SetupGPIO()
    app.run(host='0.0.0.0', port=5000)