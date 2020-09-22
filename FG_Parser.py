#+============================================================================+
#| Imports and Constants:                                                     |
#+============================================================================+

import sys;
TAB = '\t';

#+============================================================================+
#| Declaration and Initialization of Global Variables:                        |
#+============================================================================+
outputFile = 'out.fprg';
inputFile = 'in.fgs';

if(sys.argv[1]=='-o'):
    inputFile = sys.argv[2];
    outputFile = sys.argv[3];
    if(inputFile=='' or outputFile==''):
        Expected('Input and/or Output File Names');
elif(sys.argv[1]=='make'):
    inputFile = sys.argv[2];
    outputFile = inputFile[:inputFile.find('.')]+'.fprg';
else:
    inputFile = sys.argv[1];
    if(inputFile == ''):
        Expected('Input File Name');

code='';
outputCode = '';
Index = 1;
Look = '';
lineIndex = 1;
depth = 0;

#+============================================================================+
#| Load code from File:                                                       |
#+============================================================================+

code = open(inputFile).read();

#+============================================================================+
#| FileOutput Stream - Loads to Global Variable "outputCode":                 |
#+============================================================================+

def out(s):
    global depth;
    global outputCode;
    for i in range(depth):
        outputCode = outputCode + '   ';
    outputCode = outputCode + s + '\n';

#+============================================================================+
#| Character Input Stream from Global Variable "code":                        |
#+============================================================================+

def getChar():
    global Index;
    global Look;
    global code;
    if(Index<=len(code)):
        Look = code[Index-1:Index];
        Index = Index+1;
    return Look;

#+============================================================================+
#| Error Handling Functions:                                                  |
#+============================================================================+

def Error(s):
    print();
    print('Error on line '+str(lineIndex)+': '+s);
    print('Found: '+Look);

def Abort(s):
    Error(s);
    exit();

def Expected(s):
    Abort('Expected: '+s);

#+============================================================================+
#| Character Handling Functions                                               |
#+============================================================================+

def exitCodes():
    global Look;
    if(Look=='\\'):
        getChar();
        if(Look=='n'):
            Look = '&#13;&#10;';
    elif(Look=='"'):
        Look = '&quot;';    
    elif(Look=='&'):
        Look = '&amp;';
    elif(Look=='<'):
        Look = '&lt;';
    elif(Look=='>'):
        Look = '&gt;';
    else:
        print(end='');

def Match(c):
    if(Look==c):
        getChar();
        skipWhite();
    else:
        Expected(c);

def newLine():
    global lineIndex;
    if(Look=='\n'):
        lineIndex = lineIndex+1;
        skipWhite();
        getChar();

def isAlpha(ch):
    if(ord(ch) >= 48 and ord(ch) <= 57):
        print(end='');
        #print('The Given Character', ch, 'is a Digit Character');
    elif((ord(ch) >= 65 and ord(ch) <= 90) or (ord(ch) >= 97 and ord(ch) <= 122)):
        print(end='');
        #print('The Given Character', ch, 'is an Alphabetic Character');
        return True;
    else:
        print(end='');
        #print('The Given Character', ch, 'is a Special Character');
    return False;

def isDigit(ch):
    if(ord(ch) >= 48 and ord(ch) <= 57):
        print(end='');
        #print('The Given Character', ch, 'is a Digit Character');
        return True;
    elif((ord(ch) >= 65 and ord(ch) <= 90) or (ord(ch) >= 97 and ord(ch) <= 122)):
        print(end='');
        #print('The Given Character ', ch, 'is an Alphabetic Character');
    else:
        print(end='');
        #print('The Given Character ', ch, 'is a Special Character');
    return False;

def isAlNum(ch):
    if(isDigit(ch) or isAlpha(ch)):
        return True;
    else:
        return False;

def isWhite(ch):
    if(ch==' ' or ch==TAB):
        return True;
    else:
        return False;

