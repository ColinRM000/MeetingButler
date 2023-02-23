# PACKAGE
import discord, json, random, asyncio
from discord.utils import get
from discord.ext.commands import has_permissions, CheckFailure
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType
from discord_components import DiscordComponents, ComponentsBot, Button, SelectOption, Select, ButtonStyle
from discord.ext import tasks
#####################################################

with open("config.json", "r", encoding="utf-8") as file:
    config = json.load(file) # CONFIG.JSON

intents = discord.Intents.default()
client = commands.Bot(command_prefix=config['bot']['prefix'], intents=intents, case_insensitive=False) 
intents.members = True 
DiscordComponents(client) 
client.remove_command('help') 

CHNAME = ["124xr23", "142rxfty", "qrq43ty", "qt12td", "1323r2", "t25321", "q35q2", "sf341", "qegi43", "q5tg0", "rqr245", "atgwer2", "q5r349f", "wer4521", "afgxb23", "45thre3", "isgk34", "ko3452", "ostti75", "wgort98", "afat452", "aafgqr54", "qfesafg3", "aftq3", "ghi315", "sggi634", "aga856", "wwrsg34", "psro32", "sgg075", "TdSae174", "qgsg2", "gtwtq54", "otk435", "agto346", "ageir2", "25dwrwt", "agaer35", "sgorwr532", "qgwer4", "lkrr24", "geeri2", "2g26s", "atgi34", "sgo345", "germt4", "ari53", "j3r55", "hw351", "kwsg23", "oertj42", "gshi35", "pwtw66", "gwti53", "srfwr5", "hjsg43", "sgoiw753", "age34is", "qgi35", "qgew245", "ag3412", "wtw46"]
CHNAMEE = random.choice(CHNAME)

#START UP

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Prefix:'!', Developed by Pablo"))
    print(f"{client.user.name} is online.")
    print("[!] CONSOLE LOG:")

@client.command()
@commands.has_any_role('ADMIN')
async def clean(ctx, limit: int):
    await ctx.channel.purge(limit=limit, check=lambda msg: not msg.pinned)

@client.command()               # INTERVIEW BUTTON
@commands.has_any_role('ADMIN', '📧│Transfer Team')
async def interview(ctx):
    clear = client.get_channel(954261911678099537)
    await clear.purge(limit=1, check=lambda msg: not msg.pinned)
    embed = discord.Embed(title="⛓️**Interview Panel**⛓️", colour= 0x9b15d4)
    embed.set_thumbnail(url="https://i.imgur.com/ABj9N0O.png")
    embed.add_field(name="Click the button below to open a interview room with the transfer team for server 1636!", value="🛎", inline=False)
    embed.set_footer(text="Powered by https://crm-bots.com / Pablo")
    await ctx.send(embed=embed, components = [
        [Button(label="Start interview", style="1", emoji = "📧", custom_id="interview")]
        ])
    while True:   
        interaction = await client.wait_for("button_click") 
        if interaction.component.label == "Start interview":
            exist = discord.utils.get(ctx.guild.text_channels, name=f"{interaction.author.name.lower()}")
            if exist:
                embed = discord.Embed(title="Warning:", colour= 0xff00ea)
                embed.add_field(name="You already have a open room!", value=":warning:", inline=False)
                embed.set_thumbnail(url="https://i.imgur.com/UMo5pIR.png")
                await interaction.send(embed=embed)
            else:
                clear = client.get_channel(954261911678099537)
                name = 'Interviews Chat'
                category = discord.utils.get(ctx.guild.categories, name=name)
                name2 = 'Interviews Voice'
                category2 = discord.utils.get(ctx.guild.categories, name=name2)
                channel3 = client.get_channel(954048535018504202)
                CHN = f"{interaction.author.name.lower()}"
                CHN2 = f"VC-{interaction.author.name.lower()}"
                guild = ctx.guild
                member = interaction.user
                admin_role = get(guild.roles, name="📧│Transfer Team")
                overwrites = {
                    guild.default_role: discord.PermissionOverwrite(read_messages=False),
                    member: discord.PermissionOverwrite(read_messages=True),
                    admin_role: discord.PermissionOverwrite(read_messages=True)
                }
                description = '''
                Please tell us what brings you here, what server you are coming from, as well a screenshot of your Main Hero's/Battle report, stats/Main March, and comps/tree/equipment.
                
                We will get back to you soon!
                '''
                channel = await guild.create_text_channel(CHN, category=category, overwrites=overwrites)
                channel2 = await guild.create_voice_channel(CHN2, category=category2, overwrites=overwrites)
                alert2 = discord.Embed(title=f"📌 Interview Alert:", description=f"{interaction.author.name} opened a new ticket!", colour= 0x00ff48)
                alert2.set_author(name=interaction.user, icon_url=interaction.author.avatar_url)
                alert2.set_thumbnail(url="https://i.imgur.com/UMo5pIR.png")
                await channel3.send(embed=alert2)
                embed = discord.Embed(title="Success!", colour= 0xff00ea)
                embed.add_field(name=f"Your interview room was created! {interaction.user}", value=":white_check_mark:", inline=False)
                await interaction.send(embed=embed)
                embed = discord.Embed(title=f"**Hello, how are you dear?**", colour= 0x9b15d4)
                embed.add_field(name= description, value="🤝", inline=False)
                embed.set_thumbnail(url="https://i.imgur.com/XEYbe30.png")
                embed.set_footer(text="Powered by https://crm-bots.com / Pablo")
                await channel.send(embed=embed)
                
