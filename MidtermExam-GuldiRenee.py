# Renee Guldi
# SDEV140 MJovanovich
# Practical Exam - Midterm
""" The goal of this program is to allow users to manage a list of tasks. Users will be able
to add tasks, display all currently active tasks, and quit the program. """

# defining the function used to add a task to the list
def addTask(tasksList) -> str:
    # taskInput allows for the user to enter their task as a string variable
    taskInput = input("Enter your task: ")
    # if the user enters no value the program will ask for user input again
    if taskInput == '':
        print("Please enter a task: ")
       
    # when the user enters a valid string variable, this will add the user input the task list.
    elif taskInput:
        tasksList.append(taskInput)
        print(f"Your task: {taskInput} has been added/")
    else:
        return tasksList


# display_tasks will allow for a user to display their current active tasks / validate
# if the list is empty of current tasks.
def display_tasks(tasksList):
    if not tasksList:
        print("No in process tasks yet.")
    else: 
        print("Current Task List: ")
        for index, tasksList in enumerate(tasksList, start=1):
            print(f"{index}")


def main():

    # the brackets [] allow for us to create a list variable to store our user input in.
    tasksList = []

    # utilize a loop based off conditionals , i.e. 
    while True:

        print("Please enter a task to begin or type 'display' to view active lists, if you would like to exit, please type 'quit' ")

        if addTask is None:
            print("Please enter a task: ")

# if the user enters display, it will display current list properties
        elif addTask == 'display':
            display_tasks

        # if the user enters quit this will break the loop
        elif addTask == 'quit': 
            break


if __name__ == "__main__":
    main()