import re

def find_first(string, pattern, group = None):
    '''
    Gets the first matched. return the group value if the group is specified, otherwise the whole matched value.
    '''
    matched = re.search(pattern, string)
    if matched:
        groups = matched.groupdict()
        if groups and group:
            return groups.get(group)
        return matched.group(0)
    return None

def find_all(string, pattern, group = None):
    '''
    Gets the matched array. Return the group value array if the group is specified, otherwise typed dict.
    '''
    c = re.compile(pattern)
    if group:
        lst = []
        for m in c.finditer(string):
            lst.append(m.groupdict().get(group))
        return lst
    else:
        if c.groups > 0:
            lst = []
            for m in c.finditer(string):
                lst.append(m.groupdict())
            return lst
        else:
            return re.findall(pattern, string)
    return None

