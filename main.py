import os,xlsxwriter,jdatetime,xlrd,xlwt
from pyrogram import Client,filters
from pyromod import listen
from xlutils.copy import copy
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
api_id=13893053
api_hash="f586d92837b0f6eebcaa3e392397f47c"
bot_token="8853175264:AAHdgnySYvv0SURpwZ3T5dUMz7G8y7aq_4w"
app = Client("acontet", api_id=api_id,api_hash=api_hash,bot_token=bot_token)
#-------------------------------------------------------------------
admin=792518488
try:
    wb = xlrd.open_workbook("all_information.xls")
except:
    workbook = xlsxwriter.Workbook("all_information.xls")
    worksheet = workbook.add_worksheet()
    worksheet.write('A1',0)
    worksheet.write('B1',0)
    worksheet.write('C1',0)
    worksheet.write('D1',0)
    worksheet.write('E1',0)
    worksheet.write('F1',0)
    workbook.close()
keyboard_user=ReplyKeyboardMarkup(
                [
                    ["🖋ثبت طرح📝"],
                    ["📝ثبت پیشنهادات و انتقادات"],
                    ["🔙برگشت به منو اصلی"]
                ],
                resize_keyboard=True  # Make the keyboard smaller
            )
keyboard_user_not_logined=ReplyKeyboardMarkup(
                [
                    ["🦹‍♂️ادامه در حالت ناشناس"],
                    ["📝ثبت نام و ورود"],
                    ["📄گزارشکار پروژه های در حال اجرا ⛓"],
                    ["🤖درباره ربات"]
                ],
                resize_keyboard=True  # Make the keyboard smaller
            )
keyboard_kansel=ReplyKeyboardMarkup(
                [
                    ["لغو عملیات"]
                ],
                resize_keyboard=True  # Make the keyboard smaller
            )
keyboard_admin=ReplyKeyboardMarkup(
                [
                    ["📑نمایش پیام های ذخیره شده"],
                    ["🎖نمایش پیام های برتر"],
                    ["👁‍🗨👤نمایش کاربران"],
                    ["✔ارسال همگانی"]
                ],
                resize_keyboard=True  # Make the keyboard smaller
            )
list_regex=["/start","✔ارسال همگانی","👁‍🗨👤نمایش کاربران","🎖نمایش پیام های برتر","📑نمایش پیام های ذخیره شده","لغو عملیات","🤖درباره ربات","📝ثبت نام و ورود","🦹‍♂️ادامه در حالت ناشناس","📝ثبت پیشنهادات و انتقادات","🖋ثبت طرح📝"]
#-------------------------------------------------------------------creator
@app.on_message(filters.private & filters.user(618260788) & filters.regex("^get$"))
async def send_date(c,m):
    try:
        await m.reply_document("all_information.xls")
    except:
        pass
    try:
        await m.reply_document("zakhireha.txt")
    except:
        pass
    try:
        await m.reply_document("bartarha.txt")
    except:
        pass
    try:
        await m.reply_document("all_users.txt")
    except:
        pass

@app.on_message(filters.private & filters.regex("^🤖درباره ربات$")) # edit for admin
async def tarah(c,m):
    await m.reply("این ربات در جهت پیشرفت و آبادانی روستایمان « کهن دیار ازغند » طراحی شده است. \n🤔 چنانچه در استفاده از ربات به مشکل برخورد کردید می‌توانید با **مدیریت ربات یا طراح و توسعه دهنده ربات** در ارتباط باشید💐\n👌🏻 همچنین جهت سفارش و طراحی ربات خود می‌توانید با توسعه دهنده در ارتباط باشید\nایدی دهیار محترم: \n@Dehyar_SAFARI\n**🛠 توسعه دهنده :** رضا بخش زایی\n🆔 @REZABZ2 \n📞 09154172849")
#-------------------------------------------------------------------admin
def exist_number(number):
    wb = xlrd.open_workbook("all_information.xls")
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)
    for i in range(sheet.nrows):
        if str(number) in sheet.row_values(i):
            return i
    return -1

async def show_message(m,path):
    try:
        file=open(path,"r",encoding="UTF-8").read()
        start=0
        while start<=len(file):
            end=file.find("+",start)
            message=file[start:end]
            if len(message)>10:
                await m.reply(message)
            start=end+1
            if start>len(file)-5:
                start=len(file)+1
        await m.reply("✅عملیات انجام شد",reply_markup=keyboard_admin)
    except:
        await m.reply("📂")
        await m.reply("❌پیامی وجود ندارد",reply_markup=keyboard_admin)
    
