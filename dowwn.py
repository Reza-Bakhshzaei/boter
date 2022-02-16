from pyrogram import Client,filters
from pyrogram.types import*
import os,pyminizip,random
import time
from pyrogram.types import ChatPermissions
import youtube_dl
from pytube import YouTube
from os.path import exists as file_exists
api_id=13893053
api_hash="f586d92837b0f6eebcaa3e392397f47c"
bot_token="5102000083:AAHKoWGuHKriH4Z4_Oc-QwR4tz6IhM2fH68"
app=Client("my_bot",api_id=api_id,api_hash=api_hash,bot_token=bot_token)
#-------------------------------------------------------------------------------------------------------------
START="""سلام سلام \nخوش اومدی \n😍من hero هستم\nاگه میخای با قابلیت های من اشنا بشی منو تو گروهت ادد و بعد از اون ادمینم کن😍😎\nبزن بریم🏃🏻‍♂️ \n\n\nیه سوپرایز برات دارم 🥳\nاگه میخوای که برنامه نویسی کامپیوتر یاد بگیری 😍همین الان تو چنلم جوین شو😍🤩\n@learning_programing_language"""
NOTEXIS="""oops..\nyour not joined to my chanel\nplease join and so send /start\nmy chanel: @learning_programing_language"""
EXIS="""WELCOME FRIND.\ni'm moving.\nthanks for start me."""
PANEL="""😑🤦🏻تو که میدونی پنلی برام ننوشتی چرا هعی پنل پنل میکنی؟\n🥲حالا دلت و نمیشکنم بیا یه لیست کوچولو بدمت که میتونم انجام بدم \n**🔠✅ادد کردن کلمه برای پاسخگویی از طرف خود ربات با دستور :**\n-> tadd (kalame)|(javab)\n-> Tadd (kalame)|(javab)\n**☃️ادد کردن استیکر برای پاسخ گویی از طرف ربات:**\nریپلی کردن استیکر و سپس تایپ این دو دستور\n->sadd\n->Sadd\n**📝📘لیست استیکر هایی که برای پاسخ گویی دارم و نشون میدم به دستور سازنده📝📘**\n**🔒قفل گروه🔒**\n**📝📘لیست کلمه هایی که یاد دارم و نشون میدم به دستور سازنده📝📘**\n**🗑حذف پیام ها به دستور پدرم🗑**\n**🆔تگ کاربران توسط سازنده🆔**\n**❌⛔️بن کاربران توسط سازنده❌⛔️**\n**🧷📌سنجاق کردن پیام توسط سازنده🧷📌**\n\n**🧷📌برداشتن پیام سنجاق شده توسط سازنده🧷📌**\n**♥️♦️خوشامد گویی به دوستان تازه وارد♥️♦️**\n**🙆🏻‍♂️فعلا همیناس ولی پدرم داره رشدم میده و در اینده نزدیک کاملم میکنه🙆🏻‍♂️**"""
#-------------------------------------------------------------------------------------------------------------
list_locked={}

#-------------------------------------------------------------------------------------------------------------
# def user():
#     file=open("user.txt","w+")
#     f=app.get_chat_members("@learning_programing_language")
#     for member in f:
#         file.write(str(member.user.id))
#         file.write("\n")
#     file.close()
# def fin(user):
#     fil=open("user.txt","r")
#     file=fil.read()
#     exis=file.find(str(user))
#     return exis-
def is_admin(client,message):
    list=[]
    for admin in client.get_chat_members(chat_id=message.chat.id,filter="administrators"):
        list.append(admin.user.id)
    if message.from_user.id in list:
        return True
    else:
        return False
    
def find_message(text):
    list=[]
    file=open("defult_answer.text","r",encoding="UTF-8")
    for line in file:
        st=line.find(text)
        s=line.find("|")
        te=line[:s]
        if text == te:
            en=line.find("\n",st)
            list.append(line[s+1:en])
    file.close()
    size=len(list)
    if size!=0:
        rand=random.randint(0,size-1)
        return list[rand]
    else:
        return "n"

