from tkinter import *  # Importing all tkinter classes and methods
import random
import ttkthemes
from tkinter import ttk # heps to appy themes on your buttons
from time import sleep
import threading

##########Functionality Part
totaltime=60
time=0
wrongwords=0
elapsedtimeinminutes=0

def start_timer():
    startButton.config(state=DISABLED)
    global time
    textarea.config(state=NORMAL)
    textarea.focus()

    for time in range(1,61):
        elapsed_timer_label.config(text=time)
        remainingtime=totaltime-time
        remaining_timer_label.config(text=remainingtime)
        sleep(1)
        root.update()


    textarea.config(state=DISABLED)
    resetButton.config(state=NORMAL)

def count():
    global wrongwords
    while time != totaltime:
        sleep(1)
        entered_paragraph=textarea.get(1.0,END).split()
        totalwords=len(entered_paragraph)

        totalwords_count_label.config(text=totalwords)

    para_word_list=label_paragraph['text'].split()

    for pair in list(zip(para_word_list,entered_paragraph)):
        if pair[0] != pair[1]:
            wrongwords += 1

    wrongwords_count_label.config(text=wrongwords)

    elapsedtimeinminutes=time/60
    wpm=(totalwords-wrongwords)/elapsedtimeinminutes
    wpm_count_label.config(text=wpm)
    gross_wpm=totalwords/elapsedtimeinminutes
    accuracy=wpm/gross_wpm*100
    accuracy_percent_label.config(text=str(int(accuracy))+'%')

def start():
    t1 = threading.Thread(target=start_timer)
    t1.start()

    t2 = threading.Thread(target=count)
    t2.start()

def reset():
    global time,elapsedtimeinminutes
    time=0
    elapsedtimeinminutes=0
    startButton.config(state=NORMAL)
    resetButton.config(state=DISABLED)
    textarea.config(state=NORMAL)
    textarea.delete(1.0,END)
    textarea.config(state=DISABLED)

    elapsed_timer_label.config(text='0')
    remaining_timer_label.config(text='0')
    wpm_count_label.config(text='0')
    accuracy_percent_label.config(text='0')
    totalwords_count_label.config(text='0')
    wrongwords_count_label.config(text='0')



##########GUI Part

root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')
root.geometry('940x800+200+10')
root.resizable(0, 0)
root.overrideredirect(True)


mainframe = Frame(root, bd=4,)
mainframe.grid()

titleframe = Frame(mainframe, bg='red')
titleframe.grid()

titleLabel = Label(titleframe, text='Master Typing', font=('Algerian', 28, 'bold'),
                   bg='silver', fg='lightyellow', width=38, bd=10)
titleLabel.grid(pady=5)

paragraph_frame = Frame(mainframe)
paragraph_frame.grid(row=1, column=0)

