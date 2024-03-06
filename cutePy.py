####################        --      INFORMATION     --      ####################


## Member  : Simon Goni                   
## Member  : Spilios Spiliopoulos                  



import time
import sys
import os

## for execution time: ##
start_time = time.time()
 

letters =       [ 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                  'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z' ]

numbers =       [ '0','1','2','3','4','5','6','7','8','9']

addOp   =       ['+','-']

mulOp   =       ['*','/','//']
operators =     {"+":"add","-":"sub","*" :"mul","/":"div"}
relOp     =     {"=" :"beq","!=":"bne",">" :"bgt","<":"blt",">=":"bge","<=":"ble"}

equal =         ['=']

not_eq =        ['!']

smaller =       ['<']

larger =        ['>']

group_symbols = ['(',')','[',']']

hashgroup =     ['{','}']

hashtag =       ['#']

dollar =        ['$']

empty =         ['\n','\t',' ','']

delimiters =    [';',':','.','"',',']

underscore =    ['_']

                                                                
                                                                    ## FOR CHARACTERS  ##

marked =        ['!','=','/','<','>']                            


                                                                    ##    FOR WORDS    ##
reserved_words = ['if','else','not','and','or','main','#declare','while','return','print','def','int','input','__name__','"__main__"'] 





## Lists for Lex() ##

results     = []

word_tokens = []

line_words  = []

 
## Lists for Syn() ##

main_functions_ids  = []

def_functions_ids   = []

identifiers         = []





## This fucntion's purpose is to assign the Tag/Family based on a given word and its character_tokens that make it up
## checking the first index and if the word does not aply any of the rules, it gets assigned with a 'not_valid' token
## If there are words with a not valid token, we already have an error occuring, which we check for after Lex() and before Syn()

def tag_maker(word_tokens):

    if word_tokens:
        if word_tokens[0] == 'char':
            for i in range(0,len(word_tokens)):
                    if word_tokens[i] == 'char' or word_tokens[i] == 'num' or word_tokens[i] == 'underscore':
                        word_token = 'identifier'
    
                    else:
                        word_token = 'not_valid'
                        print("ERROR: Can only have 'char', 'num', 'under' type tokens if the first token is 'char' type ")
                        break
     
        elif word_tokens[0] == 'num' :
            for i in range(0,len(word_tokens)):
                if word_tokens[i] == 'num':
                    word_token = 'num'
                else: 
                    word_token = 'not_valid'
                    print("ERROR: cant have anything but 'num' type tokens if the first token is 'num' type'")
                    break
        
   
        elif word_tokens[0] == 'addOP':
            if len(word_tokens) == 1:
                word_token = 'addOP'
            else:
                word_token = 'not_valid'
        
        elif word_tokens[0] == 'smaller' :

            if len(word_tokens) == 2:

                if word_tokens[1] == 'equal':
                    word_token = 'relOP'
                
                else:
                    word_token = 'not_valid'
                    print("ERROR: can have only '=' token with '<' s")
            
            elif len(word_tokens) == 1:
                word_token = 'relOP'
            
            else: 
                word_token = 'not_valid'
                print("ERROR: Can have only smaller or smaller_equal ")

        elif word_tokens[0] == 'divOP':
            
            if len(word_tokens) == 2:
                if word_tokens[1] == 'divOP':
                    word_token = 'mulOP'
                else:
                    word_token = 'not_valid'
            else:
                word_token='not_valid'
        
        
        elif word_tokens[0] == 'mulOP':
            
            if len(word_tokens) == 1:
                    word_token = 'mulOP'
            else:
                word_token='not_valid'
        

                
        
        elif word_tokens[0] == 'larger':

            if len(word_tokens) == 2:

                if word_tokens[1] == 'equal':
                    word_token = 'relOP'

                else:
                    word_token = 'not_valid'
                    print("ERROR: can have only '=' token with '>' ")
            
            elif len(word_tokens) == 1:
                word_token = 'relOP'
            else:
                word_token = 'not_valid'
                print("ERROR: Can have only larger or larger_equal ")
            

        elif word_tokens[0] == 'equal':

            if len(word_tokens) == 2:

                if word_tokens[1] == 'equal':
                    word_token = 'relOP'
                
                
                else:
                    word_token = 'not_valid'
                    print("ERROR: can have only '=' token with '=' ")
            
            elif len(word_tokens) == 1:
                word_token = 'assignment'
            else: 
                word_token = 'not_valid'
                print("ERROR: Can have only assignment or equality ")
            
        
        elif word_tokens[0] == 'not_equal':

            if len(word_tokens) == 2:

                if word_tokens[1] == 'equal':
                    word_token = 'relOP'
                
                else:
                    word_token = 'not_valid'
                    print("ERROR: '!' without '=' is not allowed")
                    
            else:
                word_token = 'not_valid'
                print("ERROR: '!' without '=' is not allowed")
            

        
        elif word_tokens[0] == 'group':
            if len(word_tokens) == 1:
                word_token = 'group_symbol'
            else:
                word_token = 'not_valid'
                print("Error: Group symbols should be only 1 character")
        
        elif word_tokens[0] == 'delimiter':

            if len(word_tokens) == 1 :
                word_token = 'delimiter'
            else:
                word_token = 'not_valid'
                ## Except from reserved word : ""__main__"" (which we check later)
    
                

        elif word_tokens[0] == 'hashtag':

            if len(word_tokens) == 2:

                if word_tokens[1] == 'agk':
                    word_token = 'parenthesis'
                
                elif word_tokens[1] == 'dollar':
                    word_token = 'comments'
                
                else:
                    word_token = 'not_valid'
                    print("ERROR: Hastag can only have  'agk'({) or 'dollar'($) in the same word ")
            else:
                word_token = 'not_valid'
                ## Except from reserved word :#delcare (which we check later)
                
        
        ## we dont need that 
        elif word_tokens[0] == 'empty':

            print("Empty characters shouldnt be part of word_tokens")

        ## We dont need that
        elif word_tokens[0] == 'tab':
            print("Empty characters shouldnt be part of word_tokens")
            

        elif word_tokens[0] == 'underscore':
            word_token = 'not_valid'
            ## Except from resreved word: __name__ (which we check later)
                
        else:
            word_token = 'not_valid'
            print("Error: couldnt recognize symbol")

        return word_token

    else:
        print("Word_tokens list is empty")
        
    

## This fucntion's purpose is to create words based on a text file which has to be .cpy only. Then it analyzes every character and creates words
## which : 1) are sent to tag_maker(word_tokens) to create a Tag/Family for the current word and 2) afterwards stores the current word with
## its Tag and line in the form of a list[word,tag,line] inside another list named results[]

