from pyrogram import Client, filters
from pyrogram.enums import ParseMode
import datetime
import time
from database.users_chats_db import db
from info import ADMINS
from utils import broadcast_messages # ആവശ്യമെങ്കിൽ നിലനിർത്താം, പക്ഷെ ഇവിടെ നമ്മൾ നേരിട്ടാണ് അയക്കുന്നത്
import asyncio
from pyrogram.errors import FloodWait, ChatAdminRequired, ChatWriteForbidden

@Client.on_message(filters.command("broadcast") & filters.user(ADMINS) & filters.reply)
async def verupikkals(bot, message):
    users = await db.get_all_users()
    b_msg = message.reply_to_message
    
    sts = await message.reply_text(
        text='Broadcasting personalized messages to Users...'
    )
    
    start_time = time.time()
    total_users = await db.total_users_count()
    done = 0
    blocked = 0
    deleted = 0
    failed = 0
    success = 0

    for user in users:
        user_id = int(user['id'])
        u_name = user.get('username')
        first_name = user.get('name', 'User')
        
        if u_name:
            mention = f"@{u_name}"
        else:
            mention = f'<a href="tg://user?id={user_id}">{first_name}</a>'

        original_text = b_msg.caption if b_msg.caption else (b_msg.text if b_msg.text else "")
        
        if original_text:
            personalized_text = f"{mention}\n\n{original_text}"
        else:
            personalized_text = f"{mention}"

        reply_markup = b_msg.reply_markup

        try:
            if b_msg.photo:
                await bot.send_photo(chat_id=user_id, photo=b_msg.photo.file_id, caption=personalized_text, parse_mode=ParseMode.HTML, reply_markup=reply_markup)
            elif b_msg.video:
                await bot.send_video(chat_id=user_id, video=b_msg.video.file_id, caption=personalized_text, parse_mode=ParseMode.HTML, reply_markup=reply_markup)
            elif b_msg.document:
                await bot.send_document(chat_id=user_id, document=b_msg.document.file_id, caption=personalized_text, parse_mode=ParseMode.HTML, reply_markup=reply_markup)
            elif b_msg.audio:
                await bot.send_audio(chat_id=user_id, audio=b_msg.audio.file_id, caption=personalized_text, parse_mode=ParseMode.HTML, reply_markup=reply_markup)
            else:
                await bot.send_message(chat_id=user_id, text=personalized_text, parse_mode=ParseMode.HTML, reply_markup=reply_markup, disable_web_page_preview=True)
            
            success += 1

        except FloodWait as e:
            await asyncio.sleep(e.value)
            try:
                if b_msg.photo: await bot.send_photo(chat_id=user_id, photo=b_msg.photo.file_id, caption=personalized_text, parse_mode=ParseMode.HTML, reply_markup=reply_markup)
                else: await bot.send_message(chat_id=user_id, text=personalized_text, parse_mode=ParseMode.HTML, reply_markup=reply_markup, disable_web_page_preview=True)
                success += 1
            except: failed += 1
        except Exception:
            failed += 1

        done += 1
        await asyncio.sleep(0.5) 
        
        if not done % 20:
            await sts.edit(f"Broadcast in progress:\n\nTotal Users {total_users}\nCompleted: {done} / {total_users}\nSuccess: {success}")    
            
    time_taken = datetime.timedelta(seconds=int(time.time()-start_time))
    await sts.edit(f"Broadcast Completed:\nCompleted in {time_taken} seconds.\n\nTotal Users {total_users}\nSuccess: {success}")


@Client.on_message(filters.command("grp_broadcast") & filters.user(ADMINS) & filters.reply)
async def grp_brodcst(bot, message):
    chats = await db.get_all_chats()
    b_msg = message.reply_to_message
    sts = await message.reply_text(
        text='Broadcasting your messages to groups...'
    )
    start_time = time.time()
    total_chats = await db.total_chat_count()
    done = 0
    failed = 0
    success = 0
    
    for chat in chats:
        chat_id = int(chat['id'])
        
        # ഗ്രൂപ്പിലെ എല്ലാവരുടെയും ശ്രദ്ധ കിട്ടാൻ വേണ്ടിയുള്ള ടാഗ് ലൈൻ മുകളിൽ ചേർക്കുന്നു
        group_mention = "📢 <b>Attention Everyone! / ശ്രദ്ധിക്കുക!</b> \n@admins"
        
        original_text = b_msg.caption if b_msg.caption else (b_msg.text if b_msg.text else "")
        
        if original_text:
            group_text = f"{group_mention}\n\n{original_text}"
        else:
            group_text = f"{group_mention}"
            
        reply_markup = b_msg.reply_markup

        try:
            # ഗ്രൂപ്പുകളിലേക്ക് ഫോട്ടോ/വീഡിയോ/ടെക്സ്റ്റ് നേരിട്ട് അയക്കുന്നു
            if b_msg.photo:
                await bot.send_photo(chat_id=chat_id, photo=b_msg.photo.file_id, caption=group_text, parse_mode=ParseMode.HTML, reply_markup=reply_markup)
            elif b_msg.video:
                await bot.send_video(chat_id=chat_id, video=b_msg.video.file_id, caption=group_text, parse_mode=ParseMode.HTML, reply_markup=reply_markup)
            elif b_msg.document:
                await bot.send_document(chat_id=chat_id, document=b_msg.document.file_id, caption=group_text, parse_mode=ParseMode.HTML, reply_markup=reply_markup)
            elif b_msg.audio:
                await bot.send_audio(chat_id=chat_id, audio=b_msg.audio.file_id, caption=group_text, parse_mode=ParseMode.HTML, reply_markup=reply_markup)
            else:
                await bot.send_message(chat_id=chat_id, text=group_text, parse_mode=ParseMode.HTML, reply_markup=reply_markup, disable_web_page_preview=True)
                
            success += 1
            
        except FloodWait as e:
            await asyncio.sleep(e.value)
            try:
                if b_msg.photo: await bot.send_photo(chat_id=chat_id, photo=b_msg.photo.file_id, caption=group_text, parse_mode=ParseMode.HTML, reply_markup=reply_markup)
                else: await bot.send_message(chat_id=chat_id, text=group_text, parse_mode=ParseMode.HTML, reply_markup=reply_markup, disable_web_page_preview=True)
                success += 1
            except: failed += 1
        except (ChatAdminRequired, ChatWriteForbidden):
            # ബോട്ടിന് മെസ്സേജ് അയക്കാൻ പെർമിഷൻ ഇല്ലാത്ത ഗ്രൂപ്പുകൾ ഒഴിവാക്കും
            failed += 1
        except Exception:
            failed += 1
            
        done += 1
        await asyncio.sleep(2) # ഗ്രൂപ്പുകളിൽ ഫ്ലഡ് വെയ്റ്റ് വരാതിരിക്കാൻ 2 സെക്കന്റ് ഗ്യാപ്പ് വേണം
        
        if not done % 20:
            await sts.edit(f"Group Broadcast in progress:\n\nTotal Chats {total_chats}\nCompleted: {done} / {total_chats}\nSuccess: {success}\nFailed: {failed}")    
            
    time_taken = datetime.timedelta(seconds=int(time.time()-start_time))
    await sts.edit(f"Group Broadcast Completed:\nCompleted in {time_taken} seconds.\n\nTotal Chats {total_chats}\nSuccess: {success}\nFailed: {failed}")