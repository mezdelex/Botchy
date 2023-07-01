"""Actions module"""
import discord

commands = ['!help', '!purge', '!frontline', '!dynamite', '!tierlist', '!fusion', '!wheel', '!sv', '!root', '!boss']

async def execute(message):
    """Execute bot actions"""
    if message.content.startswith(commands[0]):
        await message.channel.send(f'Available commands are: {", ".join(commands)}')

    if message.content.startswith(commands[1]):
        messages_to_delete = int(message.content.split()[1]) + 1
        messages = [message async for message in message.channel.history(limit=messages_to_delete)]
        await message.channel.delete_messages(messages)

    if message.content.startswith(commands[2]):
        embed = discord.Embed(title='Welcome to 🍑🍑🍑!', description=
        """Here in Peaches | Peachy | Peach we coordinate Frontline events using specific tags on Forts, Camps, and City Centers also called bases.  Understanding what these tags mean is vital to our combined success!  Tags are as follows:

        ENTRENCH: Place defenses here asap.

        COUNTERATTACK:  Let the enemy conquer  this base, and we will take it back once the protection ends. Don’t waste defensive lineups here.

        OBSERVE:  Take no action but watch carefully.  Usually used for bases where we may be attacked, but have sufficient defenses.

        WITHDRAW:  Do not place defenses/offenses here.  Tactical retreat.

        BOMBARD: Send your lineups to attack immediately. 

        BUZZER BEAT:  This is the most critical tag.  In Frontline, you have 6 minutes of immunity after capturing a base.  This tag means do NOT attack until 6 minutes are left for the daily battle to end.  Capturing a base within the last 6 minutes means no defenses are required to keep it!

        FEINT: When our opponent has many strong lineups set to defend a base we want to conquer, we attack early with a few lineups to defeat the majority of their defenses. We only dispatch a few, we never conquer immediately as we follow what’s written in buzzer beat. 

        Everyone who won’t be online during battle phase your duty is to ✅ONLY DEFEND✅ the bases tagged with Entrench. 

        Please 🚫 DO NOT 🚫 take the initiate to attack an enemy base, this will only harm us. This is the most important rule and will ensure us a smooth victory.

        Hidden settings in the lineup tab can optimize your defensive participation.  Go to lineups, top right corner click the  ratchet wheel ⚙️ next to “quick add” and turn “auto team commands” &  “auto convert” on.

        This function will automatically re-place your teams on a base once defeated - even if you are offline.""")
        embed.set_image(url="https://media.discordapp.net/attachments/1124766858902523965/1124782265721958420/Screenshot_20230106-114527.png")
        await message.channel.send(embed=embed)
        embed = discord.Embed()
        embed.set_image(url="https://media.discordapp.net/attachments/1124766858902523965/1124782266086858783/IMG_9920.png?width=1307&height=671")
        await message.channel.send(embed=embed)

    if message.content.startswith(commands[3]):
        embed = discord.Embed(title='What is dynamite and how to use it properly', description=
        """Dynamite 🧨 (1st pic) can be obtained at the end of each battle from morale booster (2nd pic) after you have
        defeated any offensive or defensive lineups.

        The way it works is by dealing damage equal to 20% Max HP to the opponent’s lineup but it doesn’t defeat it. This will
        greatly impact the damage we deal to super strong lineups. That max Hp is shown as a green bar while the energy is shown
        as yellow bar.

        Once enough dynamite has been used the green life will disappear (3rd pic) and at that point any extra dynamite won’t
        take effect therefore save for other strong opponents.

        The way to use dynamite is to click on the intelligence tab of each base we are attacking or defending and click on
        use dynamite. When someone attack us the dynamite will be on the left side (4th pic) when we are attacking the dynamite
        will be on the right side (5th pic) with lines no longer than 120 characters.""")
        embed.set_image(url="https://media.discordapp.net/attachments/1124766858902523965/1124786924050194523/6ED167A9-53C0-4ABA-BD28-C8A0C0FF88AE.jpg")
        await message.channel.send(embed=embed)
        embed = discord.Embed()
        embed.set_image(url="https://cdn.discordapp.com/attachments/1124766858902523965/1124786924394119168/IMG_3272.png")
        await message.channel.send(embed=embed)
        embed.set_image(url="https://media.discordapp.net/attachments/1124766858902523965/1124786925098770516/IMG_3275.png?width=1193&height=671")
        await message.channel.send(embed=embed)
        embed.set_image(url="https://media.discordapp.net/attachments/1124766858902523965/1124786924763238500/IMG_3276.png?width=1193&height=671")
        await message.channel.send(embed=embed)
        embed.set_image(url="https://media.discordapp.net/attachments/1124766858902523965/1124786925446889532/IMG_3274.png?width=1193&height=671")
        await message.channel.send(embed=embed)

    if message.content.startswith(commands[4]):
        embed = discord.Embed(title='Tier list')
        embed.set_image(url='https://media.discordapp.net/attachments/1041544918516113508/1116406148287975464/tierlist310523.png?width=714&height=671')
        await message.channel.send(embed=embed)

    if message.content.startswith(commands[5]):
        embed = discord.Embed(title='Hero fusion cost')
        embed.set_image(url='https://media.discordapp.net/attachments/1041544918516113508/1115983977409413201/MLA_Stars.png?width=876&height=671')
        await message.channel.send(embed=embed)

    if message.content.startswith(commands[6]):
        embed = discord.Embed(title='Wheel of time')
        embed.set_image(url='https://media.discordapp.net/attachments/1041544918516113508/1111759388533866617/unknown.png?width=632&height=671')
        await message.channel.send(embed=embed)

    if message.content.startswith(commands[7]):
        embed = discord.Embed(title='Soul vessel')
        embed.set_image(url='https://media.discordapp.net/attachments/1041544918516113508/1111759375581855834/Soul_Vessel_Yes_Its_Final.png?width=1009&height=671')
        await message.channel.send(embed=embed)

    if message.content.startswith(commands[8]):
        embed = discord.Embed(title='Soul root', description=
        """The importance of leveling up soul root for long term progress.
        When your sanctuary reach level 500 you will need +50K yellow essence to increase the lvl by 1.
        When you reach lvl 600 you will need close to 70K.
        So even though leveling up Hwang Jini sounds tempting a hero copy is not worth more than resources.
        If you get enough coins to buy the aureate run stones and the HJ copy then wonderful but if you don’t prioritize aureate.
        Last picture is the bonus you get of all 3 resources for every soul root level.""")
        embed.set_image(url='https://media.discordapp.net/attachments/1041544918516113508/1095812698786242580/IMG_3269.png?width=895&height=671')
        await message.channel.send(embed=embed)
        embed = discord.Embed()
        embed.set_image(url="https://media.discordapp.net/attachments/1041544918516113508/1095812699251814500/IMG_2814.png?width=1193&height=671")
        await message.channel.send(embed=embed)
        embed.set_image(url="https://media.discordapp.net/attachments/1041544918516113508/1095812699784478730/Screenshot_2022-09-24-04-32-35-51_64779e9ab56c96eef77afe24eee7e2fc.jpg?width=1440&height=648")
        await message.channel.send(embed=embed)
        embed.set_image(url="https://media.discordapp.net/attachments/1041544918516113508/1095812700027756615/IMG_2812.png?width=377&height=671")
        await message.channel.send(embed=embed)

    if message.content.startswith(commands[9]):
        embed = discord.Embed(title='Guild boss', description=
        """How to calculate your score in Guild Boss?! And discover if it’s worth to keep the new challenge score or do sweep instead.

        Take your sweep score, let’s say it's 100K, take your bonus % lets say it’s 240%. Now sum 100 to the bonus 240% = 340% Divide that % into 100 = 3.4

        Then do the following math calculations:
        (your sweep score= 100.000) divided into (3.4)you’d get in this case 29.411

        If your new challenges score is below the number (in this example case 29.411) you do sweep but if its higher you keep the new challenge score. You can calculate any boss with any bonus percentage.
        """)
        embed.set_image(url='https://media.discordapp.net/attachments/1041544918516113508/1093905919269687457/01E24E33-622F-4380-8E42-8C81054D4EAC.jpg')
        await message.channel.send(embed=embed)