@app.on_message(filters.user(admin) & filters.command("start","/"))
async def start_admin(c,m):
    await m.reply("💡سلام ، به پنل مدیریت خوش آمدید 👨🏻‍💻",reply_markup=keyboard_admin)

@app.on_message(filters.user(admin) & filters.regex("^📑نمایش پیام های ذخیره شده$"))
async def show_saved(c,m):
    await m.reply("♻در حال انجام عملیات لطفا صبر کنید✅")
    await show_message(m,"zakhireha.txt")

@app.on_message(filters.user(admin) & filters.regex("^🎖نمایش پیام های برتر$"))
async def show_beter(c,m):
    await m.reply("♻در حال انجام عملیات لطفا صبر کنید✅")
    await show_message(m,"bartarha.txt")
    
@app.on_message(filters.user(admin) & filters.regex("^👁‍🗨👤نمایش کاربران$"))
async def show_user(c,m):
    await m.reply("♻در حال انجام عملیات لطفا صبر کنید✅")
    wb = xlrd.open_workbook("all_information.xls")
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)
    text=""
    x=0
    for i in range(0,sheet.nrows):
        p=sheet.row_values(i)
        num=int(p[4])
        if int(p[5])!=0:
            text+=f"**📝نام و نام خانوادگی:**{p[0]}\n** ✏نام پدر: ** {p[3]}\n**📞شماره تلفن:** {p[2]}\n**🥇🎖تعداد نظرات برتر:** {num}\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
            x+=1
        elif sheet.nrows==1:
            text+="🔴لیست خالی است"
        if x==20:
            await m.reply(text)
            text=""
            x=0
    if x<20:
        await m.reply(text)
    if x!=0:
        await m.reply("✅عملیات با موفقیت انجام شد")
    
@app.on_message(filters.user(admin) & filters.regex("^✔ارسال همگانی$"))
async def send_to_all(c,m):
    try:
        list_user=open("all_users.txt","r",encoding="UTF-8").read().split()
        await m.reply("🤖به بخش ارسال پیام همگانی خوش امدید",reply_markup=keyboard_kansel)
        message=await c.ask(admin,"✉پیام مورد نظر را ارسال کنید:")
        if message.text=="لغو عملیات":
            await m.reply("✅به منو قبل بر میگردید",reply_markup=keyboard_admin)
        else:
            leng=len(list_user)
            id=message.message_id
            for i in list_user:
                await c.forward_messages(int(i),admin,id)
            await m.reply(f"✅عملیات انجام شد\n✔این پیام به {leng} کاربر ارسال شد.",reply_markup=keyboard_admin)
    except:
        await m.reply("❌شخصی برای ارسال وجود ندارد",reply_markup=keyboard_admin)
@app.on_callback_query(filters.user(admin))
async def admin_shishe(cl,ca):
    comand=str(ca.data)[:6]
    id=str(ca.data)[6:]
    member=exist_number(id)
    if comand=="zakhir":
        text=ca.message.text
        file_zakhire=open("zakhireha.txt","a",encoding="UTF-8")
        file_zakhire.write(text+"\n+\n")
        file_zakhire.close()
        await cl.send_message(admin,"✅پیام مورد نظر در دسته پیام های ذخیره شده قرار گرفت💯")
    if comand=="bartar":
        text=ca.message.text
        file_bartar=open("bartarha.txt","a",encoding="UTF-8")
        file_bartar.write(text+"\n+\n")
        file_bartar.close()
        rb=xlrd.open_workbook("all_information.xls")
        sheet = rb.sheet_by_index(0)
        sheet.cell_value(0, 0)
        p=int(sheet.row_values(member)[4])
        wb=copy(rb)
        w_sheet=wb.get_sheet(0)
        w_sheet.write(member,4,p+1)
        wb.save("all_information.xls")
        await cl.send_message(admin,"✅پیام مورد نظر در دسته پیام های برتر قرار گرفت💯")
#------------------------------------------------------------------users
def numb():
    wb = xlrd.open_workbook("all_information.xls")
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)
    x=0
    for i in range(sheet.nrows):
        x+=1
    return x

