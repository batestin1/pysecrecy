
#############################################################################################################################
#   filename:Pysecrecy.py                                                       
#   created: 2023-02-13                                                              
#   import your librarys below                                                    
#############################################################################################################################


class Pysecrecy:
    def __init__(self, text=None):
        self.text = text

    def encode(self):
        return ''.join(['*' for char in self.text])
    
    def decode(self):
        return self.text.replace('*', '')



