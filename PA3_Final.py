
import time
import matplotlib.pyplot as plt
from tabulate import tabulate

p_type = {

}
c_type = {

}
f_type = {

}

fr_type = {

}

#Creates pie chart using lists with info
def pie_chart(sizes, labels, title):
    plt.ion()
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    plt.title(title)
    plt.show()

#Creates a table using lists with info
def create_table(headers, info):
    print(tabulate(info, headers=headers, tablefmt="grid"))

#Formats string cooly
def circle_text(info):
    length = len(info)-2
    print("╭─"+"-"*length+"─╮")
    print("|"+info+"|")
    print("╰─"+"-"*length+"─╯")

#datatypes of parameters: correct_list-list, user_input-string
#Dataypes of return: user_input - string
def error_handle(correct_list, user_input, input_type):
    while user_input not in correct_list:
        print("*"*50)
        print(" "*22+"❌!ERROR!❌"+" "*22)
        print(" "*12+"That is not a valid option"+" "*12)
        print(" "*17+"Please try again"+" "*17)
        print("*"*50)
        print("-"*20)
        time.sleep(2)
        print("\n✅ Acceptable choices:")
        for i in correct_list:
            print(f"- {i}")
        time.sleep(1)
        if input_type == "u":
            user_input = input("Please re-enter your answer using the acceptable choices above:\n>>").upper().strip()
        elif input_type == "c":
            user_input = input("Please re-enter your answer using the acceptable choices above:\n>>").capitalize().strip()
        else:
            user_input = input("Please re-enter your answer using the acceptable choices above:\n>>").lower().strip()
        print("-"*20)
    return user_input

#Uses time to delay answers using a string to have a word before the delay
def user_experience(string, n):
    for i in range(n):
        time.sleep(0.15)
        print(string)

#Checks if a string is an integer and returns the input after considering it
def integer_check(input_str, topic):
    int_loop = True
    while int_loop:
        ans = input(input_str)
        try:
            ans = int(ans)
            int_loop = False
        except ValueError:
            print(f"{"*"*20} ❌!ERROR!❌{"*"*20} \n Please enter a number to represent the {topic}: ")
            int_loop = True
    return ans

#Checks if a float is an integer and returns the input after considering it
def float_check(input_str, topic):
    cost_loop = True
    while cost_loop:
        budget = input(input_str)
        try:
            budget = float(budget)
            cost_loop = False
        except ValueError:
            print(f"{"*"*20} ❌!ERROR!❌{"*"*20}\nPlease enter a number to represent {topic} (e.g. 6.00 or 19.99):")
            cost_loop = True
    return budget

#Starts a while loop for an input to replay it and returns the status of the while loop after getting user input info
def replay(loop_control):
    p_type.clear()
    c_type.clear()
    f_type.clear()
    fr_type.clear()

    user_experience("",1)
    print("~"*50)
    replay = input("\n😞 Would you like to leave (yes/no) 😞?\n>>").lower().strip()
    ans = ["yes","y","no","n"]
    error_handle(ans,replay,"l")
    if replay in ["no","n"]:
        loop_control = True
    else:
        loop_control = False
        print("\n☀️ Have a wonderful rest of your day! ☀️\n")
    print("~"*50)
    return loop_control

