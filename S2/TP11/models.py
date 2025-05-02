class Annotation:
    def __init__(self, manual_text:str, auto_text:str, manual_tag:str, auto_tag:str):
        self.manual_text = manual_text
        self.auto_text = auto_text
        self.manual_tag = manual_tag
        self.auto_tag = auto_tag
        self.category = None

    def category(self):
        pass

    def __str__(self):
        return f"[MANUEL] {self.manual_text} : {self.manual_tag}\t[AUTO] : {self.auto_text} : {self.auto_tag}\n"