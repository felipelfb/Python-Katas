# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

# domain_name("http://github.com/carbonfive/raygun") == "github" 
# domain_name("http://www.zombie-bites.com") == "zombie-bites"
# domain_name("https://www.cnet.com") == "cnet"

# https://www.codewars.com/kata/extract-the-domain-name-from-a-url-1

def domain_name(url):
    http = ['http:', 'https:']
    www = ['www']
    splitted_url = url.split('//')
    if splitted_url[0] in http:
        splitted_url = ''.join(splitted_url[1:])
    else:
        splitted_url = ''.join(splitted_url)
    splitted_url = splitted_url.split('.')
    if splitted_url[0] not in http and splitted_url[0] not in www:
        return splitted_url[0]
    else:
        return splitted_url[1]