#Runs an entire process which uses the functions from above and returns the scores of each category of food
def sample_chart(filename, c_score, p_score, f_score, fr_score, budget):

    user_experience("",1)
    print("~"*150)
    print("\nDISCLAIMER: This program is for you own good! You have the freedom to decide a lot of aspects (such as if a certain ingredient is a carb or fiber)\n We suggest you follow the dietry labels on the back of the food or even google, as self-evaluation could result in data bias.\n")
    print("~"*150)
    input("👉 Press enter when you are ready to move on >>")

    user_experience("",1)
    user_experience("next page...🔄",1)
    user_experience("",1)

    print("="*80)
    print("\nNow we will share some info regarding nutrition value -> ")
    print("-"*40)
    print("Above is the suggested dietary chart you should follow:\n".center(80))
    print("="*80)

    sizes = [15, 15, 20, 10]
    labels = ["Carbs", "Protein", "Fiber", "Fruits"]
    time.sleep(0.5)
    pie_chart(sizes, labels, "Suggested Diet Chart")

    input("\n👉 Press enter when you want to move on >> ")

    table_info = []

    with open(filename, "r") as f:
        lines = f.read().splitlines()
        number = (len(lines))
        
        total_cost = 0
        for i in lines:
            line_list = [item.strip() for item in i.split(",")]
            food = line_list[0]
            ftype = line_list[1]
            cost = float(line_list[2])
            total_cost += cost
            round_cost = f"{cost:.2f}"
            table_info.append([food,ftype,round_cost])

            if ftype == "P":
                p_type[food] = cost
            elif ftype == "F":
                f_type[food] = cost
            elif ftype == "FR":
                fr_type[food] = cost
            else:
                c_type[food] = cost
        
        goal = True

        user_experience("",1)
        user_experience("loading food list...🔄",1)
        user_experience("",1)

        print("Below is the table with sample food items, their types (refer to below) and food prices.")
        print("\nType: Carbs, Proteins, Fibers, FRuits\n")
        time.sleep(1)
        create_table(["Food", "Type", "Cost($)"], table_info)
        input("\n👉 Press enter when you want to move on >> ")

        user_experience("",1)
        user_experience("analyzing...🔄",1)
        user_experience("",1)

        print("Based on these items...")

        print("\nYou will now receive a score summary.\n. -Higher negative points -> consistently not reaching your score ❌ \n. -Higher positive points -> consistently reaching your score ✅")

        #Calculates carb score
        if len(c_type) < 2/8*number:
            time.sleep(0.5)
            c_score-=1
            cgoal=f"❌You have not reached your carb goal! Your score was {c_score}"
            circle_text(cgoal)
            goal = False
        elif len(c_type) >= 2/8*number:
            time.sleep(0.5)
            c_score+=1
            cgoal=f"✅CONGRATS! You have reached your carb goal! Your score was +{c_score}"
            circle_text(cgoal)
            goal = False

        #Calculates protein score
        if len(p_type) < 2/8*number:
            time.sleep(0.5)
            p_score-=1
            pgoal=f"❌You have not reached your protein goal! Your protein score was {p_score}"
            circle_text(pgoal)
            goal = False
        elif len(p_type) >= 2/8*number:
            time.sleep(0.5)
            p_score+=1
            pgoal=f"✅CONGRATS! You have reached your protein goal! Your protein score was +{p_score}"
            circle_text(pgoal)
            goal = False

        #Calculates fiber score
        if len(f_type) < 3/8*number:
            time.sleep(0.5)
            f_score-=1
            fgoal=f"❌You have not reached your fiber goal! Your fiber score was {f_score}"
            circle_text(fgoal)
            goal = False
        elif len(f_type) >= 3/8*number:
            time.sleep(0.5)
            f_score+=1
            fgoal=f"✅CONGRATS! You have reached your fiber goal! Your fiber score was +{f_score}"
            circle_text(fgoal)

        #Calculates fruit score
        if len(fr_type) < 1/8*number:
            time.sleep(0.5)
            fr_score-=1
            frgoal=f"❌You have not reached your fruit goal! Your fruit score was {fr_score}"
            circle_text(frgoal)
            goal = False
        elif len(fr_type) >= 1/8*number: 
            time.sleep(0.5)
            fr_score+=1
            frgoal=f"✅CONGRATS! You have reached your fruit goal! Your fruit score was +{fr_score}"
            circle_text(frgoal)

        #Calculates overall score
        if goal:
            time.sleep(1)
            c_score+=1
            p_score+=1
            f_score+=1
            fr_score+=1
            print("🎉 CONGRATS! You have reached all your dietary goals! 🎉")

    f.close()

    input("\n👉 Press enter when you want to move on >> ")

    user_experience("",1)
    user_experience("loading chart...🔄",1)
    user_experience("",1)

    def_size = [len(c_type), len(p_type), len(f_type), len(fr_type)]
    pie_chart(def_size, labels, "Your dietary chart")
    input("👉 Press enter when you want to move on >> ")

    user_experience("",1)
    user_experience("now loading budget...🔄",1)
    user_experience("",1)

    print("Here is your budget tracker for these items:")
    left_over = budget-total_cost
    if left_over<0:
        left_over = 0

    create_table(["Budget", "Total Cost", "Left Over"],[[f"${budget:.2f}", f"${total_cost:.2f}", f"${left_over:.2f}"]])
    
    time.sleep(2)
    print("~"*75)
    print("\nReference Sheet:")
    print("->Budget-The amount you entered at the beginning\n->Total Cost-The sum of the costs of all items\n->Left Over-How much money you have left over (0 means you have none or you owe money AND ENDS THIS PART)\n")
    print("~"*75)
    input("\n👉 Press enter when you want to move on >> ")
    user_experience("",1)
    if left_over==0:
        print("\nYour budget is less than you total cost 😢 \nUh oh! It looks like you need to either increase your budget or lower the number of items you have!")
        return
    
    else:
        print(f"With ${left_over} left, you can supplement more items into one of the categories!\n")
        print("❌Types of food that are needed (in order of most urgent)❌:")
        if f_score<0:
            time.sleep(0.5)
            circle_text("!Fiber! -> Most important") 
        if fr_score<0:
            time.sleep(0.5)
            circle_text("!Fruit! -> Very important") 
        if p_score<0:
            time.sleep(0.5)
            circle_text("Protein -> Moderately important")     
        if c_score<0:
            time.sleep(0.5)
            circle_text("Carbs -> Not required")
        
        print("\n🎉✅Types of food you reached your goal for!✅🎉")
        if f_score>0:
            time.sleep(0.5)
            circle_text("!Fiber!") 
        if fr_score>0:
            time.sleep(0.5)
            circle_text("Fruit") 
        if p_score>0:
            time.sleep(0.5)
            circle_text("Protein")     
        if c_score>0:
            time.sleep(0.5)
            circle_text("Carbs")

    return c_score, p_score, f_score, fr_score, budget, total_cost

