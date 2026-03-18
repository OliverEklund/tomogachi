class Tama: 
    namn = input("Vad ska ditt husdjur heta? ")
    health = 100
    happiness = 30
    hunger = 50
    mess = 0
    age = 1

actions = ["discipline", "feed", "play", "pet", "clean"]

print(f"\nVälkommen! Ta hand om {namn} väl.")
,bv
while health > 0:

    print("\n" + "-"*30)
    print(f"STATUS FÖR {namn.upper()}:")
    print(f"Hälsa:  {health}/100")
    print(f"Glädje: {happiness}/100")
    print("-" * 30)
    

    hunger += 10
    happiness -= 5

    if health <= 0:
        break

    print("\nVad vill du göra?")
    
    print(f"Alternativ: {actions}") # Fixa

    val = input("Skriv vad du vill göra: ").lower()
    
    if val == "feed":
        print(f"Du matar {namn}.")
        hunger -= 30
        mess += 1
        
    elif val == "play":
        print(f"Du leker med {namn}!")
        
        
    else:
        print("Ogiltigt val! Djuret tittar förvirrat på dig och tiden går...")

print("\n" + "="*30)
print(f"GAME OVER. {namn} blev {age} år, men har nu dött eller rymt.")
print("="*30)