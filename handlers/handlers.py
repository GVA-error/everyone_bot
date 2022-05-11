
def isEveryoneCall(text):
    return "@everyone" in text

def isSaveCall(text):
    if "@OldLyingSuprime_bot" not in text:
        return False
    callVariants = ["запомни", "Запомни"]
    for callVariant in callVariants:
        if callVariant in text:
            return True
    return False