def Lex() :

    ## INITIALIZE ##
    
    characters = ''     # the character to be examined

    word = ''           # word with all characters

    tag = ''            # set tag to empty

    line = 1

    ## For second argument
    filename = sys.argv[1]
    print("Filename = ",filename)


    ## Check if we got a .cpy file extension
    if filename.endswith(".cpy") == False :
        print("ERROR: Expected a '.cpy' extension as second argument but instead got :",filename)
        sys.exit()

    # Check if the file exists in the current directory
    if os.path.exists(filename):
        # If the file exists, print its full path
        full_path = os.path.abspath(filename)
        print("Full path = ", full_path)
    else:
        print("File not found in current directory.")
        sys.exit()


    # Open file with read permissions
    with open(filename, 'r') as file: 

        # Always read the 1st character
        while True:
             
            characters = file.read(1)
            
            # If EOF
            if not characters:

                ## PREVIOUS WORD ##
                if word !='':
                    tag = tag_maker(word_tokens)
                    results.append([word,tag,line])

                    word_tokens.clear()

                ## Clear Everything after it ends
                word_tokens.clear()
                word = ''
                tag = ''
                break  


            # if word_tokens list is empty
            if not word_tokens:

                if (characters in numbers):
                    character_token = 'num'
                    word_tokens.append(character_token)
                    word = characters
                
            
                elif characters in letters:
                    character_token = 'char'

                    ## FOR CURRENT WORD ##
                    word_tokens.append(character_token)
                    word = characters
                    
                
                elif characters in addOp:
                    character_token = 'addOP'

                    ## FOR CURRENT WORD ( = '+') ##
                    word_tokens.append(character_token)
                    tag = tag_maker(word_tokens)
                    word = characters
                    results.append([word,tag,line])

                    ## CLEAR ##
                    word = ''
                    word_tokens.clear()
                
                elif characters in mulOp:
                    if characters == '*':
                        character_token = 'mulOP'

                        ## FOR CURRENT WORD ( = '*') ##
                        word_tokens.append(character_token)
                        tag = tag_maker(word_tokens)
                        word = characters
                        results.append([word,tag,line])
                        
                        ## CLEAR ##
                        word = ''
                        word_tokens.clear()
                    
                    else:
                        ## FOR CURRENT WORD ( = '/') ##
                        character_token = 'divOP'
                        word_tokens.append(character_token)
                        word = characters

                elif characters in smaller:

                    ## FOR CURRENT WORD ##
                    character_token = 'smaller'
                    word_tokens.append(character_token)
                    word = characters
                
                elif characters in larger:

                    ## FOR CURRENT WORD ##
                    character_token = 'smaller'
                    word_tokens.append(character_token)
                    word = characters


                elif characters in equal:
                    character_token = 'equal'

                    ## FOR CURRENT WORD ##
                    word = characters
                    word_tokens.append(character_token)


                elif characters in not_eq:
                    character_token = 'not_equal'
                    
                    ## FOR CURRENT WORD ##
                    word = characters
                    word_tokens.append(character_token)

                
                elif characters in group_symbols:
                    character_token = 'group'

                    ## FOR CURRENT WORD ##
                    word = characters
                    word_tokens.append(character_token)
                    tag = tag_maker(word_tokens)
                    results.append([word,tag,line])

                    ## CLEAR ##
                    word = ''
                    word_tokens.clear()
                
                elif characters in hashtag:
                    character_token= 'hashtag'
                    
                    ## FOR CURRENT WORD ##
                    word_tokens.append(character_token)
                    word = characters
                
                elif characters in dollar:
                    character_token = 'dollar'

                    ## FOR CURRENT WORD ##
                    word = characters
                    word_tokens.append(character_token)
                    tag = tag_maker(word_tokens)
                    results.append([word,tag,line])

                    ## CLEAR ##
                    word = ''
                    word_tokens.clear()
                    
                
                elif characters in hashgroup:
                    character_token = 'agk'

                    ## FOR CURRENT WORD ##
                    word = characters
                    word_tokens.append(word_tokens)
                    tag = tag_maker(word_tokens)
                    results.append([word,tag,line])

                    ## CLEAR ##
                    word = ''
                    word_tokens.clear()


                elif characters in empty:

                    if characters == '\n':
                        ## Count lines based on '\n' character
                        line = line + 1

                        ## IGNORE AND GET READY FOR THE NEXT WORD ##
                        ## CLEAR ##
                        word = ''
                        word_tokens.clear()

                    else: 
                        ## IGNORE AND GET READY FOR THE NEXT WORD ##
                        ## CLEAR ##
                        word = ''
                        word_tokens.clear()
                
                elif characters in delimiters:
                    character_token = 'delimiter'

                    if characters != '"': 
                        ## FOR CURRENT WORD ##
                        word = characters
                        word_tokens.append(character_token)
                        tag = tag_maker(word_tokens)
                        results.append([word,tag,line])
                        
                         ## CLEAR ##
                        word = ''
                        word_tokens.clear()
                    
                    else:
                        ## Just so we can create ' "__main__" '
                        word = characters
                        word_tokens.append(character_token)

                   
                
                elif characters in underscore:
                    character_token = 'underscore'
                    word = characters
                    word_tokens.append(character_token)

                    ## IF WORD CANT START WITH UNDER SCORE ##
                    #results.append(word)
                    #Tag_Maker(word_tokens)
                    
                    # word = ''
                    #word_tokens.clear()
                
                else:
                    ## It gets here only for characters that are not part of our language
                    print('Word_token list is empty, but we have an unreconginzed character: '+characters+' in line :',line)
                    raise ValueError("Unrecognized character",characters)


                    

                ## LIST IS NOT EMPTY ##
            else:
                
                if (characters in numbers):
                    character_token = 'num'

                    ## if the last character not in marked list
                    if word[-1] not in marked:

                        ## FOR CURRENT WORD ##
                        word = word + characters
                        word_tokens.append(character_token)
                    
                    else:
                        ## FOR PREVIOUS WORD ##
                        tag= tag_maker(word_tokens)
                        results.append([word,tag,line])

                        ## CLEAR ##
                        word_tokens.clear()

                        ## FOR CURRENT WORD ##
                        word = characters
                        word_tokens.append(character_token)


                elif characters in letters:
                    character_token ='char'
                    if word[-1] not in marked:
                        
                        ## FOR CURRENT WORD ##
                        word = word + characters
                        word_tokens.append(character_token)
                    
                    else:
                        
                        ## FOR PREVIOUS WORD ##
                        tag = tag_maker(word_tokens)
                        results.append([word,tag,line])

                        ## CLEAR ##
                        word_tokens.clear()

                        ## FOR CURRENT WORD ##
                        word = characters
                        word_tokens.append(character_token)


                    


                elif characters in addOp:
                    character_token = 'addOP'

                    ## FOR PREVIOUS WORD ##
                    tag = tag_maker(word_tokens)
                    results.append([word,tag,line])

                    ## CLEAR ##
                    word_tokens.clear()
                    
                    ## FOR CURRENT WORD ##
                    word = characters
                    word_tokens.append(character_token)
                    tag = tag_maker(word_tokens)
                    results.append([word,tag,line])

                    
                    word = ''
                    word_tokens.clear()
                



                    
                elif characters in mulOp:
                    if characters == '*':
                        character_token = 'mulOP'

                        ## FOR PREVIOUS WORD ##
                        tag = tag_maker(word_tokens)
                        results.append([word,tag,line])

                        ## CLEAR ##
                        word_tokens.clear()

                        ## FOR CURRENT WORD #
                        word = characters
                        word_tokens.append(character_token)
                        tag = tag_maker(word_tokens)
                        results.append([word,tag,line])

                        ## CLEAR ##
                        word = ''
                        word_tokens.clear()

                    else:

                        character_token = 'divOP'

                        if word[-1] != '/':

                            ##  FOR PREVIOUS WORD ##
                            tag = tag_maker(word_tokens)
                            results.append([word,tag,line])

                            ## CLEAR ##
                            word_tokens.clear()

                            ## FOR CURRENT WORD ##
                            word = characters
                            word_tokens.append(character_token)
                        

                        else:

                            ## FOR CURRENT WORD ##
                            word = word + characters
                            word_tokens.append(character_token)
                            tag = tag_maker(word_tokens)
                            results.append([word,tag,line])

                            ## CLEAR ##
                            word = ''
                            word_tokens.clear()
                            
                
                elif characters in smaller:
                    character_token = 'smaller'

                    ## FOR PREVIOUS WORD ##
                    tag = tag_maker(word_tokens)
                    results.append([word,tag,line])

                    ## CLEAR ##
                    word_tokens.clear()

                    ## FOR CURRENT WORD ##
                    word = characters
                    word_tokens.append(character_token)

                elif characters in larger:
                    character_token = 'larger'

                    ## FOR PREVIOUS WORD ##
                    tag = tag_maker(word_tokens)
                    results.append([word,tag,line])

                    ## CLEAR ##
                    word_tokens.clear()

                    ## FOR CURRENT WORD ##
                    word = characters
                    word_tokens.append(character_token)


                elif characters in equal:
                    character_token = 'equal'

                    if word[-1] == '=' :    # or word[-1] == '!'
                        
                        ## FOR CURRENT WORD ##
                        word = word + characters
                        word_tokens.append(character_token)
                        tag = tag_maker(word_tokens)
                        results.append([word,tag,line])

                        ## CLEAR ##
                        word = ''
                        word_tokens.clear()
                    
                    elif word[-1] == '!':

                        ## FOR CURRENT WORD ##
                        word = word + characters
                        word_tokens.append(character_token)
                        tag = tag_maker(word_tokens)
                        results.append([word,tag,line])

                        ## CLEAR ##
                        word = ''
                        word_tokens.clear()
                    
                    elif word[-1] == '>':

                        ## FOR CURRENT WORD ##
                        word = word + characters
                        word_tokens.append(character_token)
                        tag = tag_maker(word_tokens)
                        results.append([word,tag,line])

                        ## CLEAR ##
                        word = ''
                        word_tokens.clear()
                    
                    elif word[-1] == '<':

                        ## FOR CURRENT WORD ##
                        word = word + characters
                        word_tokens.append(character_token)
                        tag = tag_maker(word_tokens)
                        results.append([word,tag,line])

                        ## CLEAR ##
                        word = ''
                        word_tokens.clear()
                    
                    else:

                        ## FOR PREVIOUS WORD ##
                        tag = tag_maker(word_tokens)
                        results.append([word,tag,line])

                        ## CLEAR ##
                        word_tokens.clear()


                        ## FOR CURRENT WORD ##
                        word = characters
                        word_tokens.append(character_token)
                
                elif characters in not_eq:
                    character_token = 'not_equal'
                    
                    ## FOR PREVIOUS WORD ##
                    tag = tag_maker(word_tokens)
                    results.append([word,tag,line])

                    ## CLEAR ##
                    word_tokens.clear()

                    ## FOR CURRENT WORD ##
                    word = characters
                    word_tokens.append(character_token)
                
                elif characters in group_symbols:
                    character_token = 'group'

                    ## FOR PREVIOUS WORD ##
                    tag = tag_maker(word_tokens)
                    results.append([word,tag,line])

                    ## CLEAR ##
                    word_tokens.clear()


                    ## FOR CURRENT WORD ##
                    word = characters
                    word_tokens.append(character_token)
                    tag = tag_maker(word_tokens)
                    results.append([word,tag,line])

                    ## CLEAR ##
                    word = ''
                    word_tokens.clear()
                
                elif characters in hashtag:
                        character_token = 'hashtag'

                        ## FOR PREVIOUS WORD ##
                        tag = tag_maker(word_tokens)
                        results.append([word,tag,line])

                        ## CLEAR ##
                        word_tokens.clear()

                        ## FOR CURRENT WORD ##
                        word = characters
                        word_tokens.append(character_token)
                
                elif characters in dollar:
                    character_token = 'dollar'

                    if word[-1] == '#':

                        ## FOR CURRENT WORD ##
                        word = word + characters
                        word_tokens.append(character_token)
                        tag = tag_maker(word_tokens)
                        results.append([word,tag,line])

                        ## CLEAR ##
                        word = ''
                        word_tokens.clear()
                        
                    else:

                        ## FOR PREVIOUS WORD ##
                        tag = tag_maker(word_tokens)
                        results.append([word,tag,line])

                        ## CLEAR ##
                        word_tokens.clear()

                        ## FOR CURRENT WORD ##
                        word = characters
                        word_tokens.append(character_token)
                        tag = tag_maker(word_tokens)
                        results.append([word,tag,line])

                        ## CLEAR ##
                        word = ''
                        word_tokens.clear()
                        
                
                elif characters in hashgroup:
                    character_token = 'agk'

                    if word[-1] == '#':

                        ## FOR CURRENT WORD ##
                        word = word + characters
                        word_tokens.append(character_token)

                        tag = tag_maker(word_tokens)
                        results.append([word,tag,line])

                        ## CLEAR ##
                        word = ''
                        word_tokens.clear()
                    
                    else:

                        ## FOR PREVIOUS WORD ##
                        tag = tag_maker(word_tokens)
                        results.append([word,tag,line])

                        ## CLEAR ##
                        word_tokens.clear()

                        ## FOR CURRENT WORD ##
                        word = characters
                        word_tokens.append(character_token)
                        tag = tag_maker(word_tokens)
                        results.append([word,tag,line])

                        ## CLEAR ##
                        word = ''
                        word_tokens.clear()
                
                elif characters in empty:
                    if characters == '\n':
                        
                        ## FOR PREVIOUS WORD ##
                        tag = tag_maker(word_tokens)
                        results.append([word,tag,line])

                        ## CLEAR ##
                        word = ''
                        word_tokens.clear()

                        ## FOR CURRENT WORD ##
                        line = line + 1

                    
                    else:
                        
                        ## FOR PREVIOUS WORD ##
                        tag = tag_maker(word_tokens)
                        results.append([word,tag,line])

                        ## FOR CURRENT WORD ##
                        ## CLEAR ## 
                        word = ''
                        word_tokens.clear()
                
                elif characters in delimiters:
                    character_token = 'delimiter'
                    
                    if characters != '"':
                        ## FOR PREVIOUS WORD ## 
                        tag = tag_maker(word_tokens)
                        results.append([word,tag,line])

                        ## CLEAR ## 
                        word_tokens.clear()

                        ## FOR CURRENT WORD ##
                        word = characters
                        word_tokens.append(character_token)
                        tag = tag_maker(word_tokens)
                        results.append([word,tag,line])

                        ## CLEAR ##
                        word = ''
                        word_tokens.clear()
                    
                    else:
                        ## FOR CURRENT WORD ## 
                        word = word + characters
                        word_tokens.append(character_token)


                elif characters in underscore:
                    character_token = 'underscore'

                    if word[-1] not in marked:

                        ## FOR CURRENT WORD ##
                        word = word + characters
                        word_tokens.append(character_token)
                    

                    else:

                        ## FOR PREVIOUS WORD ##
                        tag = tag_maker(word_tokens)
                        results.append([word,tag,line])

                        ## CLEAR ##
                        word_tokens.clear()

                        ## FOR CURRENT WORD ## (We need to figure out where and when underscore is valid to use)
                        word = characters
                        word_tokens.append(character_token)


                else:
                    ## It gets here only for characters that are not part of our language
                    print('List is not empty, but we have an unreconginzed character: '+characters+' in line :',line)
                    raise ValueError("Unexpected character",characters)

    ## Lex is ready 
    print('Results list is ready from Lex ')
    return
  


