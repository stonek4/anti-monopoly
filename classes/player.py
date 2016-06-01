class PLAYER:
    def get_name(self):
        return self.name
    def get_style(self):
        return self.style
    def get_owned(self):
        return self.owned
    def add_prop(self, prop):
        self.owned.append(prop)
        return True
    def get_s_priorities(self):
        return self.s_priorities
    def get_b_priorities(self):
        return self.b_priorities
    def get_tolerance(self):
        return self.tolerance
    def get_budget(self):
        return self.budget
    def set_budget(self, amount):
        self.budget = amount
        return True
    def set_out(self):
        self.owned = []
        self.out = True
        return True
    def check_out(self):
        return self.out
    def set_jailed(self, option):
        self.jailed = option
        self.jail_timer = 2
        return True
    def get_jail_timer(self):
        return self.jail_timer
    def dec_jail_timer(self):
        self.jail_timer -= 1
        return True
    def check_jailed(self):
        return self.jailed
    def __init__(self, name, style, b_priorities, s_priorities, tolerance, budget):
        self.name = name
        self.style = style
        self.owned = []
        self.s_priorities = s_priorities
        self.b_priorities = b_priorities
        self.tolerance = tolerance
        self.budget = budget
        self.out = False
        self.jailed = False
        self.jail_timer = 0