paragraph_list = [
    "We live in an age of science. Science has made us civilized. Every progress in human civilization is the gift of science. Science has solved our problem of getting basic needs. It has helped us to grow more food. It has given us comfortable shelter. Science has given us clothes. Science has made the world small. The train, aircraft, car, and other speedy transport take us from one place to another within a short time. Science has brought about a revolution in the field of communication. We can talk to a friend living in a distant country. The field of entertainment is filled with cinema, TV, radio and video. The gifts of science like medicine and surgery are considered to be untold blessings. Science can diagnose hidden diseases. It has been able to prevent most fatal diseases. Science has done something beyond our imagination in the field of space research.",

    "Science is a great boon to human civilization. All signs of progress in civilization have been made possible by science. Science has made our life easy and comfortable. It has given us electric fans and lights. Fans cool us; lights remove darkness. Lifts and washing machines save our labour. Cars, trains, buses and aircraft have made our travel speedy and comfortable. The computer has taken the excess load off our brains. Science has given us life-saving medicine. Surgery can do something miraculous. Thus, science is a blessing to us. But it is a curse at the same time. Science has given us speed but has taken away our emotions. It has made us like machines. The introduction of the mobile phone has destroyed the art of letter writing. Science has made war more dreadful by inventing sophisticated weapons. Peace has become scarce. But who is responsible for making science a curse? Certainly, it is the evil intention of a few scientists and malignant politicians.",

    "My favourite subject is History. The range of History is very wide. There is a history for every subject. Any research on any subject is helped by earlier research. History keeps a record of earlier research. It is not merely a chronicle of the dead past. The past is still living in History. It breaks the limits of time. The range of History is extended from the remote past to the age we live in. It is interesting to everybody. Who does not like to know the history of their village, town or country? Who does not like to know the history of their ancestors or the ancient people of their country? The study of History broadens our outlook. It develops patriotism. It teaches one to love one’s country. History teaches lessons because it repeats itself. History is thus a great teacher. History teaches how to take our present steps flawlessly.",

    "The newspaper is one of the most powerful media. The first newspaper in India, India Gazette, was published in 1774. A newspaper is a sort of contemporary history. It collects news, publishes it and circulates it. The newspaper is a record of current events, both national and international. All kinds of news—political, economic, commercial, sports, etc.—are published. The newspaper is of great importance in modern life. It is a strong medium to form public opinion. Every section of society finds it necessary to go through a newspaper. It has educational value. Politicians and thinkers spread their ideas through newspapers. The newspaper tells us about the latest discoveries and inventions of the world. It is one of the easiest ways of increasing general knowledge. But the newspaper has a bad side too. It can mislead people with false or fabricated news. The newspaper should always provide impartial and correct information.",

    "Unity means living and working together. At first, man was alone in this world. But he found it impossible to live alone. Then the idea of unity came to him because unity is strength. Unity gives us power. United we stand, divided we fall. Unity is needed in a family. A family breaks down for want of unity among the members. A united joint family is a source of happiness. Unity is needed for the welfare of society. A man alone in society is weak. Even a strong man cannot protect himself. United efforts give us social security. Unity is very important in our national life. History gives us many examples of the value of unity. We lost our independence for lack of unity. We had to divide our country because we were not united. Even today, we are not fully aware of the importance of national unity.",

    "Friendship is a sincere bond between two people. Man is a social animal and cannot live alone. So, he needs companions. But not every companion is a friend. A good and true friend must possess some qualities. It is said, ‘A friend in need is a friend indeed.’ A true friend helps us not only in difficult times but also corrects our faults and guides us on the right path. He always stands by us in hardship. A person without friends is an object of pity. But true friendship is rare. An open enemy is better than a false friend. A true friend is a blessing, while a false one is a curse. A false friend can lead us astray. So, we must be careful in choosing our friends."
]

# Shuffle the paragraph list to display a random one
random.shuffle(paragraph_list)

# Create and place the paragraph label
label_paragraph = Label(paragraph_frame, text=paragraph_list[0], wraplength=912, font=('Arial', 14), justify=LEFT)
label_paragraph.grid(row=0, column=0, padx=10, pady=10)

textarea_frame=Frame(mainframe)
textarea_frame.grid(row=2, column=0)

textarea=Text(textarea_frame,font=('Areal',12,'bold'),width=100,height=7,bd=4,relief=GROOVE,wrap='word'
              ,state=DISABLED)
textarea.grid()

frame_output=Frame(mainframe)
frame_output.grid(row=3, column=0)

elapsed_time_label=Label(frame_output,text='Elapsed Time',font=('Tahoma',12,'bold'),fg='red')
elapsed_time_label.grid(row=0,column=0,padx=5)

elapsed_timer_label=Label(frame_output,text='0',font=('Tahoma',12,'bold'),)
elapsed_timer_label.grid(row=0,column=1,padx=5)

remaining_time_label=Label(frame_output,text='Remaining Time',font=('Tahoma',12,'bold'),fg='red')
remaining_time_label.grid(row=0,column=2,padx=5)

