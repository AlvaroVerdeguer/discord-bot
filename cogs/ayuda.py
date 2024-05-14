import discord
from discord.ext import commands

class ayuda(commands.Cog):
    def __init__(self,bot):
      self.bot = bot
 
    @commands.Cog.listener()
    async def on_ready(self):
        print('ayuda cog successfully loaded.')

    @commands.command(pass_context=True,aliases=['comm','comandos','Com','COM','Comandos','Comando','comando','Comm'])
    async def com(self,ctx):
      await ctx.send('''```diff
hola pana, aquí te dejo una lista de comandos útiles:

-$commusica
saca una lista con todos los comandos del bot de música
ej: $commusica

-$motivacion / motivar / motivacion
manda una frase motivadora(la vd solo existe para probar cosas nueva)
ej: $motivacion

-$youtube
busca por ti en youtube (aun no esta completo al 100%)
ej: $youtube [lo que quieras buscar]

-$clear / limpiar / limpieza
limpia el chat, por defecto borra 5 mensajes(necesitas permisos especiales)
ej: $clear / $clear [numero de mensajes a borrar]

-$info / tarjeta / informacion
crea una tarjeta con info sobre el servidor
ej: $info

-$ping
devuelve la latencia del bot
ej: $ping

-$loro / repeat / repetir
repite todo lo que dices
ej: $loro [lo que quieras que repita]

-$melon
me lon
ej: $melon

-$ban / banear
banea al usuario mencionado(necesitas permisos de admin)
ej: $ban [usuario]

-$kick / tirar / expulsar / desterrar
kickea al usuario mencionado(necesitas permisos de admin)
ej: $kick [usuario]

-$desbanear / unban
desbanea al usuario seleccionado
ej: $unban [usuario]

-los comandos kick,unban y ban aun estan desarrollandose,
-funcionan pero no de la manera mas optima

-$adivino / adivina / FortuneTeller
responde con una precisión científica al 100% de tus preguntas, con respuestas para nada al azar y totalmente coherentes
ej: $adivino [tu pregunta aqui]

-$html
saca el html de una búsqueda o página web
ej: $html [la búsqueda aqui]

-$com
saca esta lista de comandos
ej: $com

-$me
te dice quien eres 0.0
ej: $me

-$soy_yo
un mensaje creado solo para testear que hay formas de que el bot solo reconozca al creador
ej:$soy_yo

-$nsfw,$AlmaSucia
para ver marranadas(hay que usarlo en un canal NSFW)
ej: $nsfw

-$meme 
te muestra memes en ingles, ya lo mejorare
ej: $meme

-$github
te lleva al github del mejor programador

-$twitchquotes

-$banner
```''')
    @commands.command(pass_context=True,aliases=['comMusica','comusica'])
    async def commusica(self,ctx):
      await ctx.send('''```diff
-$connect / join / summon / conectar / unir
conecta al bot a tu canal de voz o al que tu decidas
ej: $join / $join [el canal de voz que quieras]

-$play / sing
reproduce la canción seleccionada
ej: $play [link de youtube] / $play [nombre cancion]

-$pause / pausar
pausa la canción que este sonando
ej: $pause

-$resume / continue / start / continuar
continua con la reproducción de la canción
ej: $resume

-$skip / next / siguiente / sig
salta a la siguiente canción de la lista
ej: $skip

-$stop / leave / parar
detiene la reproducción y desconecta al bot del canal de voz
ej: $stop

-$change_volume / volume / vol / volumen
cambia el volumen de la música
ej: $volume [valor del 1 al 100]

-$np / current / currentsong / sonando
muestra que canción esta sonando en ese momento
ej: $np

-$queue_info / q / playlist / cola / lista / list
muestr la lista de canciones que estan por sonar
ej: $q



```''')
    @commands.command(pass_context=True,aliases=['ayuda'])
    async def help(self,ctx):
          await ctx.send('''```ini
que pasa [wachin]

si buscas [ayuda], aqui abajo te dejare unas indicaciones
si lo que quieres es saber los comando,
tienes el comando [$com], que te los listara y bueno...

por ahora no hay mucho que hacer, pero espera con ansias,que mi desarrollador no descansa ^^
[gracias por participar en la beta]
```''')



def setup(bot):
  bot.add_cog(ayuda(bot))