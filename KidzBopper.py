import discord

from discord.ext import commands

import lyricsgenius as lg

import random

import math

import os

client = commands.Bot(command_prefix='-')

genius = lg.Genius("H7LWN-Xp-B86v4j39jZFAeYDPK600i1GEPunoP2rYYHGxQZPvis5EN-t9gMwTUq9", skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"])

def no_mo_nonos(lyrics):
    lyr = lyrics
    wholesome_nwords = ["homie", "fellow black man", "friend", "brother from another mother"]
    wholesome_ass = ["bedonkadonk", "mouse pad", "pirate's booty", "squirrel from spongebob", "fart zone", "birthday cake"]
    wholesome_shit = ["bad", "trash", "garbage"]
    wholesome_hoe = ["person who hugs a lot of people", "minecraft hoe", "premarital hand holder"]
    wholesome_dick = ["harry potter wand", "minecraft sword", "iphone charger", "type-b usb", "breathalizer", "eggplant emoji"]
    wholesome_pussy = ["torus", "peach emoji", "pit of sin", "queef zone", "abort port"]
    wholesome_sex = ["hammer time", "mario party", "hand holding", "dance party", "bible study", "parent teacher conference", "bible discussion study meeting"]
    wholesome_wap = ["worship and prayer", "warm apple pie", "william's awesome party", "World History AP", "Walking around paris", "where are parents", "women are poggers", "waffles and pancakes"]
    wholesome_titty = ["hunkers", "awoogas", "watermelons", "pillows of sin", "flotation devices", "clouds", "badonkers","dobonhonkeros", "dohoonkabhankoloos", "tonhongerekoogers",
                       "bonkhonagahoogs","hungolomghnonoloughongous"]
    wholesome_fword = ["kisser of the homies", "men hugger", "rainbow man"]
    wholesome_cum = ["pogchamp goo","marinara","ghostbusters slime"]
    wholesome_bitch = ["wamen", "women", "pog champ", "meanie", "ea sports"]
    lyr = lyr.upper().lower()
    #actually replaces all of the swear words
    return lyr.replace("nigga", wholesome_nwords[random.randint(0, len(wholesome_nwords)-1)]).replace("niggas", wholesome_nwords[random.randint(0, len(wholesome_nwords)-1)])\
        .replace("wet-ass pussy", wholesome_wap[random.randint(0, len(wholesome_wap)-1)]).replace("wet ass pussy", wholesome_wap[random.randint(0, len(wholesome_wap)-1)])\
        .replace("whores", wholesome_hoe[random.randint(0, len(wholesome_hoe) - 1)])\
        .replace("ass", wholesome_ass[random.randint(0, len(wholesome_ass)-1)]).replace("asses", wholesome_ass[random.randint(0, len(wholesome_ass)-1)])\
        .replace("thicc", wholesome_ass[random.randint(0, len(wholesome_ass)-1)]).replace("fatty", wholesome_ass[random.randint(0, len(wholesome_ass)-1)])\
        .replace("shit", wholesome_shit[random.randint(0, len(wholesome_shit)-1)]).replace("hoe", wholesome_hoe[random.randint(0, len(wholesome_hoe)-1)])\
        .replace("hoes", wholesome_hoe[random.randint(0, len(wholesome_hoe)-1)]).replace("slut", wholesome_hoe[random.randint(0, len(wholesome_hoe)-1)])\
        .replace("whore", wholesome_hoe[random.randint(0, len(wholesome_hoe)-1)])\
        .replace("sluts", wholesome_hoe[random.randint(0, len(wholesome_hoe)-1)]).replace("dick", wholesome_dick[random.randint(0, len(wholesome_dick)-1)])\
        .replace("cock", wholesome_dick[random.randint(0, len(wholesome_dick)-1)]).replace("penis", wholesome_dick[random.randint(0, len(wholesome_dick)-1)])\
        .replace("dicks", wholesome_dick[random.randint(0, len(wholesome_dick)-1)]).replace("cocks", wholesome_dick[random.randint(0, len(wholesome_dick)-1)])\
        .replace("penises", wholesome_dick[random.randint(0, len(wholesome_dick)-1)]).replace("pussy", wholesome_pussy[random.randint(0, len(wholesome_pussy)-1)])\
        .replace("vagina", wholesome_pussy[random.randint(0, len(wholesome_pussy)-1)]).replace("pussies", wholesome_pussy[random.randint(0, len(wholesome_pussy)-1)])\
        .replace("vaginas", wholesome_pussy[random.randint(0, len(wholesome_pussy)-1)]).replace("sex", wholesome_sex[random.randint(0, len(wholesome_sex)-1)])\
        .replace("fuck", wholesome_sex[random.randint(0, len(wholesome_sex)-1)]).replace("fucking", wholesome_sex[random.randint(0, len(wholesome_sex)-1)])\
        .replace("sex", wholesome_sex[random.randint(0, len(wholesome_sex)-1)]).replace("ho ", wholesome_hoe[random.randint(0, len(wholesome_hoe)-1)])\
        .replace("titty", wholesome_titty[random.randint(0, len(wholesome_titty)-1)]).replace("titties", wholesome_titty[random.randint(0, len(wholesome_titty)-1)])\
        .replace("faggot", wholesome_fword[random.randint(0, len(wholesome_fword)-1)]).replace("cum", wholesome_cum[random.randint(0, len(wholesome_cum)-1)])\
        .replace("cumming", wholesome_cum[random.randint(0, len(wholesome_cum)-1)]).replace("bitch", wholesome_bitch[random.randint(0, len(wholesome_bitch)-1)])



def split_seq(seq, size):
    newseq = []
    splitsize = 1.0/size*len(seq)
    for i in range(size):
        newseq.append(seq[int(round(i*splitsize)):int(round((i+1)*splitsize))])
    return newseq

@client.event
async def on_ready():
    print("Bot is ready.")
    await client.change_presence(status=discord.Streaming, activity=discord.Game("Family friendly jams"))

@client.command()
async def kb(ctx, *, arg):
    try:
        #print("Searching for " + arg)
        try:
            song = (genius.search_song(arg, get_full_info=True))
        except:
            await ctx.send("could not find " + arg)
        if(len(song.lyrics) > 5999):
            await  ctx.send("Song is too long to process")
        else:
            x = "".join(no_mo_nonos(song.lyrics)).split("\n\n")
            print(song.lyrics)
            embed = discord.Embed(title="Wholesome-ified lyrics for \"" + song.title + "\" by " + song.artist, description="\u200b")
            for i in x:
                y = i.split("\n")
                if(len("\n".join(y[1:])) > 1023):
                    a = math.ceil(len("\n".join(y[1:]))/1023)
                    print(a)
                    #print("\n".join(y[1:round(len(y)/a)]))
                    y = split_seq(y, a)
                    for w in y:
                        if(w == y[0]):
                            embed.add_field(name=w[0], value="\n".join(w[1:]), inline=False)
                        else:
                            embed.add_field(name="\u200b", value="\n".join(w))
                else:
                    embed.add_field(name=y[0], value="\n".join(y[1:]), inline=False)
            await ctx.send(embed=embed)
    except:
        if(arg == None):
            await ctx.send("Add a song name after kb")
        else:
            raise



client.run(os.environ['KIDZBOP'])