def list_file(message):
    pyminizip.compress("defult_answer.text",None,"list_word.zip","reza0021",1)
    message.reply_document("list_word.zip")
    os.remove("list_word.zip")

def del_anderline():
    file=open("defult_answer.text","r",encoding="UTF-8")
    text=""
    for line in file:
        fin=line.find("|")
        kalam=line[:fin]
        kalame=kalam.replace("_"," ")
        javab=line[fin+1:]
        javabe=javab.replace("_"," ")
        text+=f"📝📘**kalame:** {kalame}\n->{javabe}\n---------------------------------\n"
    file.close()
    return text

def imogis(imogi):
    file=open("sticker.txt","r",encoding="UTF-8")
    list=[]
    for line in file:
        if imogi in line:
            img=line[2:]
            img=img.replace("\n","")
            list.append(img)
    size=len(list)
    if size==0:
        return "n"
    else:
        rand=random.randint(0,size-1)
        return list[rand]

def base_number_btok(number,d_base):
    text=""
    while number:
        print(number)
        rest=number%d_base
        text+=str(rest)
        number=int(number/d_base)
    return text[::-1]

def base_number_ktob(number,s_base):
    number_txt=str(number)[::-1]
    sum=0
    count=0
    for i in number_txt:
        sum+=int(i)*(s_base**count)
        count+=1
    return sum
def check_number(number,s_base):
    number=str(number)
    for i in number:
        if int(i)>=s_base:
            return 0
    return 1

@app.on_message(filters.group & filters.regex("^(t|T)abdil "))
def change_base(client,message):
    text=str(message.text)
    text=text[7:].split()
    s_base=int(text[0])
    d_base=int(text[1])
    number=int(text[2])
    if(check_number(number,s_base) ==1) and (s_base<=10 and d_base<=10):
        if s_base>d_base:
            result=base_number_btok(number,d_base)
        else:
            result=base_number_ktob(number,s_base)
        message.reply(f"**Resulte:** `{result}`")
    else:
        message.reply("یکم دقت کن\nعدد در مبنای داده شده نیس یا مبنا ها از 10 بیشتر هستند\n در حال حاضر فقط تبدیل اعداد در مبناهای کوچک تر از 10 امکان پذیر است!!!!")

@app.on_message(filters.group & filters.regex("^(d|D)l "))
def download_youtube(client,message):
    url=str(message.text)[3:]
    infor=YouTube(url)
    caption=f"📝**Title:** `{infor.title}`\n👀**Views:** {infor.views}\n⏮⏸▶️⏹⏭**Length:** {infor.length} s\n🏅🎖**Rating:** {infor.rating}\n"
    message.reply(caption+"-_-_-_-_-_-_-_-_-_-_-_-_-_-\n📥📤**Downloading and Uploading...**")
    with youtube_dl.YoutubeDL({}) as file:
        file.download([url])
    time.sleep(3)
    list_suffix=['mp4','webm']
    for file in os.listdir():
        for index in list_suffix:
            if file.endswith(f".{index}"):
                filer=os.path.join(file)
    message.reply_document(filer,caption=caption)
    os.remove(filer)
    
@app.on_message(filters.group & filters.regex("^(l|L)ock$")& filters.user(618260788))
def lock(client,message):
    global list_locked
    swit=0
    for i,k in list_locked.items():
        if i==int(message.chat.id):
            swit=1
    if (swit==1)and(is_admin(client,message)):
       message.reply("🔒گروه قفل بود!")
    elif (swit==0)and(is_admin(client,message)):
        list_locked[int(message.chat.id)]=True
        message.reply("🔒قفل گروه فعال شد!")
    else:
        message.reply("برو بچه جان با دم شیر بازی نکن\nاین دستور برای مدیر و ادمین هاست")

