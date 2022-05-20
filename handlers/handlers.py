
def isEveryoneCall(text):
    if "@everyone" in text:
        return True
    if "@OldLyingSuprime_bot" in text:
        return True
    if "!всем" in text:
        return True
    if "!Всем" in text:
        return True
    if "!все" in text:
        return True
    if "!Все" in text:
        return True
    if "@all" in text:
        return True
    if "@All" in text:
        return True
    return False

def isSaveCall(text):
    callVariants = ["!запомни", "!Запомни"]
    for callVariant in callVariants:
        if callVariant in text:
            return True
    return False

def isMessSattusCall(text):
    callVariants = ["!пиши мне", "!Пиши мне"]
    for callVariant in callVariants:
        if callVariant in text:
            return True
    return False

def isUnMessSattusCall(text):
    callVariants = ["!не пиши мне", "!Не пиши мне"]
    for callVariant in callVariants:
        if callVariant in text:
            return True
    return False

def isRemoveCall(text):
    callVariants = ["!забудь", "!Забудь"]
    for callVariant in callVariants:
        if callVariant in text:
            return True
    return False
