import os
from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def home():
<<<<<<< HEAD
    return render_template('index.html')


#verkefni A
@app.route('/a-hluti')
def ahluti():
    return render_template('kennitala.html')
=======
    return render_template('default.html')
>>>>>>> dfb284844b7e8cbc3ff6cde38824ae81d791c742

@app.route('/kt-sida/<kt>') 
def ktsida(kt):
    summa=0
    for item in kt:
        summa = summa + int(item)

    return render_template('kt-sum.html', kt=kt, summa=summa)

<<<<<<< HEAD
#verkhluti B
#database er utfærður sem tvívíður listi(dictionary)
#id, fyrirsögn, frétt, e-mail
frettir = [
    ["0","Guðmundur veldur usla á Flórída",
     "Það er bara helv... vesen á Guðmundur í Flórída.  Milljónir manna hafa þurft að yfirgefa heimili sin vegna yfirvofandi eyðileggingar Guðmundur...", 
     "dsg@frettir.is"],
    ["1","Veiðin er dræm þetta haustið",
     "Veiðin hefur heldur verið döpur þetta haustið þrátt fyrir ágætis rigninar upp á síðkastið...", 
     "est@frettir.is"],
    ["2","Ólafía stendur sig vel",
     "Ólafía er komin í 65 sæti peningalistans og hefur því tryggt sér keppnisrétt á LPG mótaröðinni á komandi keppnistimabili...", 
     "htg@frettir.is"],
    ["3","Ísland dottið úr leik",
     "Íslenska karlalandsliðið í körfubolta er dottið úr leik a Eurobasket þrátt fyrir ágætis spretti inn a milli.  Ísland spilaði lokaleik sinn á mótinu fyrir troðfullri höll gegn heimamönnum Finnum..", 
     "dsg@frettir.is"]
]

@app.route('/b-hluti')
def bhluti():
    return render_template('frettir.html', frettir=frettir)


@app.route('/frett/<int:id>')
def news(id):
    return render_template('frett.html', frett=frettir[id], nr=id)

#villuskilaborð
=======

>>>>>>> dfb284844b7e8cbc3ff6cde38824ae81d791c742
@app.errorhandler(404)
def pagenotfound(error):
    return render_template('pagenotfound.html'), 404

if __name__== '__main__':
    app.run(debug=True)
    