def skipWhite():
    while isWhite(Look):
        getChar();

#+============================================================================+
#| Multi-Character Getting Functions:                                         |
#+============================================================================+

def getName():
    global Look;
    stop=False;
    token = '';
    if(Look=='#'):
        token = '#';
    elif(Look=='\n'):
        token = '#n';
    elif(Look=='}'):
        token = '#n';
    else:
        if(isAlpha(Look)==False and Look!='[' and Look!=']'):
            Expected('Name or Token');
        elif(Look=='['):
            token = token+Look
            getChar();
            while(isDigit(Look)):
                token = token + Look;
                getChar();
            token = token +Look;
            getChar();
        else:
            while(isAlNum(Look)):
                token = token + Look;
                getChar();
        skipWhite();
    return token;


def getExpression():
    exp='';
    stop = False;
    while((Look==';')==False and stop==False): 
        if(Look=='\n'):
            Expected(';');
            stop=True;
        exitCodes();
        exp = exp + Look;
        getChar();
    skipWhite();
    return exp;

def getParameters():
    stop = False;
    param = '';
    while(Look!=')' and stop==False):
        if(Look=='\n'):
            Expected(';');
            stop=True;
        exitCodes();
        param = param + Look;
        getChar();
    skipWhite();
    return param;

def getString():
    stop = False;
    param = '';
    param = param+'&quot;';
    while(Look!='"' and stop==False):
        if(Look=='\n'):
            Expected('"');
            stop=True;
        exitCodes();
        param = param + Look;
        getChar();
    param = param+'&quot;';
    skipWhite();
    return param;

def getComment():
    comment = '';
    while(Look!='\n'):
        comment = comment + Look;
        getChar();
    newLine();
    skipWhite();
    if(Look=='#'):
        Match('#');
        comment = comment + '&#13;&#10;' + getComment();
    return comment;


def getNum():
    value = '';
    if (isDigit(Look)==False):
        Expected('Integer');
    while(isDigit(Look)):
        value = value + Look;
        getChar();
    skipWhite();
    return value;

#+============================================================================+
#| Primitive Types:                                                           |
#+============================================================================+

def parseTypes(s):
    if(s=='int'):
        return 'Integer';
    elif(s=='String'):
        return 'String';
    elif(s=='real'):
        return 'Real';
    elif(s=='bool'):
        return 'Boolean';
    else:
        Expected('Primative Type');


#+============================================================================+
#| Single Line Token Parsing Functions:                                       |
#+============================================================================+

def Declare(Type):
    skipWhite();
    array = 'False';
    size = '';
    name = getName();
    if(Type=='int'):
        Type = 'Integer';
    elif(Type=='real'):
        Type = 'Real';
    elif(Type=='bool'):
        Type = 'Boolean';

    if(name[0]=='['):
        size = name[1:-1];
        array = 'True';
        skipWhite();
        name = getName();
    Match(';');
    out('<declare name=\"'+name+'\" type=\"'+Type+'\" array=\"'+array+'\" size=\"'+size+'\"/>');

def Assignment(name):
    skipWhite();
    if(Look=='['):
        name = name+getName();
    Match('=');
    exp = getExpression();
    Match(';');
    out('<assign variable=\"'+name+'\" expression=\"'+exp+'\"/>');

def Input():
    Match('(');
    param = getParameters();
    Match(')');
    Match(';');
    out('<input variable=\"'+param+'\"/>');

def Output():
    Match('(');
    param = '';
    while(Look!=')'):
        while(Look=='(' or Look=='\"' or Look=='&'):
            if(Look=='\"'):
                Match('\"');
                param = param + getString();
                Match('\"');
            elif(Look=='('):
                Match('(');
                param = param + getParameters();
                Match(')');
            elif(Look=='&'):
                Match('&');
                param = param + '&amp;';
                skipWhite();
            elif(Look=='\n'):
                Expected('Parameter');
        if(Look!=')'):
            param = param + getName();
            skipWhite();
    Match(')');
    Match(';');
    out('<output expression=\"'+param+'\" newline=\"True\"/>');

