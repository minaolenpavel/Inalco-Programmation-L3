# LE NOM DU FICHIER EST my_token.py ET NON token.py car "token.py" is overriding the stdlib module "token"PylancereportShadowedImports"

class Token:
    def __init__(self, forme:str, lemme:str, spart:str):
        self.__forme = forme
        self.__lemme = lemme
        self.__spart = spart

    def affichage(self):
        return f"{self.forme}/{self.lemme}/{self.spart}"

    @property
    def forme(self) -> str:
        return self.__forme
    
    @property
    def lemme(self) -> str:
        return self.__lemme
    
    @property
    def spart(self) -> str:
        return self.__spart
    
    @forme.setter
    def forme(self, new_forme:str):
        if new_forme and isinstance(new_forme, str):
            self.__forme = new_forme
    
    @lemme.setter
    def lemme(self, new_lemme:str):
        if new_lemme and isinstance(new_lemme, str):
            self.__lemme = new_lemme

    @spart.setter
    def spart(self, new_spart):
        if new_spart and isinstance(new_spart, str):
            self.__spart = new_spart