global current_index
current_index = 0


#	                       Synarthseis Endiamesou kwdika:		              #
###############################################################################	


QuadsList = []  # lista me Oles tis tetrades pou tha paraxthoun apo to programma.
quadList = []   # gia teliko kwdika
QuadsCounter = 1  # O arithmos pou xarakthrizei thn tetrada. Brisketai mprosta apo thn 4ada.


def nextQuad():             # returns the next quad
    global QuadsCounter
    return QuadsCounter


def genQuad(first, second, third, fourth): # create a quad in a list
    global QuadsCounter
   
    QuadsList.append([nextQuad(),  first ,second, third, fourth])
    quadList.append([nextQuad(), first , second, third, fourth])
    # Bazw prwta ton arithmo. Epeita ta orismata
    QuadsCounter += 1  
    return [nextQuad(), first , second, third, fourth]


T_i = 1
VarTempList = [] #This was responsible for c file but is not necessary


def newTemp():          # crate new temporary variable
    global T_i, VarTempList
    
    Var_temp =  'T_' + str(T_i)
    T_i += 1
    # Save them in VarTempList
    VarTempList += [Var_temp]

    # create Entity for Temporary Variable
    T = TemporaryVariable()
    T.name = Var_temp
    T.type = "TEMP"
    T.dataType = 'Int'
    T.offset = compute_offset()
    add_entity(T)

    return Var_temp


def emptyList():  # return an empty list
    return []


def makeList(label): # make a list with this label
    return [label]


def merge(list1, list2): # concatenate two lists
    return list1 + list2


def backPatch(list, z): 
   
    global QuadsList

    for i in range(len(list)):                    # gia kathe item ths list  
        for j in range(len(QuadsList)): # gia kathe quad ths quadlist
            # Briskoume tetrada me sygkekrimeno label kai sto telos tou pername thn parametro z
            if (list[i] == QuadsList[j][0]): # mporei kai na paralhftei
                QuadsList[j][4] = z
                break  
    
    for i in range(len(list)):                    # gia kathe item ths list  
        for j in range(len(quadList)): # gia kathe quad ths quadlist
            # Briskoume tetrada me sygkekrimeno label kai sto telos tou pername thn parametro z
            if (list[i] == quadList[j][0]): # mporei kai na paralhftei
                quadList[j][4] = z
                break
    return


###############################################################################
#	Synarthseis PINAKA SYMBOLWN:											  #
###############################################################################	
class Entity():
    def __init__(self):
        self.name = ''
        self.type = '' #"VAR" or 'FUNC' or 'PARAM' or 'TEMP' or 'PROC'


class FormalParameter(Entity):  # Arguments
    def __init__(self):
        super().__init__()
        self.dataType = 'Int'
        self.mode = ''  # eite 'cv' eite 'ref'


class Variable(Entity):

    def __init__(self):
        super().__init__()
        self.datatype = 'Int'
        self.offset = 0

#Not needed but created 
class Procedure(Entity):
    def __init__(self):
        super().__init__()
        self.startingQuad = 0
        self.frameLength = 0
        self.argumentList = []  # h lista parametrwn


class Function(Procedure):
    def __init__(self):
        super().__init__()  # 'Procedure' h' 'Function' .
        self.datatype = ''

#cutePy supports only CV
class Parameter(Variable, FormalParameter):
    def __init__(self):
        Variable().__init__()
        FormalParameter().mode = ''  # 'CV', 'REF'


class TemporaryVariable(Entity):
    def __init__(self):
        super().__init__()
        self.datatype = 'Int'
        self.offset = 0


class Scope():
    def __init__(self):
        self.entityList = []  # h lista apo entities
        self.level = 0  # Bathos fwliasmatos


class Table():
    def __init__(self):
        self.scopes = []


def add_argument(object):  # SubProg : flag gia na xerw an eimai se function h procedure
    'Add given object to list'
    global table

    # Tha pame sto teleutaio entity(pou tha einai procedure h function) kai ekei sto pedio
    # argumentList tha kanoume append to object

    table.scopes[-1].entityList[-1].argumentList.append(object)

def add_entity(object):  # ftiaxnw entity
    'Add given object to list'
    global table

    table.scopes[-1].entityList.append(object)  # bazei sto telos ths listas apo entities to kainourgio entity pou dhmiourghthhke

def add_scope(name):  # ftiaxnw kyklo
    global table

    if not len(table.scopes):
        scopeZero = Scope()  # otan prosthetoume prwth fora scope
        table.scopes.append(scopeZero)
    else:
        nextLevelScope = Scope()
        nextLevelScope.level = (table.scopes[-1].level) + 1  # to epomeno scope +1 level se sxesh me to prohgoumeno
        table.scopes.append(nextLevelScope)  # to prosthetoume sth lista

def compute_offset():
    global table

    counter = 0  # mono gia entites me 'VAR' or 'PARAM' or 'TEMP'

    if len(table.scopes[-1].entityList) > 0:
        for i in range(len(table.scopes[-1].entityList)):
            if (table.scopes[-1].entityList[i].type == "VAR" or table.scopes[-1].entityList[i].type == "TEMP" or table.scopes[-1].entityList[i].type == "PARAM"):
                counter += 1

    offset = 12 + (counter * 4)
    return offset

def add_parameters():  # kaleite stin "block" amesos meta tin "add_scope" kai metatrepei ta orismata tou apo katw epipedou se entitties sto top Scope

    # proteleuataio scope (katw tou top scope)
    for arg in range(len(table.scopes[-2].entityList[-1].argumentList)):
        E = Parameter()
        E.name = table.scopes[-2].entityList[-1].argumentList[arg].name
        E.type = "PARAM"
        E.dataType = "Int"
        E.mode = table.scopes[-2].entityList[-1].argumentList[arg].mode
        E.offset = compute_offset()
        add_entity(E)


