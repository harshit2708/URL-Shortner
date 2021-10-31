import random 
import string

class UrlShort():
    domain = 'https://www.urlshort.py/'
    
    def __init__(self):
        
        self.data = {}
    
    def create_shortURL(self,url):
        
        
        chars = string.ascii_lowercase
        s_url = ''.join(random.choice(chars) for i in range(5))
        short_url = self.domain+s_url
            
        if not short_url  in self.data:
            self.data[short_url] = url
        else:
            for self.i in range(5):
                try:
                    s_url = ''.join(random.choice(chars) for i in range(5))
                    short_url = self.domain+s_url        
                
                    if not short_url  in self.data:
                       self.data[short_url] = url
                       break
                except:
                    pass
                    
            
        print('------------ Your short URL was created!...............')
        
        print('Your URL:',url)
        print('Shorten URL:',short_url)
        
        return short_url
        
        #print(self.data)
    def check_URL(self,url):
        if url in self.data:
            print('\n................. Here is yours...................')
            print('Your original url:',self.data[url.strip()])
        else:
            print('No url found..!')
    
    def update_url(self,url):
        if url in self.data:
            self.data.pop(url.strip())
            
            main_url = input('Enter Your original URL:')
            short_url = input('enter www.urlshort/')
            short_url = self.domain+short_url
            
            if short_url not in self.data and not main_url=='':
                self.data.update(short_url=main_url)
                print('\n.............Successfully updated..!..................')
                print('customized url:',short_url)
            else:
                print('Alredy taken..!')
        else:
            print('No data found...!')
            
            
s = UrlShort()
print("--------------------WELCOME TO URL SHORTNER----------------------\n\n")

url = s.create_shortURL(input('Enter your long url: ')) 
s.data  
print("\n\n--------------------Checking my url------------------")
s.check_URL(url)
print("\n\n--------------------Customise my short url on my own------------------")
s.update_url(url)