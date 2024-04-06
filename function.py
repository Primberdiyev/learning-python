def toliq_ism(ism,familiya,sharif=''):
    if sharif:
        return f"{ism} {familiya} {sharif}".title()
    else:
        return f"{ism} {familiya}".title()
