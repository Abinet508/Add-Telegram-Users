from telethon import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser, InputPeerUserFromMessage
from telethon.errors.rpcerrorlist import (PeerFloodError, UserNotMutualContactError ,
                                          UserPrivacyRestrictedError, UserChannelsTooMuchError,
                                          UserBotError, InputUserDeactivatedError)
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.channels import LeaveChannelRequest
import time, os, sys, json
import  csv



re = "\u001b[31;1m"
gr = "\u001b[32m"
ye = "\u001b[33;1m"

    
if sys.version_info[0] < 3:
    telet = lambda :os.system('pip install -U telethon')
elif sys.version_info[0] >= 3:
    telet = lambda :os.system('pip3 install -U telethon')

telet()
time.sleep(1)

path=os.path.dirname(__file__)

with open('members.json', 'r') as r:
                users = json.load(r)      

def JsonReader(filename,Environment):
    with open('{}\\{}'.format(path,filename))as f:
        data = json.load(f)
        for First in data:
            if Environment in First:
                        return (First[Environment])
                    
async def main(client:TelegramClient,SessionCounter):
        try:    
                if(not client.is_connected()):
                        await client.connect()
                def check(username):
                    datafile=open('MemberError.txt','r')
                    found=False
                    for line in datafile:
                        if username in line:
                            found=True
                        else:
                            found=False     
                    return found   
                # To Add Members.......
                async def getmem():
                      
                    countrollback=1
                    boolrollback=False  
                    outputval=[]
                    a=0
                    opt1=[]
                    opt1.append(0)
                    if len(channel)>2:
                        opt1.clear()
                        for i in channel:
                            #print(gr+'['+str(a)+']', i.title)
                            a += 1
                        opt1.append(int(input(ye+'Enter a number: ')))
                    elif len(channel)==2:
                        opt1.clear()
                        opt1.append(1)
                    try:    
                        my_participants = await client.get_participants(channel[opt1[0]])
                        target_group_entity = InputPeerChannel(channel[opt1[0]].id, channel[opt1[0]].access_hash)
                    except:
                        my_participants = await client.get_participants(channel[0])
                        target_group_entity = InputPeerChannel(channel[0].id, channel[0].access_hash)    
                    my_participants_id = []
                    for my_participant in my_participants:
                        my_participants_id.append(my_participant.id)
                    
                    filemycount = open("userid.txt","r")  
                    count = 1
                    countmy = 1
                    row=filemycount.readlines()
                    i = 0
                    for user in users:  
                     if int(row[0])>=countmy :
                    
                            ##print(str(countmy)+" "+user['username'])
                            countmy +=1
                            continue
                     elif check(user['username']) or user['username']=="":
                       
                          #print(re+"black-listed user passing") 
                          if os.path.isfile('userid.txt'):
                                file1 = open("userid.txt","w")
                                file1.writelines(str(countmy))
                                #file1.writelines()
                                file1.close() 
                          countmy +=1
                          continue                                           
                      
                     elif user['uid'] in my_participants_id:
                           # #print(gr+'User present. Skipping.')
                            f = open('MemberError.txt','a')
                            f.writelines(str(user['username'])+"\n")
                            ##print(r" added to blacklist numbers")
                            f.close() 
                            if os.path.isfile('userid.txt'):
                                file1 = open("userid.txt","w")
                                file1.writelines(str(countmy))
                                #file1.writelines()
                                file1.close() 
                
                            countmy+=1
                            #outputval.append(user['uid'])
                            continue  
                        ##print("checking") 
                     elif  count%5==0:
                            #clear()
                            ##print(colorText(wt))
                            #print('')
                            #print('')
                            print(ye+"Limit reached for Session "+str(SessionCounter)+" please wait for 1 minute...")
                            await client.disconnect()
                            return True
                                    
                            #time.sleep(60)
                            #await client.disconnect()
                            #break
                     elif count >= 300:
                            await client.disconnect()
                           
                            break
                     elif i >= 8:
                            if boolrollback:
                                  if os.path.isfile('userid.txt'):
                                            file1 = open("userid.txt","w")
                                            file1.writelines(str(countmy-countrollback))
                                            file1.close()  
                            await client.disconnect()
                           
                            break  
                        
                        #time.sleep(1)
                     else:
                            try:
                                    
                                    #user_to_add = InputPeerUser(int(user['uid']), int(user['access_hash']))
                                    user_to_add = await client.get_input_entity(user['username'])
                                    #add=  client(InviteToChannelRequest(target_group_entity, [user_to_add]))
                                    #user_to_add =  InputPeerUser(int(user['uid']), int(user['access_hash']))
                                    add = await client(InviteToChannelRequest(target_group_entity,[user_to_add]))
                                    #print(gr+'Added ', str(user['username']))
                                    time.sleep(4)
                                    if boolrollback==True:
                                        countrollback+=1  
                                        #print(countrollback)
                                    #time.sleep(1)
                                    if os.path.isfile('userid.txt'):
                                        file1 = open("userid.txt","w")
                                        file1.write(str(countmy))
                                        #file1.writelines()
                                        file1.close() 
                                    i=0
                                    count+=1
                                    countmy+=1
                                    #time.sleep(1)
                                    ##print("moving")    
                                
                            except PeerFloodError:
                            
                                print(re+"Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
                            
                                i += 1
                                await client.disconnect()
                                return False
                            
                            except UserPrivacyRestrictedError:
                                #outputval.append(user['uid'])
                               
                                if os.path.isfile('userid.txt'):
                                            file1 = open("userid.txt","w")
                                            file1.writelines(str(countmy))
                                            #file1.writelines()
                                            file1.close() 
                               
                                countmy+=1
                                
                               # continue
                                #print(re+"The user's privacy settings do not allow you to do this. Skipping.")
                                f = open('MemberError.txt','a')
                                f.writelines(str(user['username'])+"\n")
                                f.close() 
                                i = 0
                            except UserBotError:
                                if os.path.isfile('userid.txt'):
                                            file1 = open("userid.txt","w")
                                            file1.write(str(countmy))
                                            #file1.writelines()
                                            file1.close() 
                                 
                                countmy+=1
                                f = open('MemberError.txt','a')
                                f.writelines(str(user['username'])+"\n")
                             #   #print(re+" added to blacklist numbers")
                                f.close() 
                                #print(re+"Can't add Bot. Skipping.")
                                i = 0
                            except InputUserDeactivatedError:
                           
                                if os.path.isfile('userid.txt'):
                                            file1 = open("userid.txt","w")
                                            file1.writelines(str(countmy))
                                            #file1.writelines()
                                            file1.close() 
                                            countmy+=1 
                             
                                #print(re+"The specified user was deleted. Skipping.")
                                f = open('MemberError.txt','a')
                                f.writelines(str(user['username'])+"\n")
                               # #print(re+" added to blacklist numbers")
                                f.close() 
                                
                                i = 0
                            except UserChannelsTooMuchError:
                                    if os.path.isfile('userid.txt'):
                                            file1 = open("userid.txt","w")
                                            file1.writelines(str(countmy))
                                            #file1.writelines()
                                            file1.close() 
                                            countmy+=1
                               
                                    #print(re+"User in too much channel. Skipping.")
                                    f = open('MemberError.txt','a')
                                    f.writelines(str(user['username'])+"\n")
                                 #   #print(re+" added to blacklist numbers")
                                    f.close() 
                                   
                            except UserNotMutualContactError:
                                    if os.path.isfile('userid.txt'):
                                            file1 = open("userid.txt","w")
                                            file1.writelines(str(countmy))
                                            #file1.writelines()
                                            file1.close() 
                                            countmy+=1
                              
                                
                                    #print(re+'Mutual No. Skipped.')
                                    f = open('MemberError.txt','a')
                                    f.writelines(str(user['username'])+"\n")
                                   # #print(r" added to blacklist numbers")
                                    f.close() 
                                    
                                    i = 0
                            except Exception as e:
                                #print(re+"Error:", e)
                                boolrollback=True
                        
                                #print("Trying to continue...")
                                i += 1
                                continue
                            #end
               
                print(gr+"Logged in with session :newsession"+str(SessionCounter))   
                ##print(colorText(wt))
                chats = []
                channel = []
                result = await client(GetDialogsRequest(
                    offset_date=None,
                    offset_id=0,
                    offset_peer=InputPeerEmpty(),
                    limit=200,
                    hash=0
                ))
               
                chats.extend(result.chats)
                for a in chats:
                    try:
                        if a.title=="Telegram_Testing":
                            channel.append(a)
                    except:
                        continue
                
                await getmem()
                    
                    #sys.exit()
        except Exception as e:
            #print(e)
            return False  
MyList=[]            
for x in os.listdir("{}\\Sessions".format(path)):
    if x.endswith(".session"):
        MyList.append(int(x.split("newsession")[1].split(".session")[0].strip()))  
MyList=sorted(MyList)
#print(MyList) 
for sessionid in MyList:
    ##print(sessionid)                 
    New_API_Detail=JsonReader("getmem_log.json",'newsession{}'.format(sessionid)) 
    #print(New_API_Detail)   
    client = TelegramClient('Sessions\\newsession'+str(sessionid), New_API_Detail["api_id"], New_API_Detail["api_hash"])     
    ##print(sessionid)
    client.loop.run_until_complete(main(client,sessionid))
         
time.sleep(5)    
          