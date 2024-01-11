import discord
from discord.ext import commands

# Define las intenciones que tu bot usará
intents = discord.Intents.all()

# Crea el objeto Bot con intenciones
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}')

@bot.command(name='calcular_consumo', help='Calcula el consumo eléctrico. Uso: !calcular_consumo [potencia en watts] [tiempo en horas]')
async def calcular_consumo(ctx, potencia: float, tiempo: float):
    consumo = potencia * tiempo / 1000  # Convertir a kilovatios
    await ctx.send(f'El consumo eléctrico es de {consumo} kilovatios-hora.')

@bot.command(name='consejos_ahorro', help='Proporciona consejos para el ahorro de energía.')
async def consejos_ahorro(ctx):
    consejos = [
        'Apaga los dispositivos electrónicos cuando no los estés utilizando.',
        'Utiliza bombillas LED de bajo consumo.',
        'Desconecta los cargadores de dispositivos cuando no estén en uso.'
    ]
    await ctx.send('\n'.join(consejos))

@bot.command(name='informacion_energia', help='Proporciona información sobre la energía eléctrica. Uso: !informacion_energia [tema]')
async def informacion_energia(ctx, tema: str):
    # Puedes personalizar esta sección con la información que desees proporcionar sobre el tema seleccionado
    if tema.lower() == 'eficiencia':
        info = 'La eficiencia energética es crucial para reducir el consumo y los costos.'
    elif tema.lower() == 'renovable':
        info = 'Las fuentes de energía renovable, como la solar y la eólica, son clave para un futuro sostenible.'
    else:
        info = 'Tema no reconocido. Intenta con "eficiencia" o "renovable".'

    await ctx.send(info)

@bot.command(name='imagen_energia', help='Muestra una imagen relacionada con la energía eléctrica.')
async def imagen_energia(ctx):
    # Puedes proporcionar el enlace a una imagen relacionada con la energía eléctrica
    imagen_url = 'imagen\carbon o gas.jpg'
    imagen_url = 'imagen\eolica.jpg'
    imagen_url = 'imagen\hidraulica.jpg'
    await ctx.send(f'Imagen relacionada con la energía eléctrica: {imagen_url}')

bot.run("MTE5NDc3NTAyNDk2ODY2MzA3MQ.G1HzRA.h-134PpQ8otD1kkyU_xvdtzzNwYogCLyAPzAc8")