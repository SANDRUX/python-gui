# -*- coding: utf-8 -*-

from tkinter import *
import wikipedia
import os
#from pptx import Presentation
from PIL import ImageTk, Image
import urllib.request
#import selenium
#import wget 

#MADE BY SEBASTIAN SANCHEZ AND KANIEL OUTIS

def get_photo():
    global our_files
    global count_loop
    global image_file_source
    count_loop = 0
    size_order = len(var.images)
    print(var.images)
    print(size_order)
    image_file_source = []
    opener=urllib.request.build_opener()
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)
    #urllib.request.urlretrieve(image_url, filename)
    for t in var.images:
        if t.find("jpg") != -1:
            image_file_source.append("file"+str(count_loop)+".jpg")
            urllib.request.urlretrieve(t ,image_file_source[count_loop])
            count_loop += 1
    
        elif t.find("png") != -1:
            image_file_source.append("file"+str(count_loop)+".png")
            urllib.request.urlretrieve(t ,image_file_source[count_loop])
            count_loop += 1
        
        elif t.find("svg") != -1:
            image_file_source.append("file"+str(count_loop)+".svg")
            urllib.request.urlretrieve(t ,image_file_source[count_loop])
            count_loop += 1

def get_text_pres():
    global unpars
    global parsed 
    global size_parsed
    global _prs_
    unpars = var.content
    parsed = unpars.split("==")
    size_parsed = len(parsed)
    #os.startfile("my_presentation")
    print("==================== \n")
    print(parsed)
    print("\n ====================")
#def make_slides():


def create_filecontent():
    myfile = open("MyFile.txt","w+")
    myfile.write(parsed)
    myfile.close()


def getListOrder():
    global topic
    global var
    gottenSuggestInfo = number.get()
    topic = string[gottenSuggestInfo]
    var = wikipedia.page(topic)
    print('\n'+var.content)
    get_photo()
    
    ########################
            

def clear():
    mylabel.destroy()
    myButton['state'] = NORMAL
    mybtn.destroy()
    newline.destroy()
    newSuggestSection.destroy()


def suggestWindow():
   if status == 1:
        root = Toplevel(main)
        root.geometry("450x300")
        root.title('Selection Window')

        global number
        global getResultNumber
        global entrySuggest
        global mysuggestBtn
        number = IntVar()

        Label(root, text='გთხოვთ შეიყვანოთ თქვენი არჩევანი.').pack()

        entrySuggest = Entry(root, textvariable = number)
        entrySuggest.pack()

        Label(root, text='').pack()

        mysuggestBtn = Button(root, text="მიიღეთ სრული ინფორმაცია.", command=getListOrder, width="50", height="2", bg="#00fab7", fg="white")
        mysuggestBtn.pack()

        root.mainloop()


   elif status == 2:
        root = Toplevel(main)
        root.geometry("450x300")
        root.title('Selection Window')
        number = IntVar()

        Label(root, text='Please enter your suggestion.').pack()

        entrySuggest = Entry(root, textvariable = number)
        entrySuggest.pack()

        Label(root, text='').pack()

        mysuggestBtn = Button(root, text="Get Information.", command=getListOrder, width="50", height="2", bg="#00fab7", fg="white")
        mysuggestBtn.pack()

        root.mainloop()


   elif status == 3:
        root = Toplevel(main)
        root.geometry("450x300")
        root.title('Selection Window')

        number = IntVar()

        Label(root, text='Пожалуйста, введите ваше предложение.').pack()

        entrySuggest = Entry(root, textvariable = number)
        entrySuggest.pack()

        Label(root, text='').pack()

        mysuggestBtn = Button(root, text="Получить информацию.", command=getListOrder, width="50", height="2", bg="#00fab7", fg="white")
        mysuggestBtn.pack()

        root.mainloop()
            

def fun1():

    global string
    global search_engine
    global suggest_status
    global suggest_size
    last_info = search.get()

    if status == 1:
        wikipedia.set_lang("ka")
        search_engine = wikipedia.search(last_info)
        string = search_engine

    elif status == 2:
        wikipedia.set_lang("en")
        search_engine = wikipedia.search(last_info)
        string = search_engine

    elif status == 3:
        wikipedia.set_lang("ru")
        search_engine = wikipedia.search(last_info)
        string = search_engine

    #mylist = string.split('')
    #lenght = len(mylist)
    # print(mylist)
    print(search_engine)
    size = len(string)
    global newline
    global newSuggestSection
    global mylabel
    global mybtn
    word = []
    for i in range(1, size): 
        word.append('\n' + str(i) + ') ' + string[i] + '\n')

    strl = len(word)

    if strl >= 1:
        mylabel = Label(textFrame, text=word, bg="#fa8857", fg="#0c00fa")
        mylabel.pack()
        newSuggestSection = Button(textFrame, text="Open Selection Window", bg="lightgreen",
        fg="#263D42", command=suggestWindow, width="20", height="2")
        newSuggestSection.pack()

    else:
        mylabel = Label(textFrame, text="არ მოიძებნა / not found / Нет результатов", bg="#fa8857", fg="white", font=('Consolas', 23))
        mylabel.pack()
        

    newline = Label(textFrame, text="", bg="#fa8857")
    newline.pack()
    mybtn = Button(textFrame, text="Clear", bg="lightgreen",
    fg="#263D42", command=clear, width="20", height="2")
    mybtn.pack()
    myButton['state'] = DISABLED


