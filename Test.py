import turtle
import math
import random
import string


with open("WorldPopulationData2019.txt") as data:
    file1 = data.readlines()[1:]

with open("WorldPopulationData2019.txt") as data:
    file2 = data.readlines()[2:]

def print_menu():
    for i in range(4):
        y = 250
        turtle.penup()
        turtle.goto(-150, y + (i*-175))
        turtle.pendown()
        turtle.begin_fill()
        button_color(i)
        turtle.fd(300)
        turtle.left(90)
        turtle.fd(125)
        turtle.left(90)
        turtle.fd(300)
        turtle.left(90)
        turtle.fd(125)
        turtle.left(90)
        turtle.end_fill()
        menu_name(i)

def eight_print_menu():
    for i in range(3):
        y = 250
        turtle.penup()
        turtle.goto(-150, y + (i*-175))
        turtle.pendown()
        turtle.begin_fill()
        button_color(i)
        turtle.fd(300)
        turtle.left(90)
        turtle.fd(125)
        turtle.left(90)
        turtle.fd(300)
        turtle.left(90)
        turtle.fd(125)
        turtle.left(90)
        turtle.end_fill()
        eight_menu_name(i)
    
def nine_print_menu():
    for i in range(3):
        y = 250
        turtle.penup()
        turtle.goto(-150, y + (i*-175))
        turtle.pendown()
        turtle.begin_fill()
        button_color(i)
        turtle.fd(300)
        turtle.left(90)
        turtle.fd(125)
        turtle.left(90)
        turtle.fd(300)
        turtle.left(90)
        turtle.fd(125)
        turtle.left(90)
        turtle.end_fill()
        nine_menu_name(i)

def diff_print_menu():
    for i in range(4):
        y = 250
        turtle.penup()
        turtle.goto(-150, y + (i*-175))
        turtle.pendown()
        turtle.begin_fill()
        button_color(i)
        turtle.fd(300)
        turtle.left(90)
        turtle.fd(125)
        turtle.left(90)
        turtle.fd(300)
        turtle.left(90)
        turtle.fd(125)
        turtle.left(90)
        turtle.end_fill()
        diff_menu_name(i)

def change_print_menu():
    for i in range(3):
        y = 250
        turtle.penup()
        turtle.goto(-150, y + (i*-175))
        turtle.pendown()
        turtle.begin_fill()
        button_color(i)
        turtle.fd(300)
        turtle.left(90)
        turtle.fd(125)
        turtle.left(90)
        turtle.fd(300)
        turtle.left(90)
        turtle.fd(125)
        turtle.left(90)
        turtle.end_fill()
        change_menu_name(i)
        
def nine_chart_print_menu():
    for i in range(4):
        y = 250
        turtle.penup()
        turtle.goto(-150, y + (i*-175))
        turtle.pendown()
        turtle.begin_fill()
        button_color(i)
        turtle.fd(300)
        turtle.left(90)
        turtle.fd(125)
        turtle.left(90)
        turtle.fd(300)
        turtle.left(90)
        turtle.fd(125)
        turtle.left(90)
        turtle.end_fill()
        nine_chart_menu_name(i)
        
def eight_chart_print_menu():
    for i in range(4):
        y = 250
        turtle.penup()
        turtle.goto(-150, y + (i*-175))
        turtle.pendown()
        turtle.begin_fill()
        button_color(i)
        turtle.fd(300)
        turtle.left(90)
        turtle.fd(125)
        turtle.left(90)
        turtle.fd(300)
        turtle.left(90)
        turtle.fd(125)
        turtle.left(90)
        turtle.end_fill()
        eight_chart_menu_name(i)
        
def nine_pie_chart_screen():
    pie_chart(nine_pop_count(file1))
    i = 0
    turtle.penup()
    turtle.goto(-390, 350)
    turtle.pendown()
    turtle.begin_fill()
    button_color(i)
    turtle.fd(90)
    turtle.left(90)
    turtle.fd(40)
    turtle.left(90)
    turtle.fd(90)
    turtle.left(90)
    turtle.fd(40)
    turtle.left(90)
    turtle.end_fill()
    pie_chart_name()

