from flask import Flask, render_template, request

# Initialise new Flask app
app = Flask(__name__)

# Set new name to name_error, to inform the user if the name was lost
name = "name_error"
namecap = "NAME_ERROR"

# Create an empty list for the xC saga to indicate conditions and items held
items = []

# xChips saga boolean
imRude = Tired = newGame = tvSleep = lateNightChips = False

# xC saga boolean
badTeeth1 = badTeeth2 = isEmail = noAmbo = noimmediateCare = False

# Base route to home page
@app.route('/')
def home():
    return render_template('index.html')


# Endings page direct
@app.route('/endings')
def endings():
    return render_template('endings.html')


# Initialise game with HTTP GET request for username
@app.route('/story', methods=["GET"])
def story():
    global name, namecap

    # Get player input for their username
    name = request.args.get("playername")

    # Capitalise the first letter of their name
    name = name.capitalize()

    # Create a fullcaps varient
    namecap = name.upper()

    return render_template(
        'intro.html',
        NAME=name,
    )


# Restart story method
@app.route('/storyrestart')
def storyrestart():
    global name, items, imRude, Tired, newGame, tvSleep, lateNightChips, badTeeth1, badTeeth2, isEmail, noAmbo, noimmediateCare

    # As the code has not been reloaded, we need to set every variable back to False
    imRude = Tired = newGame = tvSleep = lateNightChips = badTeeth1 = badTeeth2 = isEmail = noAmbo = noimmediateCare = False
    items.clear()

    return render_template(
        'intro.html',
        NAME=name,
    )


@app.route('/startgame')
def startgame():
    global name
    return render_template(
        'xBase.html',
        NAME=name,
    )


@app.route('/tv')
def tv():
    global name
    return render_template(
        'xTV.html',
        NAME=name,
    )


@app.route('/mum')
def mum():
    global name, imRude
    imRude = False  # Resetting to False because of back key messing up variables
    return render_template(
        'xTV-Mum.html',
        NAME=name,
    )


@app.route('/standforever')
def standforever():
    global name, lateNightChips

    if lateNightChips:
        target = 'ENDING-ChipFinder.html'
    else:
        target = 'ENDING-StandForever.html'

    return render_template(
        target,
        NAME=name,
    )


@app.route('/standforevermum')
def standforevermum():
    global name
    return render_template(
        'ENDING-StandForeverMum.html',
        NAME=name,
    )


@app.route('/berude')
def berude():
    global name, imRude
    imRude = True
    return render_template(
        'xTV-Ignore.html',
        NAME=name,
    )


@app.route('/sleep')
def sleep():
    global name
    global Tired
    Tired = False

    return render_template(
        'xTV-Mum-Sleep.html',
        NAME=name,
    )


@app.route('/chipstv')
def chipstv():
    global name, Tired, imRude, tvSleep
    tvSleep = True

    if imRude:
        Tired = True
        target = 'xTV-ChipsDecide.html'
    else:
        target = 'xTV-WatchTVChipsMum.html'

    return render_template(
        target,
        NAME=name,
    )


@app.route('/gaming')
def gaming():
    global name, imRude, Tired

    if imRude:
        Tired = True

    return render_template(
        'xTV-GamingBridge.html',
        NAME=name,
    )


@app.route('/takeoutchips')
def takeoutchips():
    global name, Tired

    if Tired:
        target = 'ENDING-TiredTakeOutChips.html'
    else:
        target = 'ENDING-NotTiredTakeOutChips.html'

    return render_template(
        target,
        NAME=name,
    )


@app.route('/bringoutchips')
def bringoutchips():
    global name
    return render_template(
        'ENDING-EnthusiasticTakeOutChips.html',
        NAME=name,
    )


@app.route('/gamedontknow')
def gamedontknow():
    global name, imRude

    if imRude:
        target = 'xTV-PlayOGameFallAsleep.html'
    else:
        target = 'xTV-PlayOGameMum.html'

    return render_template(
        target,
        NAME=name,
    )


@app.route('/newgame')
def newgame():
    global name, imRude, newGame
    newGame = True

    if imRude:
        target = 'xTV-PlayNGameFallAsleep.html'
    else:
        target = 'xTV-PlayNGameMum.html'

    return render_template(
        target,
        NAME=name,
    )


@app.route('/lie')
def lie():
    global name, tvSleep, lateNightChips

    if tvSleep and lateNightChips:
        target = 'xTV-Mum-RushTVAte.html'
    else:
        target = 'xTV-Mum-RushTV.html'

    return render_template(
        target,
        NAME=name,
    )