remaining_timer_label=Label(frame_output,text='60',font=('Tahoma',12,'bold'))
remaining_timer_label.grid(row=0,column=3,padx=5)

wpm_time_label=Label(frame_output,text='WPM',font=('Tahoma',12,'bold'),fg='red')
wpm_time_label.grid(row=0,column=4,padx=5)

wpm_count_label=Label(frame_output,text='0',font=('Tahoma',12,'bold'),)
wpm_count_label.grid(row=0,column=5,padx=5)

totalwords_label=Label(frame_output,text='Total Words',font=('Tahoma',12,'bold'),fg='red')
totalwords_label.grid(row=0,column=6,padx=5)

totalwords_count_label=Label(frame_output,text='0',font=('Tahoma',12,'bold'))
totalwords_count_label.grid(row=0,column=7,padx=5)

wrongwords_label=Label(frame_output,text='Wrong Words',font=('Tahoma',12,'bold'),fg='red')
wrongwords_label.grid(row=0,column=8,padx=5)

wrongwords_count_label=Label(frame_output,text='0',font=('Tahoma',12,'bold'))
wrongwords_count_label.grid(row=0,column=9,padx=5)

accuracy_label=Label(frame_output,text='Accuracy',font=('Tahoma',12,'bold'),fg='red')
accuracy_label.grid(row=0,column=10,padx=5)

accuracy_percent_label=Label(frame_output,text='0',font=('Tahoma',12,'bold'))
accuracy_percent_label.grid(row=0,column=11,padx=5)

#####BUTTON
button_Frame=Frame(mainframe)
button_Frame.grid(row=4,column=0)

startButton=ttk.Button(button_Frame,text='Start',command=start)
startButton.grid(row=0,column=0,padx=10)

resetButton=ttk.Button(button_Frame,text='reset',state=DISABLED,command=reset)
resetButton.grid(row=0,column=1,padx=10)

exitButton=ttk.Button(button_Frame,text='Exit',command=root.destroy)
exitButton.grid(row=0,column=2,padx=10)

keyboard_frame=Frame(mainframe)
keyboard_frame.grid(row=5, column=0)

frame1to0=Frame(keyboard_frame)
frame1to0.grid(row=0,column=0,pady=3)

