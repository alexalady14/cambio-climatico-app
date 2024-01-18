import discord
from discord.ext import commands

# Define las intenciones que tu bot usará
intents = discord.Intents.default()
intents.message_content = True
# Crea el objeto Bot con intenciones
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def e1(ctx):
    await ctx.send(f'informacion sobre la energia eolica:')
    informacion = (
        "La energía eólica es una forma de generación de energía que utiliza la fuerza del viento para producir electricidad. "
            "Los aerogeneradores o turbinas eólicas capturan la energía cinética del viento y la convierten en energía eléctrica. "
            "Algunas características de la energía eólica incluyen:\n\n"
            "- Es una fuente de energía renovable y sostenible.\n"
            "- Contribuye a la reducción de las emisiones de gases de efecto invernadero.\n"
            "- Puede instalarse en tierras agrícolas o marinas, aprovechando espacios compartidos.\n"
            "- Aunque tiene beneficios, también puede tener impactos en la vida silvestre y generar preocupaciones estéticas en algunas comunidades.\n\n"
        "La tecnología de la energía eólica sigue avanzando para mejorar la eficiencia y minimizar los impactos ambientales."
    )
    await ctx.send(informacion)

@bot.command()
async def e2(ctx):
    await ctx.send(f'informacion sobre la energia hidraulica ')
    informacion = (
        "La energía hidráulica se genera principalmente en centrales hidroeléctricas, que pueden ser de dos tipos: de embalse y de flujo libre.\n\n"
        "Ventajas de la Energía Hidráulica:\n"
        "Bajas Emisiones: Produce bajas emisiones de gases de efecto invernadero en comparación con las fuentes de energía basadas en combustibles fósiles.\n\n"
        "Positivo:\n"
        "Reducción de Emisiones: Contribuye a la reducción de emisiones de gases de efecto invernadero al proporcionar una alternativa a las fuentes de energía basadas en combustibles fósiles.\n\n"
        "Desafíos y Consideraciones:\n"
        "Alteración del Ecosistema: La construcción de presas puede alterar el ecosistema local y afectar la vida silvestre, como la migración de peces.\n\n"
        "Tecnologías para Mitigar Impactos:\n"
        "Escaleras de Peces: Estructuras diseñadas para permitir el paso de peces alrededor de presas y turbinas.\n"
        "Mejoras en Diseño: Diseños de presas que minimizan el impacto ambiental y permiten el flujo natural del agua.\n\n"
        "Es importante señalar que, aunque la energía hidroeléctrica es una fuente de energía renovable con beneficios significativos, también presenta desafíos ambientales y sociales que deben abordarse cuidadosamente."
    )
    await ctx.send(informacion)

@bot.command()
async def e3(ctx):
    await ctx.send(f'informacion sobre la energia carbon ')
    informacion = (
        "Energía a partir de Carbón:\n"
        "La energía a partir del carbón implica la combustión de carbón para generar electricidad en plantas de energía térmica.\n\n"
        "Impacto en el Medio Ambiente:\n"
        "Emisiones de CO2: La quema de carbón libera grandes cantidades de dióxido de carbono, un gas de efecto invernadero que contribuye al cambio climático.\n"
        "Contaminantes Atmosféricos: Además de CO2, la quema de carbón emite otros contaminantes atmosféricos como óxidos de azufre, óxidos de nitrógeno y partículas finas, que pueden afectar la calidad del aire y la salud humana."
    )
    await ctx.send(informacion)

@bot.command()
async def e4(ctx):
    await ctx.send(f'informacion sobre la energia de carbon ')
    informacion = (
        "Energía a partir de Carbón:\n"
        "La energía a partir del carbón implica la combustión de carbón para generar electricidad en plantas de energía térmica.\n\n"
        "Impacto en el Medio Ambiente:\n"
        "Emisiones de CO2: La quema de carbón libera grandes cantidades de dióxido de carbono, un gas de efecto invernadero que contribuye al cambio climático.\n"
        "Contaminantes Atmosféricos: Además de CO2, la quema de carbón emite otros contaminantes atmosféricos como óxidos de azufre, óxidos de nitrógeno y partículas finas, que pueden afectar la calidad del aire y la salud humana."
    )
    await ctx.send(informacion)

