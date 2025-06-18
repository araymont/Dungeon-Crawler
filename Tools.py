import time

# Return over multiple lines "\x1B[2A" or "\x1B[3A" for 2 and 3 lines
# clear rest of carriage "\x1B[0K"

class Clean_Tool():
    def __init__(self):
        pass
        
    def Clean(self, lines_to_clean=11):
        #Clean Lines
        for i in range(0,lines_to_clean):
            print("\x1B[1A",end = "") # L1
            print("\x1B[0K",end = "")


class Writer_Tool():
    def __init__(self,string_to_write):
        self.data = string_to_write
        self.data_list = list(self.data)


    def write(self,string = "..."):
        if(not (string == "...")):
            self.data = string
            self.data_list = list(self.data)
        alphabet = ['!','?',' ','.',',','£','*','%','(',')',
                    'a','b','c','d','e','f','g','h','i','j',
                    'k','l','m','n','o','p','q','r','s','t',
                    'u','v','w','x','y','z','#','-','+','=',
                    'A','B','C','D','E','F','G','H','I','J',
                    'K','L','M','N','O','P','Q','R','S','T',
                    'U','V','W','X','Y','Z','^','&','~','/',
                    '0','1','2','3','4','5','6','7','8','9']
        str_over = ['#'] * len(self.data)
        print("".join(str_over))
        for i in range(0,len(str_over)):
            count = 0
            while(str_over[i]!=self.data_list[i]):
                str_over[i] = alphabet[count]
                #print(alphabet[count],end = " ")
                print("\r",end = "")
                print("".join(str_over), end="")
                count +=1
                time.sleep(0.015)

