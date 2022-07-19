import discord
import requests
import json

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
TOKEN = 'TOOOOOOOOOOOKEN'

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if client.user in message.mentions:
        await message.channel.send("逆翻訳します。")
        api_url = "https://script.google.com/macros/s/AKfycbwINFoYS0KfVRc_snYCRVGW9EdE56hCNgr1GQ4Vi--l3zH8U-c/exec"

        def trans(data, s_lang , t_lang):
            params = {
            'text': data,
            'source': s_lang,
            'target': t_lang
            }

            r_data = requests.post(api_url, data=params)
            j_data = json.loads(str(r_data.text))
            
            return j_data["text"]

        mess = message.content.replace('<@965087223840137246>', '')
        print(mess)
        trans_data = mess
        print("入れたよ")
        trans_data = trans(trans_data,"ja" , "am")
        trans_data = trans(trans_data,"am" , "ja")
        trans_data = trans(trans_data,"ja" , "lo")
        trans_data = trans(trans_data,"lo" , "am")
        trans_data = trans(trans_data,"am" , "lo")
        trans_data = trans(trans_data,"lo" , "ja")

        await message.channel.send(mess + " \n ⇓ \n " + trans_data)
        
    
client.run(TOKEN)