@app.on_message(filters.group & filters.regex("^(u|U)nlock$"))
def lock(client,message):
    global list_locked
    swit=0
    for i,k in list_locked.items():
        if i==int(message.chat.id):
            swit=1
    if (swit==1)and(is_admin(client,message)):
        list_locked.pop(int(message.chat.id))
        message.reply("🔓قفل گروه غیر فعال شد!")
    elif (swit==0)and(is_admin(client,message)):
        message.reply("🔓گروه باز بود!")
    else:
        message.reply("برو بچه جان با دم شیر بازی نکن\nاین دستور برای مدیر و ادمین هاست")

@app.on_message(filters.group & filters.regex("^(s|S)add$"))
def add_sticker(client,message):
    if message.reply_to_message.sticker:
        file=open("sticker.txt","a",encoding="UTF-8")
        id=message.reply_to_message.sticker.file_id
        imogi=message.reply_to_message.sticker.emoji
        file.write(imogi+"|"+str(id)+"\n")
        file.close()
        message.reply("✅")

@app.on_message(filters.group & filters.regex("^بگو "))
def add_sticker(client,message):
    text=str(message.text)[4:]
    message.reply(text)

@app.on_message(filters.group & filters.regex("^کی "))
def add_sticker(client,message):
    diction={}
    namer=""
    ids=0
    i=0
    text=str(message.text)[3:]
    members=app.get_chat_members(f"{message.chat.id}")
    for member in members:
        id=member.user.id
        name=member.user.first_name
        if str(id)!="5102000083":
            diction[name]=str(id)
    index=random.randint(0,len(diction)-1)
    for k,v in diction.items():
        if i==index:
            namer+=k
            ids=int(v)
        i+=1
    message.reply(f"[{str(namer)}](tg://user?id={int(ids)}) {text}😆")

@app.on_message(filters.user(618260788) & filters.regex("^(l|L)ists$"))
def add_sticker(client,message):
    pyminizip.compress("sticker.txt",None,"list_sticker.zip","reza0021",1)
    message.reply_document("list_sticker.zip")
    os.remove("list_sticker.zip")

@app.on_message(filters.group & filters.regex("^(d|D)el "))
def delete_message(client,message):
    message_id=message.message_id
    chat_id=message.chat.id
    count=message.text[4:]
    if is_admin(client,message):
        if count=="all":
            count=message_id
        list_id=[]
        for i in range(int(message_id-1),int(message_id-1)-int(count),-1):
            list_id.append(i)
        client.delete_messages(chat_id,list_id)
        message.reply("✅")
    else:
        message.reply("برو بچه جان با دم شیر بازی نکن\nاین دستور برای مدیر و ادمین هاست")

@app.on_message(filters.command("start","/") & filters.private )
def main(client, message):
    client.send_message(chat_id=message.chat.id,text=START,reply_to_message_id=message.message_id)
    # chat_id=message.chat.id
    # user()
    # exis=fin(chat_id)
    # if exis==-1:
    #     client.send_message(chat_id=chat_id,text=NOTEXIS,reply_to_message_id=message.message_id)
    # else:
    #     main(client,message)

@app.on_message(filters.group & filters.new_chat_members)
def new_member(client,message):
    name=str(message.new_chat_members)
    fin_name=name.find("first_name")
    fon_name=name.find(",",fin_name)
    na=name[fin_name+11:fon_name]
    na=na.replace("'","")
    fin_id=name.find("id")
    fon_id=name.find(",",fin_id)
    id=name[fin_id+3:fon_id]
    id=id.replace("'","")
    if id=="5102000083":
        message.reply("        |------------------------------------|\n                     سلووووم به بروبچ 😍\n         |------------------------------------|\n                 \                        /\n                   \   ( ✿ ♡‿ ♡) /\n                     \                /\n                        ____   \n                           |       | \n                           |       |    \n                          π       π\n\nمدیر گل برای استفاده از من ادمین کن فقط خوشگل😎😜")
    else:
        message.reply(f" سلام \nخوش اومدی [{na}](tg://user?id={int(id)})\nاز قوانین گروه پیروی کن تا مدیر ناراحت نشه😁")