def extract_symbolic_table():
    global table

    # anoigma arxeiou gia grapsimo sto telos kathe fora pou to anoigoume
    f = open("test.symb", "a")

    for i in range(len(table.scopes)):
        f.write("SCOPE: " + str(table.scopes[i].level) + "\n")
        f.write("\tENTITIES:" + "\n")
        counter_Entities = 0
        for ent in table.scopes[i].entityList:
            if (ent.type == 'VAR'):
                counter_Entities += 1
                f.write("\tENTITY{" + str(
                    counter_Entities) + "}: " + " NAME:" + ent.name + "\t TYPE:" + ent.type + "\t VARIABLE-TYPE:" + ent.dataType + "\t OFFSET:" + str(
                    ent.offset) + "\n")
            elif (ent.type == 'TEMP'):
                counter_Entities += 1
                f.write("\tENTITY{" + str(
                    counter_Entities) + "}: " + " NAME:" + ent.name + "\t TYPE:" + ent.type + "\t Temporary VARIABLE-TYPE:" + ent.dataType + "\t OFFSET:" + str(
                    ent.offset) + "\n")
            elif (ent.type == 'PAR'):
                counter_Entities += 1
                f.write("\tENTITY{" + str(
                    counter_Entities) + "}: " + " NAME:" + ent.name + "\t TYPE:" + ent.type + "\t PARAMETER-TYPE:" + ent.dataType + "\t MODE:" + ent.mode + "\t OFFSET:" + str(
                    ent.offset) + "\n")
            elif (ent.type == "FUNC"):
                counter_Entities += 1
                f.write("\tENTITY{" + str(
                    counter_Entities) + "}: " + " NAME:" + ent.name + "\t TYPE:" + ent.type + "\t STARTING QUAD:" + str(
                    ent.startingQuad) + "\t FRAME LENGTH:" + str(
                    ent.frameLength) + "\t RETURN TYPE:" + ent.dataType + "\n")
                f.write("\t\tARGUMENTS:" + "\n")
                counter_Arguments = 0
                for arg in range(len(ent.argumentList)):
                    counter_Arguments += 1
                    f.write(
                        "\t\t\tARGUMENT{"+str(counter_Arguments)+"} : " + " NAME:" + ent.argumentList[arg].name + "\t ARGUMENT TYPE : " + ent.argumentList[arg].dataType + "\t MODE:" + ent.argumentList[arg].mode + "\n")
            elif (ent.type == 'PROC'):
                counter_Entities += 1
                f.write("\tENTITY{" + str(
                    counter_Entities) + "}: " + " NAME:" + ent.name + "\t TYPE:" + ent.type + "\t STARTING QUAD:" + str(
                    ent.startingQuad) + "\t FRAME LENGTH:" + str(ent.frameLength) + "\n")
                f.write("\t\tARGUMENTS :" + "\n")
                counter_Arguments = 0
                for arg in range(len(ent.argumentList)):
                    counter_Arguments += 1
                    f.write(
                        "\t\t\tARGUMENT{"+str(counter_Arguments)+"}: " + " NAME:" + ent.argumentList[arg].name + "\t ARGUMENT TYPE : " + ent.argumentList[arg].dataType + "\t MODE:" + ent.argumentList[arg].mode + "\n")
    
    f.close()

def searchEntity(name):
    global table
    scope=table.scopes[-1]
    j = 1
    while table.scopes != []:
        for i in scope.entityList:
            if (i.name==name):
                return scope,i
        j += 1
        if (j > len(table.scopes)):
           break
        scope = table.scopes[-j]
    if name.isdigit():
        return "num",name
    print(" not found in symbol table : " + str(name)+" Program crashed  \n")
    sys.exit()

table = Table()  # einai to pio PANW scope kathe stigmi


#	                       Synarthseis TELIKOU KWDIKA:		                  #
###############################################################################	
asmFile = open("test.asm", "w")
checkForPar = True
def gnvlcode(name):
    global table,asmFile
    scope,entity=searchEntity(name)
    asmFile.write("lw t0,-4(sp)\n")
    for i in range(0,(table.scopes[-1].level-scope.level)-1):
        asmFile.write("lw t0,-4(t0)\n")
    entityOffset = entity.offset
    asmFile.write("addi t0,t0,-"+str(entityOffset)+"\n")

def loadvr(v,r):
    global table,asmFile
    scope,entity=searchEntity(v)
    if (scope=="num"):
        asmFile.write("li t"+str(r)+","+str(v)+"\n")
    elif(entity.type=="VAR"):
        if (scope.level==0):
            asmFile.write("lw t"+str(r)+",-"+str(entity.offset)+"(gp)"+"\n")
        elif(scope.level==table.scopes[-1].level):
            asmFile.write("lw t"+str(r)+",-"+str(entity.offset)+"(sp)"+"\n")
        else :
            gnvlcode(v)
            asmFile.write("lw t"+str(r)+",(t0)"+"\n")
    elif(entity.type=="TEMP"):
        if (scope.level == 0):
            asmFile.write("lw t" + str(r) + ",-" + str(entity.offset) + "(gp)" + "\n")
        elif(scope.level==table.scopes[-1].level):
            asmFile.write("lw t" + str(r) + ",-" + str(entity.offset) + "(sp)" + "\n")
    elif(entity.type=="PAR" and entity.mode=="CV"):
        if (scope.level == table.scopes[-1].level):
            asmFile.write("lw t" + str(r) + ",-" + str(entity.offset) + "(sp)" + "\n")
        elif (scope.lLevel < table.scopes[-1].level):
            gnvlcode(v)
            asmFile.write("lw t" + str(r) + ",(t0)" + "\n")
    elif (entity.type == "PAR" and entity.mode == "REF"):
        if (scope.level == table.scopes[-1].level):
            asmFile.write("lw t0,-"+ str(entity.offset) + "(sp)" + "\n")
            asmFile.write("lw t"+str(r)+",(t0)"+"\n")
        elif (scope.nestingLevel < scope.List[-1].nestingLevel):
            gnvlcode(v)
            asmFile.write("lw t0,(t0)\n")
            asmFile.write("lw t"+str(r)+",(t0)"+"\n")

def storerv(r,v):
    global table, asmFile
    scope, entity = searchEntity(v)
    if(entity.type=="VAR"):
        if (scope.level==0):
            asmFile.write("sw t"+str(r)+",-"+str(entity.offset)+"(gp)"+"\n")
        elif(scope.level==table.scopes[-1].level):
            asmFile.write("sw t"+str(r)+",-"+str(entity.offset)+"(sp)"+"\n")
        else :
            gnvlcode(v)
            asmFile.write("sw t"+str(r)+",(t0)"+"\n")
    elif(entity.type=="TEMP"):
        if (scope.level == 0):
            asmFile.write("sw t"+str(r)+",-"+str(entity.offset)+"(gp)"+"\n")
        elif(scope.level==table.scopes[-1].level):
            asmFile.write("sw t"+str(r)+",-"+str(entity.offset)+"(sp)"+"\n")
    elif(entity.type=="PAR" and entity.mode=="CV"):
        if (scope.level == table.scopes[-1].level):
            asmFile.write("sw t" + str(r) + ",-" + str(entity.offset) + "(sp)" + "\n")
        elif (scope.level < table.scopes[-1].level):
            gnvlcode(v)
            asmFile.write("sw t" + str(r) + ",(t0)" + "\n")
    elif (entity.type == "PAR" and entity.mode == "REF"):
        if (scope.level == table.scopes[-1].level):
            asmFile.write("sw t" + str(r) + ",-" + str(entity.offset) + "(sp)" + "\n")
            asmFile.write("sw t"+str(r)+",(t0)"+"\n")
        elif (scope.level < table.scopes[-1].level):
            gnvlcode(v)
            asmFile.write("lw t0,(t0)\n")
            asmFile.write("sw t"+str(r)+",(t0)"+"\n")

