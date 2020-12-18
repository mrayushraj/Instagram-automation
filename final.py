import random
import time
import tkinter
from tkinter import Label, Button, Entry, messagebox
from time import sleep
from selenium import webdriver, common
from selenium.webdriver.common.keys import Keys
from threading import *


def login(username, passw):
    fn()
    root.update()
    bot.get('https://instagram.com')
    root.update()
    time.sleep(5)
    email = bot.find_element_by_name('username')
    password = bot.find_element_by_name('password')
    root.update()
    email.clear()
    password.clear()
    email.send_keys(username)
    password.send_keys(passw)
    root.update()
    password.send_keys(Keys.RETURN)
    time.sleep(7)
    try:
        root.update()
        bot.find_element_by_xpath("//*[@id=\"slfErrorAlert\"]")
        if not messagebox.askyesno("Login Error", "Wrong Username or Password \nLogin Again?"):
            bot.close()
            root.destroy()

    except:
        click_button = bot.find_element_by_css_selector('.sqdOP.yWX7d.y3zKF')
        click_button.click()
        time.sleep(2)
        click_button2 = bot.find_element_by_css_selector('.aOOlW.HoLwm')
        click_button2.click()
        time.sleep(2)

        if messagebox.showinfo("Logged In", "Login Successful! Proceed Further?"):
            login_success()


def login_success():
    emails.destroy()
    entry1.destroy()
    entry2.destroy()
    passwords.destroy()
    b1.destroy()
    b2.destroy()
    newFrame()


def feedliker():
    def starting():
        try:
            temp = 1
            cont = 1
            while temp <= int(num.get()):
                random_time = random.randint(0, 1)

                a = '/html/body/div[1]/section/main/section/div/div[2]/div/article[{}]/div[3]/section[1]/span[1]/button'.format(
                    cont)
                sleep(random_time)
                like_button = bot.find_element_by_xpath(a)
                sleep(random_time)
                bot.execute_script("arguments[0].scrollIntoView;", a)
                sleep(2)
                like_button.click()
                sleep(0.5)
                cont = cont + 1
                temp = temp + 1

                if cont == 8:
                    bot.refresh()
                    cont = 1
                    continue

            numPost.destroy()
            num.destroy()
            ok.destroy()
            root.geometry("500x300")
            liked = Label(root, text="Total no. of posts liked is " + str(temp - 1), relief="solid", bg="AntiqueWhite3",
                          fg="black", width="20", font='times 20 bold')
            liked.place(x=90, y=70)

        except common.exceptions.WebDriverException:
            root.geometry("500x300")
            numPost.destroy()
            num.destroy()
            ok.destroy()
            liked = Label(root, text="bot not responding", bg="AntiqueWhite3", fg="black",
                          width="20", font='times 20 bold')
            liked.place(x=90, y=70)

    # feed liker code is  here
    killnewFrame()
    root.geometry("500x300")
    global numPost, num, ok
    numPost = Label(root, text="Enter number of posts (in digits)", font='times 15 bold')
    numPost.place(x=90, y=60)
    num = Entry(root, bg="mint cream")
    num.place(x=175, y=100)
    ok = Button(root, text="Start", bg="azure", fg="black", command=starting, width=12, border=0, font="corbel 12 bold")
    ok.place(x=180, y=155)


# def dm_request():