def eight_pie_chart_screen():
    pie_chart(eight_pop_count(file1))
    i = 0
    turtle.penup()
    turtle.goto(-390, 350)
    turtle.pendown()
    turtle.begin_fill()
    button_color(i)
    turtle.fd(90)
    turtle.left(90)
    turtle.fd(40)
    turtle.left(90)
    turtle.fd(90)
    turtle.left(90)
    turtle.fd(40)
    turtle.left(90)
    turtle.end_fill()
    pie_chart_name()

def button_color(i):
    if i == 0:
        turtle.fillcolor('white')
    elif i == 1:
        turtle.fillcolor('blue')
    elif i == 2:
        turtle.fillcolor('green')
    else:
        turtle.fillcolor('yellow')

def chart_color(turtle):
    R = random.random()
    G = random.random()
    B = random.random()
    return(turtle.color(R, G, B))

def menu_name(i):
    if i == 0:
        turtle.ht()
        turtle.penup()
        turtle.goto(0, 250)
        turtle.color("black")
        turtle.write("    World\nPopulation\n     Data", move=False, align="center", font=("Calibri", 24, "bold"))
    elif i == 1:
        turtle.ht()
        turtle.penup()
        turtle.goto(0, 100)
        turtle.color("black")
        turtle.write("2019", move=False, align="center", font=("Calibri", 50, "bold"))
    elif i == 2:
        turtle.ht()
        turtle.penup()
        turtle.goto(0, -75)
        turtle.color("black")
        turtle.write("2018", move=False, align="center", font=("Calibri", 50, "bold"))
    else:
        turtle.ht()
        turtle.penup()
        turtle.goto(0, -235)
        turtle.color("black")
        turtle.write("% Difference", move=False, align="center", font=("Calibri", 30, "bold"))

def eight_menu_name(i):
    if i == 0:
        turtle.ht()
        turtle.penup()
        turtle.goto(0, 265)
        turtle.color("black")
        turtle.write("     2018\nPopulation", move=False, align="center", font=("Calibri", 30, "bold"))
    elif i == 1:
        turtle.ht()
        turtle.penup()
        turtle.goto(0, 90)
        turtle.color("black")
        turtle.write(" View\nMode", move=False, align="center", font=("Calibri", 30, "bold"))
    else:
        turtle.ht()
        turtle.penup()
        turtle.goto(0, -65)
        turtle.color("black")
        turtle.write("Main Menu", move=False, align="center", font=("Calibri", 30, "bold"))

def nine_menu_name(i):
    if i == 0:
        turtle.ht()
        turtle.penup()
        turtle.goto(0, 265)
        turtle.color("black")
        turtle.write("     2019\nPopulation", move=False, align="center", font=("Calibri", 30, "bold"))
    elif i == 1:
        turtle.ht()
        turtle.penup()
        turtle.goto(0, 90)
        turtle.color("black")
        turtle.write(" View\nMode", move=False, align="center", font=("Calibri", 30, "bold"))
    else:
        turtle.ht()
        turtle.penup()
        turtle.goto(0, -65)
        turtle.color("black")
        turtle.write("Main Menu", move=False, align="center", font=("Calibri", 30, "bold"))

def diff_menu_name(i):
    if i == 0:
        turtle.ht()
        turtle.penup()
        turtle.goto(0, 290)
        turtle.color("black")
        turtle.write("Bar Graph", move=False, align="center", font=("Calibri", 30, "bold"))
    elif i == 1:
        turtle.ht()
        turtle.penup()
        turtle.goto(0, 90)
        turtle.color("black")
        turtle.write("      All\nCountries", move=False, align="center", font=("Calibri", 30, "bold"))
    elif i == 2:
        turtle.ht()
        turtle.penup()
        turtle.goto(0, -85)
        turtle.color("black")
        turtle.write("   Enter No.\nof Countries", move=False, align="center", font=("Calibri", 30, "bold"))
    else:
        turtle.ht()
        turtle.penup()
        turtle.goto(0, -235)
        turtle.color("black")
        turtle.write("Main Menu", move=False, align="center", font=("Calibri", 30, "bold"))
        