def produce():
    global quadList,table,finalCounter,asmFile,checkForPar
    for i in range(len(quadList)-1):
        count = quadList[i][0]
        op = quadList[i][1]
        x = quadList[i][2]
        y = quadList[i][3]
        z = quadList[i][4]
        asmFile.write("L%d: \n" % (count))
        if(op=="jump"):
            asmFile.write("b L"+str(z)+"\n")
        elif (op in relOp):
            loadvr(x,1)
            loadvr(y,2)
            asmFile.write(relOp.get(op) + ",t1,t2, L"+str(z)+"\n")
        elif (op== "="):
            loadvr(x,1)
            storerv(1,z)
        elif (op in operators):
            loadvr(x, 1)
            loadvr(y, 2)
            asmFile.write(operators.get(op) + ",t1,t1,t2"+"\n")
            storerv(1, z)
        elif(op == "out"):
            loadvr(x, 1)
            asmFile.write("li a0, t1"+"\n")      
            asmFile.write("li a7, 1"+"\n")                        
            asmFile.write("ecall"+"\n")
        elif (op == "inp"):
            asmFile.write("li a7, 5"+"\n")
            asmFile.write("ecall"+"\n")                                # tha topotheththei ston a0 o akeraios pou tha diabastei apo to plhktrologio
            asmFile.write("mv t1, a0"+"\n") 
            storerv(1, x)
        elif (op == "retv"):
            loadvr(x, 1)
            asmFile.write("lw t0,-8(sp)"+ "\n")
            asmFile.write("sw t1,(t0)"+ "\n")
        elif (op == "par"):
            if (checkForPar == True):
                checkForPar=False
                for j in range(i,len(quadList)):
                    if (quadList[j][1] == "call"):
                        FuncOrProcName = str(quadList[j][2])
                        break
                scope,entity=searchEntity(FuncOrProcName)
                asmFile.write("addi fp, sp,"+str(entity.frameLength)+ "\n")
                finalCounter=0
            if (y=="CV"):
                loadvr(x, 0)
                asmFile.write("sw t0,-" + str(12 + 4 * finalCounter) + "(fp)\n")
                finalCounter+=1
            elif (y == "REF"):
                scope,entity=searchEntity(x)
                if (scope.level==table.scopes[-1].level):
                    if (entity.type=="VAR"):
                        asmFile.write("addi t0,sp,-"+str(entity.offset)+"\n")
                        asmFile.write("sw t0,-"+str(12+4*finalCounter)+"(fp)\n")
                    elif (entity.type=="PAR" and entity.mode=="CV"):
                        asmFile.write("addi t0,sp,-"+str(entity.offset)+"\n")
                        asmFile.write("sw t0,-"+str(12+4*finalCounter)+"(fp)\n")
                    elif (entity.type == "PAR" and entity.mode == "REF"):
                        asmFile.write("lw t0,-"+str(entity.offset)+"(sp) \n")
                        asmFile.write("sw t0,-" + str(12 + 4 * finalCounter) + "(fp) \n")
                elif(scope.level<table.scopes[-1].level):
                        gnvlcode(x)
                        if(entity.type == "PAR" and entity.mode == "REF"):
                            asmFile.write("lw t0,(t0)\n")
                            asmFile.write("sw t0,-"+str(12 + 4 * finalCounter)+"(fp)\n")
                        else:
                            asmFile.write("sw t0,-" + str(12 + 4 * finalCounter) + "(fp)\n")
                finalCounter+=1
            elif (y == "RET"):
                scope,entity=searchEntity(x)
                asmFile.write("addi t0,sp,-"+str(entity.offset)+"\n")
                asmFile.write("sw t0,-8(fp)\n")     
        elif (op == "call"):
            checkForPar=True
            scope, entity = searchEntity(x)
            if (scope.level == table.scopes[-1].level):
                asmFile.write("lw t0,-4(sp)\n")
                asmFile.write("sw t0,-4(fp)\n")
            elif(table.scopes[-1].level<scope.level):
                asmFile.write("sw sp,-4(fp)\n")
            asmFile.write("addi sp, sp, "+str(entity.frameLength)+"\n")
            asmFile.write("jal  L"+str(entity.startingQuad)+"\n")
            asmFile.write("addi sp, sp, -"+str(entity.frameLength)+"\n")        
        elif(op=="begin_block" and table.scopes[-1].level!=0):
            asmFile.write("sw ra,(sp)\n")
        elif (op == "end_block" and table.scopes[-1].level!=0):
            asmFile.write("lw ra,(sp)\n")
            asmFile.write("jr ra\n")
        elif (op == "begin_block" and table.scopes[-1].level == 0):
            asmFile.seek(0, os.SEEK_SET)
            asmFile.write("b L"+str(count)+"\n")
            asmFile.seek(0, os.SEEK_END)
            asmFile.write("addi sp,sp,"+str(compute_offset())+"\n")
            asmFile.write("mv gp,sp\n")
        elif (op == "halt"):
            asmFile.write("li a0, 0\n")
            asmFile.write("li a7, 93\n")
            asmFile.write("ecall\n")
    quadList=[]

def block(name, flag):
        #global result_lex, table

        if (results[current_index][0] == "#{"):
            check_current_index()

            add_scope(name)  # ftiaxnw kainourgio scope kathe fora pou mpainw edw
            
            #if (flag == 0):  # an den eimaste sthn main prosthese tis parametrous tou subprogram sto topScope
                #add_parameters()
            ## Could be zero declaration_lines, but we check that afterwards
            declarations()

            ## We could have zero functions inside of a main function
            while (results[current_index][0] == 'def'):
                #print("We have a def_function")
                def_function()
               
            
            
            genQuad('begin_block', name, 'null', 'null')  

            ## We call statements at this point
            #statements()

            if (flag == 0):  # an den eimaste sthn main bale to starting Quad gia to subprogram
                table.scopes[-1].startingQuad = nextQuad()

            statements()

            if (flag == 1):
                genQuad('halt', 'null', 'null', 'null')
            else:
                table.scopes[-1].frameLength = compute_offset()
            genQuad('end_block', name, 'null', 'null')
            

            ## mporoume na krathsoume auto to shmeio stis def_main_fucntion kai def_function
            #check_current_index()

            if (results[current_index][0] == "#}"):
                
                extract_symbolic_table()  # grapsimo sto arxeio to ekastote stigmiotypo
                produce()                 # produce teliko kwdika
                table.scopes.pop()  # delete to teleutaio scope

                check_current_index()

                return
            else:
                print("ERROR: Expected '#}' ")
                ## If we got to this point, something is missing so we raise Error    
                raise ValueError ("Unexpected Token in def_main_function",results[current_index])
                

def blockstatements():
        #global result_lex, line

        statements()
        #while (results[current_index][0] == question_marktk):
            #statements()

## Changing/Increasing the current index if not Out Of Bounds
def check_current_index():
    global current_index
    
    if current_index < total_length -1:
        #print("Index In bounds, moving to the next one...")
        current_index = current_index +1
        #print("Current index after increament : ",current_index)
        return
    
    else:
        print("We reached last index")
    
    return


def start_rule():
    #global current_index
    ## For def_main_part
    #print("Calling def_main_part...")
    def_main_part()
    #print("Def_main_part is valid ",current_index)


    ## For call_main_part
    #print("Ready to call main_part")
    call_main_part()
    #print("Call_main_part is valid ",current_index)

    ## If we reach here
    ## End of Start Rule, Program is Valid
    #print("End of Start Rule, Program is Valid")

    ## List should not have any more indeces 
    #print("c1",current_index)
    #print("tl",total_length)
    #if len(results) - current_index >= 1:
    #raise ValueError("ERROR: Did not expect any more words",results[current_index])
        

    return

def def_main_part():
    #global current_index
    # At least once but we could have more def_main_functions
    def_main_function()
    while (results[current_index][0] == 'def'):
        #print("We have another def_main_function")
        def_main_function()

    ## Done defining main functions
    #print("We are done with the def_main_function part")

    return


def def_main_function():
    #global current_index
    ## Check for the sequence of words that define a main function
    #print("Current index for the first time is",current_index)
    if results[current_index][0] == 'def':
        check_current_index()
        #print("Current index after check is",current_index)

        if results[current_index][1] == 'identifier':
            ## We need to keep track for def_main_functions id's in order to check if they are called at the end of the definitions
            ## List for main_function id's: main_functions_ids
            main_functions_ids.append(results[current_index][0])

            #block(results[current_index][0],1)
            name = results[current_index][1]
            flag = 1
            

            
            check_current_index()

            if results[current_index][0] == '(': 
                check_current_index()

                if results[current_index][0] == ')': 
                    check_current_index()

                    if results[current_index][0] == ':': 
                        check_current_index()

                        # when we see that a block begins, call block function:
                        if (results[current_index][0] == "#{"):
                            block(name,flag)
                        return

                        
                    else:
                        print("ERROR: Expected ':' " )
                else:
                    print("ERROR: Expected ')' " )
            else:
                print("ERROR: Expected '(' " )
        else:
            print("ERROR: Expected 'identifier' " )
    else:
        print("ERROR: Expected 'def' " )
    
    ## If we got to this point, something is missing so we raise Error    
    raise ValueError ("Unexpected Token in def_main_function",results[current_index])      

def def_function():
    #global current_index
    ## Its not needed, but we keep that, it will always be true (about the 'def')
    if results[current_index][0] == 'def':
        check_current_index()

        if results[current_index][1] == 'identifier':
            ## We need to keep track of normal function_ids 
            ## List for not main functions id's: def_fucntion_ids
            def_functions_ids.append(results[current_index][0])

            #block(results[current_index][0],1)
            name2 = results[current_index][1]
            


            F = Function()
            #F.name = result_lex[0]
            F.name = results[current_index][0]
            F.type = "FUNC"
            F.dataType = "Int"
            add_entity(F)

            check_current_index()

            if results[current_index][0] == '(':
                check_current_index()

                ## We dont need to check for errors because they will occur in id_list function, if any
                ## So we have to call it anyways
                id_list()

                if results[current_index][0] == ')':
                    check_current_index()

                    if results[current_index][0] == ':':
                        check_current_index()
                        
                        block(name2,0)
                        return
                        
                    
                    else:
                        print("ERROR: Expected ':' ")

                
                else:
                    print("ERROR: Expected ')' ")
                

            else:
                print("ERROR: Expected '(' ")
        
        else: 
            print("ERROR: Expected 'identifier' ")
    
    else:
        print("ERROR: Expected 'def' ")
    
    # If we got up to here, something is missing
    raise ValueError("Unexpected Token in def_function",results[current_index])

def declarations():
    
    #global current_index
    ## Can be zero times called, so we will only call declaration line if we have a '#declare'
    while (results[current_index][0] == '#declare' ):

        #print("We have a declaration line")
        declaration_line()

        ## we will reutrn the current_index anyway so we dont need to return here
        ## there is no condition that this can cuz an Error if it is called
        ## because declarations can be skipped (*)
            

    #print("We are done with the declarations part") 

    ## this function cant have errors
    return

