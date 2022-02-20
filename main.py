import turtle
import pandas

# screen set up
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# writing turtle
tim = turtle.Turtle()
tim.hideturtle()
tim.pu()

# use this if you want to tweak any of the state position coordinates
# def get_mouse_click_coor(x, y):
#     print(x, y)
# screen.onscreenclick(get_mouse_click_coor)


score = 0
guessed_states_list = []

# read from the csv and prepare the data to be used
states_data = pandas.read_csv("50_states.csv")
states_dict = {
    "state": states_data["state"].to_list(),
    "x_coordinate": states_data["x"].to_list(),
    "y_coordinate": states_data["y"].to_list()
}

# main game loop
while score != 50:

    # get the user input for a state
    answer_state = screen.textinput(title=f"{score}/50 Guess the state", prompt="What's another state name?").title()

    # if the user types exit then the game will end and we will be presented with a new csv file with states we can
    # brush up on to get better
    if answer_state == "Exit":
        states_to_learn = []
        for state in states_dict["state"]:
            if state not in guessed_states_list:
                states_to_learn.append(state)

        # here is where we actually write the csv file with our states to learn
        df_states_to_learn = pandas.DataFrame(states_to_learn).to_csv("states_to_learn.csv")
        break
    # check the input given to see if it's a valid answer
    if answer_state in states_dict["state"]:
        # grab the index of the correct answer
        temp_index = states_dict["state"].index(answer_state)

        # print(f"you got hold of the state and it's index is: {temp_index}")

        # get the turtle to go to the state's coordinates and write the name of the state there
        tim.goto(states_dict["x_coordinate"][temp_index], states_dict["y_coordinate"][temp_index])
        tim.write(states_dict["state"][temp_index])
        guessed_states_list.append(answer_state)
        score += 1
        # tim.showturtle()



