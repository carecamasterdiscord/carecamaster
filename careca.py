import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.presences = True  # Habilitar eventos de presença

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot está pronto como {bot.user.name}')

@bot.event
async def on_member_update(before, after):
    role_name = "COMANDO"  # Substitua pelo nome exato do cargo
    role = discord.utils.get(after.guild.roles, name=role_name)

    if role in before.roles and role not in after.roles:
        if str(after.status) in ['online', 'idle']:  # Verificar se o membro ficou online ou ocupado
            channel = bot.get_channel(1033950693251354644)  # Substitua pelo ID do canal onde o bot deve enviar as mensagens
            await channel.send(f'{after.display_name} ficou online ou ocupado!')

# Substitua 'TOKEN_DO_SEU_BOT' pelo token real do seu bot
bot.run('TMTEzOTU4MjkyNjE2MjUwOTgzNA.GhaE8k.wg59Q0k1jfcSK5n68vMnVhsXgXrlfcezcwc6OM')