def declaration_line():
    #global current_index
    ## Its not needed, but we keep it anyways, we already know its true from declarations func
    if results[current_index][0] == '#declare':
        check_current_index()

        ## We dont need to check for errors because they will occur in id_list function
        id_list()

        #print("We got up to here so declaration_list is okay")
        return
    
    else:
        ## Cant get here
        print("ERROR: Expected declaration")
    
    #raise Error
    raise ValueError("Unexpected token in declaration_line",results[current_index])


def statement():
    #global current_index
    ## assignment_stat, print_stat, return_stat
    ## We do that check in order to knonw what funciton we need to call
    if results[current_index][1] == 'identifier' or results[current_index][0] == 'print' or results[current_index][0] == 'return':
       
        simple_statement()
        return
        
    ## if_stat, while_stat
    ## We do that check in order to knonw what funciton we need to call
    elif results[current_index][0] == 'if' or results[current_index][0] == 'while':

        structured_statement()
        return
    
    else:
        ## Should stop if that happens, because everything else was not expected
        print("ERROR: Expected simple_statement('identifier','print','return') or structured statement('if','else') ")

    

    ## If we got up to this point
    #raise Error
    raise ValueError("Unexpected Token in statement",results[current_index])


def statements():
    #global current_index
    # At least one statement, but could have multiple (+)
    statement()
    
    ## we need to know the current index so we can know if we gonna add more statements or we can procced and return index
    while (results[current_index][0] == 'print' or results[current_index][0] == 'return' or results[current_index][1] == 'identifier' or results[current_index][0] == 'if' or results[current_index][0] == 'while'):
        #print("We have another statement")       

        statement()
    
    #print("We are done with statements part") 

    ## Statements must return index, if an error occurs, it will occur on statement function, not here
    return



def simple_statement():
    #global current_index
    if results[current_index][1] == 'identifier':
        
        ## We need to call assignment_stat then
        assignment_stat()

        return

    elif results[current_index][0] == 'print' :

        ## We need to call print_stat then
        print_stat()
        return

    elif results[current_index][0] == 'return':
        
        ## We need to call return_stat then
        return_stat()
        return
    
    else:
        ## Cant get in there i think, true because its checked up on statement
        print("ERROR: Expected 'ID' or 'print' or 'return' in simple statement")

    ## We cant get to this point, we think
    #raise ERROR
    raise ValueError("Unexpected Token in simple_statement",results[current_index])


def structured_statement():
    #global current_index
    if results[current_index][0] == 'if':

        ## We need to call if_stat then
        if_stat()
        return

    elif results[current_index][0] == 'while':

        ## We need to call while_stat then
        while_stat()
        return

    else:
        # Cant get in there i think, true because its checked up on statement
        print("ERROR: Expected 'if' or 'while'")
        #return ERROR?

    ## We cant get to this point, we think
    #raise Error
    raise ValueError("Unexpected Token in structured_statement",results[current_index])


def assignment_stat():
    #global current_index
    # idk if its even needed, it isnt, we already checked that on simple_statement, but anyways
    if results[current_index][1] == 'identifier':

        ## we need to check if the identifier has already been declared in declarations -> (which means) id_list
        if results[current_index][0] in identifiers:
            

            new_id = results[current_index][0]

            check_current_index()

            
            if results[current_index][0] == '=' :
                check_current_index()

                ## For expression
                ## we need that check  because we have two possible scenarios, 1) expression ... or  2) 'int'... and we need to know which function to call next 
                if results[current_index][1] == 'num' or results[current_index][1] =='addOP' or results[current_index][1] =='identifier' or results[current_index][0] == '(':
                    
                    ## We got an expression
                    Eplace = expression()
                    genQuad('=', Eplace, "null", new_id)

                    if results[current_index][0] == ';':
                        check_current_index()

                        #print("assignment_stat is valid with: expression")
                        return

                    else:
                        print("ERROR: Expected ';' ")
                        
                
                ## For 'int'
                elif results[current_index][0] == 'int':
                    check_current_index()

                    if results[current_index][0] == '(':
                        check_current_index()

                        if results[current_index][0] == 'input':
                            check_current_index()

                            if results[current_index][0] == '(':
                                check_current_index()

                                if results[current_index][0] == ')':
                                    check_current_index()

                                    if results[current_index][0] == ')':
                                        check_current_index()

                                        if results[current_index][0] == ';':
                                            #print("assignment_stat is valid with: int(input();")

                                            input_value = input("Enter Integer:")
                                            genQuad('inp', input_value, 'null', 'null') 

                                            check_current_index()
                                            return
                                        
                                        else:
                                            print("ERROR: Expected ';' ")
                                    else:
                                        print("ERROR: Expected ')' ")
                                else:
                                    print("ERROR: Expected '(' ")
                            else:
                                print("ERROR: Expected '(' ")
                        else:
                                print("ERROR: Expected 'input' ")
                    else:
                                print("ERROR: Expected '(' ")
                else:
                    print("ERROR: Expected expression or 'int' ")
            else:
                print("Expected '=' ")
        else:
            print("ERROR: We got identifier in assignment_stat but it has not been declared earlier")
    else:
        ## Cant get in here i think
        print("ERROR: Expected identifer")
    
    ## If we get to this point
    ## raise Error
    raise ValueError("Unexpected Token in assignment_statement",results[current_index])
    



def print_stat():
    #global current_index
    ## We dont needed to check, because we know for sure thats a print if print_stat is called
    ## and we know that from simple_statements, but anyways
    if results[current_index][0] == 'print':
        check_current_index()

        if results[current_index][0] == '(':
            check_current_index()

            ## We want just an expression at this point so no need to check for more possible scenarios
            ## and if error occurs, it will be on expression function.
            expression()

            if results[current_index][0] == ')' :
                check_current_index()

                if results[current_index][0] == ';' :
                    #print("print_stat is valid")
                    check_current_index()
                    return

                else:
                    print("ERROR: Expected  print';' ")   
            else: 
                print("ERROR: Expected ')' print ")        
        else: 
            print("ERROR: Expected '(' ")
    else:
        ## Cant get here 
        print("ERROR: Expected 'print' ")
        
    ## If we get to here
    ## raise Error
    raise ValueError("Unexpected Token in print_statement",results[current_index])



def return_stat():
   #global current_index
    ## We dont needed to check, because we know for sure thats a print if print_stat is called
    ## and we know that from simple_statements, but anyways
    if results[current_index][0] == 'return':
        check_current_index()            
        
        if results[current_index][0] == '(':
            check_current_index()

            ## Same as print_statement
            Eplace = expression()  
            genQuad('retv', Eplace, "null", "null") 

            if results[current_index][0] == ')':
                check_current_index()

                if results[current_index][0] == ';':
                    check_current_index()
                    #print("return_stat is valid")
                    return


                else:
                    print("ERROR: Expected ';' ")
                
            else: 
                print("ERROR: Expected ')' ") 
        
        else: 
            print("ERROR: Expected '(' ")
    
    else:
        ## Cant get in here, same as print_statement
        print("ERROR: Expected 'return' ")
    
    ## Same as print_stat
    ## raise Error
    raise ValueError("Unexpected Token in return_statement",results[current_index])

    
def if_stat():
    #global current_index
    # idk if its even needed, it isnt, we already checked that on structed_statement, but anyways
    if results[current_index][0] == 'if':
        check_current_index()            
        
        if results[current_index][0] == '(':
            check_current_index()

            ## No need to check anything here, Errors will occur in condition function
            Cond = condition()
            backPatch(Cond[0], nextQuad())

            if results[current_index][0] == ')':
                check_current_index()

                if results[current_index][0] == ':':
                    check_current_index()

                    if results[current_index][0] == '#{':
                        check_current_index()

                        ## No need to check anything here, Errors will occur in expression function
                        statements()
                        

                        if results[current_index][0] == '#}':
                            
                            ifStatList = makeList(nextQuad())  
                            genQuad('jump', 'null', 'null', 'null')  
                            backPatch(Cond[1], nextQuad()) 
                            check_current_index()
                            #print("We are done with the first part of if_stat, with statements")
                            #print("Checking for else part...")

                            ## We could potentially have an else part so we call else_stat function
                            else_stat()
                            backPatch(ifStatList, nextQuad())
                            return
                        
                        else:
                            print("ERROR: Expected '#}' ")

                            
                    else:
                        
                        ## If we dont have '#{' after if that means we could only have statement so we call that function
                        ## Errors will occur there
                        statement()

                        #print("We got the first part right of if_stat, with statement")
                        #print("Checking for else part...")
                        else_stat()
                        
                        return
                else:
                    print("ERROR: Expected ':' ")
            else:
                print("ERROR: Expected ')' ")
        else:
            print("ERROR: Expected '(' ")
    else:
        ## Cant get in here but anyways
        print("ERROR: Expected ':' ")

    ## If we get up to here means that we got nothing of the above two scenarios
    ## raise ERROR
    raise ValueError("Unexpected Token in if_stat part",results[current_index])


def else_stat():
    #global current_index
    if results[current_index][0] == 'else':
            #print("We got an else part here")
            check_current_index()

            if results[current_index][0] == ':':
                check_current_index()

                if results[current_index][0] == '#{':
                    check_current_index()

                    statements()

                    if results[current_index][0] == '#}':
                        check_current_index()
                        #print("The else_part is valid with statements")
                        
                        return
                    
                    else:
                        print("ERROR: Expected '#}' ")
                else:
                    ## If it doesnt start with '#{' then we have a statements and the errors will occur there, if any
                    statement()
                    #print("The else_part is valid with statement")
                    return
            else:
                print("ERROR: Expected ':' ")
                
    else:
        #print("There is no 'else' part but its okay")
        return
    
    ## If we got up to here, something is missing
    return ValueError("Unexpected Token in else_stat")
    

