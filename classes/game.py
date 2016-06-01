import time
import math
import random
from functions import roll
from functions import num_owned
from functions import get_owner
from board import BOARD
from player import PLAYER

class GAME:
    def print_out(self, text):
        if self.debugging == True:
            print text
    def check_t_bankruptcy(self, player, val):
        outcome = self.check_bal(player, val)
        if outcome == False:
            self.pay(player, player.get_budget())
            player.set_out()
            self.inc_turn()
            for prop in player.get_owned():
                prop.un_mortgage()
            self.print_out("Player "+str(player.get_name())+" has gone bankrupt to the bank, all properties are freed.")
            return True
        self.pay(player, val)
        return False
    def check_p_bankruptcy(self, player, val, owner):
        outcome = self.check_bal(player, val)
        if outcome == False:
            self.collect(owner, player.get_budget())
            self.pay(player, player.get_budget())
            for pprop in player.get_owned():
                owner.add_prop(pprop)
            player.set_out()
            self.inc_turn()
            self.print_out("Player "+str(player.get_name())+" has gone bankrupt to Player "+str(owner.get_name())+", all properties were turned over.")
            return True
        self.pay(player, val)
        self.collect(owner, val)
        return False
    def check_win(self):
        left = 0
        winner = ""
        for player in self.players:
            if player.check_out() == False:
                left += 1
                winner = player.get_name()
        if left >= 2:
            return False
        self.print_out("Player "+str(winner)+" wins!!!")
        return True
    def move(self, player):
        value = roll(2)
        self.print_out("Player "+str(self.turn)+" rolled " + str(value))
        self.locations[self.turn] += value
        if (self.locations[self.turn] >= len(self.board)-1):
            self.locations[self.turn] -= len(self.board)-1
            self.collect(player, 100)
        self.print_out("Player "+str(self.turn)+" moved to "+self.board[self.locations[self.turn]].get_name())
    def move_to(self, player, prop):
        while True:
            if(self.board[self.locations[self.turn]].get_name() == prop):
                self.print_out("Player "+str(self.turn)+" moved to "+self.board[self.locations[self.turn]].get_name())
                return
            else:
                self.locations[self.turn] += 1
            if (self.locations[self.turn] >= len(self.board)-1):
                self.locations[self.turn] -= len(self.board)-1
                self.collect(player, 100)
    def straight(self, player, prop):
        while True:
            if(self.board[self.locations[self.turn]].get_name() == prop):
                player.set_jailed(True)
                self.print_out("Player "+str(self.turn)+" moved straight to "+self.board[self.locations[self.turn]].get_name())
                return
            else:
                self.locations[self.turn] += 1
            if (self.locations[self.turn] >= len(self.board)-1):
                self.locations[self.turn] -= len(self.board)-1
        player.set_jailed(True)
    def collect(self, player, value):
        player.set_budget(player.get_budget()+value)
        self.print_out("Player "+str(player.get_name())+" collected $"+str(value) + " | ($" + str(player.get_budget()) + ")")
    def pay(self, player, value):
        player.set_budget(player.get_budget()-value)
        self.print_out("Player "+str(player.get_name())+" paid $"+str(value) + " | ($" + str(player.get_budget()) + ")")
        return True
    def buy_prop(self, player, prop):
        if player.get_budget >= prop.get_cost():
            self.pay(player, prop.get_cost())
            player.add_prop(prop)
            self.print_out("Player "+str(player.get_name())+" purchased "+ prop.get_name())
    def sell_houses(self, player, value):
        for pprop in player.get_owned():
            if pprop.get_style() == "property":
                while pprop.get_houses() > 0:
                    pprop.rem_house()
                    self.print_out("Player "+str(player.get_name())+" sold a house on "+ pprop.get_name())
                    self.collect(player, pprop.get_h_val()/2)
                    if player.get_budget >= value:
                        return True
        return False
    def buy_houses(self, player):
        for pprop in player.get_owned():
            if pprop.get_style() == "property":
                if pprop.get_houses() < 4 or (pprop.get_houses() == 4 and player.get_style() == "c"):
                    if pprop.check_mortgage() == False and player.get_budget() >= pprop.get_h_val():
                        if num_owned(player, pprop) > 1:
                            self.pay(player, pprop.get_h_val())
                            pprop.add_house()
                            self.print_out("Player "+str(player.get_name())+" bought a house for "+ pprop.get_name() + " | ($" + str(player.get_budget()) + " rem)")
                            return True
        return False
    def mortgage(self, player, value):
        for pprop in player.get_owned():
            if pprop.get_style() == "property" and pprop.check_mortgage() == False:
                if pprop.get_houses() == 0:
                    pprop.mortgage()
                    self.print_out("Player "+str(player.get_name())+" mortgaged "+ pprop.get_name())
                    self.collect(player, pprop.get_m_val())
            elif pprop.check_mortgage == False:
                pprop.mortgage()
                self.print_out("Player "+str(player.get_name())+" mortgaged "+ pprop.get_name())
                self.collect(player, pprop.get_m_val())
            if player.get_budget() >= value:
                return True
        return False
    def unmortgage(self, player):
        for pprop in player.get_owned():
            if pprop.check_mortgage() == True and pprop.get_um_val() < player.get_budget():
                self.pay(player, pprop.get_um_val())
                pprop.un_mortgage()
                self.print_out("Player "+str(player.get_name())+" unmortgaged "+ pprop.get_name())
                return True
        return False
    def check_bal(self, player, val):
        while val > player.get_budget():
            for p in player.get_s_priorities():
                if p == "h":
                    outcome = self.sell_houses(player, val)
                if p == "m":
                    outcome = self.mortgage(player, val)
            if outcome != True:
                outcome = self.mortgage(player, val)
                if outcome != True:
                    return False
        return True
    def inc_turn(self):
        if (self.turn == len(self.players)-1):
            self.turn = 0
        else:
            self.turn += 1
    def take_turn(self):
        player = self.players[self.turn]
        if (player.check_out() == True):
            self.inc_turn()
            return
        if player.check_jailed() == True:
            if player.budget >= 50 and player.get_style() == "m":
                self.pay(player, 50)
                player.set_jailed(False)
                self.print_out ("Player " + str(self.turn) + " left jail")
            else:
                if player.get_jail_timer() > 0:
                    first = roll(1)
                    second = roll(1)
                    self.print_out("Player "+str(self.turn)+" is in jail and rolled " + str(first)+ " " + str(second))
                    if first != second:
                        player.dec_jail_timer()
                        self.inc_turn()
                        return
                player.set_jailed(False)
                self.print_out ("Player " + str(self.turn) + " left jail")
        self.move(player)
        prop = self.board[self.locations[self.turn]]
        if (prop.get_style() == "property tax"):
            outcome = self.check_t_bankruptcy(player, prop.get_value())
            if outcome == True:
                return
        if (prop.get_style() == "income tax"):
            total = 0
            for pprop in player.get_owned():
                if pprop.check_mortgage() == False:
                    total += pprop.get_cost()
                    if pprop.get_style() == "property":
                        total += pprop.get_houses() * pprop.get_h_val()
            total *= .10
            total += player.get_budget() * .10
            total = int(math.floor(total))
            outcome = self.check_t_bankruptcy(player, prop.get_value(total))
            if outcome == True:
                return
        if (prop.get_style() == "go to"):
            self.straight(player, "sightseeing tour")
        if (prop.get_style() == "cm" or prop.get_style() == "anti-monopoly foundation"):
            chance = prop.get_value(player.get_style())
            self.print_out ("Player " + str(self.turn) + " must " + chance[0] + " " + str(chance[1]))
            if (chance[0] == "move"):
                self.move_to(player, chance[1])
            elif(chance[0] == "collect"):
                self.collect(player, chance[1])
            elif(chance[0] == "pay"):
                outcome = self.check_t_bankruptcy(player, chance[1])
                if outcome == True:
                    return
            elif(chance[0] == "straight"):
                self.straight(player, chance[1])
            elif(chance[0] == "collect_c"):
                for opp in self.players:
                    if opp.get_style() == "c" and opp.check_out() == False:
                        outcome = self.check_p_bankruptcy(player, chance[1], opp)
                        if outcome == True:
                            return
            elif(chance[0] == "collect_m"):
                for opp in self.players:
                    if opp.get_style() == "m" and opp.check_out() == False:
                        outcome = self.check_p_bankruptcy(player, chance[1], opp)
                        if outcome == True:
                            return
        can_buy = False
        prop = self.board[self.locations[self.turn]]
        if (prop.get_style() == "property" or prop.get_style() == "utility" or prop.get_style() == "transport"):
            owner_name = get_owner(prop.get_name(), self.players)
            if owner_name >= 0:
                owner = self.players[owner_name]
                if owner_name != self.turn and owner_name >= 0 and prop.check_mortgage() == False and owner.check_jailed() == False:
                    val = prop.get_value(owner.get_style(), num_owned(owner, prop))
                    outcome = self.check_p_bankruptcy(player, val, owner)
                    if outcome == True:
                        return

            if owner_name < 0:
                can_buy = True
        if player.get_tolerance() <= player.get_budget():
            for p in player.get_b_priorities():
                if p == "p":
                    if can_buy == True:
                        if player.get_budget() > prop.get_cost():
                            self.buy_prop(player, prop)
                if p == "h":
                    buying = True
                    while buying == True and player.get_tolerance() <= player.get_budget():
                        buying = self.buy_houses(player)
                if p == "u":
                    unmort = True
                    while unmort == True and player.get_tolerance() <= player.get_budget():
                        unmort = self.unmortgage(player)
        self.inc_turn()
    def get_stats(self):
        print " "
        print "~~~~STATISTICS~~~~"
        for player in self.players:
            print "Player " + str(player.get_name()) + " ~ $" + str(player.get_budget()),
            if player.get_style() == "m":
                print " is a monopolist"
            else:
                print " is a competitor"
            for prop in player.get_owned():
                if prop.get_style() == "property":
                    print prop.get_name() + " " + str(prop.get_houses()) + " houses",
                else:
                    print prop.get_name(),
                if prop.check_mortgage() == True:
                    print " is mortgaged"
                else:
                    print ""
    def __init__(self, num_players, debugging, slow):
        i = 0
        min_tol = 50
        max_tol = 400
        self.debugging = debugging
        self.turn = 0
        self.locations = []
        self.new_board = BOARD()
        self.board = self.new_board.get_board()
        self.players = []
        while (i < num_players):
            if ((i % 2) == 0):
                self.players.append(PLAYER(i, "m", ["h","p","u"], ["h","m"], random.randint(min_tol,max_tol),1500))
            else:
                self.players.append(PLAYER(i, "c", ["h","p","u"], ["m","h"], random.randint(min_tol,max_tol),1500))
            self.locations.append(0)
            i += 1
        i = 0
        while i <= 1000:
            alive = False
            while alive == False:
                if self.players[self.turn].check_out() == False:
                    alive = True
                else:
                    self.inc_turn()
            print "TURN " + str(i+1)
            self.take_turn()
            print ""
            if slow == True:
                time.sleep(5)
            winner = self.check_win()
            if winner == True:
                break
            i += 1
        self.get_stats()
