import glob
class merge :
    
    def mergingfiles():
        
    
      
        
        read_files = glob.glob("*.txt")
        
        with open("result.text", 'a') as outfile:
            for f in read_files:
                with open(f, "r") as infile:
                    outfile.write('\n'+infile.read())
                    
                   
    mergingfiles()
    
