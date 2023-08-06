import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import time
import os
from PIL import ImageSequence
import webbrowser

class ChatBot:
    def __init__(self, root):
        self.root = root
        self.root.title("School Chatbot")
        self.root.geometry("760x615")
        self.loading_frame = None
        self.load_loading_screen()

        self.root.bind('<Return>', self.enter_func)

        main_frame = Frame(self.root, bd=4, bg='light blue', width=610)
        main_frame.pack()


        img_chat = Image.open('chatbot.jpg')
        img_chat = img_chat.resize((200, 80))
        self.photoimg = ImageTk.PhotoImage(img_chat)

        Title_label = Label(main_frame, bd=4, relief=RAISED, anchor='nw', width=730, compound=LEFT, image=self.photoimg,
                            text='SCHOOL QUERIES CHATBOT', font=('Comic Sans MS', 20, 'bold'), fg='blue',
                            bg='white')
        Title_label.pack(side=TOP)

        self.scroll_y = ttk.Scrollbar(main_frame, orient=VERTICAL)
        self.scroll_y.pack(side=RIGHT, fill=Y)

        self.text = Text(main_frame, width=80, height=25, bd=3, relief=RAISED, yscrollcommand=self.scroll_y.set)
        self.text.pack()

        btn_frame = Frame(self.root, bd=4, bg='white', width=730)
        btn_frame.pack()

        label = Label(btn_frame, text="Ask Something", font=('arial', 14, 'bold'), fg='Black', bg='white')
        label.grid(row=0, column=0, padx=5, sticky=W)

        self.entry = StringVar()
        
        self.entry1 = ttk.Entry(btn_frame, textvariable=self.entry, width=30, font=('arial', 17, 'bold'))
        self.entry1.grid(row=0, column=1, padx=5, sticky=W)

        self.send = Button(btn_frame, text="Send", command=self.send_message, font=('arial', 16, 'bold'), width=6,
                           bg='light grey')
        self.send.grid(row=0, column=2, padx=5, sticky=W)

        self.clear = Button(btn_frame, text="Clear", font=('arial', 16, 'bold'), width=6, bg='grey', fg='white',
                            command=self.clear)
        self.clear.grid(row=1, column=0, padx=5, sticky=W)

        self.msg = ''
        self.label1 = Label(btn_frame, text=self.msg, font=('arial', 14, 'bold'), fg='Black', bg='white')
        self.label1.grid(row=1, column=1, padx=5, sticky=W)

 
    def load_loading_screen(self):
        self.loading_frame = Frame(self.root, bd=4, bg='white', width=760, height=615)
        self.loading_frame.pack()

        image = Image.open("chatboot.gif")
        self.loading_icon_img = ImageTk.PhotoImage(image)

        canvas = Canvas(self.loading_frame, width=760, height=615, bg='black', highlightthickness=0)
        canvas.pack()

        x = (760 - image.width) // 2
        y = (615 - image.height) // 2

        frames = [ImageTk.PhotoImage(frame.copy()) for frame in ImageSequence.Iterator(image)]
        self.loading_frames = frames
        self.loading_label = Label(canvas, image=self.loading_icon_img, bg='black')
        self.loading_label.place(x=x, y=y, anchor='nw')

        label_loading = Label(self.loading_frame, text="Welcome...", font=("Arial", 20, "bold"), fg='white', bg='black')
        label_loading.place(relx=0.5, rely=0.9, anchor='center')
        self.animate_loading_icon(0)

        # Adjust the loading time based on the total duration of the GIF animation (in milliseconds)
        total_duration = sum(image.info.get('duration', 100) for frame in ImageSequence.Iterator(image))
        self.root.after(total_duration, self.load_main_app)

    def animate_loading_icon(self, index):
        self.loading_label.configure(image=self.loading_frames[index])
        index = (index + 1) % len(self.loading_frames)
        self.loading_frame.after(10, self.animate_loading_icon, index)
    def load_main_app(self):
        self.loading_frame.destroy()        
        main_frame = Frame(self.root, bd=4, bg='light blue', width=610)
        main_frame.pack()

    def open_link(self):
        webbrowser.open("https://www.ipwspv.com/")





    def get_bot_response(self):
        if "hello" in self.user_input.lower() or "hi" in self.user_input.lower():
            return("Hello! How can I help you?")

        elif "timetable" in self.user_input.lower() or "schedule" in self.user_input.lower():
            return("The timetable will be provided by your class teacher. ")
        
        elif "facilities" in self.user_input.lower() or "activities" in self.user_input.lower():
            return("There are many facilities in our school such as Computer Lab, Science Lab, Library, Auditorium, Playground, Canteen and more.  ")
        
        elif "principal" in self.user_input.lower():
            return("The principal is the head of the school.")

        elif "library" in self.user_input.lower():
            return("Our school has a big library which has all sorts of books for the students to read. ")

        elif "canteen" in self.user_input.lower() or "cafeteria" in self.user_input.lower():
            return("The canteen provides with a variety of food which is open to all students above 6th class. ")

        elif "science lab" in self.user_input.lower():
            return("Our school has a Physics Lab,Chemistry Lab and Biology Lab.")
        
        elif "Computer Lab" in self.user_input.lower():
            return("In our school there are two computer labs:a Junior Computer Lab and a Senior Computer Lab.")
        
        elif "transport" in self.user_input.lower() or "bus facility" in self.user_input.lower():
            return("Our school provides a bus facility. It has a gps installed so that the parents have a track on their kids. ")
                   
        elif "homework" in self.user_input.lower() or "assignment" in self.user_input.lower():
            return("You can find your homework on the school website.")
        
        
        elif "curriculum" in self.user_input.lower() or "syllabus" in self.user_input.lower():
            return("Our school follows the CBSE Board curriculum.")
        
        elif "co-curricular activities" in self.user_input.lower() or "extra curricular activities" in self.user_input.lower():
            return("Our school offers various extracurricular activities, including sports, music, dance, art, and debate club.")
        
        elif "scholarship" in self.user_input.lower():
            return("Yes, our school provides scholarship opportunities for meritorious students. You can check the school's website for more details")

        elif "school hours" in self.user_input.lower():
            return("The school starts at 8:00 AM and ends at 3:00 PM. Please note that the timings may vary for different grade levels.")
    

    
        elif "third language" in self.user_input.lower():
            return("We offer third language courses, including French and Sanskrit as part of our language program.")
        
        elif "clubs" in self.user_input.lower():
            return("We have several student clubs, such as the Eco Club, Art Club, Computer Club where students can engage in various interests. \n\n To know more about clubs \n Type:viewclub")
        elif "viewclub" in self.user_input.lower():
            webbrowser.open("https://www.ipwspv.com/servlet/General?id=20&cid=4&title=Clubs-Hands%20on%20Experience")
        elif "swimming pool" in self.user_input.lower():
            return("We have a swimming pool which is used for swimming lessons and sports activities.")
      
        elif "counselling" in self.user_input.lower() or "guidance" in self.user_input.lower() or "counseller" in self.user_input.lower():
            return("Indraprastha is aware of the stress which the students undergo. Keeping in sync with the problems faced by them in this fast changing world, the school has a guidance and counselling cell.\n  The counsellor helps them cope with their problems and facilitates balanced growth.\nThe developmental needs of adolescents are anticipated and corrective steps are taken to help them experience a smooth transition from one stage to another. In order to ensure a healthy and all round development, the following activities are conducted at regular intervals:- \n\n • Parental interviews to ascertain the exact nature of the students' problems. \n\n • Individual and group counselling to guide the students to be self-reliant. \n\n • Follow-up of children with special needs and providing them the required facilities based on CBSE  guidelines. \n\n  • Orientation workshops and seminars for the teachers, parents and students")

        elif "curriculum" in self.user_input.lower() or "syllabus" in self.user_input.lower():
            return("Our school follows the CBSE Board curriculum.")
        
        elif "timings" in self.user_input.lower():
            return("Visiting Hours:\n School Office    : 9.00 a.m  to 3.30 p.m \n Principal    : 9.00 a.m to 10.00 a.m (by appointment only) \n : 2.30 p.m to 3.30 p.m  (by appointment only) \n School Timings: \n School will follow a five days working schedule for all classes. However, school will work on certain Saturdays, as and when required. The details for the same will be shared through the almanac.")
                
        elif "medical" in self.user_input.lower() or "infirmary" in self.user_input.lower():
            return("The well-equipped Infirmary at Indraprastha World School provides immediate medical attention First Aid to the students. The school has a full time qualified doctor and an experienced nurse to treat minor ailments and injuries. The medical staff periodically carries out medical checkup of all students and maintains records/findings for future references.  For emergency, students requiring medical attention are referred to a nearby hospital or clinic. Parents are informed in case the child is advised special treatment.")
        
        elif "house system" in self.user_input.lower() or "housesystem" in self.user_input.lower():
            return("The House System of the school promotes the feeling of coordination, healthy competitive spirit, leadership and self-restraint among the students.\n\n The students from classes I to XII are divided into four houses, namely Charity, Honesty, Purity and Unity.\n\n  Each house comprises a House Warden along with the team of Captain, Vice Captain and Prefects who are an epitome of personal integrity, teamwork and cooperation.Inter-house competitions are conducted on regular basis under different categories such as drawing, craft, quiz, debate, extempore, poetry recitation, elocution and dance, to foster the spirit of confidence and to hone the talent in young children.Students display articles and pictures on a specific theme given for the decoration of the house boards.\n\n The boards are assessed and graded every month by competent authorities. Points are awarded to houses for their performance to keep up their competitive spirit.\n\n type: view housesystem \n To know more about house system")      
        elif "viewhousesystem" in self.user_input.lower():
            webbrowser.open("https://www.ipwspv.com/servlet/General?id=10&cid=2&title=Other%20Information")

        elif "interhouse" in self.user_input.lower():
            return("Indraprastha World School believes that every child is a reservoir of courage, energy and talent which is recognized and nurtured through multifarious inter house activities and competitions. These activities aim at giving right exposure and opportunity for self expression both on stage and play field. To keep pace with the changing times, the co-curricular activities are given equal importance as the academics as they aim at bringing out the best in each child. These activities not only broaden the horizon, but also give them an exposure that is par excellence .The zeal with which the students participate in these  activities and competitions   not only exhibits their spirit of competitiveness, camaraderie, group dynamics but also strengthen their confidence.\n\nFor more information go to: \n https://www.ipwspv.com/servlet/General?id=21&cid=4&title=Interhouse%20Activities")
        elif "facilities" in self.user_input.lower():
            return("There are many facilities in our school such as Computer Lab, Science Lab, Library, Auditorium, Playground, Canteen and more.")
        elif "website" in self.user_input.lower():
            
            self.open_link()
            return("Loading School Website...")
        elif "sports" in self.user_input.lower():
            return("Sports hold an important and prominent place in the school curriculum and immense stress is laid on regular games and sports being played by the students to keep them physically fit and mentally alert.\n\n To learn more about Sports and Fitness\n type view sport")
           
        elif "view" and "sport" in self.user_input.lower():
            webbrowser.open("https://www.ipwspv.com/servlet/General?id=25&cid=4&title=Health%20and%20Physical%20Education")
            
        elif "bye" in self.user_input.lower():
            root.quit()
            return("Bye, Have a good day.")




                                                                                     


        
        

        else:
            return ("I apologise; I don't have an answer to that")

    def enter_func(self, event):
        self.send_message()
        self.entry.set('')

    def clear(self):
        self.text.config(state=tk.NORMAL)
        self.text.delete('1.0', tk.END)
        self.text.config(state=tk.DISABLED)
        self.entry.set('')

    def send_message(self):
        self.user_input = self.entry.get()
        if self.user_input.strip() != "":
            self.text.config(state=tk.NORMAL)
            self.text.insert(tk.END, "You: " + self.user_input + "\n")
            self.text.config(state=tk.DISABLED)

            response = self.get_bot_response()
            self.text.config(state=tk.NORMAL)
            self.text.insert(tk.END, "Chatbot: " + response + "\n")
            self.text.config(state=tk.DISABLED)


if __name__ == '__main__':
    root = tk.Tk()
    obj = ChatBot(root)
    root.mainloop()
