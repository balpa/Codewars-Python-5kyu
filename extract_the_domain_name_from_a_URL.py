def domain_name(url):
    if "http://" in url:
        domain = url.split("//")[-1].split(".")[0]
        if "http://www." in url:
            domain = url.split("www.")[-1].split(".")[0]
            if "https://www." in url:
                domain = url.split("www.")[-1].split(".")[0]
    elif "https://" in url:
        domain = url.split("//")[-1].split(".")[0]
        
    elif "www" in url:
        domain = url.split("www.")[-1].split(".")[0]
    else:
        domain = url.split()[-1].split(".")[0]
    return domain 
