def file_hevleh():
        
        filename = "example.txt"
        
        with open(filename, 'r') as file:
            content = file.read()
        
        print(content)
    

file_hevleh()