def username_bot():
    def start():
        try:
            comment_list = (comments.get()).split(',')
            length = len(comment_list)

            bot.get("https://www.instagram.com/" + str(user.get()) + "/")
            try:
                button = bot.find_element_by_xpath(
                    "/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button")
                button.click()
                bot.find_element_by_class_name("_9AhH0").click()
            except common.exceptions.NoSuchElementException:
                root.update()
                bot.find_element_by_class_name("_9AhH0").click()

            sleep(2)
            while True:
                bot.find_element_by_xpath(
                    "/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button").click()  # like

                bot.find_element_by_class_name("RxpZH").click()  # textclick
                bot.find_element_by_xpath(
                    ' /html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(
                    comment_list[random.randint(0, length - 1)])
                send_button = bot.find_element_by_xpath(
                    "/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/button ")
                send_button.click()
                root.update()
                sleep(5)
                # next photo
                next = bot.find_element_by_xpath("//a[text()=\"Next\"]")
                next.click()
                root.update()
                sleep(3)
        except:
            root.update()
            root.geometry("500x300")
            text.destroy()
            comments.destroy()
            user_target.destroy()
            user.destroy()
            ok.destroy()
            liked = Label(root, text="bot not responding", relief="solid", bg="AntiqueWhite3", fg="black",
                          width="20", font='times 20 bold')
            liked.place(x=90, y=70)

    killnewFrame()
    user_target = Label(root, text="Enter target Username", font='times 15 bold')
    user_target.place(x=180, y=60)
    user = Entry(root, bg="mint cream")
    user.place(x=175, y=100)
    text = Label(root, text="Enter comments separated by commas,", font='times 15 bold')
    text.place(x=90, y=140)
    comments = Entry(root, bg="mint cream", width=24)
    comments.place(x=175, y=180)
    ok = Button(root, text="Start", bg="azure", fg="black", command=start, width=12, border=0, font="corbel 12 bold")
    ok.place(x=180, y=215)
    
    
def auto_reply():
    def start():
        try:
            response_message = str(msg.get())
            bot.get('https://www.instagram.com/direct/inbox/general')
            root.update()
    
            while True:
    
                sleep(1)
    
                unread_elements = bot.find_elements_by_css_selector('._41V_T.Sapc9.Igw0E.IwRSH.eGOV_._4EzTm')
                root.update()
                for message in unread_elements:
                    try:
    
                        message.click()
    
                        textbox_element = bot.find_element_by_tag_name('textarea')
    
                        textbox_element.send_keys(response_message)
    
                        send_button = bot.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button')
    
                        send_button.click()
                    except common.exceptions.WebDriverException:
                        root.update()

        except common.exceptions.WebDriverException:
            root.update()
            root.geometry("500x300")
            numPost.destroy()
            msg.destroy()
            ok.destroy()
            liked = Label(root, text="bot not responding", relief="solid", bg="AntiqueWhite3", fg="black",
                          width="20", font='times 20 bold')
            liked.place(x=90, y=70)

    killnewFrame()
    root.geometry("500x300")
    global numPost, num, ok
    numPost = Label(root, text="Enter the comments you wanna send", font='times 15 bold')
    numPost.place(x=90, y=60)
    msg = Entry(root, bg="mint cream")
    msg.place(x=175, y=100)
    ok = Button(root, text="Start", bg="azure", fg="black", command=start, width=12, border=0, font="corbel 12 bold")
    ok.place(x=180, y=155)
            
            
