import requests
import json

def dicformat():
    def strvalid():
        pass
    def op(wrd,dic):
        a=dic['def'][0]['sseq']
        for i in a:
            b=i[0][1]['dt'][0][1]
            print(b.replace("{bc}",""))

  
    def strvalid():
        while True:
            wrd=input('Enter the word ')
            print("ENTER 'exit' TO CLOSE")
            if(wrd=="exit"):
                break
            elif(len(wrd)<1):
                print("blank entry please enter a vaild word")
            elif(len(wrd)>1):
                reqwrd=requests.get('https://dictionaryapi.com/api/v3/references/collegiate/json/%s?key=7db6a77c-1b86-41e1-8317-cda669c99769'%wrd)
                data=reqwrd.json()
                dic=data[0]
                try:
                    dickeys=dic.keys()
                    op(wrd,dic)
                    break
                except AttributeError :
                    print("Word not found ,few simmilar words are")
                    for i in data:
                        print(i ,end=" ,")
                    strvalid()
            

            
              
                
    strvalid()

 
   
dicformat()

