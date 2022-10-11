from Config.colors import white_color
from disnake.ext import commands
import disnake
import random


palavras = open("palavras.txt").read().splitlines()
EMOJI_CODES = {
    "green": {
        "a": "<:1000176813236043877:1000177485247430666>",
        "b": "<:1000176813236043877:1000177534316593173>",
        "c": "<:1000176813236043877:1000177569435484192>",
        "d": "<:1000176813236043877:1000177600926318683>",
        "e": "<:1000176813236043877:1000177645947998348>",
        "f": "<:1000176813236043877:1000177693574299759>",
        "g": "<:1000176813236043877:1000177715296600184>",
        "h": "<:1000176813236043877:1000177744598028389>",
        "i": "<:1000176813236043877:1000177770648838154>",
        "j": "<:1000176813236043877:1000177795500081183>",
        "k": "<:1000176813236043877:1000177844124668034>",
        "l": "<:1000176813236043877:1000177870662021151>",
        "m": "<:1000176813236043877:1000177910101061632>",
        "n": "<:1000176813236043877:1000177948390871101>",
        "o": "<:1000176813236043877:1000177974873686207>",
        "p": "<:1000176813236043877:1000178004087021598>",
        "q": "<:1000176813236043877:1000178032172073030>",
        "r": "<:1000176813236043877:1000178069253922836>",
        "s": "<:1000176813236043877:1000178101407457370>",
        "t": "<:1000176813236043877:1000178124862005258>",
        "u": "<:1000176813236043877:1000178566614495414>",
        "v": "<:1000176813236043877:1000178672692625458>",
        "w": "<:1000176813236043877:1000178731572269057>",
        "x": "<:1000176813236043877:1000178767265796196>",
        "y": "<:1000176813236043877:1000178805069074432>",
        "z": "<:1000176813236043877:1000178834844426351>"
    },
    "yellow": {
        "a": "<:1000181470096269403:1000181849995358329>",
        "b": "<:1000181470096269403:1000181893167325254>",
        "c": "<:1000181470096269403:1000181933088710717>",
        "d": "<:1000181470096269403:1000181951984062534>",
        "e": "<:1000181470096269403:1000181984045301820>",
        "f": "<:1000181470096269403:1000182003645296740>",
        "g": "<:1000181470096269403:1000182025363390615>",
        "h": "<:1000181470096269403:1000182055956664401>",
        "i": "<:1000181470096269403:1000182084935106692>",
        "j": "<:1000181470096269403:1000182108205092904>",
        "k": "<:1000181470096269403:1000182132074893362>",
        "l": "<:1000181470096269403:1000182162085122090>",
        "m": "<:1000181470096269403:1000182192787439617>",
        "n": "<:1000181470096269403:1000182217064054866>",
        "o": "<:1000181470096269403:1000182245274951750>",
        "p": "<:1000181470096269403:1000182266477158460>",
        "q": "<:1000181470096269403:1000182293794656266>",
        "r": "<:1000181470096269403:1000182341865582672>",
        "s": "<:1000181470096269403:1000182368054808707>",
        "t": "<:1000181470096269403:1000182385914151042>",
        "u": "<:1000181470096269403:1000182409494548500>",
        "v": "<:1000181470096269403:1000182444424708116>",
        "w": "<:1000181470096269403:1000182459910082621>",
        "x": "<:1000181470096269403:1000182485260451910>",
        "y": "<:1000181470096269403:1000182509339951174>",
        "z": "<:1000181470096269403:1000182559742906428>"
    },
    "gray": {
        "a": "<:1000176813236043877:1000179029648887958>",
        "b": "<:1000176813236043877:1000179053690626138>",
        "c": "<:1000176813236043877:1000179075815591957>",
        "d": "<:1000176813236043877:1000179106031349860>",
        "e": "<:1000176813236043877:1000179138008711251>",
        "f": "<:1000176813236043877:1000179158258819102>",
        "g": "<:1000176813236043877:1000179179180007565>",
        "h": "<:1000176813236043877:1000179220246429696>",
        "i": "<:1000176813236043877:1000179255319212106>",
        "j": "<:1000176813236043877:1000179286738739290>",
        "k": "<:1000176813236043877:1000179323749273662>",
        "l": "<:1000176813236043877:1000179359837073428>",
        "m": "<:1000176813236043877:1000179412366536754>",
        "n": "<:1000176813236043877:1000179435024154624>",
        "o": "<:1000176813236043877:1000179465189601320>",
        "p": "<:1000176813236043877:1000179479110492163>",
        "q": "<:1000176813236043877:1000179503059972238>",
        "r": "<:1000176813236043877:1000179559880196197>",
        "s": "<:1000176813236043877:1000179634987618324>",
        "t": "<:1000176813236043877:1000179657011896351>",
        "u": "<:1000176813236043877:1000179680999116810>",
        "v": "<:1000176813236043877:1000179694613835906>",
        "w": "<:1000176813236043877:1000179722615009431>",
        "x": "<:1000176813236043877:1000179748451909745>",
        "y": "<:1000181470096269403:1000181724958957608>",
        "z": "<:1000181470096269403:1000181764146335745>"
    }
}