def Call():
    Match('(');
    name = getName();
    param = '';
    if(Look=='('):
        Match('(');
        param = getParameters();
        Match(')');
    else:
        Expected('Function call parameters');
    if(param!=''):
        param = '('+param+')';
    Match(')');
    Match(';');
    out('<call expression=\"'+name+param+'\"/>');

def Comment():
    Match('#');
    comment = getComment();
    out('<comment text=\"'+comment+'\"/>');

#+============================================================================+
#| Container Token Parsing Functions:                                         |
#+============================================================================+

def Function():
    global depth;
    skipWhite();
    returnType = getName();
    if(returnType!='void'):
        returnType = parseTypes(returnType);
    else:
        returnType = 'None';
    skipWhite();
    if(Look=='('):
        Match('(');
        returnVar = getParameters();
        Match(')');
        skipWhite();
    else:
        Expected('Parameters for Function');
    name = getName();
    skipWhite();
    out('<function name=\"'+name+'\" type=\"'+returnType+'\" variable=\"'+returnVar+'\">');
    paramName = '';
    paramType = '';
    paramArray = 'False';
    if(Look=='('):
        Match('(');
        if(Look==')'):
            depth = depth + 1;
            out('<parameters/>');
            depth = depth - 1;
        else:
            depth = depth + 1;
            out('<parameters>');
            depth = depth + 1;
            while(Look!=')'):
                skipWhite();
                paramArray = 'False';
                paramType = parseTypes(getName());
                if(Look=='['):
                    Match('[');
                    Match(']');
                    paramArray = 'True';
                paramName = getName();
                out('<parameter name=\"'+paramName+'\" type=\"'+paramType+'\" array=\"'+paramArray+'\"/>');
                skipWhite();
                if(Look!=')'):
                    Match(',');
            depth = depth - 1;
            out('</parameters>');
            depth = depth - 1;
        Match(')');
        skipWhite();
    else:
        Expected('Parameters for Function');   
    if(Look=='{'):
        Match('{');
        depth = depth+1;
        out('<body>');
        depth = depth + 1;
        while(Look!='}'):    
            token();
            newLine();
            skipWhite();
        Match('}');
        depth = depth - 1;
        out('</body>');
        depth = depth - 1;
        out('</function>');
    else:
        Expected('Function Container');
    

def While():
    global depth;
    skipWhite();
    param = '';
    if(Look=='('):
        Match('(');
        while(Look!=')'):
            while(Look=='('):
                Match('(');
                param = param + getParameters();
                Match(')');
            skipWhite();
            if(Look!=')'):
                param = param +' '+getName()+' ';
    else:
        Expected('Expression in While Loop');
    Match(')');
    out('<while expression=\"'+param+'\">');
    if(Look=='{'):
        Match('{');
        depth = depth + 1;
        while(Look!='}'):
            token();
            newLine();
            skipWhite();
        Match('}');
        depth = depth - 1;
        out('</while>');
    else:
        Expected('While Loop Container');

def For():
    global depth;
    skipWhite();
    if(Look=='('):
        Match('(');
        countVarName = getName();
        startCount = '';
        endCount = '';
        increment = '';
        direction = 'inc';
        if(Look==';'):
            Match(';');
            Match('(');
            startCount = getNum();
            Match(',');
            endCount = getNum();
            Match(')');
        else:
            Expected('Range Parameters in For Loop');
        if(Look==';'):
            Match(';');
            increment = getParameters();
            if(increment.find('-')!=-1):
                increment = increment[1:];
                direction = 'dec'
        else:
            Expected('Increment Parameter in For Loop');
        Match(')');
        skipWhite();
    else:
        Expected('Parameters in For Loop');
    out('<for variable=\"'+countVarName+'\" start=\"'+startCount+'\" end=\"'+endCount+'\" direction=\"'+direction+'\" step=\"'+increment+'\">');
    if(Look=='{'):
        Match('{');
        depth = depth + 1;
        while(Look!='}'):
            token();
            newLine();
            skipWhite();
        Match('}');
        depth = depth - 1;
        out('</for>');
    else:
        Expected('For Loop Container');

