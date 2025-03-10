
# Bibliotek
import openai  





"""
API KEY er viktig for chatbot. ellers funker den ikke.
Brukes til å identifisere brukeren. 
"""
openai.api_key = "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" 








"""
'messages' er til å logge samtale.
Du definerer en liste []

LIST:
Ordered:    Det betyr at hvert verdi har samme rekkefølge og kan ikke byttes tilfeldig. Lett å finne posisjoen til hvert verdi.
Changeable: Du kan endre, slette og oppdatere list.
Dublicate:  Du kan dublisere verdi. For eksempel [1, 2, 3, 4, 4]. Du har 2 firer.
"""
messages = [
    {"role": "system", "content": "Reply me like a dark hacker"}    # Dictionary eller dict. Defineres som key:value. Samme som å lagre mobilnummer. Slik ser den ut {key:value, key:value}
]










while True:                                                         # while True brukes til å gjenta brukeren's input flere ganger helt til programmet stopper.

    input_to_AI = input("User input: ")                             # Du gir input til chatbotten og deretter legg til samtalen din i 'messages' variabel.
    messages.append({"role": "user", "content": input_to_AI},)      # append() er å legge til messages. Vi legger til dictionary. Det inneholder rollen er user som sier hva som er i content.    

    
    
    
    outputs = openai.ChatCompletion.create(                         # Gitt outputs variabel, kan vi få response fra AI ved å bruke print()             
        model="gpt-3.5-turbo",                                      # Vi bruker modellen: gpt-3.5-turbo
        messages=messages                                           # messages til å hente samtalen fra 'messages' variabel.
    )


    reply = outputs.choices[0].message.content                      # For at AI svarer kun med tekst. Ikke objekt.           
                          
    print(reply)                                                    # Printer ut svar fra AI. 

    messages.append({"role": "assistant", "content": reply})        # append() er å legge til messages. Vi legger til dictionary. Det inneholder rollen er assistant som svarer til user om hva som er i content.    

    