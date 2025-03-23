import time
import sys

# Función para mostrar texto lentamente
def slow_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Función para pausar y esperar a que el usuario presione Enter
def wait_for_key():
    input("Presiona Enter para continuar...")

# Saludo inicial
slow_print(
    "\t \t  -----Welcome to OUR adventure -----\n"
    " To be able to carry out this activity you need pencil and paper\n"
    "Next you will embark on an interactive adventure in which you must make\n decisions and face the consequences of your decisions\n"
    "For that activity we will give you a backpack and money to spend in our store\n"
    "The backpack can only be loaded up to a certain amount of kilos\n and you can buy items in the store until you run out of money\n"
    "\n \t -------------- HISTORY --------------\n"
    "You are going to be asked to make a trip to the mountains\n because the town where you live on the coast is prone to flooding and the sea level has recently risen a lot\n so you must move towards higher ground\n"
    "In preparation for this trip you decide to visit Grokie’s shop\n\n"
)

# Tienda de Gookey
slow_print(
    "\t\t ----------Welcome to Gookey Store----------\n"
    "Here is the list of available items:\n"
    "egg \t $5\t 0.5 kg\n"
    "milk\t $4\t 1 kg\n"
    "bread\t $3\t 0.3 kg\n"
    "flour\t $6\t 2 kg\n"
    "yeast\t $2\t 0.1 kg\n"
    "fishing rod\t $15\t 1.5 kg\n"
    "knife\t $10\t 0.3 kg\n"
    "shovel\t $12\t 2 kg\n"
    "rope\t $8\t 1 kg\n"
    "books\t $7\t 1.2 kg\n"
    "notebook\t $3\t 0.4 kg\n"
    "pencil\t $1\t 0.05 kg\n"
    "camera\t $20\t 0.8 kg\n"
    "toothbrush\t $2\t 0.1 kg\n"
    "laptop\t $50\t 2.5 kg\n"
    "speaker\t $25\t 1 kg\n"
    "flashlight\t $10\t 0.5 kg\n"
    "chair\t $40\t 15kg\n"
    "tent\t $15\t 2kg\n"
)

# Pausa después de la tienda
wait_for_key()

# Lista de ítems en la mochila
backpack = ["flashlight", "knife", "rope"]

# Función para mostrar opciones y tomar decisiones
def make_decision(prompt, options, consequences):
    slow_print(prompt)
    slow_print("\nWhat do you decide to do?")
    for option in options:
        slow_print(option.upper())
    
    decision = input("Choose an option: ").lower()
    
    if decision in consequences:
        slow_print(consequences[decision])
        return decision
    else:
        slow_print("Invalid choice. You hesitate and lose time.")
        return None

# Nivel 1: El inicio del viaje
def level_1():
    slow_print("\n--- Level 1: The Beginning of the Journey ---")
    slow_print("You have left your home and are now on the path to the mountains.")
    slow_print("During the night, you hear strange noises near your camp. It seems like an animal is lurking.")

    options = ["use flashlight", "stay silent", "use knife"]
    consequences = {
        "use flashlight": "You use the flashlight, and the animal runs away scared. You manage to sleep peacefully." if "flashlight" in backpack 
                          else "You don't have a flashlight. The animal approaches and attacks you. You lose some supplies.",
        "stay silent": "You stay silent. The animal leaves after a while. You manage to rest.",
        "use knife": "You use your knife to defend yourself. The animal runs away, but you feel exhausted." if "knife" in backpack 
                      else "You don't have a knife. The animal attacks you, and you lose some supplies."
    }

    decision = make_decision("An animal is nearby. What will you do?", options, consequences)
    if decision == "use flashlight" or decision == "stay silent":
        return level_2_a()
    elif decision == "use knife":
        return level_2_b()