def If():
    global depth;
    skipWhite();
    param = '';
    if(Look=='('):
        Match('(');
        while(Look!=')'):
            while(Look=='('):
                Match('(');
                param = param + getParameters();
                Match(')');
            skipWhite();
            if(Look!=')'):
                param = param +' '+ getName()+' ';
    else:
        Expected('Expression in If Statement');
    Match(')');
    out('<if expression=\"'+param+'\">');
    depth = depth + 1;
    if(Look=='{'):
        out('<then>');
        Match('{');
        depth = depth + 1;
        while(Look!='}'):
            token();
            newLine();
            skipWhite();
        Match('}');
        depth = depth - 1;
        out('</then>');
        tok = getName();
        if(tok=='else'):
            Match('{');
            out('<else>');
            depth = depth + 1;
            while(Look!='}'):
                token();
                newLine();
                skipWhite();
            Match('}');
            depth = depth - 1;
            out('</else>');
        else:
            Expected('Else Statement after If Statement');
    depth = depth - 1;
    out('</if>');

#+============================================================================+
#| Find Tokens:                                                               |
#+============================================================================+

def token():
    if(Index>=len(code)):
        exit();
    skipWhite();
    name = getName();
    if(name=='def'):
        Function();
    elif(name=='#'):
        Comment();
    elif(name=='#n'):
        print(end=''); 
    elif(name=='if'):
        If();
    elif(name=='while'):
        While();
    elif(name=='for'):
        For();
    elif(name=='call'):
        Call();
    elif(name=='input'):
        Input();
    elif(name=='output'):
        Output();
    elif(name=='int' or name=='String' or name=='real' or name=='bool'):     
        Declare(name);
    else:
        Assignment(name);
    skipWhite();

#+=============================================================================+
#| Initialize Parser:                                                          |
#+=============================================================================+

def Init():
    getChar();
    skipWhite();
    Prefixes();
    while(Index<=len(code)):
        token();
        newLine();
    End();

#+============================================================================+
#| Create XML Header:                                                         |
#+============================================================================+

def Prefixes():
    global depth;
    out('<?xml version=\"1.0\"?>');
    out('<flowgorithm fileversion="2.11">');
    depth = depth+1;    
    out('<attributes>');
    depth = depth + 1;        
    out('<attribute name="name" value=""/>');
    out('<attribute name="authors" value="Generated by FlogoScript Parser"/>');
    out('<attribute name="about" value="FlowgoScript Parser is made by JustBobinAround, Check it out on github: https://github.com/JustBobinAround/Flowgorithm-Save-File-Parser"/>');
    out('<attribute name="saved" value="2020-00-00 00:00:00 APM"/>');
    out('<attribute name="created" value="emVsdGVrO3plbHRlay1QQzsyMDIwLTA5LTA5OzA5OjUwOjMwIFBNOzI3ODU="/>');
    out('<attribute name="edited" value="emVsdGVrO3plbHRlay1QQzsyMDIwLTA5LTA5OzEwOjEyOjI2IFBNOzM7Mjg5MA=="/>');
    depth = depth - 1;
    out('</attributes>');
    
#+============================================================================+
#| Write Output Code to File:                                                 |
#+============================================================================+

def End():
    global depth;
    global outputCode;
    global outputFile;
    depth = depth - 1;
    out('</flowgorithm>');
    code = open(outputFile,"a").write(outputCode);

#+============================================================================+
#| Starting Parser Starts Here:                                               |
#+============================================================================+

Init();
exit();
