#create lists
valid_credits = [0,20,40,60,80,100,120] 
list1=[]
mlist=[]

#function for credits append to the list
def append_list():
    list1=[]
    list1.append(progress)
    list1.append(passs)
    list1.append(defer)
    list1.append(fail)
    mlist.append(list1) 
    
#function for create and print into the text file
def text_file():
    filename="Progression history.txt"
    with open(filename, "a") as file:
        file.write(f"{progress} - {passs}, {defer}, {fail}")
        file.write(f"\n")
        file.close()

#function for print values in the list(mlist)
def print_last():
    for item in mlist:
        print(item[0],"-",item[1],",",item[2],",",item[3])
    
#function for create variable and count how many times output progression outcomes
def graph_count():
    global progress_count
    progress_count=0
    global trailer_count
    trailer_count=0
    global retriever_count
    retriever_count=0
    global exclude_count
    exclude_count=0
    global all_g_count
    all_g_count=0
    for i in mlist:
        for j in i:
            if j=='Progress':
                progress_count=progress_count+1 #count how many progress credits
            elif j=='Progress(Module Trailer)':
                trailer_count=trailer_count+1 #count how many trailer credits  
            elif j=='Module retriever': #
                retriever_count=retriever_count+1 #count how many module retriever credits
            elif j=='Exclude':
                exclude_count=exclude_count+1 #count how many exclude credits
    
    all_g_count=progress_count+trailer_count+retriever_count+exclude_count

from graphics import *   #import the graphics.py module
def graphs():
    
#OPEN THE WINDOW
    win = GraphWin("Histogram", 664, 650)#open a window object called "win" with size and title 
    win.setBackground("Mint Cream")# Set the background colour of the window

    bar_hight_progress_count=(progress_count/all_g_count)*500
    y1=0
    y1=500-bar_hight_progress_count

    bar_hight_trailer_count=(trailer_count/all_g_count)*500
    y2=0
    y2=500-bar_hight_trailer_count

    bar_hight_retriever_count=(retriever_count/all_g_count)*500
    y3=0
    y3=500-bar_hight_retriever_count

    bar_hight_exclude_count=(exclude_count/all_g_count)*500
    y4=0
    y4=500-bar_hight_exclude_count

    my_heading = Text(Point(120, 20), 'Histogram Result')
    my_heading.setSize(15)
    my_heading.draw(win)

    bar1=Rectangle(Point(100,70+y1),Point(210,570))
    bar1.setFill("lightgreen")
    bar1.draw(win)
    tot_progress = Text(Point(150, 70+(y1-10)), f"{progress_count}")
    tot_progress.draw(win)
    bar_name1 = Text(Point(153, 583), 'Progress')
    bar_name1.draw(win)

    bar2=Rectangle(Point(218,70+y2), Point(328,570))
    bar2.setFill("bisque")
    bar2.draw(win)
    tot_trailer = Text(Point(272, 70+(y2-10)), f"{trailer_count}")
    tot_trailer.draw(win)
    bar_name2 = Text(Point(274, 583), 'Trailer')
    bar_name2.draw(win)
    

    bar3=Rectangle(Point(336,70+y3), Point(446,570))
    bar3.setFill("linen")
    bar3.draw(win)
    tot_retriever = Text(Point(390, 70+(y3-10)), f"{retriever_count}")
    tot_retriever.draw(win)
    bar_name3 = Text(Point(390, 583), 'Retriever')
    bar_name3.draw(win)

    bar4=Rectangle(Point(454,70+y4), Point(564,570))
    bar4.setFill("lightpink")
    bar4.draw(win)
    tot_exclude = Text(Point(510, 70+(y4-10)), f"{exclude_count}")
    tot_exclude.draw(win)
    bar_name4= Text(Point(510, 583), 'Excluded')
    bar_name4.draw(win)

    line=Line(Point(50,570), Point(614,570))
    line.setWidth(2)
    line.draw(win)

    total_outcomes = Text(Point(110, 624), f"{all_g_count}  Outcomes in total")
    total_outcomes.setSize(15)
    total_outcomes.draw(win)
    try:
        win.getMouse()
        win.close()
    except GraphicsError:
        print("\n Graphic Window Closed")


def reapet():
    global multi
    multi=str(input("\nWould like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results:"))
    multi=multi.lower()
    if multi=='y':
        print('\n')
        get_inputs()
    elif multi=='q':
        print("\n")
        print_last()
        graph_count()
        graphs()
        raise SystemExit #Stop the program
        
    else:
       reapet()

