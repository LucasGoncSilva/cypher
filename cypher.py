from tkinter import *


def cypher():
    text = input_camp.get()
    new_text = text.replace("a","A")
    new_text = new_text.replace("c","a")
    new_text = new_text.replace("d","D")
    new_text = new_text.replace("e","E")
    new_text = new_text.replace("f","F")
    new_text = new_text.replace("g","G")
    new_text = new_text.replace("h","H")
    new_text = new_text.replace("i","I")
    new_text = new_text.replace("j","J")
    new_text = new_text.replace("k","K")
    new_text = new_text.replace("l","L")
    new_text = new_text.replace("m","M")
    new_text = new_text.replace("n","N")
    new_text = new_text.replace("p","n")
    new_text = new_text.replace("q","m")
    new_text = new_text.replace("r","l")
    new_text = new_text.replace("s","k")
    new_text = new_text.replace("t","j")
    new_text = new_text.replace("u","i")
    new_text = new_text.replace("v","h")
    new_text = new_text.replace("w","g")
    new_text = new_text.replace("x","f")
    new_text = new_text.replace("y","e")
    new_text = new_text.replace("z","d")
    new_text = new_text.replace("A","c")
    new_text = new_text.replace("D","z")
    new_text = new_text.replace("E","y")
    new_text = new_text.replace("F","x")
    new_text = new_text.replace("G","w")
    new_text = new_text.replace("H","v")
    new_text = new_text.replace("I","u")
    new_text = new_text.replace("J","t")
    new_text = new_text.replace("K","s")
    new_text = new_text.replace("L","r")
    new_text = new_text.replace("M","q")
    new_text = new_text.replace("N","p")

    output_txt.set(f"{new_text}")


main_color = '#fff'
secundary_color = '#4717f6'
alert_color = '#f00'


win = Tk()
win.title('Cypher')
win.configure(bg=main_color)


image = PhotoImage(file = 'icon.png')
win.iconphoto(True, image)


info = Label(
    win,
    text='INSIRA O TEXTO NA JANELA ABAIXO PARA (DES)CRIPTOGRAFAR',
    bg=main_color,
    fg=secundary_color
)
info.grid(column=0, row=0, padx=10, pady=5)


rule1 = Label(
    win,
    text='*escreva sempre em minúsculo',
    bg=main_color,
    fg=alert_color
)
rule1.grid(column=0, row=2, padx=10, pady=2)


rule2 = Label(
    win,
    text='*quantidade max indicada de carac. = 60',
    bg=main_color,
    fg=alert_color
)
rule2.grid(column=0, row=4, padx=10, pady=2)


input_camp = Entry(
    win,
    width=64, bg='#ddd',
    fg=secundary_color
)
input_camp.grid(column=0, row=5, padx=10, pady=5)


submit_button = Button(
    win,
    text='Converter texto',
    command=cypher,
    bg=secundary_color,
    fg=main_color
)
submit_button.grid(column=0, row=6, padx=10, pady=5)


output_txt = StringVar()

output_camp = Entry(win, textvariable=output_txt, state="readonly", width=64, fg=secundary_color)
output_camp.grid(column=0, row=8, padx=10, pady=5)


win.mainloop()