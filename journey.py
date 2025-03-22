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
        slow_print(option)
    
    decision = input("Choose an option: ").lower()
    
    if decision in consequences:
        slow_print(consequences[decision])
        return decision  # Devuelve la decisión para manejar finales fatales
    else:
        slow_print("Invalid choice. You hesitate and lose time.")
        return None

# Semana 1: El inicio del viaje
def week_1():
    slow_print("\n--- Week 1: The Beginning of the Journey ---")
    slow_print("You have left your home and are now on the path to the mountains.")
    slow_print("During the night, you hear strange noises near your camp. It seems like an animal is lurking.")

    options = [
        "a) Use the flashlight to scare the animal and protect yourself.",
        "b) Stay silent, hoping the animal will go away.",
        "c) Take your knife (if you have one) and prepare to defend yourself."
    ]

    consequences = {
        "a": "You use the flashlight, and the animal runs away scared. You manage to sleep peacefully." if "flashlight" in backpack 
             else "You don't have a flashlight. The animal approaches and attacks you. You lose some supplies.",
        "b": "You stay silent. The animal leaves after a while. You manage to rest.",
        "c": "You use your knife to defend yourself. The animal runs away, but you feel exhausted." if "knife" in backpack 
             else "You don't have a knife. The animal attacks you, and you lose some supplies."
    }

    return make_decision("An animal is nearby. What will you do?", options, consequences)

# Semana 2: Cruzar el río
def week_2():
    slow_print("\n--- Week 2: Crossing the River ---")
    slow_print("You reach a rushing river blocking your path. The water is cold and looks dangerous.")

    options = [
        "a) Use the rope (if you have one) to cross carefully.",
        "b) Look for a bridge or an alternative path, even if it takes longer.",
        "c) Try to swim across the river."
    ]

    consequences = {
        "a": "You use the rope to cross the river carefully. You make it to the other side safely." if "rope" in backpack 
             else "You don't have a rope. You try to cross and almost drown. You lose some supplies.",
        "b": "You find a bridge and manage to cross the river, though you lose a day of travel.",
        "c": "You try to swim across the river. The current is too strong, and you drown. You die."
    }

    decision = make_decision("A river blocks your path. What will you do?", options, consequences)
    if decision == "c":
        return "death"  # Final fatal

# Semana 3: La tormenta
def week_3():
    slow_print("\n--- Week 3: The Storm ---")
    slow_print("A heavy storm catches you in the middle of your journey. The wind and rain make it hard to move forward.")

    options = [
        "a) Use your shovel (if you have one) to dig a temporary shelter.",
        "b) Look for a cave or a large tree to take cover.",
        "c) Decide to keep walking in the rain, risking getting sick."
    ]

    consequences = {
        "a": "You dig a temporary shelter and manage to protect yourself from the storm." if "shovel" in backpack 
             else "You don't have a shovel. The storm hits you, and you get sick. You lose some supplies.",
        "b": "You find a cave and take shelter there. The storm passes without major issues.",
        "c": "You keep walking in the rain. You get sick and lose time recovering."
    }

    return make_decision("A storm is approaching. What will you do?", options, consequences)

# Semana 4: Encuentro con otros viajeros
def week_4():
    slow_print("\n--- Week 4: Meeting Other Travelers ---")
    slow_print("You come across a group of travelers who are also fleeing the floods.")

    options = [
        "a) Join the group and share your supplies with them.",
        "b) Decide to continue alone but exchange information about the path.",
        "c) Avoid them completely and take a different route."
    ]

    consequences = {
        "a": "You join the group. Although you share supplies, you feel safer with company.",
        "b": "You exchange information with the group and continue your journey alone.",
        "c": "You avoid the group and take a different route. You feel alone but avoid potential conflicts."
    }

    return make_decision("You meet other travelers. What will you do?", options, consequences)

# Semana 5: Quedarse sin suministros
def week_5():
    slow_print("\n--- Week 5: Running Out of Supplies ---")
    slow_print("Your supplies are running low. Food is scarce, and exhaustion begins to affect you.")

    options = [
        "a) Use the fishing rod (if you have one) to fish in a nearby stream.",
        "b) Look for fruits and berries in the forest, risking eating something poisonous.",
        "c) Decide to ration your supplies and walk faster to reach the mountains sooner."
    ]

    consequences = {
        "a": "You fish in the stream and get some food. You feel more prepared to continue." if "fishing rod" in backpack 
             else "You don't have a fishing rod. You waste time trying to fish with your hands and catch nothing.",
        "b": "You look for fruits and berries. Unfortunately, you eat something poisonous and die.",
        "c": "You ration your supplies and walk faster. You get closer to the mountains but feel weak."
    }

    decision = make_decision("You are running out of supplies. What will you do?", options, consequences)
    if decision == "b":
        return "death"  # Final fatal

# Semana 6: El destino final
def week_6():
    slow_print("\n--- Week 6: The Final Destination ---")
    slow_print("Finally, you reach the mountains. The landscape is breathtaking, but you are not alone.")

    options = [
        "a) Look for a secluded spot to build your own shelter.",
        "b) Join a group of people to work together and build a community.",
        "c) Explore the area for resources and potential dangers before deciding what to do."
    ]

    consequences = {
        "a": "You build a secluded shelter. You live in solitude but in peace.",
        "b": "You join a group and build a community. You work together to survive.",
        "c": "You explore the area and encounter a dangerous animal. You are attacked and die."
    }

    decision = make_decision("You have reached the mountains. What will you do?", options, consequences)
    if decision == "c":
        return "death"  # Final fatal

# Función principal para iniciar la aventura
def start_adventure():
    if week_1() == "death":
        slow_print("\n--- Game Over ---")
        slow_print("You have died. Your journey ends here.")
        return
    if week_2() == "death":
        slow_print("\n--- Game Over ---")
        slow_print("You have died. Your journey ends here.")
        return
    if week_3() == "death":
        slow_print("\n--- Game Over ---")
        slow_print("You have died. Your journey ends here.")
        return
    if week_4() == "death":
        slow_print("\n--- Game Over ---")
        slow_print("You have died. Your journey ends here.")
        return
    if week_5() == "death":
        slow_print("\n--- Game Over ---")
        slow_print("You have died. Your journey ends here.")
        return
    if week_6() == "death":
        slow_print("\n--- Game Over ---")
        slow_print("You have died. Your journey ends here.")
        return

    slow_print("\n--- End of the Adventure ---")
    slow_print("Thank you for playing. We hope you enjoyed your journey!")

# Iniciar la aventura
start_adventure()