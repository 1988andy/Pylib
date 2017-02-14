import codecs

def read_file(filepath, encoding = "utf-8"):
    '''
    Reads the file using the specified encoding.
    '''
    return codecs.open(filepath, "r", encoding).read()

def write_file(filepath, content, dropIfExisted = False):
    '''
    Writes the content to the specified file.
    '''
    mode = "w" if dropIfExisted else "a"
    with codecs.open(filepath, mode, "utf-8") as f:
        f.write(content)
        f.flush()