def nine_chart_menu_name(i):
    if i == 0:
        turtle.ht()
        turtle.penup()
        turtle.goto(0, 290)
        turtle.color("black")
        turtle.write("By Continent", move=False, align="center", font=("Calibri", 30, "bold"))
    elif i == 1:
        turtle.ht()
        turtle.penup()
        turtle.goto(0, 80)
        turtle.color("black")
        turtle.write("Largest/Smallest\n  Population per\n      Continent", move=False, align="center", font=("Calibri", 24, "bold"))
    elif i == 2:
        turtle.ht()
        turtle.penup()
        turtle.goto(0, -75)
        turtle.color("black")
        turtle.write("Filter Countries\n   by Alphabet", move=False, align="center", font=("Calibri", 24, "bold"))
    else:
        turtle.ht()
        turtle.penup()
        turtle.goto(0, -235)
        turtle.color("black")
        turtle.write("Main Menu", move=False, align="center", font=("Calibri", 30, "bold"))

def eight_chart_menu_name(i):
    if i == 0:
        turtle.ht()
        turtle.penup()
        turtle.goto(0, 290)
        turtle.color("black")
        turtle.write("By Continent", move=False, align="center", font=("Calibri", 30, "bold"))
    elif i == 1:
        turtle.ht()
        turtle.penup()
        turtle.goto(0, 80)
        turtle.color("black")
        turtle.write("Largest/Smallest\n  Population per\n      Continent", move=False, align="center", font=("Calibri", 24, "bold"))
    elif i == 2:
        turtle.ht()
        turtle.penup()
        turtle.goto(0, -75)
        turtle.color("black")
        turtle.write("Filter Countries\n   by Alphabet", move=False, align="center", font=("Calibri", 24, "bold"))
    else:
        turtle.ht()
        turtle.penup()
        turtle.goto(0, -235)
        turtle.color("black")
        turtle.write("Main Menu", move=False, align="center", font=("Calibri", 30, "bold"))

def pie_chart_name():
    turtle.ht()
    turtle.penup()
    turtle.goto(-345, 360)
    turtle.color("black")
    turtle.write("< Back", move=False, align="center", font=("Calibri", 14, "bold"))

def user_bar_chart_input():
    turtle.ht()
    turtle.penup()
    turtle.goto(0, 360)
    turtle.write("Enter the number of countries in the shell", move=False, align="center", font=("Calibri", 16, "bold"))
    while True:
        user = int(input("How many countrie would you like to see? Enter a number between 0-32 = "))
        if 31 < user < 0:
            print("Please enter a number between 0-32 = ")
        else:
            break
    turtle.reset()
    draw_lines(user_line_chart(user))
        
def check_button(x, y): #main menu
    if -150 < x < 150 and 75 < y < 200:
        turtle.reset()
        nine_print_menu()
        turtle.onscreenclick(nine_check_button)
    elif -150 < x < 150 and -100 < y < 25:
        turtle.reset()
        eight_print_menu()
        turtle.onscreenclick(eight_check_button)
    elif -150 < x < 150 and -275 < y < -150:
        turtle.reset()
        count_pop_pert(file2)
        diff_print_menu()
        turtle.onscreenclick(diff_check_button)
        
def nine_check_button(x, y): #2019
    if -150 < x < 150 and 75 < y < 200:
        turtle.reset()
        nine_chart_print_menu()
        turtle.onscreenclick(nine_chart_check_button)
    elif -150 < x < 150 and -100 < y < 25: 
        turtle.reset()
        main()

def eight_check_button(x, y): #2018
    if -150 < x < 150 and 75 < y < 200:
        turtle.reset()
        eight_chart_print_menu()
        turtle.onscreenclick(eight_chart_check_button)
    elif -150 < x < 150 and -100 < y < 25:
        turtle.reset()
        main()

