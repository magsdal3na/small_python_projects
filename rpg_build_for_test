full_dot = '●'
empty_dot = '○'

strength = 0
intelligence = 0
charisma = 0


def create_character(character_name, strength, intelligence, charisma):

    stats = [strength, intelligence, charisma]

    if not isinstance(character_name, str):
        return "The character name should be a string"
    if len(character_name) > 10:
        return "The character name is too long"
    if ' ' in character_name:
        return "The character name should not contain spaces"

    if not all(isinstance(s, int) for s in stats):
        return "All stats should be integers"
    if not all(s >= 1 for s in stats):
        return "All stats should be no less than 1"
    if not all(s <= 4 for s in stats):
        return "All stats should be no more than 4"
    if strength + intelligence + charisma != 7:
        return "The character should start with 7 points"

#character stats return
    str_stat = f"STR {full_dot * strength}{empty_dot * (10 - strength)}"
    int_stat = f"INT {full_dot * intelligence}{empty_dot * (10 - intelligence)}"
    cha_stat = f"CHA {full_dot * charisma}{empty_dot * (10 - charisma)}"

    stat_output = f"{character_name}\n{str_stat}\n{int_stat}\n{cha_stat}"

    return stat_output

output = create_character('ren', 4, 2, 1)