#Uses all the functions from above and gives user the option to create and edit their own food list
# Returns the budget info and the scores in each category for the add function   
def create_new_file(file_name, c_score, p_score, f_score, fr_score, budget):
    
    with open(file_name,"a") as f:
        add_loop = True
        while add_loop:
            time.sleep(0.5)
            print("\n"+"="*40)
            print("🍽️ Add New Food Item:".center(40))
            print("="*40)
            user_experience("",1)

            food = input("👉 Enter your food item: ").capitalize().strip()
            ftype = input("👉 Enter the type [C: Carb | P: Protein | F: Fiber | FR: Fruit]: ").upper().strip()
            ftype = error_handle(["C", "P","FR","F"],ftype,"u")
            cost = float_check("👉 Enter the price of your food: $", "price")
            user_experience("",1)
            user_experience("saving info...🔄",1)
            f.write(f"{food}, {ftype}, {cost:.2f}\n")
            
            add_loop = replay(add_loop)

    f.close()

    c_score, p_score, f_score, fr_score, budget, total_cost = sample_chart(file_name, c_score, p_score, f_score, fr_score, budget)

    user_experience("",1)
    user_experience("loading...🔄",1)
    user_experience("",1)

    print("~"*50)
    file_choice = input("\n👉 Would you like to edit any items (yes/no)?\n>>").lower().strip()
    print("~"*50)
    file_choice = error_handle(["yes","y","n","no"], file_choice, "l")
    
    while file_choice not in ["n","no"]:
        print("\n"+"="*50)
        user_experience("",1)
        dict_name = input("👉 Which category would you like to edit (protein, carb, fruit, or fiber)? ").lower().strip()
        error_handle(["carb","c","protein","p","fiber","f","fruit","fr"], dict_name, "l")
        user_experience("",1)
        user_experience("loading...🔄",1)
        file_opts = ["add", "change", "remove", "exit"]
        print("\nHow would you like to change your items? Options:")
        for index, r in enumerate(file_opts):
                print(f"  {index + 1}. {r.capitalize()}")
        file_choice = input("👉 >>").lower().strip()
        error_handle(["add","1","1.","change","2","2.","remove","3.","3", "exit", "4","4."], file_choice, "l")

        user_experience("",1)
        user_experience("loading...🔄",1)
        user_experience("",1)
        

        print("="*50)

        if dict_name in ["carb","c"]:
            c_choices = []
            print("📋 Current items in your carb list:")
            for key in c_type:
                c_choices.append(key)
                print(f" {key} ⋅⋅⋅⋅⋅⋅⋅ ${c_type[key]}")
            if file_choice in ["remove","3","3."]:
                food_item = input("\n👉 What item would you like to remove (only type in the name of your food, do not include the cost)?\n>>").capitalize()
                error_handle(c_choices, food_item, "c")
                c_type.pop(food_item)
                tracker = "removed"
            elif file_choice in ["add","1.","1"]:
                food_item = input("\n👉 What item would you like to add (refer to the table above with all your food items)?\n>>").capitalize()
                cost = float_check("👉 What is the cost of {food_item}?\n>>$","cost")
                c_type[food_item] = cost
                tracker = "added"
            else:
                food_item = input("\n👉 What item would you like to change the cost to (refer to the table above with all your food items)?\n>>").capitalize()
                error_handle(c_choices, food_item, "c")
                cost = float_check("👉 What is the new cost of {food_item}?\n>>$","cost")
                c_type[food_item] = cost
                tracker = "changed the cost of"

            print(f"You have now {tracker} {food_item} in/to/from your carbs list ")
        
        elif dict_name in ["protein","p"]:
            p_choices = []
            print("📋 Current items in your protein list:")
            for key in p_type:
                p_choices.append(key)
                print(f" {key} ⋅⋅⋅⋅⋅⋅⋅ ${p_type[key]}")
            if file_choice in ["remove","3","3."]:
                food_item = input("\n👉 What item would you like to remove (only type in the name of your food, do not include the cost)?\n>>").capitalize()
                error_handle(p_choices, food_item, "c")
                p_type.pop(food_item)
                tracker = "removed"
            elif file_choice in ["add","1.","1"]:
                food_item = input("\n👉 What item would you like to add (refer to the table above with all your food items)?\n>>").capitalize()
                cost = float_check("👉 What is the cost of {food_item}?\n>>$","cost")
                p_type[food_item] = cost
                tracker = "added"
            else:
                food_item = input("\n👉 What item would you like to change the cost to (refer to the table above with all your food items)?\n>>").capitalize()
                error_handle(p_choices, food_item, "c")
                cost = float_check("👉 What is the new cost of {food_item}?\n>>$","cost")
                p_type[food_item] = cost
                tracker = "changed the cost of"

            print(f"You have now {tracker} {food_item} in/to/from your protein list ")
        
        elif dict_name in ["fiber","f"]:
            f_choices = []
            print("📋 Current items in your fiber list:")
            for key in f_type:
                f_choices.append(key)
                print(f" {key} ⋅⋅⋅⋅⋅⋅⋅ ${f_type[key]}")
            if file_choice in ["remove","3","3."]:
                food_item = input("\n👉 What item would you like to remove (only type in the name of your food, do not include the cost)?\n>>").capitalize()
                error_handle(f_choices, food_item, "c")
                f_type.pop(food_item)
                tracker = "removed"
            elif file_choice in ["add","1.","1"]:
                food_item = input("\n👉 What item would you like to add (refer to the table above with all your food items)?\n>>").capitalize()
                cost = float_check("👉 What is the cost of {food_item}?\n>>$","cost")
                f_type[food_item] = cost
                tracker = "added"
            else:
                food_item = input("\n👉 What item would you like to change the cost to (refer to the table above with all your food items)?\n>>").capitalize()
                error_handle(f_choices, food_item, "c")
                cost = float_check("👉 What is the new cost of {food_item}?\n>>$","cost")
                f_type[food_item] = cost
                tracker = "changed the cost of"

            print(f"You have now {tracker} {food_item} in/to/from your fiber list ")
        
        else:
            fr_choices = []
            print("📋 Current items in your fruit list:")
            for key in fr_type:
                fr_choices.append(key)
                print(f" {key} ⋅⋅⋅⋅⋅⋅⋅ ${fr_type[key]}")
            if file_choice in ["remove","3","3."]:
                food_item = input("\n👉 What item would you like to remove (only type in the name of your food, do not include the cost)?\n>>").capitalize()
                error_handle(fr_choices, food_item, "c")
                fr_type.pop(food_item)
                tracker = "removed"
            elif file_choice in ["add","1.","1"]:
                food_item = input("\n👉 What item would you like to add (refer to the table above with all your food items)?\n>>").capitalize()
                cost = float_check("👉 What is the cost of {food_item}?\n>>$","cost")
                fr_type[food_item] = cost
                tracker = "added"
            else:
                food_item = input("\n👉 What item would you like to change (refer to the table above with all your food items)?\n>>").capitalize()
                error_handle(fr_choices, food_item, "c")
                cost = float_check("👉 What is the new cost of {food_item}?\n>>$","cost")
                fr_type[food_item] = cost
                tracker = "changed the cost of"

            print(f"You have now {tracker} {food_item} in/to/from your fruit list ")

        file_choice = input("\n+ Would you like to continue adding (yes/no)? +\n>> ").lower().strip()
        error_handle(["yes", "y", "no","n"],file_choice, "l")

    with open(file_name,"w") as f:
        for food in c_type:
            f.write(f"{food}, C, {c_type[food]:.2f}\n")
        for food in p_type:
            f.write(f"{food}, P, {p_type[food]:.2f}\n")
        for food in f_type:
            f.write(f"{food}, F, {f_type[food]:.2f}\n")
        for food in fr_type:
            f.write(f"{food}, FR, {fr_type[food]:.2f}\n")

    f.close()
    
    user_experience("saving info...🔄",1)
    return c_score, p_score, f_score, fr_score, budget, total_cost