@app.route('/truth')
def truth():
    global name
    return render_template(
        'ENDING-MadMum.html',
        NAME=name,
    )


@app.route('/givechipseveryone')
def givechipseveryone():
    global name
    return render_template(
        'ENDING-ChipsGenocide.html',
        NAME=name,
    )


@app.route('/dietician')
def dietician():
    global name
    global tvSleep
    global imRude
    tvSleep = True

    if imRude:
        target = 'xTV-WatchTVChipsFallAsleep.html'
    else:
        target = 'xTV-WatchTVChipsMum.html'

    return render_template(
        target,
        NAME=name,
    )


@app.route('/fatty')
def fatty():
    global name
    global lateNightChips
    global imRude
    global tvSleep
    lateNightChips = True
    tvSleep = True

    if imRude:
        target = 'xTV-WatchTVChipsFallAsleepAte.html'
    else:
        target = 'xTV-WatchTVChipsMum.html'

    return render_template(
        target,
        NAME=name,
    )


@app.route('/taketime')
def taketime():
    global name
    return render_template(
        'ENDING-MadMumDeliquent.html',
        NAME=name,
    )


@app.route('/rush')
def rush():
    global name
    return render_template(
        'xTV-DoAnythingFallAsleepBridge.html',
        NAME=name,
    )


@app.route('/newgametalk')
def newgametalk():
    global name
    global Tired

    if Tired:
        target = 'ENDING-FSNewGame.html'
    else:
        target = 'ENDING-MumNewGame.html'

    return render_template(
        target,
        NAME=name,
    )


@app.route('/oldgametalk')
def oldgametalk():
    global name
    global Tired
    global namecap

    if Tired:
        target = 'ENDING-FSOldGame.html'
    else:
        target = 'ENDING-MumOldGame.html'

    return render_template(
        target,
        NAME=name,
        NAMECAP=namecap,
    )


@app.route('/takeoutdrone')
def takeoutdrone():
    global name
    return render_template(
        'ENDING-TakeOutDrone.html',
        NAME=name,
    )


@app.route('/computerinvestigate')
def computerinvestigate():
    global name
    return render_template(
        'ENDING-VistaMum.html',
        NAME=name,
    )


@app.route('/chips')
def chips():
    global name
    return render_template(
        'xC.html',
        NAME=name,
    )


@app.route('/bed')
def bed():
    global name
    global badTeeth1
    badTeeth1 = True
    return render_template(
        'xC-Bed.html',
        NAME=name,
    )


@app.route('/cleanteeth')
def cleanteeth():
    global name
    global badTeeth1
    badTeeth1 = False
    return render_template(
        'xC-Teeth.html',
        NAME=name,
    )


@app.route('/gowork')
def gowork():
    global name
    return render_template(
        'xC-Work.html',
        NAME=name,
    )


@app.route('/callfriend')
def callfriend():
    global name
    return render_template(
        'xC-Friend.html',
        NAME=name,
    )


@app.route('/friendconvo')
def friendconvo():
    global name
    return render_template(
        'ENDING-FriendConvo.html',
        NAME=name,
    )


@app.route('/eatchips')
def eatchips():
    global name
    global items

    if "chips" in items:
        target = 'ENDING-HomeChips.html'
    else:
        target = 'xC-NoChips.html'

    return render_template(
        target,
        NAME=name,
    )


@app.route('/vanish')
def vanish():
    global name
    return render_template(
        'ENDING-Vanish.html',
        NAME=name,
    )


@app.route('/turnoncomputer')
def turnoncomputer():
    global name
    return render_template(
        'xC-TurnOnPC.html',
        NAME=name,
    )


@app.route('/eatmorechips')
def eatmorechips():
    global name
    global badTeeth1
    global badTeeth2
    global items

    if badTeeth1:
        target = 'xC-EatExtraChips.html'
        badTeeth2 = True
    else:
        target = 'xC-EatMoreChips.html'
        badTeeth1 = False
        items.append("chips")

    return render_template(
        target,
        NAME=name,
    )


@app.route('/checkemails')
def checkemails():
    global name
    return render_template(
        'xC-TurnOnPC.html',
        NAME=name,
    )


@app.route('/eatchipshome')
def eatchipshome():
    global name
    global badTeeth1
    global badTeeth2

    if badTeeth1 and badTeeth2 is True:
        target = 'ENDING-ChipOverload.html'
    else:
        target = 'xC-EatChips.html'

    return render_template(
        target,
        NAME=name,
    )


@app.route('/embracecheese')
def embracecheese():
    global name
    return render_template(
        'ENDING-EmbraceCheese.html',
        NAME=name,
    )


