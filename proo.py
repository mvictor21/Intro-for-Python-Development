preach = ['PREACH', 'preach', 'Preach']
pray = ['PRAY', 'pray', 'Pray']
curse = ['Curse', 'curse', 'CURSE']
run = ['Run away', 'run away', 'RUN AWAY']
repent = ['Repent', 'repent', 'REPENT']
remain = ['Remain', 'remain', 'REMAIN']
exhorts = ['Exhorts', 'exhorts', 'EXHORTS']
go = ['Go back', 'go back', 'GO BACK']

#\n

answer = input("You just reincarnated in Lehi, an ancient prophet that had a dream. God, in that dream warns you 'Lehi' to take your family and leave Jerusalem because the city will be destroyed if the people of the city do not repent. What do you do?\nWith faith, you 'PREACH' to the people so that they can repent of their sins and thus save the city?\nor\nWithout any hope for the people of Jerusalem, you take what you need and 'RUN AWAY' with your family? ")
if answer in preach:
    answer = input("Consequently, people despise you and throw stones at you. What do you do?\nYou 'PRAY' for the Lord to forgive them and run away with your family.\nor\nYou 'CURSE' the city and run away with your family. ")
    if answer in pray:
        answer = input("Because of your love for your fellow beings, the Lord protects you and blesses you towards the desert with your family, but two of your four sons are rebellious and want to return to Jerusalem because they love the temporary things they owned.\nYou 'EXHORTS' them to repent and to trust in the God who created them.\nor\nYou tell them that if they don't trust God, they can 'GO BACK' with the riches they possessed in Jerusalem. ")
        if answer in exhorts:
            print("Thanks to your faith, your youngest son, Nephi is guided by the Lord to build a ship and your whole family crosses the ocean protected by God.\nYOU WIN!")
        elif answer in go:
            print("Because of your hopelessness to your family and unfaithfulness to your God, you and your wife with your two other children get lost into the desert and die of starvation. ")
    elif answer in curse:
        print("Because of your rebellion and pride, God destroys Jerusalem with your family. In fear, you flee alone into the desert and lost in it, you die of starvation.\nGAME OVER.")
elif answer in run:
    answer = input("An angel of God, in another dream, teaches you that must have faith in the people and not judge them even if they don't believe in God and are sinners.\nYou 'REPENT', continue to the desert with your family and teach them the goodness of God with love and humility.\nor\nYou 'REMAIN' your way with your family, they are safe, and you trust that your faith in God will save you just as he has previously shown you in dreams what will happen. ")
    if answer in repent:
        answer = input("You feel peace in your heart and God shows you, His mercy. Now, two of your four sons are rebellious and want to return to Jerusalem because they love the temporary things they owned.\nYou 'EXHORTS' them to repent and to trust in the God who created them.\nor\nYou tell them that if they don't trust God, they can 'GO BACK' with the riches they possessed in Jerusalem. ")
        if answer in exhorts:
            print("Thanks to your faith, your youngest son, Nephi is guided by the Lord to build a ship and your whole family crosses the ocean protected by God.\n \nYOU WIN!")
        elif answer in go:
            print("Because of your hopelessness to your family and unfaithfulness to your God, you and your wife with your two other children get lost into the desert and die of starvation.\n \nGAME OVER.")
    elif answer in remain:
        answer = input('\nGod warns you that you must be humble and to continue with your family running away from Jerusalem, instructing them with the good word and to keep His commandments. Two of your four sons are rebellious and want to return to Jerusalem because they love the temporary things they owned. ')
    if answer in exhorts:
        print("Thanks to your faith, your youngest son, Nephi is guided by the Lord to build a ship and your whole family crosses the ocean protected by God.\n \nYOU WIN!")
    elif answer in go:
        print("Because of your hopelessness to your family and unfaithfulness to your God, you and your wife with your two other children get lost into the desert and die of starvation.\n \nGAME OVER.")

    else:
        print('\nYou are not worthy to continue. See you next time!')