def diff_check_button(x, y): #diff
    if -150 < x < 150 and 75 < y < 200:
        turtle.reset()
        draw_lines(line_chart(file2))
        pie_chart_name()
        turtle.onscreenclick(bar_chart_menu_back)
    elif -150 < x < 150 and -100 < y < 25:
        turtle.reset()
        user_bar_chart()
        pie_chart_name()
        turtle.onscreenclick(bar_chart_menu_back)
    elif -150 < x < 150 and -275 < y < -150:
        turtle.reset()
        main()
        
def nine_chart_check_button(x, y): #2019 view menu
    if -150 < x < 150 and 250 < y < 375:
        turtle.reset()
        nine_pie_chart_screen()
        turtle.onscreenclick(nine_pie_chart_back)
    elif -150 < x < 150 and 75 < y < 200: 
        print("L/S")
    elif -150 < x < 150 and -100 < y < 25:
        print("Filter")
    elif -150 < x < 150 and -275 < y < -150:
        turtle.reset()
        main()

def eight_chart_check_button(x, y): #2018 view menu
    if -150 < x < 150 and 250 < y < 375:
        turtle.reset()
        eight_pie_chart_screen()
        turtle.onscreenclick(eight_pie_chart_back)
    elif -150 < x < 150 and 75 < y < 200: 
        print("L/S")
    elif -150 < x < 150 and -100 < y < 25:
        print("Filter")
    elif -150 < x < 150 and -275 < y < -150:
        turtle.reset()
        main()

def nine_pie_chart_back(x, y):
    if -390 < x < -300 and 350 < y < 390:
        turtle.clearscreen()
        turtle.tracer(0)
        nine_chart_print_menu()
        turtle.onscreenclick(nine_chart_check_button)

def eight_pie_chart_back(x, y):
    if -390 < x < -300 and 350 < y < 390:
        turtle.clearscreen()
        turtle.tracer(0)
        eight_chart_print_menu()
        turtle.onscreenclick(eight_chart_check_button)

def bar_chart_menu_back(x, y):
    if -390 < x < -300 and 350 < y < 390:
        turtle.clearscreen()
        turtle.tracer(0)
        diff_print_menu()
        turtle.onscreenclick(diff_check_button)
