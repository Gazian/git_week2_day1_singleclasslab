class Team:
    def __init__(self,input_name,input_players,input_coach,input_points):
        self.name = input_name
        self.players = input_players
        self.coach = input_coach
        self.points = input_points(0)

    def add_player(self,new_player):
        self.players.append(new_player) 

    def has_player(self,player_found):
        for player in self.players:
            if player == player_found:
                return True
        return False

    # def play_game(self,result):

    #     if result = 

        # for player in self.players:
        #     if player == player_found:
        #         return True
        #     else: 
        #         return False