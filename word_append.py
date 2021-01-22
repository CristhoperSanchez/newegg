
call = open('random_words_list.txt', 'r')
check = call.read()
print("Type any word youd like to append, use -Exit()- to exit")
word = input(": " )
word_list = []
ap = ""
def view():
    for i in word_list:
     print("-"+i)

def swap():
    for i in word_list:
        if i == var_swap:
            print(i)
            user = input("What would you like to change" +i+ "to?")
            if len(user.strip()) == 0:
                print("Invalid input, re-type word or use -Exit()- to exit")
                user = input(":")
                if user == "Exit()":
                    return("Word Change Exited..")
            if len(user.strip()) != 0: 
                i = user
                print(i)
def append(word):
    for i in word_list: 
        if word.strip() in word_list:
            print("Word already in list, select a new one. n\ :")
   
    if word.strip() not in word_list:
        print("word not found in list!")
        word_list.append(word)
        print(word_list)
    print("function ran")

def list_removal(w):
    for i in word_list:
        if i == word_rem:
            confirm = input("Would you like to delete: "+ word_rem +"?:") 
            if confirm.upper() == "Y":
                word_list.remove(i)
            #Working on this part..
               # another = input("Would you like to moidfy another word?")
                #if another.upper() == "Y":
                  # word_rem = input("What word would you like to delete?\n: ")
                  # list_removal(word_rem)
                #else:
                    #print("Exiting..")
            if confirm.upper() == "N":
                delete = input("Is there a different word you would like to select? (Y/N/Exit()")
                if delete.strip() == "Y":
                    new_del = input("What word would you like to delete?:")
                    new_del(delete)  
        if word_rem not in i:
            print("Word not found.")

while word != "Exit()":
    if len(word.strip()) == 0:
        print("Invalid Input") 
        word = input("Try a new word: ")
        if len(word_list) != 0 and word != "Exit()" and len(word.strip()) != 0:
            append(word)
    if len(word_list) == 0 and word != "Exit()" and len(word.strip()) != 0:
        word_list.append(word) 
    if len(word.strip()) > 1 and word != "Exit()":
        print("     " + word + " : Added to list!")
        word = input("Continue adding words, use -Exit()- to exit \n: ") 
        if word != "Exit()" and len(word.strip()) != 0:
                append(word)

    
if word == "Exit()" and len(word_list) > 0:
    choice = input("Would you like to view the words added? (Y/N): ")
    if choice.upper() == "Y":
        print("Words Inputed:")
        view()
        ap = input("Would you like to Change/Append/Exit? \n (C/A/E): ")
        if len(ap) < 1:
            print("invalid entry")
            ap = input("Would you like to Change/Append/Exit? \n (C/A/E): ")
    #if choice.upper() == "N":
        
    #if choice.upper() != "N" or "Y":
        #print("Invalid input")
        if ap.upper() == "C":
            print("C")
            modify = input("What word would you like to modify?\n: ")
            if len(modify.strip()) == 0:
                print("Invalid input!")

            if len(modify.strip()) > 0:
                print("Would you like to delete or change?(C/D)" +modify)
                modify_select = input(": ")
                if modify_select.upper() == "D":
                    word_rem = modify.strip()
                    list_removal(word_rem)
                if modify_select.upper() == "C":
                    new_var = modify
                    swap(new_var)
        if ap.upper() == "A":
            print("practice")
            print(check) 
           
            

           #currentplace =           
view()           
print("Goodbye!")    
