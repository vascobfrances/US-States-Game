import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
all_states = [elemento.lower() for elemento in all_states]
print(all_states)
guessed_states = []
trys = 0
game_is_on = True

while game_is_on == True:
    answer_state = screen.textinput(title= f"Guess the State {trys}/50", prompt="What's another stat's name?r")
    if answer_state in all_states:
        trys += 1
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state.title()]
        print(state_data)
        t.goto(
            int(state_data.x), int(state_data.y))
        t.write(answer_state)
    elif answer_state == "Exit" or answer_state =="exit":
        game_is_on = False
    else:
        print("Wrong Answer!!")

if len(guessed_states) == 50:
    print(f"you guessed all states! Congratulations! You used {trys} trys to guess all states")
else:
    print(f"you guessed {len(guessed_states)} states, you used {trys} trys")
    respostas_por_apreender = 'respostas_por_apreender.csv'
    exclusivos_lista_completa = list(set(all_states) - set(guessed_states))
    with open(respostas_por_apreender, 'w') as file:
        file.write('')
        for elemento in exclusivos_lista_completa:
            file.write(elemento + '\n')
    print("0")

screen.exitonclick()