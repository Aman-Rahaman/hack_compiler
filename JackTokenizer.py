file = ""
outputFileName = ""


tokens = []
numberOfTokens = 0


def getTokens():
    input_file = open(file, 'r')

    content = input_file.read()
    length = len(content)

    symbols = ['(', ')', ',', '.', ';', '{', '}', '[', ']', '=', '-', '+', '*', '/', '<', '>', '~', '&', '|']
    keyword = ['class', 'constructor', 'function', 'method', 'field', 'static', 'var', 'int', 'char', 'boolean', 'void','true', 'false', 'null', 'this', 'let', 'do', 'if', 'else', 'while', 'return']

    global numberOfTokens
    identifier = ""
    i = 0
    while (i<length):

        if content[i] == "/":
            i += 1
            if (i<length):
                if content[i] == "/":
                    i += 1
                    while((i<length) and (content[i] != "\n")):
                        i += 1
                    i += 1

                elif content[i] == "*":
                    i += 1
                    while ((i+1 < length)):
                        if content[i]+content[i+1] == "*/":
                            break
                        i += 1
                    i += 2

                else:
                    tokens.append("/")
                    i += 1
            continue

        if (content[i] == "\""):
            if identifier != "":
                tokens.append(identifier)
                identifier = ""

            string = "\""
            i += 1
            while content[i] != "\"":
                string += content[i]
                i += 1
            string += "\""
            tokens.append(string)
            i += 1
            continue

        if content[i] in symbols:
            if identifier != "":
                tokens.append(identifier)
                identifier = ""

            new_symbols = {"<": "&lt;", ">": "&gt;", "&": "&amp;"}
            if content[i] in new_symbols:
                tokens.append(new_symbols[content[i]])
                i += 1
                continue
            tokens.append(content[i])
            i += 1
            continue

        if content[i] == "\n":
            if identifier != "":
                tokens.append(identifier)
                identifier = ""
            i += 1
            continue

        if content[i] == " ":
            if identifier != "":
                tokens.append(identifier)
                identifier = ""
            i += 1
            continue

        if content[i] == "\t":
            if identifier != "":
                tokens.append(identifier)
                identifier = ""
            i += 1
            continue

        identifier += content[i]
        i += 1
    if identifier != "":
        tokens.append(identifier)
    numberOfTokens = len(tokens)
    input_file.close()
    return tokens, numberOfTokens