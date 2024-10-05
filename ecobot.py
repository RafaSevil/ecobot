import discord
from discord.ext import commands
import os, random
import requests

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='%', intents=intents)

@bot.event
async def on_ready():
    print(f'El {bot.user} ha iniciado con exito')

funfacts= [
    "El papel se puede reciclar hasta 11 veces.",
    "Para producir 1 tonelada de papel, se tienen que cortar 17 árboles grandes.",
    "El reciclaje de papel ahorra un 30 porciento de la energía eléctrica y un 70 porciento del agua que se utilizaría normalmente para producirlo a partir de madera.",
    "Cada segundo, se cortan en el mundo espacios de bosques y selvas del tamaño de una cancha de futbol",
    "Una bolsa de plástico tiene un tiempo de uso medio de entre 12 y 20 minutos, pero tarda entre 15 a 1,000 años para degradarse.",
    "El vidrio es 100 porciento reciclable Puede reciclarse infinitamente, jamás pierde sus propiedades."
    ]
@bot.command()
async def funfact(ctx):
    facts=random.choice(funfacts)
    await ctx.send(facts)

@bot.command()
async def ayuda(ctx):
    await ctx.send(f""" Mis comandos son:
**%funfact**
**%mem**
**%tips**
**%reciclar** """)
    
@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
 
    await ctx.send(file=picture)

@bot.command()
async def reciclar(ctx):
    await ctx.send(f"¿Quieres aprender a reciclar? Has buscado al bot correcto!, escribe el comando %tips para leer tips acerca de como empezar a reciclar.")

Tips = ["Reserva un sitio en casa para el reciclaje.",
        "Separa bien los envases de la basura orgánica.",
        "Recicla cada material en el lugar que corresponde",
        "Reutiliza las bolsas de plástico o uso bolsas de tela",
        ]

@bot.command()
async def tips(ctx):
    tip = random.choice(Tips)
    await ctx.send(tip)

@bot.event
async def on_guild_join(guild):
    channel = discord.utils.get(guild.text_channels, name='general') 
    if channel is not None: 
        await channel.send(f'¡Hola {guild.name}! ¡Para empezar prueba este comando: %reciclar o si necesitas ayuda %ayuda') 

bot.run("TOKEN")