'''     
def eight_pop_count(file1):
    x = 0
    asia = 0
    NA = 0
    SA = 0
    EU = 0
    OC = 0
    AF = 0

    for i in file1:
        n = i.split("; ")
        if "Asia\n" in n[7]:
            asia += int(n[2])
        elif "North America\n" in n[7]:
            NA += int(n[2])
        elif "South America\n" in n[7]:
            SA += int(n[2])
        elif "Europe\n" in n[7]:
            EU += int(n[2])
        elif "Oceania\n" in n[7]:
            OC += int(n[2])
        elif "Africa\n" in n[7]:
            AF += int(n[2])
    pop_total = asia + NA + SA + EU + OC + AF
    asia_pert = "{:.1f}".format((asia/pop_total)*100)
    NA_pert = "{:.1f}".format((NA/pop_total)*100)
    SA_pert = "{:.1f}".format((SA/pop_total)*100)
    EU_pert = "{:.1f}".format((EU/pop_total)*100)
    OC_pert = "{:.1f}".format((OC/pop_total)*100)
    AF_pert = "{:.1f}".format((AF/pop_total)*100)
    cont = {"Asia":[asia, asia_pert], "North America":[NA, NA_pert], "South America":[SA, SA_pert], "Europe":[EU, EU_pert], "Oceania":[OC, OC_pert], "Africa":[AF, AF_pert]}
    cont_pert = [asia_pert, NA_pert, SA_pert, EU_pert, OC_pert, AF_pert]
    print("Continent--Total Population--Percentage")
    for key, value in cont.items():
        print(key,"--", value[0],"--", value[1],"%")
        x += 1
        
    return(cont_pert)

def nine_pop_count(file1):
    x = 0
    asia = 0
    NA = 0
    SA = 0
    EU = 0
    OC = 0
    AF = 0

    for i in file1:   
        n = i.split("; ")
        if "Asia\n" in n[7]:
            asia += int(n[3])
        elif "North America\n" in n[7]:
            NA += int(n[3])
        elif "South America\n" in n[7]:
            SA += int(n[3])
        elif "Europe\n" in n[7]:
            EU += int(n[3])
        elif "Oceania\n" in n[7]:
            OC += int(n[3])
        elif "Africa\n" in n[7]:
            AF += int(n[3])
    pop_total = asia + NA + SA + EU + OC + AF
    asia_pert = "{:.1f}".format((asia/pop_total)*100)
    NA_pert = "{:.1f}".format((NA/pop_total)*100)
    SA_pert = "{:.1f}".format((SA/pop_total)*100)
    EU_pert = "{:.1f}".format((EU/pop_total)*100)
    OC_pert = "{:.1f}".format((OC/pop_total)*100)
    AF_pert = "{:.1f}".format((AF/pop_total)*100)
    cont_pert = [asia_pert, NA_pert, SA_pert, EU_pert, OC_pert, AF_pert]
    cont = {"Asia":[asia, asia_pert], "North America":[NA, NA_pert], "South America":[SA, SA_pert], "Europe":[EU, EU_pert], "Oceania":[OC, OC_pert], "Africa":[AF, AF_pert]}
    print("Continent--Total Population--Percentage")
    for key, value in cont.items():
        print(key,"--", value[0],"--", value[1],"%")
        x += 1

    return(cont_pert)

def line(t, n, length, angle):
    for _ in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    arc_len = 2 * math.pi * r * abs(angle)/360
    n = int(arc_len/4) + 1
    step_len = arc_len/n
    step_ang = float(angle)/n
    t.lt(step_ang/2)
    line(t, n, step_len, step_ang)
    t.rt(step_ang/2)

def pie_chart(draw):
    cont = ["Asia", "North America", "South America", "Europe", "Oceania", "Africa"]
    pert = ["59.7%", "7.6%", "5.5%", "9.7%", "0.5%", "17.0%"]
    xcor = ["-125", "-260", "-180", "25", "100", "185"]
    ycor = ["185", "-170", "-215", "-225", "-200", "-120"]
    turtle.reset()
    turtle.ht()
    y = draw
    x = 0
    z = 0
    for i in y:
        turtle.begin_fill()
        chart_color(turtle)
        turtle.fd(200)
        turtle.left(90)
        turtle.pendown()
        arc(turtle, 200, float(y[x])*3.6)
        turtle.end_fill()
        turtle.goto(0,0)
        turtle.right(90)
        turtle.penup()
        x += 1
    turtle.color('black')
    for i in cont:
        turtle.setpos(float(xcor[z]), float(ycor[z]))
        turtle.write(cont[z], font = ("Calibri", 15, "bold"))
        turtle.setpos(200, 300 - (z*-20))
        turtle.write(i, font=("Calibri", 12, "bold"))
        turtle.setpos(330, 300 - (z*-20))
        turtle.write(pert[z], font=("Calibri", 12, "bold"))
        z += 1
    turtle.update()
    turtle.setpos(0, 300)
    turtle.color("black")
    turtle.write("Pie Chart of the Continents", move=False, align="center", font=("Calibri", 20, "bold"))
'''
def user_bar_chart(user):
    neg_list = {}
    user_list1 = []
    user_list2 = []
    for i in file2:
        n = i.split("; ")
        if "-" in n[6]:
            key, v1, v2 = n[1], n[3], n[6]
            neg_list[key] = n[3], n[6]
            sort_neg_list = sorted(neg_list.items(), key = lambda k_v: float(k_v[1][1]))
    i = user
    n = i
    x = 0
    y = 0
    for i in range(x, i):
        custom_list2.append(sort_neg_count_list[x])
        x += 1
    for i in range(y, n):
        custom_list1.append(sort_neg_count_list[y][1][1])
        y += 1
    custom_list1.sort()
    a = -1
    xcor = 200
    ycor = 290
    turtle.ht()
    turtle.penup()
    turtle.goto(xcor, ycor)
    turtle.pendown()
    for i in custom_list2:
        turtle.ht()
        turtle.color("black")
        turtle.goto(xcor, ycor)
        turtle.write(custom_list2[a][0]+custom_list2[a][1][1]+'%',font=('Calibri',9,'bold'))
        turtle.penup()
        a -= 1
        ycor -= 20
        ycor1 = 295
    for i in custom_list2:
        turtle.penup()
        turtle.setpos(-350, ycor1)
        turtle.pendown()
        turtle.goto(200, ycor1)
        ycor1 -= 20
    return(custom_list)