def mainscreen_KA():
    root = Toplevel(main)
    root.title('presentation find')
    root.geometry("1920x1080")

    global status 
    status = 1
    global search
    global result
    global entryInput


    canvas = Canvas(root, width=1920, height=1080, bg="#263D42")
    canvas.pack()

    frame = Frame(root, bg="white")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    Label(frame, text=" ").pack()
    Label(frame, text="გთხოვთ შეიყვანოთ სასურველი ინფორმაციის სათაური.").pack()
    search = StringVar()
    entryInput = Entry(frame, textvariable=search,
    width="35", bg="cyan", fg="#2e2e2e")
    entryInput.pack()
    Label(frame, text=" ").pack()
    global myButton
    myButton = Button(frame, text="მიიღე შედეგები", width="40",
    height="2", bg="lightblue", fg="#fa8857", command=fun1)
    myButton.pack()
    global textFrame
    textFrame = Frame(frame, bg="#fa8857")
    textFrame.place(relwidth=0.8, relheight=0.6, relx=0.1, rely=0.3)

    root.mainloop()


def mainscreen_EN():
    root = Toplevel(main)
    root.title('presentation find')
    root.geometry("1920x1080")

    global status
    status = 2
    global search
    global result
    global entryInput


    canvas = Canvas(root, width=1920, height=1080, bg="#263D42")
    canvas.pack()

    frame = Frame(root, bg="white")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    Label(frame, text=" ").pack()
    Label(frame, text="Please enter presentation title:").pack()
    search = StringVar()
    entryInput = Entry(frame, textvariable=search,
    width="35", bg="cyan", fg="#2e2e2e")
    entryInput.pack()
    Label(frame, text=" ").pack()
    global myButton
    myButton = Button(frame, text="Get Results", width="40",
    height="2", bg="lightblue", fg="#fa8857", command=fun1)
    myButton.pack()
    global textFrame
    textFrame = Frame(frame, bg="#fa8857")
    textFrame.place(relwidth=0.8, relheight=0.6, relx=0.1, rely=0.3)

    root.mainloop()


def mainscreen_RU():
    root = Toplevel(main)
    root.title('presentation find')
    root.geometry("1920x1080")

    global status
    status = 3
    global search
    global result
    global entryInput


    canvas = Canvas(root, width=1920, height=1080, bg="#263D42")
    canvas.pack()

    frame = Frame(root, bg="white")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    Label(frame, text=" ").pack()
    Label(frame, text="Пожалуйста, введите название презентации:").pack()
    search = StringVar()
    entryInput = Entry(frame, textvariable=search,
    width="35", bg="cyan", fg="#2e2e2e")
    entryInput.pack()
    Label(frame, text=" ").pack()
    global myButton
    myButton = Button(frame, text="Получить результаты", width="40",
    height="2", bg="lightblue", fg="#fa8857", command=fun1)
    myButton.pack()
    global textFrame
    textFrame = Frame(frame, bg="#fa8857")
    textFrame.place(relwidth=0.8, relheight=0.6, relx=0.1, rely=0.3)

    root.mainloop()


def indexScreen():
    global main
    main = Tk()
    main.title('Starting - Choose language.')
    myCanvas = Canvas(main, width="1920", height="1080", bg="violet")
    myCanvas.pack()

    mainFrame = Frame(main, bg="lightgreen")
    mainFrame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    titlelabel = Label(mainFrame, text="Choose language wiki!", bg="lightgreen", font='times 50 italic', pady=50)
    titlelabel.pack()

    my_img = ImageTk.PhotoImage(Image.open("kawiki.png"))
    my_img1 = ImageTk.PhotoImage(Image.open("enwiki.png"))
    my_img2 = ImageTk.PhotoImage(Image.open("ruwiki.png"))

    ka = Button(mainFrame, image=my_img, fg="black", bg="#f77777", command= mainscreen_KA,borderwidth=2, relief="flat")
    ka.place(relx=0.2, rely=0.5)
    en = Button(mainFrame, image=my_img1, fg ="black", bg ="#90c4f5",command = mainscreen_EN,borderwidth=2, relief="flat")
    en.place(relx=0.42, rely=0.5)
    en = Button(mainFrame, image=my_img2, fg ="black", bg ="#967791",command = mainscreen_RU,borderwidth=2, relief="flat")
    en.place(relx=0.64, rely=0.5)

    main.mainloop()



indexScreen()
get_text_pres()
create_filecontent()

print("Code completeted")