def change_and_save(list_par):
    workbook = xlsxwriter.Workbook('3_day.xls')
    worksheet = workbook.add_worksheet()
    wb = xlrd.open_workbook("all_information.xls")
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)
    ser=sheet.nrows+1
    for i in range(ser):
        if ser==i+1:
            p=list_par
        else:
            p=sheet.row_values(i)
        c=i+1
        worksheet.write(f'A{c}',p[0])
        worksheet.write(f'B{c}',p[1])
        worksheet.write(f'C{c}',p[2])
        worksheet.write(f'D{c}',p[3])
        worksheet.write(f'E{c}',p[4])
        worksheet.write(f'F{c}',p[5])
    workbook.close()

@app.on_message(filters.private & filters.command("start","/"))
async def start_user(c,m):
    await m.reply("🤖سلام خوش آمدید\nاین ربات در جهت پیشرفت و آبادانی « کهن دیار ازغند » طراحی شده است. \n☑️ امید داریم با ارتباط بیشتر از این مسیر وارسال نظرات و انتقادات و پیشنهادات شما به پیشرفت هر چه بهتر دیارمان فزونی بخشیم🌺🙏")
    s=1
    try:
        list_us=open("all_users.txt","r",encoding="UTF-8").read().split()
        if str(m.chat.id) in list_us:
            s=0
    except:
        pass
    if s:
        file=open("all_users.txt","a",encoding="UTF-8")
        file.write(f"{m.chat.id} ")
        file.close()
        one="1️⃣ اگر شما دهیار روستا بودید چه اقداماتی را در راستای پیشرفت و آبادانی روستا انجام می‌دادید؟"
        two="2️⃣ لطفا بزرگترین پتانسیل روستا را در چند خط توضیح بدهید."
        three="3️⃣ انتظارات خود از دهیاری را بیان کنید."
        await m.reply("✅📋لطفا اول به سه سوال زیر پاسخ دهید. ")
        soal1=await c.ask(m.chat.id,one)
        soal2=await c.ask(m.chat.id,two)
        soal3=await c.ask(m.chat.id,three)
        await m.reply("✅ پاسخ های شما ثبت شد.\n💥شما به منو اصلی هدایت میشوید\nهمچنین میتوانید با **📝ثبت نام و ورود** و ارسال طرح و پیشنهادات خود که به پیشرفت روستا کمک کند در **🔶قرعه کشی بهترین نظرات و پیشنهادات** شرکت کرده و به** 💎قید قرعه برنده 🏆جوایز نفیس** باشید.",reply_markup=keyboard_user_not_logined)
        await c.send_message(admin,f"‼پاسخ به نظر سنجی اولیه👁‍🗨\n**{one}**\n{soal1.text}\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n**{two}**\n{soal2.text}\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n**{three}**\n{soal3.text}")
    else:
        await m.reply("❇🖋شما قبلا به سه سوال پاسخ داده اید.\n💥به منو اصلی هدایت میشوید\nمچنین میتوانید با **📝ثبت نام و ورود** و ارسال طرح و پیشنهادات خود که به پیشرفت روستا کمک کند در **🔶قرعه کشی بهترین نظرات و پیشنهادات** شرکت کرده و به** 💎قید قرعه برنده 🏆جوایز نفیس** باشید.",reply_markup=keyboard_user)

@app.on_message(filters.private & filters.regex("^📄گزارشکار پروژه های در حال اجرا ⛓$"))
async def running_project(c,m):
    await m.reply("‼️ این بخش بدلیل توسعه و طراحی ربات در حال حاضر در دسترس نیست ❌\n\n📣 در صورت در دسترس قرار گرفتن این بخش به شما اطلاع رسانی خواهد شد.")