#function for check 'Progress' or 'Prograss(Module Trailer)' or 'Module retriever' or 'Exclude'
def conditions():
    global progress
    #check 'progress'
    if(passs==120 and defer==0 and fail==0):
                        progress="Progress"
                        print(progress)
                        if s_or_s=="2":
                            append_list()
                            text_file()
                        
    #check 'Prograss(Module Trailer)'            
    elif(passs==100 and defer==20 and fail==0)or(passs==100 and defer==0 and fail==20):
                        progress="Progress(Module Trailer)"
                        print(progress)
                        if s_or_s=="2":
                            append_list()
                            text_file()
                        
    #use 6 if conditions for check 'Module retriever' beacause line is getting lagger
    #check 'Module retriever'
    elif(passs==80 and defer==40 and fail==0)or(passs==80 and defer==20 and fail==20)or(passs==80 and defer==0 and fail==40):
                        progress="Module retriever"
                        print(progress)
                        if s_or_s=="2":
                            append_list()
                            text_file()
             
    #check 'Module retriever'                   
    elif(passs==60 and defer==60 and fail==0)or(passs==60 and defer==40 and fail==20)or(passs==60 and defer==20 and fail==40):
                        progress="Module retriever"
                        print(progress)
                        if s_or_s=="2":
                            append_list()
                            text_file()
             
    #check 'Module retriever'                    
    elif(passs==60 and defer==0 and fail==60)or(passs==40 and defer==80 and fail==0)or(passs==40 and defer==60 and fail==20):
                        progress="Module retriever"
                        print(progress)
                        if s_or_s=="2":
                            append_list()
                            text_file()
                
    #check 'Module retriever'                    
    elif(passs==40 and defer==40 and fail==40)or(passs==40 and defer==20 and fail==60)or(passs==20 and defer==100 and fail==0):
                        progress="Module retriever"
                        print(progress)
                        if s_or_s=="2":
                            append_list()
                            text_file()
                       
    #check 'Module retriever'                    
    elif(passs==20 and defer==80 and fail==20)or(passs==20 and defer==60 and fail==40)or(passs==20 and defer==40 and fail==60):
                        progress="Module retriever"
                        print(progress)
                        if s_or_s=="2":
                            append_list()
                            text_file()
                  
    #check 'Module retriever'                    
    elif(passs==0 and defer==120 and fail==0)or(passs==0 and defer==100 and fail==20)or(passs==0 and defer==80 and fail==40)or(passs==0 and defer==60 and fail==60):
                        progress="Module retriever"
                        print(progress)
                        append_list()
                        text_file()
            
    #use 2 if conditions for check 'Exclude' beacause line is getting lagger
    #check 'Exclude'
    elif(passs==40 and defer==0 and fail==80)or(passs==20 and defer==20 and fail==80)or(passs==20 and defer==0 and fail==100):
                        progress="Exclude"
                        print(progress)
                        if s_or_s=="2":
                            append_list()
                            text_file()
                   
    #check 'Exclude'                    
    elif(passs==0 and defer==40 and fail==80)or(passs==0 and defer==20 and fail==100)or(passs==0 and defer==0 and fail==120):
                        progress="Exclude"
                        print(progress)
                        if s_or_s=="2":
                            append_list()
                            text_file()
                        
    if s_or_s=="1":
        print("\nThank You!!!")
        raise SystemExit #Stop the program
    if s_or_s=="2":                    
        reapet()
    


def get_inputs():
    try:
        global passs
        passs=input("Please Enter Your Credits at Pass:")
        passs=int(passs)

        if not passs in valid_credits:
            print("Out of Range")

        else:
            global defer
            defer=input("Please Enter Your Credit at Defer:")
            defer=int(defer)
            if not defer in valid_credits:
                    print("Out of Range")
            else:
                global fail
                fail=input("Please Enter Your Credit at Fail:")
                fail=int(fail)

                if not fail in valid_credits:
                    print("Out of Range")
                else:
                    total=passs+defer+fail
                    if total!=120:
                        print("Total Incorrect")
    except ValueError:
        print("Integer Required")
    conditions()

   
def student_or_staff():# function for ask 'student' or 'staff'
    global s_or_s
    while True:
        print("Student Access:1 | Staff Access:2")
        s_or_s=input("Enter your access code:")
        if  s_or_s=="1" or s_or_s=="2" :
            print("")
            get_inputs()
        else:
            print("\nYou should Enter '1' or '2'")
            continue

student_or_staff()
            
        
        
        


    
    
                    

                    
                    
                        
                    
                    
                    
                       
                                
                    
    


