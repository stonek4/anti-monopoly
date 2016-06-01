from functions import roll

class SQUARE:
    def get_name(self):
        return self.name
    def get_style(self):
        return self.style
    def __init__(self, name, style):
        self.style = style
        self.name = name

class GOTO(SQUARE):
    def get_value(self,player):
        if(player == "m"):
            return ["straight","sightseeing tour"]
        if(player == "c"):
            return ["move","sightseeing tour"]
    def __init__(self,name):
        SQUARE.__init__(self,name,"go to")

class PROPERTY_TAX(SQUARE):
    def get_value(self):
        return 75
    def __init__(self, name):
        SQUARE.__init__(self, name, "property tax")

class INCOME_TAX(SQUARE):
    def get_value(self, amount):
        if (amount < 200):
            return amount
        else:
            return 200
    def __init__(self, name):
        SQUARE.__init__(self, name, "income tax")

class AMF(SQUARE):
    def get_value(self, player):
        if(player == "m"):
            return ["pay",160]
        elif(player == "c"):
            number = roll(1)
            if (number == 1):
                return ["collect",25]
            elif (number == 2):
                return ["collect",50]
            else:
                return ["collect",0]
    def __init__(self,name):
        SQUARE.__init__(self,name,"anti-monopoly foundation")

class PROPERTY(SQUARE):
    def get_cost(self):
        return self.cost
    def get_city(self):
        return self.city
    def get_m_val(self):
        return self.v_mort
    def get_um_val(self):
        return self.v_umort
    def get_h_val(self):
        return self.c_house
    def get_houses(self):
        return self.houses
    def add_house(self):
        self.houses += 1
        return True
    def rem_house(self):
        self.houses -= 1
    def mortgage(self):
        self.is_mortgaged = True
        return True
    def un_mortgage(self):
        self.is_mortgaged = False
        return True
    def check_mortgage(self):
        return self.is_mortgaged
    def get_value(self, owner, number):
        if(owner == "m" and number > 1):
            return (self.m_rent*2) + (self.m_rise*self.houses)
        else:
            return self.c_rent + (self.c_rise*self.houses)
    def __init__(self, name, city, cost, c_house, c_rent, m_rent, c_rise, m_rise):
        SQUARE.__init__(self, name, "property")
        self.city = city
        self.cost = cost
        self.houses = 0
        self.v_mort = int(cost * .5)
        self.v_umort = int(cost * .55)
        self.c_house = c_house
        self.c_rent = c_rent
        self.m_rent = m_rent
        self.c_rise = c_rise
        self.m_rise = m_rise
        self.is_mortgaged = False

class CM(SQUARE):
    def get_value(self, player):
        number = roll(2)
        if(player == "m"):
            if(number == 2):
                return ["move","start"]
            elif(number == 3):
                return ["collect",75]
            elif(number == 4):
                return ["move","beacon st."]
            elif(number == 5):
                return ["pay",75]
            elif(number == 6):
                return ["move","u.s. electric company"]
            elif(number == 7):
                return ["collect",50]
            elif(number == 8):
                return ["move","u.s. air line"]
            elif(number == 9):
                return ["pay",50]
            elif(number == 10):
                return ["collect_c",25]
            elif(number == 11):
                return ["straight","sightseeing tour"]
            elif(number == 12):
                return ["pay",25]
        elif(player == "c"):
            if(number == 2):
                return ["move","u.s. air line"]
            elif(number == 3):
                return ["pay",75]
            elif(number == 4):
                return ["collect_m",25]
            elif(number == 5):
                return ["move","u.s. electric company"]
            elif(number == 6):
                return ["pay",25]
            elif(number == 7):
                return ["move","beacon st."]
            elif(number == 8):
                return ["collect",75]
            elif(number == 9):
                return ["move","start"]
            elif(number == 10):
                return ["pay",50]
            elif(number == 11):
                return ["collect",50]
            elif(number == 12):
                return ["move","sightseeing tour"]
    def __init__(self, name):
        SQUARE.__init__(self, name, "cm")

class UTILITY(SQUARE):
    def mortgage(self):
        self.is_mortgaged = True
        return True
    def un_mortgage(self):
        self.is_mortgaged = False
        return True
    def check_mortgage(self):
        return self.is_mortgaged
    def get_m_val(self):
        return 100
    def get_um_val(self):
        return 110
    def get_cost(self):
        return 150
    def get_value(self, owner, owned):
        number = roll(2)
        if(owned == 1):
            return (number * 4)
        elif(owned == 2):
            if(owner == "c"):
                return (number * 4)
            elif(owner == "m"):
                return (number * 10)
    def __init__(self, name):
        SQUARE.__init__(self, name, "utility")
        self.is_mortgaged = False

class TRANSPORT(SQUARE):
    def mortgage(self):
        self.is_mortgaged = True
        return True
    def un_mortgage(self):
        self.is_mortgaged = False
        return True
    def check_mortgage(self):
        return self.is_mortgaged
    def get_m_val(self):
        return 75
    def get_um_val(self):
        return 83
    def get_cost(self):
        return 200
    def get_value(self, owner, owned):
        if (owner == "c"):
            return 20
        elif (owner == "m"):
            return (40*(owned*2))
    def __init__(self, name):
        SQUARE.__init__(self,name,"transport")
        self.is_mortgaged = False