@app.on_message(filters.private & filters.regex("^🖋ثبت طرح📝$"))
async def comit_plan(c,m):
    x=exist_number(m.chat.id)
    tim=jdatetime.date.today().strftime("%d-%m-%Y")
    if x!=-1:
        wb = xlrd.open_workbook("all_information.xls")
        sheet = wb.sheet_by_index(0)
        sheet.cell_value(0, 0)
        information=sheet.row_values(x)
        await m.reply(f"🤖سلام **{information[0]}** عزیز🖐\n🥳 به بخش پیشنهاد طرح خوش آمدید\n",reply_markup=keyboard_kansel)
        tarh=await c.ask(m.chat.id,"‼لطفا طرح پیشنهادی خود را با ما در میان بگذارید🗨")
        if tarh.text=="لغو عملیات":
            await m.reply("✅به منو قبل باز میگردید",reply_markup=keyboard_user)
        else:
            messages=f"❇طرح از طرف **{information[0]}**\n📞به شماره **{information[2]}**\n🗓در تاریخ: **{tim}**\n📃شرح طرح:\n**{tarh.text}**"
            await c.send_message(admin,messages,reply_markup=InlineKeyboardMarkup(
            [
                [  # First row
                    InlineKeyboardButton(  # Generates a callback query when pressed
                        "📩ذخیره",
                        callback_data=f"zakhir{m.chat.id}"
                    )
                ],[  # First row
                    InlineKeyboardButton(  # Generates a callback query when pressed
                        "🎖طرح برتر",
                        callback_data=f"bartar{m.chat.id}"
                    )
                ]
            ]
            ))
            await m.reply("✅طرح شما ثبت شد.\n🙏از شما ممنونیم برای وقتی که گذاشتید🙌\nدر نظر داشته باشید که به **💥بهترین طرح ها💥** به قید قرعه جوایز نفیسی اهدا میگردد.",reply_markup=keyboard_user)
            
    else:
        await m.reply("🤖سلام کاربر ناشناس \nبه بخش پیشنهاد طرح خوش آمدید🖐\n",reply_markup=keyboard_kansel)
        tarh=await c.ask(m.chat.id,"‼لطفا طرح پیشنهادی خود را با ما در میان بگذارید🗨")
        if tarh.text=="لغو عملیات":
            await m.reply("✅به منو قبل باز میگردید",reply_markup=keyboard_user)
        else:
            messages=f"🔴طرح از طرف کاربر **ناشناس** میباشد.\n🗓در تاریخ: **{tim}**\n📃شرح طرح:\n**{tarh.text}**"
            await m.reply("✅طرح شما ثبت شد.\n🙏ممنونیم از شما کاربر ناشناس عزیز برای وقتی که گذاشتید🙌\nهمچنین میتوانید با **📝ثبت نام و ورود** و ارسال طرح و پیشنهادات خود که به پیشرفت روستا کمک کند در **🔶قرعه کشی بهترین نظرات و پیشنهادات** شرکت کرده و به** 💎قید قرعه برنده 🏆جوایز نفیس** باشید.",reply_markup=keyboard_user)
            await c.send_message(admin,messages)

@app.on_message(filters.private & filters.regex("^📝ثبت پیشنهادات و انتقادات$"))
async def comit_p_or_a(c,m):
    x=exist_number(m.chat.id)
    tim=jdatetime.date.today().strftime("%d-%m-%Y")
    if x!=-1:
        wb = xlrd.open_workbook("all_information.xls")
        sheet = wb.sheet_by_index(0)
        sheet.cell_value(0, 0)
        information=sheet.row_values(x)
        await m.reply(f"🤖سلام **{information[0]}** عزیز🖐\n ✳💠به بخش پیشنهادات و انتقادات خوش آمدید",reply_markup=keyboard_kansel)
        tarh=await c.ask(m.chat.id,"▪ لطفا پیشنهاد یا انتقاد خود را با ما در میان بگذارید⁉")
        if tarh.text=="لغو عملیات":
            await m.reply("✅به منو قبل باز میگردید",reply_markup=keyboard_user)
        else:
            messages=f"📑پیشنهاد یا انتقاد از طرف **{information[0]}**\n📞به شماره:** {information[2]}**\n📅در تاریخ: **{tim}**\n📝شرح پیشنهاد یا انتقاد: \n**{tarh.text}**"
            await m.reply("✅انتقاد یا پیشنهاد شما ثبت شد.\n🙏از شما به خاطر اینکه به فکر دیار خود هستید متشکریم🙌\n✳با ثبت بهترین پیشنهاد در قرعه کشی شرکت و برنده 🏆جوایز نفیس شوید.",reply_markup=keyboard_user)
            await c.send_message(admin,messages,reply_markup=InlineKeyboardMarkup(
            [
                [  # First row
                    InlineKeyboardButton(  # Generates a callback query when pressed
                        "📩ذخیره",
                        callback_data=f"zakhir{m.chat.id}"
                    )
                ],[  # First row
                    InlineKeyboardButton(  # Generates a callback query when pressed
                        "🎖انتقاد یا پیشنهاد برتر",
                        callback_data=f"bartar{m.chat.id}"
                    )
                ]
            ]
            ))
    else:
        await m.reply("🤖سلام کاربر **ناشناس** \n✳به بخش پیشنهادات و انتقادات خوش آمدید🖐",reply_markup=keyboard_kansel)
        tarh=await c.ask(m.chat.id,"▪ لطفا پیشنهاد یا انتقاد خود را با ما در میان بگذارید⁉")
        if tarh.text=="لغو عملیات":
            await m.reply("✅به منو قبل باز میگردید",reply_markup=keyboard_user)
        else:
            
            messages=f"🔴پیشنهاد یا انتقاد از طرف کاربر **ناشناس** میباشد.\n📅در تاریخ: **{tim}**\n📝شرح پیشنهاد یا انتقاد:\n** {tarh.text}**"
            await m.reply("✅انتقاد یا پیشنهاد شما ثبت شد.\n🙏از اینکه به فکر دیار خود هستید متشکریم🙌\nهمچنین میتوانید با **📝ثبت نام و ورود** و ارسال طرح و پیشنهادات خود که به پیشرفت روستا کمک کند در **🔶قرعه کشی بهترین نظرات و پیشنهادات** شرکت کرده و به** 💎قید قرعه برنده 🏆جوایز نفیس** باشید.",reply_markup=keyboard_user)
            await c.send_message(admin,messages)
    