def while_stat():
    #global current_index
    ## It's not needed, but we check anyways
    if results[current_index][0] == 'while':

        check_current_index()

        if results[current_index][0] == '(':
            check_current_index()

            ## We dont need to because its only one possible scenario so the errors will occur on condition function
            CountQuad = nextQuad()  
            Cond = condition()  
            backPatch(Cond[0], nextQuad())  

            if results[current_index][0] == ')':
                check_current_index()

                if results[current_index][0] == ':':
                    check_current_index()

                    ## Same as if_stat
                    if results[current_index][0] == '#{' :
                        check_current_index()
                        
                        ## We got statements here
                        statements()
                        genQuad('jump', 'null', 'null', CountQuad)  
                        backPatch(Cond[1], nextQuad()) 


                        if results[current_index][0] == '#}':
                            check_current_index()
                            #print("while_stat is valid with statements")
                            return
                        
                        else:
                            print("ERROR: Expected '#}' ")
                    
                    else:
                        
                        ## Same as if_stat
                        statement()

                        #print("while_stat is valid with statement")
                        return

                else:
                    print("ERROR: Expected ':' ")

            else:
                print("ERROR: Expected ')' ")
        else:
            print("ERROR: Expected '(' ")
    
    else:
        ## Can't get here but anyways
        print("ERROR: Expected 'while' ")
    
    # If we got up to here... its an ERROR
    # return Error
    raise ValueError("Unexpected Token in while_statement",results[current_index])



def id_list():
    #global current_index

    ## Needs to act as a Variable when its #declare id_list :
    ##Dont know if its need for our program...
    #if results[current_index - 1][0] == "#declare":

    if results[current_index][1] == 'identifier':

        ## We need to store the identifiers in order to check later
        ## We do that in identifiers list
        identifiers.append(results[current_index][0])

        # add variable to scope    
        V = Variable()
        #V.name = result_lex[0]
        V.name = results[current_index][0]
        V.type = "VAR"
        V.dataType = "Int"
        V.offset = compute_offset()
        add_entity(V)
        

        check_current_index()

        ## Could have ', identifier' ...
        while results[current_index][0] == ',':
            

            check_current_index()
            #print('We got comma so we expect another identifier')

            if results[current_index][1] == 'identifier':
            
                ## We need to store the identifiers in order to check later
                ## We do that in identifiers list
                identifiers.append(results[current_index][0])


                # add variable to scope    
                V = Variable()
                V.name = results[current_index][0]
                V.type = "VAR"
                V.dataType = "Int"
                V.offset = compute_offset()
                add_entity(V)
                

                check_current_index()
                #print("Another 'identifier' is valid ")
                

            
            else:
                print("Error: Expected 'identifier' after comma ',' at id_list ")
                ## raise ERROR
                raise ValueError("Unexpected Token in id_list: Expected ID after comma",results[current_index])


            #   return or we can just put it in the end ?
            # no we cant because we can have errors here if something isnt as expected 
            # so we have to put it here: that means we already have one identifier or more and the current token now is not comma
            
            #return
        
    
    
    ## Needs to act as a Formal List when its def func(id_list):
    
    
    ## Dont know if its need for our program because we dont have in/inout
    
    #elif results[current_index - 1][0] == "(":

        #if results[current_index][1] == 'identifier':

            ## We need to store the identifiers in order to check later
            ## We dont need to store that in the identifiers list
            ## Because its variables for reference
            ## identifiers.append(results[current_index][0])

            ## No need to add variable to scope    
 

            #check_current_index()

            ## Could have ', identifier' ...
            #while results[current_index][0] == ',':

                #check_current_index()
                #print('We got comma so we expect another identifier')

                #if results[current_index][1] == 'identifier':
                
                    ## We need to store the identifiers in order to check later
                    ## We dont need to store that in identifiers list
                    ## Because its variables for reference
                    #identifiers.append(results[current_index][0])

                    ## No need to add variable to scope 

                    #check_current_index()
                    #print("Another 'identifier' is valid ")

                
                #else:
                    #print("Error: Expected 'identifier' after comma ',' at id_list ")
                    ## raise ERROR
                    #raise ValueError("Unexpected Token in id_list: Expected ID after comma",results[current_index])


            #   return or we can just put it in the end ?
            # no we cant because we can have errors here if something isnt as expected 
            # so we have to put it here: that means we already have one identifier or more and the current token now is not comma
           
            #return


    ## Else is not needed here, because 'identifiers' in id_list are not necessery
   
    ## If we get up to here, we are fine
    return



def expression():
    #global current_index
    ## No need to check anything here
    optional_sign()
    #print("Calling term...")

    ## At least one term (+)
    Tplace1 = term() 

    ## Can have multiple
    while results[current_index][1] == 'addOP':

        new_add_op = results[current_index][0]
        optional_sign()

        ## And we call term again
        Tplace2 = term()
        w = newTemp()
        genQuad(new_add_op, Tplace1, Tplace2, w)
        Tplace1 = w
    
    ## No Errors here
    Eplace = Tplace1
    return Eplace

def optional_sign():
    #global current_index
    ## --OPTIONAL-- so we can have errors
    if results[current_index][1] == 'addOP':
       check_current_index()
    
    #else:
        #print("We found no addOP sign but its not an Error")
    
    ## No Errors here
    return



def term():
    #global current_index
    #print("Calling factor...")
    Fplace1 = factor() 

    ## Can have multiple
    while results[current_index][1] == 'mulOP' : 

        new_mul_op = results[current_index][0]

        check_current_index()

        Fplace2 = factor()
        w = newTemp()
        genQuad(new_mul_op, Fplace1, Fplace2, w)
        Fplace1 = w
        
    
    ## No Errors here
    Tplace = Fplace1
    return Tplace


def factor():
    #global current_index
    ## Check if number
    if results[current_index][1] == 'num':

        fact = results[current_index][0]

        check_current_index()
        #print("We got a valid number from factor")

        return fact
    
    ## Check if expression
    elif results[current_index][0] =='(':
        check_current_index()
        Eplace = expression()  
        fact = Eplace   

        if results[current_index][0] == ')':
            check_current_index() 

            #print("We got a valid expression from factor")
            return fact

        else: 
            print("ERROR: Expected ')' ")

    ## Check if id_tail
    elif results[current_index][1] == 'identifier':
        ## we need that in order to check (factor can be either a function name or a identifier from declarations) 
        ## further problem
        ## what if we got an idenitfier = x and a function_name = x  then how can we determine what it is, do we care? idk ill think of it later 
        
        
        if results[current_index][0] in identifiers or results[current_index][0] in def_functions_ids:
            fact_temp = results[current_index][0]

            

            check_current_index()

            ## no need to check, errors can occur in id_tail function
            fact = id_tail(fact_temp)
            #print("We got a valid id_tail/identifier(s) from factor")

            return fact

        else:
            print("ERROR: Expected identifier that has already been declared")
            print("Remeber: main functions cant be called inside a main function")

    else:
        print("ERROR: Expected 'num', '(' or 'identifier' in factor() ",results[current_index-1])

    
    ## If we get up to here something is missing
    ## raise Error
    raise ValueError("Unexpected Token in factor",results[current_index])



def id_tail(id): 
    #global current_index
    if results[current_index][0] == '(':
        check_current_index()

        ## Errors will occur in actual_par_list if something goes wrong
        actual_par_list()
        w = newTemp()  
        genQuad('par', w, 'RET', 'null')  
        genQuad('call', id, 'null', 'null') 

        if results[current_index][0] == ')':
            check_current_index()
            #print("Valid id_tail")
            return w
        
        else:
            print("ERROR: expected after ')' ")
            ## The only way we can get an Error here
            raise ValueError("Unexpected Token in id_tail",results[current_index])
    
    ## else is not needed because in id_tail we can have no arguments (empty) 
    return id


def actual_par_list():
    #global current_index
    ## Errors will occur in expression , if any
    new_exp = expression()
    genQuad('par', new_exp, 'CV', 'null')

    while results[current_index][0] == ',':
        check_current_index()

        ## Errors will occur there
        new_exp2 = expression()
        genQuad('par', new_exp2, 'CV', 'null')

    ## we cant have an error here 
    return


def condition():
    #global current_index
    ## errors will occur in bool_term

    CondTrue = []
    CondFalse = []
    BoolTerm1 = bool_term()
    CondFalse = BoolTerm1[1]
    CondTrue = BoolTerm1[0]


    while results[current_index][0] == 'or' :
        check_current_index()

        backPatch(CondFalse, nextQuad())  
        BoolTerm2 = bool_term()  
        CondTrue = merge(CondTrue, BoolTerm2[0])  
        CondFalse = BoolTerm2[1] 

    ## cant have Error Here
    return CondTrue, CondFalse

def bool_term():
    #global current_index
    ## errors will occur in bool_factor
    BoolTerm_True = []
    BoolTerm_False = []
    BoolFactor1 = bool_factor()
    BoolTerm_False = BoolFactor1[1]
    BoolTerm_True = BoolFactor1[0]

    while results[current_index][0] == 'and':
        check_current_index()

        backPatch(BoolTerm_True, nextQuad())
        BoolFactor2 = bool_factor()
        BoolTerm_False = merge(BoolTerm_False, BoolFactor2[1])
        BoolTerm_True = BoolFactor2[0]
        
       

    
    ## cant have errors here
    return BoolTerm_True, BoolTerm_False

