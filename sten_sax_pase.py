import random

def spela_sten_sax_pase():
    val_moeligheter = ['sten', 'sax', 'påse']
    
    while True:
        datorns_val = random.choice(val_moeligheter)
        spelarens_val = input("Välj sten, sax eller påse: ").lower()
        
        if spelarens_val not in val_moeligheter:
            print("Felaktig inmatning. Försök igen.")
            continue
        
        print(f"Datorn valde {datorns_val}. Du valde {spelarens_val}.")
        
        if spelarens_val == datorns_val:
            print("Det blev oavgjort! Spela igen.")
        elif (spelarens_val == 'sten' and datorns_val == 'sax') or \
             (spelarens_val == 'sax' and datorns_val == 'påse') or \
             (spelarens_val == 'påse' and datorns_val == 'sten'):
            print("Du vinner!")
            break
        else:
            print("Du förlorar!")
            break

spela_sten_sax_pase()
