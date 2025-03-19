from flask import Flask


app = Flask(__name__)

from views import *

if __name__ == "__main__":
    app.run()

#from flask import Flask
#import os # os.walk()

#app = Flask("checkboxes") # from flask

#def checkboxes(directory):
    #all_names = ""
    #template = "{}: <input type=\"checkbox\" value=\"{}\"/><br>\n"

    #for root, dirs, files in os.walk(directory):
        #for name in dirs:
            #all_names += template.format(name) # name vai para {0}.
    #return all_names

#@app.route("/")
#def main():
    #return checkboxes(".") # retorna all_names para a página.

#app.run()