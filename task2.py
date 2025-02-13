def typeBasedTransformer(info):
    converted = {}
    
    for kalit, qiymat in info.items():
        
        if isinstance(qiymat, (int, float)):
            converted[kalit] = qiymat ** 2
        elif isinstance(qiymat, bool):
            converted[kalit] = not qiymat
        elif isinstance(qiymat, (list, tuple)):
            converted[kalit] = qiymat[::-1]
        elif isinstance(qiymat, dict):
            converted[kalit] = {s: t for t, s in qiymat.items()}
        elif isinstance(qiymat, str):
            converted[kalit] = qiymat[::-1]
        
        else:
            converted[kalit] = qiymat
            
    return converted