@app.route('/runcheese')
def runcheese():
    global name
    return render_template(
        'ENDING-RunCheese.html',
        NAME=name,
    )


@app.route('/cheesesim')
def cheesesim():
    global name
    return render_template(
        'xC-CheeseSim.html',
        NAME=name,
    )


@app.route('/emails')
def emails():
    global name
    global isEmail

    if isEmail:
        target = '/'  # Page not yet created due to missing prerequisites
    else:
        target = 'xC-NoEmails.html'

    return render_template(
        target,
        NAME=name,
    )


@app.route('/doomsupereternal')
def doomsupereternal():
    global name
    return render_template(
        'ENDING-Doom.html',
        NAME=name,
    )


@app.route('/closeemails')
def closeemails():
    global name
    return render_template(
        'xC-CloseEmails.html',
        NAME=name,
    )


@app.route('/minecraft')
def minecraft():
    global name
    return render_template(
        'ENDING-Minecraft.html',
        NAME=name,
    )


@app.route('/fortnite')
def fortnite():
    global name
    return render_template(
        'ENDING-Fortnite.html',
        NAME=name,
    )


@app.route('/cheesesimchips')
def cheesesimchips():
    global name
    return render_template(
        'ENDING-CheeseSimChips.html',
        NAME=name,
    )


@app.route('/it')
def it():
    global name, items
    global badTeeth1, badTeeth2

    if badTeeth1 and badTeeth2 is True:
        target = 'ENDING-BadTeethIT.html'
    elif "chips" in items:
        target = 'xC-WorkITChips.html'
    else:
        target = 'xC-WorkITNoChips.html'

    return render_template(
        target,
        NAME=name,
    )


@app.route('/weld')
def weld():
    global name
    global badTeeth1, badTeeth2

    if badTeeth1 and badTeeth2 is True:
        target = 'ENDING-BadTeethWeld.html'
    else:
        target = 'xC-WorkWeld.html'

    return render_template(
        target,
        NAME=name,
    )


@app.route('/gohome')
def gohome():
    global name
    return render_template(
        'xC-HomeBridge02.html',
        NAME=name,
    )


@app.route('/itworkhelp')
def itworkhelp():
    global name
    return render_template(
        'xC-WorkITHelp.html',
        NAME=name,
    )


@app.route('/noambo')
def noambo():
    global name
    global noAmbo
    noAmbo = True
    return render_template(
        'xC-HomeBridge01.html',
        NAME=name,
    )


@app.route('/ambo')
def ambo():
    global name
    global noAmbo
    noAmbo = True
    return render_template(
        'xC-WorkITGCAmboDe.html',
        NAME=name,
    )


@app.route('/itleave')
def itleave():
    global name
    global noimmediateCare
    
    noimmediateCare = True
        
    return render_template(
        'xC-WorkITGCAmboDeLeave.html',
        NAME=name,
    )


@app.route('/subinneed')
def subinneed():
    global name
    global noimmediateCare
    
    if noimmediateCare:
        target = 'ENDING-SubInNeedLa.html'
    else:
        target = 'ENDING-SubInNeedIm.html'
        
    return render_template(
        target,
        NAME=name,
    )


@app.route('/weirdwall')
def weirdwall():
    global name
    return render_template(
        'ENDING-Backrooms.html',
        NAME=name,
    )


@app.route('/itignorerun')
def itignorerun():
    global name
    return render_template(
        'xC-WorkITGCAmboDeLeaveCall.html',
        NAME=name,
    )


@app.route('/itringout')
def itringout():
    global name
    return render_template(
        'ENDING-ITRingout.html',
        NAME=name,
    )


@app.route('/itaccept')
def itaccept():
    global name
    return render_template(
        'xC-WorkITGCCallAccept.html',
        NAME=name,
    )


@app.route('/itdeny')
def itdeny():
    global name
    return render_template(
        'xC-WorkITGCCallDeny.html',
        NAME=name,
    )

@app.route('/itnocare')
def itnocare():
    global name
    return render_template(
        'ENDING-21KO.html',
        NAME=name,
    )

@app.route('/itremainsilent')
def itremainsilent():
    global name
    return render_template(
        'ENDING-ITRemainSilent.html',
        NAME=name,
    )

@app.route('/givechips')
def givechips():
    global name
    global items
    
    # Prevent crashing if the user decides to backtrack
    if "chips" in items:
        items.remove("chips")

    return render_template(
        'xC-WorkITGC.html',
        NAME=name,
    )

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)

# if __name__ == "__main__":
#    from waitress import serve
#    serve(app, host="0.0.0.0")
