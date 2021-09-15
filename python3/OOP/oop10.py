def ispallindrom(s):
    rev=''.join(reversed(s))
    if(s==rev):
        return True

    return False

print(ispallindrom("komal"))