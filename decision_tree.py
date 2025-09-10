morning = input("Do you want to wake up (y/n)? ")

# Path 1: Wake up
if morning == "y":
    print("You wake up to your alarm clock still tired.")
    breakfast = input("Do you want to eat breakfast or skip it or drink coffee (eat/skip/coffee)? ")

    # Nested decisions based on breakfast choice
    if breakfast == "eat" or breakfast == "coffee":
        print("You feel energized and ready for the day.")
        school = input("Do you want to go to school or skip it (go/skip)? ")

        # Further nested decisions based on if you go to school
        if school == "go":
            print("You arrive at school and complete the day with your energy.")
            grades = input("Do you want to study hard or slack off (study/slack)? ")
            if grades == "study":
                print("You study hard and get straight A's. You get into a good college, but can't find a good job because you have no experience. You die poor with your debt.")
            elif grades == "slack":
                print("You slack off and get D's and F's. You can only live off your parents, but when they die, you became homeless and die.")
            else:
                print("Invalid choice. You do nothing and become homeless and die on the streets.")

        # Decisions based on if you skip school
        elif school == "skip":
            print("You skip school and stay home all day. You're an F student.")
            business = input("Do you want to start a business or get a job (business/job)? ")

            # Further nested decisions based on if you start a business
            if business == "business":
                print("You decide to start a business.")
                idea = input("Do you want to start a resturaunt or a crypto currency (resturaunt/crypto)? ")
                
                # Further nested decisions based on business idea
                if idea == "resturaunt":
                    print("You start a resturaunt but it fails and you go bankrupt. You die poor and unhappy.")
                elif idea == "crypto":
                    print("You start a crypto currency and it becomes the next big thing. You become a billionaire and live happily ever after.")
                else:
                    print("Invalid choice. You do nothing and your parents disown you. You become homeless and get struck by lightning randomly on the streets.")
            
            # Further nested decisions based on if you get a job
            elif business == "job":
                print("You get a job at McDonald's and work there for the rest of your life. You die poor and unhappy.")
            else: 
                print("Invalid choice. You do nothing and become homeless and die on the streets.")
        else:
            print("Invalid choice. You get caught by the police for truancy and go to juvie. You die in jail.")

    # Decisions based on if you skip breakfast
    elif breakfast == "skip":
        print("You feel tired and sluggish throughout the day.")
        nap = input("Do you want to take a nap or power through the day (nap/power)? ")

        # Further nested decisions based on if you take a nap
        if nap == "nap":
            print("You take a nap and feel better. However you missed school.")
            spend = input("Do you want to spend the day playing video games or doing homework (games/homework)? ")
            if spend == "games":
                print("You play video games all day and get addicted. You try to become pro, but you're bad and end up dying alone.")
            elif spend == "homework":
                print("You do your homework and catch up on school. You get good grades and find yourself a few internships. You get a good job and live happily ever after.")
            else:
                print("Invalid choice. You scroll through TikTok and die because you got addicted and forgot to drink or eat anything.")
        
        # Decisions based on if you power through the day
        elif nap == "power":
            print("You power through the day and feel exhausted. You fall asleep in class and get a bad grade.")
        else:
            print("Invalid choice. You do nothing and become homeless and die on the streets.")

# Path 2: Stay asleep
elif morning == "n":
    print("You stay asleep and dream about being in a magical forest.")
    forest_choice = input("Do you want to head to the stone tower or the castle? (tower/castle)? ")

    # Further nested decisions based on going to the tower
    if forest_choice == "tower":
        print("You head to the stone tower and find a wizard. Do you trust him or run away? (trust/run)? ")
        wizard_choice = input("Do you trust him or run away? (trust/run)? ")

        # Further nested decisions based on trusting the wizard
        if wizard_choice == "trust":
            print("The wizard gives you a magic wand and tasks you with killing a dragon.")
            dragon_choice = input("Do you take on the task or refuse? (task/refuse)? ")

            # Further nested decisions based on taking on the task
            if dragon_choice == "task":
                print("You head to the dragon's layer and find out the wand didn't do anything. The dragon eats you. It turns out a black hole was close to Earth and ate it and you die.")
            
            # Further nested decisions based on refusing the task
            elif dragon_choice == "refuse":
                print("You refuse the task and the wizard kicks you out of the tower. You fall to your death. It turns out you live on the 10th floor of an apartment and jumped out the window in your sleep and die.")
            else:
                print("Invalid choice. The wizard kills you with his ice magic. It turns out there was blizzard and you had the windows open and you die of hypothermia.")
        
        # Further nested decisions based on running away from the wizard
        elif wizard_choice == "run":
            print("You run away and fall into a pit of spikes. It turns out you were sleep walking and fell onto a pile of legoes. You die")
        else:
            print("Invalid choice. The wizard kills you with his lightning magic. You get lightning struck in real life and die.")

    # Further nested decisions based on going to the castle
    elif forest_choice == "castle":
        print("You head to the castle and find a dragon.")
        dragon_choice = input("Do you fight the dragon or try taming it? (fight/tame)? ")
        if dragon_choice == "fight":
            print("You try fighting the dragon, but the dragon cooks you with fire breath. It turns out your house was on fire and you died in real life as well.")
        elif dragon_choice == "tame":
            print("You successfully tame the dragon and rule the magical forest together. However, you never wake up from your sleep and die in your sleep.")
    else:
        print("Invalid choice. You wander aimlessly in the forest forever and die in your sleep.")
else:
    print("Invalid input. Please enter 'y' or 'n'.")