#Adds all the info into a file 
def add_chart(date, c_score, p_score, f_score, fr_score, budget, total_cost):
    with open("diet_store.txt","a") as f:
        
        f.write("\n"+"="*50+"\n")
        f.write(f"🗓️ Date of Entry: {date}\n")

        f.write("\n🏆 The Summary of Goals:\n")
        if c_score<1:
            f.write(" ❌ Carb goal not reached\n") 
        elif c_score>=1:
            f.write(" ✅ Carb goal reached!\n")
        if p_score<1:
            f.write(" ❌ Protein goal not reached\n")
        elif p_score>=1:
            f.write(" ✅ Protein goal reached!\n")
        if f_score<1:           
            f.write(" ❌ Fiber goal not reached\n")
        elif f_score>=1:
            f.write(" ✅ Fiber goal reached!\n")
        if fr_score<1:       
            f.write(" ❌ Fruit goal not reached\n")
        elif fr_score>=1:
            f.write(" ✅ Fruit goal reached!\n")

        f.write(f"\n📊 Score Summary:\n")
        f.write("-+"*30)
        f.write(f"\n| Carb | {c_score} | \n| Protein | {p_score} | \n| Fiber | {f_score} \n{"-"*30} | \n| Fruit | {fr_score}\n")
        f.write("-+"*30)

        f.write("\n\n💰 Budget Summary:\n")
        f.write("-+"*50)
        f.write(f"\n| Your {date} budget: ${budget} | Your total cost of all food items on {date}: ${total_cost}\n")
        f.write("-+"*50)
        f.wrote("\n" + "="*60+"\n\n")

    f.close()