def generate_blanks():
    return "\N{WHITE MEDIUM SQUARE}" * 5

def generate_puzzle_embed(user: disnake.User , puzzle_id: int) -> disnake.Embed:
    embed = disnake.Embed(description="\n".join([generate_blanks()] * 6), color=white_color)
    embed.set_author(name=user.name, icon_url=user.avatar.url)
    embed.set_footer(text=f"ID do Puzzle: {puzzle_id}")
    return embed

def is_valid_word(word: str) -> bool:
    return word in palavras

def random_puzzle_id() -> int:
    return random.randint(0, len(palavras) - 1)

def generate_colored_word(guess: str, answer: str) -> str:
    colored_word = [EMOJI_CODES["gray"][letter] for letter in guess]
    guess_letters = list(guess)
    answer_letters = list(answer)

    for i in range(len(guess_letters)):
        if guess_letters[i] == answer_letters[i]:
            colored_word[i] = EMOJI_CODES["green"][guess_letters[i]]
            answer_letters[i] = None
            guess_letters[i] = None

    for i in range(len(guess_letters)):
        if guess_letters[i] is not None and guess_letters[i] in answer_letters:
            colored_word[i] = EMOJI_CODES["yellow"][guess_letters[i]]
            answer_letters[answer_letters.index(guess_letters[i])] = None
        return "".join(colored_word)
    

def update_embed(embed: disnake.Embed, guess: str) -> disnake.Embed:
    puzzle_id = int(embed.footer.text.split()[3])
    answer = palavras[puzzle_id]
    print(answer)
    colored_word = generate_colored_word(guess, answer)
    empty_slot = generate_blanks()
    # substituir o primeiro espaço em branco pela palavra colorida
    embed.description = embed.description.replace(empty_slot, colored_word, 1)
    # checar se o jogo acabou
    num_empty_slots = embed.description.count(empty_slot)
    if guess == answer:
        if num_empty_slots == 0:
            embed.description += "\n\nBoa!"
        if num_empty_slots == 1:    
            embed.description += "\n\nMagnífico!"
        if num_empty_slots == 2:
            embed.description += "\n\nÓtimo!"
        if num_empty_slots == 3:
            embed.description += "\n\nIncrível!!"
        if num_empty_slots == 4:
            embed.description += "\n\nImbatível!"
        if num_empty_slots == 5:
            embed.description += "\n\nVocê acertou a resposta!"
            
    elif num_empty_slots == 0:
        embed.description += f"\n\nO jogo acabou! a resposta era ``{answer}``!"
    return embed

def is_game_over(embed: disnake.Embed) -> bool:
    return "\n\n" in embed.description

async def process_message_as_guess(bot: disnake.Client, message: disnake.Message) -> bool:
    ref = message.reference
    if not ref or not isinstance(ref.resolved, disnake.Message):
        return False
    parent = ref.resolved

    if parent.author.id != bot.user.id:
        return False

    if not parent.embeds:
        return False

    embed = parent.embeds[0]
    guess = message.content.lower()

   
    if (embed.author.name != message.author.name or embed.author.icon_url != message.author.display_avatar.url):
        if (embed.author.name != message.author.name):    
            return      
        else:
            await message.reply(f"Você não pode jogar nesse jogo pois ele foi iniciado por {embed.author.mention}. Inicie um jogo utilizando </termo:1011781821668806674>.", delete_after=5)
        try:
            await message.delete(delay=5)
        except Exception:
            pass
        return True

    if is_game_over(embed):
        await message.reply("Esse jogo já acabou. Inicie um novo jogo utilizando </termo:1011781821668806674>.", delete_after=5)
        try:
            await message.delete(delay=5)
        except Exception:
            pass
        return True

    if len(message.content.split()) < 1:
        await message.reply("Por favor digite uma palavra de 5 letras.", delete_after=5)
        try:
            await message.delete(delay=5)
        except Exception:
            pass
        return True

    if not is_valid_word(guess):
        await message.reply("Isso não é uma palavra válida!", delete_after=5)
        try:
            await message.delete(delay=5)
        except Exception:
            pass
        return True

    embed = update_embed(embed, guess)
    await parent.edit(embed=embed)

    try:
        await message.delete()
    except Exception:
        pass

    return True

    
class Utilitários(commands.Cog):

    def __init__(self):

        return

def setup(bot):
    bot.add_cog(Utilitários())