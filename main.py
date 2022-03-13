
#ReadFromFile = ("SECRET_ID", "API_TOKEN", "CLIENT")
# will return a dictionary if success or return None if not
# or maybe return a tuple?
# also need to specify filename

# will return True if success and False if not
#writeToFile = ({"SECRET_ID": "lalala","API_TOKEN": "lalalal2", "CLIENT": "LAAAAAAAAAALALALLA"})


#read.Builder("asTuple").path("filePath").lines(10).read()
# asDict


"""
ifError(Raise.Exception, Raise.specialException, do.nothing)
"""
import pathlib


class writeFile:

    @classmethod
    def Builder(cls, _type):
        temp = writeFile()
        temp._type = _type

        return temp


    def __init__(self) -> None:
        self.path = ""
        self._type = ""
        self.content = ""

        self.openType = ""

        self.errorIfExists = ""
        self.errorIfNotExist = ""
        self.errorOverlap = ""
        
    def setContent(self, content):
        toRet = ""
        if self._type == str:
            toRet+= "STR"
            toRet+=content
            toRet+="ENDSTR"

        if self._type == list:
            for item in content:
                toRet+="LISTITEM"
                toRet+=item

            toRet+="LISTEND"


        if self._type == dict:
            for key, value in content.items():
                toRet+="DICTKEY"
                toRet+=key
                toRet+="DICTVALUE"
                toRet+=value

        

        self.content = toRet
        return self

    def setPath(self, path):
        if self.path:
            if self.errorOverlap:
                raise Exception(self.errorOverlap)
        else: 
            self.path = pathlib.Path(path)
            if self.path.is_dir():
                raise Exception("path is dir")
        
        return self

#    def onlyIfEmpty(self):
#        if self.writeType:
#            return self
#        self.writeType = "OnlyIfEmpty"
#        return self

    def raiseErrorInOverlap(self):
        self.errorOverlap = "ovelap occured"
        return self

    def append(self):
        if self.openType:
            if self.errorOverlap:
                raise Exception(self.errorOverlap)
            return self
        
        self.openType = 'a'
        return self

    def overwrite(self):
        if self.openType:
            if self.errorOverlap:
                raise Exception(self.errorOverlap)
            return self
        
        self.openType = 'w'
        return self

    def raiseErrorIfNotExist(self):
        if self.errorIfExists:
            if self.errorOverlap:
                raise Exception(self.errorOverlap)
            return self

        self.errorIfNotExist = "file already exists"

        return self

    def raiseErrorIfExists(self):
        if self.errorIfNotExist:
            if self.errorOverlap:
                raise Exception(self.errorOverlap)
            return self

        self.errorIfExists = "file not exist"
        return self


    def write(self):
        if self.path.exists():
            if self.errorIfExists:
                raise Exception(self.errorIfExists)
        else:
            if self.errorIfNotExist:
                raise Exception(self.errorIfNotExist)


        with open(self.path, self.openType) as outfile:
            outfile.write(self.content)

            return self.content


class readFile:

    def __init__(self) -> None:
        self.path = ""
        self._type = ""
        self.errorIfNotExist = ""
        self.returnNoneIfNotExist = ""
        self.errorOverlap = ""

    def parse(self):

        with open(self.path, mode='r') as outfile:
            content = outfile.read()

        if self._type == str:
            toRet = content.split("STR")[0].split("ENDSTR")[0]
            return toRet

        if self._type == dict:
            pass

        if self._type == list:
            pass

        


#temp = writeToFile.Builder(dict).setContent({"Auth": "test", "Auth2": "test"}).setPath("pathToFile.txt").createIfNotExist().onlyIfEmpty().write()

# appendIfNotEmpty
# overwriteIf


writeFile.Builder(str).setContent("Yuvali pizponi haya po").setPath("text.txt").overwrite().write()
with open(pathlib.Path("text.txt"), mode='r') as outfile:
    content = outfile.read()
toRet = content.split("STR", maxsplit=1)[-1].split("ENDSTR", maxsplit=1)[0]
print(toRet)
"""
FORMATTING:

1. str -> STRthis is an example of str \nENDSTR
2. list -> LISTITEMthis is a list itemLISTITEMthis is a second list itemENDLIST
3. dict -> DICTKEYAuthDICTVALYubal123
"""