def bool_factor():
    #global current_index
    BoolFactor_True = []
    BoolFactor_False = []

    if results[current_index][0] == 'not':
        check_current_index()

        if results[current_index][0] =='[':
            check_current_index()
            
            ## We call condition, Errors will occur there, if any
            Cond = condition()

            if results[current_index][0] ==']':
                check_current_index()

                BoolFactor_False = Cond[0]
                BoolFactor_True = Cond[1]

                
                #print("Valid bool_factor")

                return BoolFactor_True, BoolFactor_False
            
            else:
                print("ERROR: Expected ']' ")
        
        else:
            print("ERROR: Expected '[' ")
    
    elif results[current_index][0] =='[':
        check_current_index()

        Cond = condition() 

        if results[current_index][0] == ']':
            check_current_index()
            #print("Valid bool_factor")

            BoolFactor_False = Cond[1]  
            BoolFactor_True = Cond[0]
            
            return BoolFactor_True, BoolFactor_False
        
        else:
            print("ERROR: Expected ']' ")
        
        
    
    else:
        ## It doesnt start with 'not' nor '[' so we send it to expression and if its not expression either we will get the error there
        Eplace1 = expression()
       
        ## potentially we need to do that on tagMaker instead of larger, larger_equal, smaller, smaller_equal, equal, not equal to just make tags as relOP 
        if results[current_index][1] == 'relOP':

            new_rel_op = results[current_index][0]

            check_current_index()
            #print("If we got up to here, then searching for another expression")
            ## errors will occur in expression if any
            Eplace2 = expression()
            #print("If we got up to here, then valid bool_factor")


            BoolFactor_True = makeList(nextQuad())
            genQuad(new_rel_op, Eplace1, Eplace2, 'null')
            BoolFactor_False = makeList(nextQuad())
            genQuad('jump', 'null', 'null', 'null')
            return BoolFactor_True, BoolFactor_False

    ## If we got up to here
    ## raise Error
    raise ValueError("Unexpected Token in bool_factor",results[current_index])




def call_main_part():
    #global current_index

    if results[current_index][0] =='if':
        check_current_index()

        if results[current_index][0] =='__name__':
            check_current_index()

            if results[current_index][0] == '==':
                check_current_index()

                if results[current_index][0] == '"__main__"':
                    check_current_index()

                    if results[current_index][0] == ':':
                        check_current_index()

                        ## At least one
                        main_function_call() 
                        # Can have multiple
                        #print(results[current_index])
                        while results[current_index][1] == 'identifier':
                            #print("call_main part is valid and we found another one ")
                           main_function_call()
                        
                        ## time to end
                        ## if we reach to this point
                        ## It means we got more words and we didnt find an identifer, because we would be in while loop, so we need to raise an Error
                        ## or return if we got EOF
                        ## This if statement is only about the last words of calling the functions 
                        if results[current_index -4][1] == 'identifier' and results[current_index-4][0] in main_functions_ids:

                            if results[current_index -3][0] == '(':

                                if results[current_index-2][0] == ')':

                                    if results[current_index-1][0] ==';':

                                        ## That means we got another element in results, which is not valid by our grammar rules
                                        ## And its not and identifier so we can raise Error safely, there is not case what follows is valid
                                        raise ValueError("ERROR: Word was not expected",results[current_index])

                        
                        ## We only return with End of File
                        return


                    else: 
                        print("ERROR: Expected ':' ")
                else:
                    print('ERROR: Expected "__main__" ')
            else:
                print("ERROR: Expected '==' ")
        else:
            print("ERROR: Expected '__name__' ")
    else:
        print("ERROR: Expected 'if' ")

    ## If we got up to here... it means something is missing
    ## raise Error
    raise ValueError("ERROR: Main_function is not called correctly",results[current_index])

def main_function_call():
    #global current_index
    ## We need to check if the identfier we found has already been a name of a main function
    if results[current_index][1] == 'identifier' and results[current_index][0] in main_functions_ids:
        
        #new_func_id = results[current_index][0]

        ## We found an identifier for main_function_call and it has already been defined
        check_current_index()

        if results[current_index][0] == '(':
            check_current_index()

            if results[current_index][0] == ')':
                #genQuad('call', new_func_id, 'null', 'null')
                
                check_current_index()
                
                if results[current_index][0] == ';':
                    #print("Valid main_fucntion_call ")
                    check_current_index() ## SHOULD WE INCREASE OR IT MUST BE THE END HERE?

                    return
                
                else:
                    print("ERROR: Expected ';' ")
            else:
                print("ERROR: Expected ')' ")
        else:
            print("ERROR: Expected '(' ")
                    
    else:
        ## we keep that
        print("ERROR: Expected identifier that has already been defined as main function")

    ## If we get up to this point
    ## raise Error
    raise ValueError("ERROR: Improper Main Function Call",results[current_index])



## This fucntion's purpose is to analyze the sequence of the words that a .cpy file might have and depending on it, it checks if the rules 
## of the language CutePy are applied. Those rules are defined by the functions above. If not, then we raise ValueErrors, else we got our selfs
## a program to work with.

def Syn():
    
    #global current_index 
   
    #current_index = 0
    ## 1 ##
    #define start_rule
    ## WE NEED TO START WITH THIS BRO, WE NEED TO CALL IT SOMEWHERE , MAYBE IN THE END OF THE DEIFINTIONS OF ALL FUNCITONS OF SYNTAX ANALYSIS

    
    start_rule()


    return


        

########## FOR LEX ###########

########## kai na elegxei an to arxeio exei katlhksh .cpy?
try:
    print("Innitiating lex analysis to produce word tokens...")
    Lex()
    print("Lex is done.")

except ValueError as e:
        print('Unrecognized character:', str(e))
        ## stop the run time if that happens
        sys.exit()


line_words.clear()
res_line = 1
last_line = -1
last_line_words = []





## FOR FINAL WORD LIST PRINTS ##



## Pop empty spaces out, bufixing\

print("Removing empty spaces...")

for i in range(0,len(results)):
    if results[i][1] == 'empty':
        #print('Found empty space and removing it')
        results.remove(i)




########## FOR COMMENTS REMOVAL ##############

print("Removing comments...")

within_comment = False
k = 0

while k < len(results):
    word, _, _ = results[k]
    if word == '#$':
        within_comment = not within_comment
        del results[k]
    elif within_comment:
        del results[k]
    else:
        k += 1


 ## CHANGE TAG FOR RESERVED WORDS ##

print("Changing tag for reserved words...")
print("Checking boundary limitations...")

for i in range(0,len(results)):
    for j in range(0,len(results[i])):
        
        if results[i][0] in reserved_words:
            results[i][1] = 'reserved'
        
        ## Check for boundary issues -- number value
        elif results[i][1] == 'num':
            if int(results[i][0]) < (-pow(2,32) +1) or int(results[i][0])  > (pow(2,32) -1):
                results[i][1] ='not_valid'
                print("ERROR: Number out of range",results[i])
                sys.exit()



        ## Check for boundary issues -- word length
        elif results[i][1] == 'identifier':
            if len(results[i][0]) > 30:
                results[i][1] ='not_valid'
                print("ERROR: String characters more than 30",results[i])
                sys.exit()



########## FOR not_valid word tokens ##############

print("Checking for not valid words...")

for i in range(0,len(results)):
    if results[i][1] == 'not_valid':
        print("ERROR: Word is not valid", results[i])
        sys.exit()


## FOR PRINTING LINE-BY-LINE ##

print("Results list is ready!")
print("Printing every line of the code...")

for i in range(0,len(results)):
    last_line = results[-1][2]

    if results[i][2] == res_line:
        line_words.append(results[i])

 
    else:

        if results[i][2] == last_line:
            last_line_words.append(results[i])

        else:
            print('Results for line :   '+str(res_line)+'   are     ',line_words)
            line_words.clear()
            line_words.append(results[i])
            res_line = res_line + 1


## FOR CHECKING EMPTY LIST (results) ##

total_length = len(results)

if total_length >=1:

    ## For previous line
    print('Results for line :   '+str(res_line)+'   are     ',line_words)
    
    ## We reached last line

    ## For last line
    print('Results for line :   '+str(last_line)+'  are     ',last_line_words)

else:
    ## Results contains only EOF:
    sys.exit("Results list is empty")


### For Syn() ###

print("Innitiating Syntax Analysis...")



## For execution time: ##
#print("\n\n\n\n\t\t\t\t\t\t\t\t\t\t Execution time :%s seconds" % (time.time() - start_time))
print("\n\n\n\n")
print("\t\t\t\t\t\t\t\t\t Execution time :%s seconds" % (time.time() - start_time))



def makefiles():
    # Open files to write
    testFile = open('testFile.int', 'w')
    
    f = open("test.symb", "w")
    
    try:
        Syn()
        if total_length-1:
            print("We reached End Of File.")
            print("Syn is done.")
            print('Program is valid and applies to all the Syntax rules.')
    

    except ValueError as e:
        print('Program is not valid:', str(e))

    f.close()
    for quad in QuadsList:
        testFile.write(str(quad[0]) + ":  " + str(quad[1]) + "  " + str(quad[2]) + "  " + str(
            quad[3]) + "  " + str(quad[4]))
        testFile.write("\n")
    testFile.close()
    asmFile.close()
makefiles()