def bar_chart(file2):
    x = -1
    i = {}
    neg_count_list1 = {}
    neg_count_list2 = {}
    for n in file2:
        i = n.split("; ")
        if "-" in i[6]:
            key,v1,v2 = i[1], i[3], i[6]
            neg_count_list1[key] = i[3] ,i[6]
            sort_neg_count_list1=sorted(neg_count_list1.items(), key = lambda k_v: float(k_v[1][1]))
    for n in file1:
        i = n.split(';')   
        if '-' in i[6]:
            key,v1 = i[1],i[6]
            neg_count_list2[key]=i[6]
            sort_neg_count_list2=sorted(neg_count_list2.values(), key = lambda x: float(x),reverse= True)
    turtle.ht()
    y = -1
    xcor = 200
    ycor = 290
    ycor1 = 295
    turtle.penup()
    turtle.goto(xcor, ycor)
    turtle.pendown()
    for n in sort_neg_count_list1:
        turtle.ht()
        turtle.color("black")
        turtle.goto(xcor, ycor)
        turtle.write(sort_neg_count_list1[y][0]+sort_neg_count_list1[y][1][1]+'%',font=('Calibri',9,'bold'))
        turtle.penup()
        y -= 1
        ycor -= 20
    for n in sort_neg_count_list1:
        turtle.penup()
        turtle.setpos(-350, ycor1)
        turtle.pendown()
        turtle.goto(200, ycor1)
        ycor1 -= 20
    return(sort_neg_count_list2)

def draw_bars(data):
    n = 0
    turtle.penup()
    turtle.goto(-350, 300)
    turtle.pendown()
    for i in data:
        chart_color(turtle)
        turtle.begin_fill()
        turtle.fd(abs(float(data[0])*150))
        turtle.right(90)
        turtle.fd(10)
        turtle.right(90)
        turtle.fd(abs(float(data[0])*150))
        turtle.left(90)
        turtle.fd(10)
        turtle.left(90)
        turtle.end_fill()
        n += 1
    turtle.reset()
    turtle.penup()
    turtle.setpos(0, 350)
    turtle.pendown()
    turtle.color("black")
    turtle.write("Chart of countries with negative percentage", font=("Calibri", 12,'bold'))

