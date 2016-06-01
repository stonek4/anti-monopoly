import random

def roll(num):
    total = 0
    while num > 0:
        total += random.randint(1,6)
        num -= 1
    return total

def get_owner(prop, players):
    for player in players:
        for pprop in player.get_owned():
            if pprop.get_name() == prop:
                return player.get_name()
    return -1

def num_owned(player,prop):
    num = 0
    for pprop in player.get_owned():
        if prop.get_style() == "property" and pprop.get_style() == "property":
            if pprop.get_city() == prop.get_city():
                num += 1
        else:
            if pprop.get_style() == prop.get_style():
                num += 1
    return num

def find_mult_own(props):
    cities = []
    mults = []
    mult_props = []
    for prop in props:
        if (prop.get_city in cities):
            mults.append(prop.get_city())
        else:
            cities.append(prop.get_city())
    for prop in props:
        if (prop.get_city() in mults):
            mult_props.append(prop)
    return mult_props
