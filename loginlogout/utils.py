import re


def validate_user_funai(username, domain):

    regex = re.compile('([^\\s]+)\\@[^\\s]+')
    matched = regex.match(username)

    if(matched):
        username = "%s%s" % (matched.group(1), domain)
    else:
        username = "%s%s" % (username, domain)

    return username