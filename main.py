palabra = input("Que pala bra quieres aprender")

meme_dict = ("cringe":"pena agena", 
  "gg": "good game",
"fps": "fotogramas por segundos".
"noob": "nobato",
"afk": "ausente del grupo",
"tmi": "demasiada informacion",
"zzz": "dormido o aburrido",
"XP": "puntos  de experiencia",
"npc": "percona no jugador",
"hitbox": "caja de daño",
"fomo": "miedo a perderse de algo")

if palabra in meme_dict.keys():
  print(meme_dict[palabra])
else:
  print("Esa Palabra No La Tenemos")