label1=Label(frame1to0,text='1',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label2=Label(frame1to0,text='2',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label3=Label(frame1to0,text='3',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label4=Label(frame1to0,text='4',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label5=Label(frame1to0,text='5',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label6=Label(frame1to0,text='6',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label7=Label(frame1to0,text='7',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label8=Label(frame1to0,text='8',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label9=Label(frame1to0,text='9',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label0=Label(frame1to0,text='0',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)

label1.grid(row=0,column=0,padx=5,pady=10)
label2.grid(row=0,column=1,padx=5,pady=10)
label3.grid(row=0,column=2,padx=5,pady=10)
label4.grid(row=0,column=3,padx=5,pady=10)
label5.grid(row=0,column=4,padx=5,pady=10)
label6.grid(row=0,column=5,padx=5,pady=10)
label7.grid(row=0,column=6,padx=5,pady=10)
label8.grid(row=0,column=7,padx=5,pady=10)
label9.grid(row=0,column=8,padx=5,pady=10)
label0.grid(row=0,column=9,padx=5,pady=10)

frameqtop=Frame(keyboard_frame)
frameqtop.grid(row=1,column=0,pady=3)

labelQ=Label(frameqtop,text='Q',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelW=Label(frameqtop,text='W',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelE=Label(frameqtop,text='E',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelR=Label(frameqtop,text='R',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelT=Label(frameqtop,text='T',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelY=Label(frameqtop,text='Y',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelU=Label(frameqtop,text='U',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelI=Label(frameqtop,text='I',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelO=Label(frameqtop,text='O',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelP=Label(frameqtop,text='P',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)

labelQ.grid(row=0,column=0,padx=5)
labelW.grid(row=0,column=1,padx=5)
labelE.grid(row=0,column=2,padx=5)
labelR.grid(row=0,column=3,padx=5)
labelT.grid(row=0,column=4,padx=5)
labelY.grid(row=0,column=5,padx=5)
labelU.grid(row=0,column=6,padx=5)
labelI.grid(row=0,column=7,padx=5)
labelO.grid(row=0,column=8,padx=5)
labelP.grid(row=0,column=9,padx=5)

frameatol=Frame(keyboard_frame)
frameatol.grid(row=2,column=0,pady=3)

labelA=Label(frameatol,text='A',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelS=Label(frameatol,text='S',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelD=Label(frameatol,text='D',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelF=Label(frameatol,text='F',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelG=Label(frameatol,text='G',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelH=Label(frameatol,text='H',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelJ=Label(frameatol,text='J',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelK=Label(frameatol,text='K',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelL=Label(frameatol,text='L',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)

labelA.grid(row=0,column=0,padx=5)
labelS.grid(row=0,column=1,padx=5)
labelD.grid(row=0,column=2,padx=5)
labelF.grid(row=0,column=3,padx=5)
labelG.grid(row=0,column=4,padx=5)
labelH.grid(row=0,column=5,padx=5)
labelJ.grid(row=0,column=6,padx=5)
labelK.grid(row=0,column=7,padx=5)
labelL.grid(row=0,column=8,padx=5)

frameztom=Frame(keyboard_frame)
frameztom.grid(row=3,column=0,pady=3)

labelZ=Label(frameztom,text='Z',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelX=Label(frameztom,text='X',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelC=Label(frameztom,text='C',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelV=Label(frameztom,text='V',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelB=Label(frameztom,text='B',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelN=Label(frameztom,text='N',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelM=Label(frameztom,text='M',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)

labelZ.grid(row=0,column=0,padx=5)
labelX.grid(row=0,column=1,padx=5)
labelC.grid(row=0,column=2,padx=5)
labelV.grid(row=0,column=3,padx=5)
labelB.grid(row=0,column=4,padx=5)
labelN.grid(row=0,column=5,padx=5)
labelM.grid(row=0,column=6,padx=5)

spaceframe=Frame(keyboard_frame)
spaceframe.grid(row=4, column=0, pady=3)

labelSpace=Label(spaceframe,bg='black',fg='white',font=('arial',10,'bold'),width=40,height=2,bd=10,relief=GROOVE)
labelSpace.grid(row=0,column=0)

def changeBG(widget):
    widget.configure(background='blue')
    widget.after(100,lambda: widget.config(bg='black'))

label_numbers=[label1,label2,label3,label4,label5,label6,label7,label8,label9,label0]

label_alphabets=[labelA,labelB,labelC,labelD,labelE,labelF,labelG,labelH,labelI,labelJ,labelK,labelL,labelM,labelN,
                 labelO,labelP,labelQ,labelR,labelS,labelT,labelU,labelV,labelW,labelX,labelY,labelZ]

space_label=[labelSpace]

binding_number=['1','2','3','4','5','6','7','8','9','0']

binding_small_alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w',
                   'x','y','z']
binding_capital_alphabets=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V'
                    ,'W','X','Y','Z']

for numbers in range(len(binding_number)):
    root.bind(binding_number[numbers],lambda event,label=label_numbers[numbers]: changeBG(label))

for capital_alphabets in range(len(binding_capital_alphabets)):
    root.bind(binding_capital_alphabets[capital_alphabets],lambda event,label=label_alphabets[capital_alphabets]: changeBG(label))

for small_alphabets in range(len(binding_small_alphabets)):
    root.bind(binding_small_alphabets[small_alphabets],lambda event,label=label_alphabets[small_alphabets]: changeBG(label))

root.bind('<space>',lambda event: changeBG(space_label[0]))






root.mainloop()

