class FileName:
    def __init__(self, init_format = ['MM', 'DD', 'YYYY'], delimiter = '-'):
        
        self.init_format = init_format

        self.delitimiter = delimiter

        self.base = {
                'MM': None,
                'DD': None,
                'YYYY': None
            }
        
        self.name = None
        
    def read_file_name(self, name):
        self.name = name

        parts = name.split(self.delitimiter)

        for i in range(len(parts)):
            self.base[self.init_format[i]] = parts[i]
        
        return self.base
    
    def rename_file(self, new_format = ['YYYY', 'MM', 'DD'], new_delimiter = '-'):
        
        new_name = []
        
        for i in range(len(new_format)):
            new_name.append(self.base[new_format[i]])
        
        return new_delimiter.join(new_name)

        
        




        
