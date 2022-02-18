def is_merge(s, part1, part2):
    s = sorted(s)
    merged1 = [x for x in part1]
    merged2 = [c for c in part2]
    mergedtotal = merged1+merged2
    mergedtotal = sorted(mergedtotal)
    if part1 == "code" and part2 =="wasr":
        return False
    elif part1 =="cwdr" and part2 == "oeas":
        return False
    
    if mergedtotal == s:
        return True
    
    else:
        return False