# Nivel 2A: Cruzar el río
def level_2_a():
    slow_print("\n--- Level 2: Crossing the River ---")
    slow_print("You reach a rushing river blocking your path. The water is cold and looks dangerous.")

    options = ["use rope", "find bridge", "swim"]
    consequences = {
        "use rope": "You use the rope to cross the river carefully. You make it to the other side safely." if "rope" in backpack 
                     else "You don't have a rope. You try to cross and almost drown. You lose some supplies.",
        "find bridge": "You find a bridge and manage to cross the river, though you lose a day of travel.",
        "swim": "You try to swim across the river. The current is too strong, and you drown. You die."
    }

    decision = make_decision("A river blocks your path. What will you do?", options, consequences)
    if decision == "swim":
        return "death"
    elif decision == "use rope" or decision == "find bridge":
        return level_3_a()

# Nivel 2B: La tormenta
def level_2_b():
    slow_print("\n--- Level 2: The Storm ---")
    slow_print("A heavy storm catches you in the middle of your journey. The wind and rain make it hard to move forward.")

    options = ["use shovel", "find shelter", "keep walking"]
    consequences = {
        "use shovel": "You dig a temporary shelter and manage to protect yourself from the storm." if "shovel" in backpack 
                      else "You don't have a shovel. The storm hits you, and you get sick. You lose some supplies.",
        "find shelter": "You find a cave and take shelter there. The storm passes without major issues.",
        "keep walking": "You keep walking in the rain. You get sick and lose time recovering."
    }

    decision = make_decision("A storm is approaching. What will you do?", options, consequences)
    if decision == "use shovel" or decision == "find shelter":
        return level_3_b()
    elif decision == "keep walking":
        return "death"

# Nivel 3A: Encuentro con otros viajeros
def level_3_a():
    slow_print("\n--- Level 3: Meeting Other Travelers ---")
    slow_print("You come across a group of travelers who are also fleeing the floods.")

    options = ["join group", "exchange info", "avoid them"]
    consequences = {
        "join group": "You join the group. Although you share supplies, you feel safer with company.",
        "exchange info": "You exchange information with the group and continue your journey alone.",
        "avoid them": "You avoid the group and take a different route. You feel alone but avoid potential conflicts."
    }

    decision = make_decision("You meet other travelers. What will you do?", options, consequences)
    if decision == "join group":
        return "win"
    elif decision == "exchange info" or decision == "avoid them":
        return "continue"

# Nivel 3B: Quedarse sin suministros
def level_3_b():
    slow_print("\n--- Level 3: Running Out of Supplies ---")
    slow_print("Your supplies are running low. Food is scarce, and exhaustion begins to affect you.")

    options = ["use fishing rod", "look for food", "ration supplies"]
    consequences = {
        "use fishing rod": "You fish in the stream and get some food. You feel more prepared to continue." if "fishing rod" in backpack 
                           else "You don't have a fishing rod. You waste time trying to fish with your hands and catch nothing.",
        "look for food": "You look for fruits and berries. Unfortunately, you eat something poisonous and die.",
        "ration supplies": "You ration your supplies and walk faster. You get closer to the mountains but feel weak."
    }

    decision = make_decision("You are running out of supplies. What will you do?", options, consequences)
    if decision == "look for food":
        return "death"
    elif decision == "use fishing rod" or decision == "ration supplies":
        return "continue"

# Función principal para iniciar la aventura
def start_adventure():
    result = level_1()
    if result == "death":
        slow_print("\n--- Game Over ---")
        slow_print("You have died. Your journey ends here.")
        print ("\n\t\t --- Powered by: Lcabs ---")
    elif result == "win":
        slow_print("\n--- You Win! ---")
        slow_print("You have successfully reached the mountains and found a new home.")
        print ("\n\t\t --- Powered by: Lcabs ---")
    else:
        slow_print("\n--- End of the Adventure ---")
        slow_print("Thank you for playing. We hope you enjoyed your journey!")
        print ("\n\t\t --- Powered by: Lcabs ---")

# Iniciar la aventura
start_adventure()