def commenting_on_hashtag():
    def start():
        try:
            tag = str(htag.get())
            counter = int(0)
            comment_list = (comments.get()).split(',')  
            n = len(comment_list)
            root.update()
            bot.get('https://www.instagram.com/explore/tags/'+tag+'/')
            post = bot.find_element_by_class_name('_9AhH0')
            post.click()
            sleep(3)
    
            while True:
                # liking the posts one by one
                likeButton = bot.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button')
                likeButton.click()
                sleep(random.randint(2,7))
    
                # commenting on all the posts
                text_area = bot.find_element_by_class_name('RxpZH')
                text_area.click()
                bot.find_element_by_xpath(' /html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(comment_list[random.randint(0, n - 1)])
                send_button = bot.find_element_by_xpath( "/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/button ")
                send_button.click()
                sleep(random.randint(4,5))
                #next photo
                next = bot.find_element_by_xpath("//a[text()=\"Next\"]")
                next.click()
                sleep(random.randint(3,6))
                # no. of post liked
                counter = counter + 1
    
        except common.exceptions.WebDriverException:
            root.geometry("500x300")
            numPost.destroy()
            num.destroy()
            ok.destroy()
            liked = Label(root, text="Window Closed...Number of liked & commented posts: " + str(counter), bg="AntiqueWhite3", fg="black",
                          width="20", font='times 20 bold')
            liked.place(x=90, y=70)
    

    killnewFrame()
    hash = Label(root, text="Enter one hashtag", font='times 15 bold')
    hash.place(x=140, y=60)
    htag = Entry(root, bg="mint cream")
    htag.place(x=175, y=100)
    text = Label(root, text="Enter comments separated by commas(,)", font='times 15 bold')
    text.place(x=90, y=140)
    comments = Entry(root, bg="mint cream", width=30)
    comments.place(x=175, y=180)
    ok = Button(root, text="Start", bg="azure", fg="black", command=start, width=12, font="corbel 12 bold")
    ok.place(x=180, y=215)
    
    
    
def dm_req_accpt():
    def start():
        x = str(num.get())
        z = "y"
        bot.get('https://www.instagram.com/direct/requests')
        count = 0
        y = [6, 2]
        while True:

            if count == 0:
                i = y[0]
            else:
                i = y[1]
            sleep(i)
            message = bot.find_element_by_xpath(
                '/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/a/div/div[2]/div[1]/div/div/div/div')
            message.click()
            sleep(1)
            allow_button = bot.find_element_by_xpath(
                '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[5]')
            allow_button.click()
            sleep(1)

            if z in 'y':
                permission = bot.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/button[2]')
                permission.click()
                sleep(1)

                textbox_element = bot.find_element_by_xpath(
                    '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                textbox_element.send_keys(x)

                send_button = bot.find_element_by_xpath(
                    '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button')
                send_button.click()
                sleep(1)
                req_btn = bot.find_element_by_xpath(
                    '/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div[2]/span/button/h5')
                req_btn.click()
                count = count + 1
                continue

            if z in 'n':
                textbox_element = bot.find_element_by_xpath(
                    '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')

                textbox_element.send_keys(x)

                send_button = bot.find_element_by_xpath(
                    '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button')
                send_button.click()

                req_btn = bot.find_element_by_xpath(
                    '/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/button/h5')
                req_btn.click()
                count = count + 1
                continue

    killnewFrame()
    root.geometry("500x300")
    global numPost, num, ok
    numPost = Label(root, text="Enter message you want to reply 👇", font='times 15 bold')
    numPost.place(x=90, y=60)
    num = Entry(root, bg="mint cream", width=30)
    num.place(x=175, y=100)
    ok = Button(root, text="Start", bg="azure", fg="black", command=start, width=12, border=0, font="corbel 12 bold")
    ok.place(x=180, y=155)

    
def story_reply():
    def start():
        try:
            story_rep = num.get().split(',')
            story = bot.find_element_by_xpath(
                '/html/body/div[1]/section/main/section/div/div[1]/div/div/div/div/ul/li[3]/div/button/div[2]')
            story.click()
            sleep(5)
            while True:
                try:
                    a = story_rep[random.randint(0, len(story_rep))]

                    sleep(3)
                    textarea = bot.find_element_by_tag_name('textarea')
                    textarea.send_keys(a)

                    send_btn = bot.find_element_by_xpath(
                        '/html/body/div[1]/section/div/div/section/div[2]/div[3]/div/div/div[1]/div[2]/button')
                    send_btn.click()
                    next = bot.find_element_by_class_name('ow3u_')
                    next.click()
                    continue
                except:

                    next = bot.find_element_by_class_name('ow3u_')
                    next.click()
                    continue

        except common.exceptions.WebDriverException:
            root.update()
            root.geometry("500x300")
            numPost.destroy()
            num.destroy()
            ok.destroy()
            liked = Label(root, text="bot not responding", relief="solid", bg="AntiqueWhite3", fg="black",
                          width="20", font='times 20 bold')
            liked.place(x=90, y=70)


    killnewFrame()
    root.geometry("500x300")
    global numPost, num, ok
    numPost = Label(root, text="Enter comments separated by comma 👇", font='times 15 bold')
    numPost.place(x=90, y=60)
    num = Entry(root, bg="mint cream", width=30)
    num.place(x=175, y=100)
    ok = Button(root, text="Start", bg="azure", fg="black", command=start, width=12, border=0, font="corbel 12 bold")
    ok.place(x=180, y=155)
        
        


def execute():
    login(str(entry1.get()), str(entry2.get()))


def Exit():
    if messagebox.askyesno("Exit", "Do you want to Quit?"):
        bot.close()
        root.destroy()


# t2 = Thread(target=login(str(entry1.get()), str(entry2.get())))


def killnewFrame():
    b3.destroy()
    b4.destroy()
    b5.destroy()
    b6.destroy()
    b7.destroy()
    b8.destroy()
    story.destroy()


def newFrame():
    root.geometry("500x500")
    global b3, b4, b5, b6, b7, b8, story
    b3 = Button(root, text="1.Feed\n Liker", bg="pink", fg="black", command=feedliker, width=12, border=0, font="corbel 12 bold")
    b3.place(x=15, y=100)

    b4 = Button(root, text="2.Message\n  Bot", bg="light yellow", fg="green", command = auto_reply, width=12, border=0,  font="corbel 12 bold")
    b4.place(x=175, y=100)

    b5 = Button(root, text="3.Request\n Acceptor", bg="cyan", fg="black",command = dm_req_accpt, width=12, border=0,  font="corbel 12 bold")
    b5.place(x=355, y=100)

    b6 = Button(root, text="4.Hashtag\n Bot", bg="blue", fg="white", width=12,command = commenting_on_hashtag, border=0,  font="corbel 12 bold")
    b6.place(x=15, y=200)

    b7 = Button(root, text="5.Username\n Bot", bg="light blue", fg="blue", command=username_bot, width=12, border=0,
                font="corbel 12 bold")
    b7.place(x=175, y=200)

    story = Button(root, text="6.Auto Story\nReply", bg='dark goldenrod', fg='azure', width=12, command=story_reply, border=0, font="corbel 12 bold")
    story.place(x=355, y=200)

    b8 = Button(root, text="Quit\n  ❌ ", bg="red", fg="white", command=Exit, width=12, border=0,  font="corbel 12 bold")
    b8.place(x=180, y=350)


def main_fn():
    global root
    root = tkinter.Tk()
    root.geometry("500x300")
    root.resizable(0, 0)
    root.configure(bg="gray90")
    root.title("Insta Automation")

    Inst_Bot = Label(root, text="Insta Automation", bg="yellow", fg="black", width="20",
                     font='Algerian 20 bold')
    Inst_Bot.place(x=80, y=0)

    global emails, entry1, passwords, entry2, b1, b2
#bg="light blue",
    emails = Label(root, text="Enter Username: ",bg="light blue", font='corbel 15 bold')
    emails.place(x=45, y=50)
    entry1 = Entry(root, bg='peach puff', fg='gray9')
    entry1.place(x=250, y=55)

    passwords = Label(root, text="Enter Password: ", bg="light blue", font='corbel 15 bold')
    passwords.place(x=45, y=100)
    entry2 = Entry(root, show="*", bg='peach puff', fg='gray9')
    entry2.place(x=250, y=105)

    b1 = Button(root, text="Log In", bg="green", fg="white", command=execute, width=12, border=0, font="Chiller 18 bold")
    b1.place(x=115, y=170)

    b2 = Button(root, text="Quit", bg="red", fg="white", command=Exit, width=12, border=0, font="Chiller 18 bold")
    b2.place(x=265, y=170)

    root.mainloop()


# starting of entire program is here

def fn():
    global bot
    bot = webdriver.Firefox()


main_fn()