'''
def letter_filter():
    lst = list(string.ascii_uppercase)
    a = -450
    b = 350
    x = 0
    pen = turtle.Turtle()
    pen.ht()
    pen.penup()
    for i in lst:
        pen.setpos(a, b)
        pen.write(lst[x], font=('Calibri',12,'bold'))
        x += 1
        a += 35
    pen.setpos(100, -350)
    pen.write("Click", font=('Calibri',12,'bold'))
    pen.setpos(400, 250)
    pen.write("Home", font=('Calibri',12,'bold'))

def undo_menu(x, y):
    turtle.reset()
    letter_filter()
    turtle.update()
    pen.fd(0.02)
    turtle.onscreenclick(select_alpha)
    turtle.listen()

def count_alpha(user, xcor, ycor):
    list1 = []
    list2 = []
    for i in files:
        n = i.split("; ")
        if user in a[1][1]:
            list1.append(a[3])
            list2.append(a[1])
    a = 0
    x = -450
    pen.up()
    for i in list2:
        pen.setpos(x, ycor)
        pen.write(list2[a], font=('Calibri',12,'bold'))
        pen.setpos(x+300, ycor)
        pen.write(list1[a], font=('Calibri',12,'bold'))
        ycor -= 22
        a += 1
    turtle.onscreenclick(undo_menu)
    turtle.listen()
'''
def count_pop_pert(file2):
    print("Continent--Total Population--Percentage")
    count_list = {}
    for i in file2:
        n = i.split("; ")
        key, v1, v2 = n[1], n[3], n[6]
        count_list[key] = n[3], n[6]
        sort_list = sorted(count_list.items(), key = lambda k_v: abs(float(k_v[1][1])), reverse = True)
    #for i in sort_list:
        #print(str(i).replace("(","").replace("'","").replace(")","").replace(",","").replace('-',''))
'''
def select_alpha(x, y):
    if -450 < x < -440 and 350 < y < 375:
        count_alpha("A", -460, 320)
    elif -450 < x < -440 and 350 < y < 375:
        count_alpha("B", -460, 320)
    elif -450 < x < -440 and 350 < y < 375:
        count_alpha("C", -460, 320)
    elif -450 < x < -440 and 350 < y < 375:
        count_alpha("D", -460, 320)
    elif -450 < x < -440 and 350 < y < 375:
        count_alpha("E", -460, 320)
    elif -450 < x < -440 and 350 < y < 375:
        count_alpha("F", -460, 320)
    elif -450 < x < -440 and 350 < y < 375:
        count_alpha("G", -460, 320)
    elif -450 < x < -440 and 350 < y < 375:
        count_alpha("H", -460, 320)
    elif -450 < x < -440 and 350 < y < 375:
        count_alpha("I", -460, 320)
    elif -450 < x < -440 and 350 < y < 375:
        count_alpha("J", -460, 320)
    elif -450 < x < -440 and 350 < y < 375:
        count_alpha("K", -460, 320)
    elif -450 < x < -440 and 350 < y < 375:
        count_alpha("L", -460, 320)
    elif -450 < x < -440 and 350 < y < 375:
        count_alpha("M", -460, 320)
    elif -450 < x < -440 and 350 < y < 375:
        count_alpha("N", -460, 320)
    elif -450 < x < -440 and 350 < y < 375:
        count_alpha("O", -460, 320)
    elif -450 < x < -440 and 350 < y < 375:
        count_alpha("P", -460, 320)
    elif -450 < x < -440 and 350 < y < 375:
        count_alpha("Q", -460, 320)
    elif -450 < x < -440 and 350 < y < 375:
        count_alpha("R", -460, 320)
    elif -450 < x < -440 and 350 < y < 375:
        count_alpha("S", -460, 320)
    elif -450 < x < -440 and 350 < y < 375:
        count_alpha("T", -460, 320)
    elif -450 < x < -440 and 350 < y < 375:
        count_alpha("U", -460, 320)
    elif -450 < x < -440 and 350 < y < 375:
        count_alpha("V", -460, 320)
    elif -450 < x < -440 and 350 < y < 375:
        count_alpha("W", -460, 320)
    elif -450 < x < -440 and 350 < y < 375:
        count_alpha("X", -460, 320)
    elif -450 < x < -440 and 350 < y < 375:
        count_alpha("Y", -460, 320)
    elif -450 < x < -440 and 350 < y < 375:
        count_alpha("Z", -460, 320)
    elif -450 < x < -440 and 350 < y < 375:
        turtle.reset()
        turtle.homepage()
'''
def main():
    print_menu()
    turtle.onscreenclick(check_button)
    turtle.listen()
    turtle.done()
    
screen = turtle.Screen()
screen.setup(800,800)
turtle.tracer(0)
turtle.ht()

main()

turtle.listen()

turtle.mainloop()