@interview.error
async def command_name_error(ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            clear = client.get_channel(954261911678099537)
            await clear.purge(limit=1, check=lambda msg: not msg.pinned)
            embed = discord.Embed(title="Warning:", colour= 0xff00ea)
            embed.add_field(name="You are on cooldown from using this command, please wait!", value=":warning:", inline=False)
            embed.set_thumbnail(url="https://i.imgur.com/UMo5pIR.png")
            embed.set_author(name=ctx.message.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed, delete_after=10)

@client.command()
@commands.has_any_role('ADMIN', '📧│Transfer Team')
async def tools(ctx):
    await ctx.channel.purge(limit=1)
    channel = ctx.channel
    embed = discord.Embed(title="**Admin Tools:**", colour= 0xff00ea)
    embed.set_thumbnail(url="https://i.imgur.com/UMo5pIR.png")
    embed.add_field(name="Choose your option.", value="👮", inline=False)
    await ctx.send(embed=embed, components = [
        [Button(label="Export Chat", style="4", emoji = "📜", custom_id="export"), Button(label="Archive", style="4", emoji = "📥", custom_id="archive"), Button(label="Close Room", style="4", emoji = "⛔", custom_id="fclose")]
        ])
    while True:
        interaction = await client.wait_for("button_click") 
        if interaction.component.label == "Export Chat":
                await ctx.channel.purge(limit=1)
                channel3 = client.get_channel(954048535018504202)
                CHH = client.get_channel(954618055634321498)
                messages = await ctx.channel.history(limit=None).flatten()
                file = open(f"{ctx.channel.name}.txt", "a")
                for i in messages:
                    file.write(f'{i.author} | {i.content} \n')
                file.close()
                await CHH.send(file=discord.File(f'{ctx.channel.name}.txt'))
                alert = discord.Embed(title=f"{ctx.message.author}:", description=f"The chat has been exported!", colour= 0x00ff48)
                alert.set_thumbnail(url="https://i.imgur.com/UMo5pIR.png")
                await interaction.send(embed=alert)
                alert2 = discord.Embed(title=f"👮 Admin Alert:", description=f"{interaction.author.name} exported the chat from #{ctx.channel.name}!", colour= 0xd100ab)
                alert2.set_author(name=interaction.user, icon_url=interaction.author.avatar_url)
                alert2.set_thumbnail(url="https://i.imgur.com/UMo5pIR.png")
                await channel3.send(embed=alert2)
        if interaction.component.label == "Archive":
            guild = ctx.guild
            channel3 = client.get_channel(954048535018504202)
            channel = discord.utils.get(guild.channels, name=f"{ctx.channel.name}")
            cat = discord.utils.get(guild.categories, name="Archive")
            vchannel = discord.utils.get(guild.channels, name=f"VC-{ctx.channel.name}")
            await ctx.channel.purge(limit=1)
            embed = discord.Embed(title="Success!", colour= 0x00ff48)
            embed.add_field(name="The room has been archived.", value=":white_check_mark:", inline=False)
            await interaction.send(embed=embed)
            alert2 = discord.Embed(title=f"👮 Admin Alert:", description=f"{interaction.author.name} archived the chat #{ctx.channel.name}!", colour= 0xd100ab)
            alert2.set_author(name=interaction.user, icon_url=interaction.author.avatar_url)
            alert2.set_thumbnail(url="https://i.imgur.com/UMo5pIR.png")
            await channel3.send(embed=alert2)
            await vchannel.delete()
            await channel.edit(category=cat)
        if interaction.component.label == "Close Room":
            guild = ctx.guild
            channel3 = client.get_channel(954048535018504202)
            channel = discord.utils.get(guild.channels, name=f"{ctx.channel.name}")
            vchannel = discord.utils.get(guild.channels, name=f"VC-{ctx.channel.name}")
            await ctx.channel.purge(limit=1)
            embed = discord.Embed(title="Closing!", colour= 0xff00ea)
            embed.add_field(name="The interview room will close in 5 seconds.", value=":white_check_mark:", inline=False)
            await interaction.send(embed=embed)
            alert2 = discord.Embed(title=f"👮 Admin Alert:", description=f"{interaction.author.name} closed the room #{ctx.channel.name}!", colour= 0xd100ab)
            alert2.set_author(name=interaction.user, icon_url=interaction.author.avatar_url)
            alert2.set_thumbnail(url="https://i.imgur.com/UMo5pIR.png")
            await channel3.send(embed=alert2)
            await asyncio.sleep(5)
            await vchannel.delete()
            await channel.delete()

@client.command()
@commands.has_any_role('ADMIN', '📧│Transfer Team')
async def approve(ctx, user: discord.Member):
    await ctx.channel.purge(limit=1)
    channel3 = client.get_channel(954048535018504202)
    role = discord.utils.get(ctx.guild.roles, name="ACCEPTED")
    await user.add_roles(role)
    embed = discord.Embed(title=f"Approved:", description=f"Congrats! @{user}, your transfer request has been approved! ✅", colour= 0x00ff48)
    embed.set_thumbnail(url="https://i.imgur.com/UMo5pIR.png")
    embed.set_footer(text="Powered by https://crm-bots.com / Pablo")
    await ctx.send(embed=embed)
    alert2 = discord.Embed(title=f"👮 Admin Alert:", description=f"{ctx.message.author} approved {ctx.channel.name}'s transfer request!", colour= 0xd100ab)
    alert2.set_author(name= ctx.author.name, icon_url=ctx.author.avatar_url)
    alert2.set_thumbnail(url="https://i.imgur.com/UMo5pIR.png")
    await channel3.send(embed=alert2)

@client.command()
@commands.has_any_role('ADMIN', '📧│Transfer Team')
async def deny(ctx, user: discord.Member):
    await ctx.channel.purge(limit=1)
    channel3 = client.get_channel(954048535018504202)
    role = discord.utils.get(ctx.guild.roles, name="Denied")
    await user.add_roles(role)
    embed = discord.Embed(title=f"Denied:", description=f"We are sorry @{user}! Your transfer request has been denied! ❌", colour= 0xff0000)
    embed.set_thumbnail(url="https://i.imgur.com/UMo5pIR.png")
    embed.set_footer(text="Powered by https://crm-bots.com / Pablo")
    await ctx.send(embed=embed)
    alert2 = discord.Embed(title=f"👮 Admin Alert:", description=f"{ctx.message.author} denied {ctx.channel.name}'s transfer request!", colour= 0xd100ab)
    alert2.set_author(name= ctx.author.name, icon_url=ctx.author.avatar_url)
    alert2.set_thumbnail(url="https://i.imgur.com/UMo5pIR.png")
    await channel3.send(embed=alert2)
        

client.run(config['bot']['token'])