@bot.command()
async def e5(ctx):
    await ctx.send(f'informacion sobre la energia de gas natural ')
    informacion = (
        "Energía a partir de Gas Natural:\n"
        "La energía a partir del gas natural implica la quema de gas en plantas de energía, que pueden ser de ciclo combinado o de turbina de gas.\n\n"
        "Impacto en el Medio Ambiente:\n"
        "Emisiones de CO2: Aunque las emisiones de CO2 de gas natural son menores en comparación con el carbón, sigue siendo una fuente significativa de CO2.\n\n"
        "Desafíos Ambientales:\n"
        "Extracción y Fracturación Hidráulica: La extracción de gas natural a través de técnicas como la fracturación hidráulica puede tener impactos ambientales locales, como el agotamiento de agua y la contaminación del agua subterránea."
    )
    await ctx.send(informacion)
    
@bot.command()
async def e6(ctx):
    await ctx.send(f'informacion sobre la energia nuclear ')
    informacion = (
        "Energía Nuclear:\n"
        "La energía nuclear se produce mediante la fisión nuclear, donde los núcleos de átomos se dividen en reacciones controladas para liberar grandes cantidades de energía.\n\n"
        "Ventajas de la Energía Nuclear:\n"
        "Bajas Emisiones de CO2: La generación de energía nuclear produce bajas emisiones de dióxido de carbono en comparación con las centrales eléctricas de combustibles fósiles.\n\n"
        "Positivas:\n"
        "Bajas Emisiones de Gases de Efecto Invernadero: La generación de energía nuclear contribuye a la mitigación del cambio climático al proporcionar una fuente de energía con bajas emisiones de gases de efecto invernadero durante la operación normal.\n\n"
        "Desafíos y Consideraciones:\n"
        "Residuos Radiactivos: La generación de energía nuclear produce residuos radiactivos que requieren una gestión cuidadosa y soluciones a largo plazo para su almacenamiento y disposición.\n"
        "Riesgos Nucleares: La posibilidad de accidentes nucleares, aunque rara, puede tener consecuencias graves para la salud humana y el medio ambiente.\n\n"
        "Desafíos Ambientales:\n"
        "Residuos Radiactivos: La gestión de los residuos radiactivos es uno de los mayores desafíos ambientales asociados con la energía nuclear. Se requiere un almacenamiento seguro y a largo plazo para los desechos radiactivos.\n\n"
        "Tecnologías Mejoradas:\n"
        "Se están investigando y desarrollando tecnologías de energía nuclear más avanzadas, como reactores de generación IV, con el objetivo de mejorar la seguridad y reducir los residuos radiactivos.\n\n"
        "Comparación con otras Fuentes de Energía:\n"
        "Aunque tiene desafíos, la energía nuclear es a menudo considerada una fuente de energía baja en carbono en comparación con los combustibles fósiles, lo que puede ser importante para la transición hacia un sistema energético más sostenible."
    )
    await ctx.send(informacion)



@bot.command(name='imagen_energia', help='Muestra una imagen relacionada con la energía eléctrica.')
async def imagen_energia(ctx):
    # Puedes proporcionar el enlace a una imagen relacionada con la energía eléctrica
    imagen_url = 'imagen\nuclear o gas.jpg'
    imagen_url = 'imagen\eolica.jpg'
    imagen_url = 'imagen\hidraulica.jpg'
    imagen_url = 'imagen\carbon.jpeg'
    await ctx.send(f'Imagen relacionada con la energía eléctrica: {imagen_url}')

bot.run("TOKEN")