@app.on_message(filters.group & filters.left_chat_member)
def left_member(client,message):
    list_left=["به درود یا حق","خوب شد که رفت","کجا میری بیتربیت منو تنها میزاری","نرووووووووو دل من به بودنت خوشه"]
    list_remove=["خوب شد بیرونش کردی بیتربیتو","از اولم منو دوس نداشت","ماییم و نوای بینوایی * بسمل که اگر حریف مایی"]
    if message.left_chat_member:
        index=random.randint(0,len(list_left)-1)
        message.reply(list_left[index])
    else:
        index=random.randint(0,len(list_remove)-1)
        message.reply(list_remove[index])

@app.on_message(filters.group & filters.regex("^(t|T)ag$"))
def tag_all(client,message):
    list=[" بیدار شوید و از زیر اب خارج شوید \n همانا خداوند فرمود : زیر ابیان گنهکارند😁 \n","تو را به سمفونی شماره پنج بتهوون قسم بیا ببین این چی میگه"]
    list.append("الو \nالو الو خدا\nحاجی کجاعن اینا 😂😂")
    list.append("قال مدیر(ع):\nای کسانی که فعال نیستید بدانید که مدیر اگاه است \nایا برای شما گروه نساخته ایم؟")
    list.append("مدیر(ع)فرمود:\nای کسانی که فعال نیستید ایا ما شما را به این گروه دعوت نکرده ایم ؟\nایا در کنارتان ده ها نفر حوری نگذاشته ایم تا عاشق شوید؟😂")
    list.append("قال مدیر(ع):\nوای بر انان که فعال نیستند \nبترسید از روزی که اخراج شوید😒")
    tex=list[random.randint(0,len(list)-1)]
    text=tex+"\n"
    if is_admin(client,message):
        list_bot=[]
        for bots in client.get_chat_members(chat_id=message.chat.id,filter="bots"):
            list_bot.append(bots.user.id)
        members=app.get_chat_members(f"{message.chat.id}")
        for member in members:
            id=member.user.id
            if (str(id)!="5102000083")and(not(id in list_bot)):
                text+=f"[{member.user.first_name}](tg://user?id={id}) O_o "
        message.reply(text,parse_mode="markdown") 
    else:
        message.reply("برو بچه جان با دم شیر بازی نکن\nاین دستور برای مدیر و ادمین هاست")

@app.on_message(filters.group & filters.regex("^(s|S)ilent "))
def ChatPermis(client,message):
    if is_admin(client,message):
        if message.reply_to_message:
            tim=int(str(message.text)[7:])
            id=message.reply_to_message.from_user.id
            client.restrict_chat_member(message.chat.id,id,ChatPermissions(),int(time.time()+(60*tim)))
        else:
            text=str(message.text)[7:]
            id=text.split()[0]
            tim=int(text.replace(id,""))
            client.restrict_chat_member(message.chat.id,id,ChatPermissions(can_send_messages=False,can_send_media_messages=False,can_invite_users=False),int(time.time()+(60*tim)))
        message.reply(f"🤐کاربر با ایدی عددی 🆔{id} برای 🕧{tim} دقیقه ساکت شد.🤐 \n♋️برای خارج کردن از حالت سکوت دستور زیر را کپی و ارسال کنید.📄\n->`Unsilent {id}`")
    else:
        message.reply("برو بچه جان با دم شیر بازی نکن\nاین دستور برای مدیر و ادمین هاست")