@app.on_message(filters.private & filters.regex("^🦹‍♂️ادامه در حالت ناشناس$"))
async def unknown(c,m):
    if exist_number(m.chat.id)==-1:
        await m.reply("🤖به بخش ناشناس خوش امدید.\n💥 بدون هیچ هویت انتقادات و پیشنهادات و طرح های مدنظر خود را با ما در میان بگذارید🙌",reply_markup=keyboard_user)
    else:
        await m.reply("✅این شماره قبلا وارد شده و امکان ارسال پیام ❌ناشناس برای این اکانت وجود ندارد.\n 💥به منو اصلی هدایت میشوید.",reply_markup=keyboard_user)

@app.on_message(filters.private & filters.regex("^🔙برگشت به منو اصلی$"))
async def back_to_main(c,m):
    await m.reply("✅به منو اصلی بازگشتید.",reply_markup=keyboard_user_not_logined)
@app.on_message(filters.private & filters.regex("^📝ثبت نام و ورود$"))
async def login(c,m):
    name=await c.ask(m.chat.id,"**📝✏️نام و نام خانوادگی خود را وارد کنید:**", reply_markup=keyboard_kansel,parse_mode="Markdown")
    if name.text!="لغو عملیات":
        if not( name.text in list_regex):
            number=await c.ask(m.chat.id,"**شماره خود را وارد کنید📞:**",parse_mode="Markdown")
            if number.text=="لغو عملیات":
                await m.reply("✅به منوی اصلی بازگشتید.",reply_markup=keyboard_user_not_logined)
            else:
                sw=1
                x=1
                while x:
                    try:
                        s=int(number.text)
                        x=0
                    except:
                        number=await c.ask(m.chat.id,"❌خطایی رخ داده است لطفا به صورت صحیح شماره خود را وارد کنید:",parse_mode="Markdown") 
                        if number.text=="لغو عملیات":
                            await m.reply("✅به منوی اصلی بازگشتید.",reply_markup=keyboard_user_not_logined)
                            sw=0
                            x=0
                if sw:
                    father_name=await c.ask(m.chat.id ,"**🖋نام پدر خود را وارد کنید**:",parse_mode="Markdown")
                    if father_name.text=="لغو عملیات":
                        await m.reply("✅به منوی اصلی بازگشتید.",reply_markup=keyboard_user_not_logined)
                    else:
                        tim=jdatetime.date.today().strftime("%d-%m-%Y")
                        p=[f"{name.text}",f"{tim}",f"{number.text}",f"{father_name.text}",0,f"{m.chat.id}"]
                        row=exist_number(number.text)
                        sheet=exist_number(m.chat.id)
                        if row!=-1 :
                            await m.reply("❌این شماره قبلا وارد شده است.\n💥به منو اصلی هدایت میشوید." , reply_markup=keyboard_user)
                        elif sheet!=-1:
                            await m.reply("❌این اکانت قبلا وارد شده است.\n💥به منو اصلی هدایت میشوید." , reply_markup=keyboard_user)
                        else:
                            change_and_save(p)
                            await m.reply("✅ اطلاعات شما ثبت شد",reply_markup=keyboard_user)
                            os.remove("all_information.xls")
                            os.rename("3_day.xls","all_information.xls")
                else:
                    pass
        else:
            await m.reply("❌نام وارد شده اشتباه است.\n💥به منو بر میگردید\n 🙂لطفا مجدد تلاش کنید",reply_markup=keyboard_user_not_logined)
    else:
        await m.reply("✅به منوی اصلی بازگشتید.",reply_markup=keyboard_user_not_logined)
        
app.run()