#Displays info from file
def show_chart():
    with open("diet_store","r") as f:
        print("Here are all previous entries with dates:")
        print(f.read())
    f.close()


def main(): 
    #initialize variables
    initial_choices = ["view/create","see previous","exit"]
    file_types = [".txt", ".csv", "txt", "csv"]
    p_options = ["view","v","view/create","1","1.", "create"]
    h_options = ["see previous", "previous", "s", "see", "sp", "s", "2","2."]
    e_options = ["exit","e","exit game", "3", "3."]
    correct_ans = ["yes","no", "y", "n"]
    c_options = ["example","e","create","c", "a.", "b.", "a", "b"]
    #create new list with the file names and append the new file name into that list

    game_on = True
    while game_on:
        user_experience("",1)
        welcome = "!Welcome back/to your diet and budget tracker!"
        circle_text(welcome)

        user_experience("",1)
        print("~"*50)
        print("🗓️ What is the date of when you are completing this entry \n(stored as month/day/year)? 🗓️".center(50))
        user_experience("",1)
        month = integer_check(">>Enter month: ", "month")
        day = integer_check(">>Enter day: ", "day")
        year = integer_check(">>Enter year: ", "year")
        date = f"{month}/{day}/{year}"
        print("~"*50)

        #Runs code if the user does not want to exit by asking them for the name and type of file
        first_choice = ""
        while first_choice not in e_options: 

            user_experience("",1)
            user_experience("loading homepage...🔄", 1)
            user_experience("",1)

            print("="*50)
            print("🏠 WELCOME TO YOUR DIET AND BUDGET TRACKER 🏠".center(50))
            print("="*50)
            print("\nPlease choose an option below:\n")
            
            for index, r in enumerate(initial_choices):
                print(f"  {index + 1}. {r.capitalize()}")
            
            user_experience("",1)
            print("-"*50)
            first_choice = input(f"👉 What would you like to do today?\n>>").lower().strip()
            print("-"*50)
            user_experience("",1)
            user_experience("redirecting...🔄", 1)
            
            if first_choice in p_options: #creating the diet chart
                user_experience("",1)
                print("="*50)
                user_experience("",1)
                print("Get your ingredients and budget ready! You can... \n|    a. View sample     |     b. Create own    |")
                user_experience("",1)
                print("="*50)
                add_terms = input("👉 What would you like to do?\n>>").lower()
                add_terms = error_handle(c_options, add_terms, "l")
                print("*"*50)
                user_experience("",1)
                user_experience("loading...🔄",1)
                user_experience("",1)

                p_score = 0
                c_score = 0
                fr_score = 0
                f_score = 0

                print("🧊Icebreaker🧊: We'll first gather and give info about your finances -> ")
                user_budget = float_check("👉 What is your budget for this week? \n>>$","the cost")

                if add_terms in ["create", "c", "b.", "b", "create own"]:
                    
                    user_experience("",1)
                    print("~"*50)
                    quiz_fn = input(f"\n👉 What would you like to name your file?\n>>").lower().strip()
                    quiz_ext = input("👉 Would you like a .txt or .csv file?\n>>").lower().strip()
                    user_experience("",1)
                    print("~"*50)
                    user_experience("",1)
                    #Checks if file name is valid, and stores the file name if it exists
                    quiz_ext = error_handle(file_types, quiz_ext, "l")

                        #Stores correct file name and inputs it into functions
                    if quiz_ext in [".csv","csv"]: #comma separated value
                        file_url = quiz_fn+".csv" #csv
                    else:
                        file_url = quiz_fn+".txt" #txt

                    loop_control = True
                    while loop_control:
                        c_score, p_score, f_score, fr_score, budget, total_cost = create_new_file(file_url, c_score, p_score, f_score, fr_score, user_budget)
                        add_chart(date, c_score, p_score, f_score, fr_score, budget, total_cost)
                        loop_control = replay(loop_control)

                else:
                    loop_control2 = True
                    while loop_control2:
                        sample_chart("sample.txt",c_score, p_score, f_score, fr_score, user_budget)
                        loop_control2 = replay(loop_control2)

            #Runs the other code if user does not want to exit or play
            elif first_choice in h_options: #Looks at previous scores
                user_experience("previewing history...🔄",1)
                user_experience("",1)
                show_chart()
            elif first_choice in e_options: #exiting
                game_on = False
            else: # print error
                first_choice = error_handle(initial_choices, first_choice, "l")
        
        #Checks if user wants to play again or exit
        game_on = replay(game_on)
        
main()