@app.on_message(filters.group & filters.regex("^(u|U)nsilent "))
def ChatPermis(client,message):
    if is_admin(client,message):
        id=str(message.text)[9:]
        client.restrict_chat_member(message.chat.id,id,ChatPermissions(can_send_messages=True,can_send_media_messages=True,can_invite_users=True))
        message.reply(f"😁کاربر با ایدی 🆔{id} از حالت سکوت خارج شد.😁")
    else:
        message.reply("برو بچه جان با دم شیر بازی نکن\nاین دستور برای مدیر و ادمین هاست")

@app.on_message(filters.group & filters.regex("^(p|P)in$"))
def pin_message(client,message):
    if is_admin(client,message):
        client.pin_chat_message(chat_id=message.chat.id,message_id=message.reply_to_message.message_id)
        message.reply("✅")
    else:
        message.reply("برو بچه جان با دم شیر بازی نکن\nاین دستور برای مدیر و ادمین هاست")

@app.on_message(filters.group & filters.regex("^(u|U)npin$"))
def unpin_message(client,message):
    if is_admin(client,message):
        client.unpin_chat_message(chat_id=message.chat.id,message_id=message.reply_to_message.message_id)
        message.reply("✅")
    else:
        message.reply("برو بچه جان با دم شیر بازی نکن\nاین دستور برای مدیر و ادمین هاست")

@app.on_message(filters.group & filters.regex("^(b|B)an$"))
def ban_user(client,message):
    if is_admin(client,message):
        id=message.reply_to_message.from_user.id
        message.chat.kick_member(id)
        message.reply("✅")
    else:
        message.reply("برو بچه جان با دم شیر بازی نکن\nاین دستور برای مدیر و ادمین هاست")

@app.on_message(filters.group & filters.regex("^(d|D)el "))
def delete_message(client,message):
    if is_admin(client,message):
        message_id=message.message_id
        chat_id=message.chat.id
        count=message.text[4:]
        if count=="all":
            count=message_id
        list_id=[]
        for i in range(int(message_id-1),int(message_id-1)-int(count),-1):
            list_id.append(i)
        client.delete_messages(chat_id,list_id)
        message.reply("✅")
    else:
        message.reply("برو بچه جان با دم شیر بازی نکن\nاین دستور برای مدیر و ادمین هاست")

@app.on_message(filters.group  & filters.regex("^(p|P)anel$"))
def panel(client,message):
    if is_admin(client,message):
        message.reply(PANEL)
    else:
        message.reply("برو بچه جان با دم شیر بازی نکن\nاین دستور برای مدیر و ادمین هاست")


@app.on_message(filters.group  & filters.regex("^(t|T)add "))
def add_text(client,message):
    txt=str(message.text)
    f=txt[5:]
    text=txt.replace(f,"")
    tx=text.replace(" ","_")
    file=open("defult_answer.text","a",encoding="UTF-8")
    file.write(tx+"\n")
    file.close()
    message.reply("ممنونم ازت دوست عزیزم که بهم کلمه یاد میدیی😍😍❤️")


@app.on_message(filters.group&filters.regex("^(l|L)ist$")&filters.user(618260788))
def list_kalamat(client,message):
    list_file(message)
    text=del_anderline()
    if len(text)<=4096:
        message.reply(text)
    else:
        ffile=open("list_word.txt","a",encoding="UTF-8")
        ffile.write(text)
        message.reply_document("list_word.txt")
        ffile.close()
        os.remove("list_word.txt")

@app.on_message(filters.group&filters.all)
def defulte_answer(client,message):
    global list_locked
    swit=0
    for i,k in list_locked.items():
        if i==int(message.chat.id):
            swit=1
    if swit==1:
        if (not(is_admin(client,message))):
            message.reply("🔒گروه قفله دوست عزیز!")
            message.delete()
    elif message.text:
        text=str(message.text)
        kalame=text.replace(" ","_")
        answer=find_message(kalame)
        ans=answer.replace("_"," ")
        if answer=="n":
            pass
        else:
            message.reply(ans)
    elif message.sticker:
        stic=imogis(message.sticker.emoji)
        if stic!="n":
            message.reply_sticker(stic)


app.run()
