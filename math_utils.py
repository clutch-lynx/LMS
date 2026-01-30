def  is_valid_password(password):
    

    if len(password) < 8:
        return False
    
    has_big_let = False
    has_smal_let = False
    has_chuslo = False
    
    for i in password:
        if i.isupper():
            has_big_let = True
        if i.islower():
            has_smal_let = True
        if i.isdigit():
            has_chuslo = True

    
    return has_big_let and has_smal_let and has_chuslo