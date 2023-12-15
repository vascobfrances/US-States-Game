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


while len(guessed_states) < 50:

    #Acrescentar o numero de estados que já se acertou estilo: 3/50
    answer_state = screen.textinput(title="Guess the State", prompt="What's another stat's name?r")
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        # t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
    elif answer_state == "Exit" or answer_state =="exit":
#acescentar forma de sair do jogo!

    else:
        print("Wrong Answer!!")

#acrescentar saida e mensagem para quando se acerta os estados todos!
#acrescentar contador de quantas tentativas foram necessárias para acertar os 50 estados
#criar um ficheiro csv com os estados que não se acertou

screen.exitonclick()