# Author: Marcello Borges
# GitHub username: borgesma
# Date: 12/25/2023
# Description: Create a Ludo Board Game

"""
Rules of the game:

1. 2-4 players can play
2. Each player has 2 tokens
3. At the beginning of the game, each player's two tokens are in the home yard, defined by H
4. On a turn, a player can move one token clockwise by the number of steps indicated on the die
5. You can only move a token out of the home yard by rolling a 6
6. Rolling a six earns that player an additional roll, but if the bonus roll results in another six, the turn is over
7. After 50 steps, the token will enter that player's home squares, where no opponent can enter
8. The token must reach the finishing square on the exact roll and if the roll is larger than the steps needed to get to the finishing square, denoted by E, the token will bounce back the remaining number of steps

Addtional Rules:

1. When a token finishes one move, if it lands on a space occupied by an opponent's token, the opponent token will be return to the home yard, denoted by H. It can only re-enter by rolling a 6, again
2. If the player's two tokens land on the same space on the board, the player will stack the two tokens and move them as one piece until they reach the finishing square, denoted by E
3. If the stacked pieces are sent back to the home yard, they are no longer stacked. Note that if two token are in the ready to go position, denoted by R, they are not stacked

Decision Making Algorithm:

1. If the die roll is 6, try to let the token that still in the home yard get out of the home yard (if both tokens are in the home yard, choose the first one (p)
2. If one token is already in the home square and the step number is exactly what is needed to reach the end square, let that token move and finish
3. If one token can move and kick out an opponent token, then move that token
4. Move the token that is further away from the finishing square
"""

class Player:
    """
    - a Player represents the player who plays the game at a certain position
    """
    def __init__(self, player_position, start_space, end_space):
        self._player_position = player_position
        self._start_space = start_space
        self._end_space = end_space
        self._token_p_position = "H"
        self._token_q_position = "H"
        self._token_p_step_count = -1
        self._token_q_step_count = -1
        self._player_state = "STILL PLAYING"

    def set_completed(self):
        self._player_state == "FINISHED"
        
    def get_player_position(self):
        return self._player_position
    
    def get_completed(self):
        """
        - takes no parameters and returns True or False if the player has finished or not finished the game
        """
        if self._player_state == "STILL PLAYING":
            return False
        return True

    def get_token_p_position(self):
        return self._token_p_position

    def get_token_q_position(self):
        return self._token_q_position

    def set_token_p_position(self, position):
        self._token_p_position = position

    def set_token_q_position(self, position):
        self._token_q_position = position

    def get_token_p_step_count(self):
        """
        - takes no parameters and returns the total steps the token p has taken on the board
        - use steps = -1 for home yard position and steps = 0 for ready to go position
        - the total step should not be larger than 57.
        """
        return self._token_p_step_count

    def set_token_p_step_count(self, steps):
        """

        """
        if self.get_token_p_step_count() == -1 and steps != 6:
            return
        elif self.get_token_p_step_count() == -1 and steps == 6:
            self._token_p_step_count = 0
            self._token_p_position = 'R'
        elif self.get_token_p_step_count() >= 0 and self.get_token_p_step_count() + steps < 57:
            self._token_p_step_count += steps
        elif self.get_token_p_step_count() == 57:
            self._token_p_position = 'E'
            return
        else:
            self._token_p_step_count = 57 - ((self.get_token_p_step_count() + steps) % 57)
        
    def get_token_q_step_count(self):
        """
        - takes no parameters and returns the total steps the token q has taken on the board
        - use steps = -1 for home yard position and steps = 0 for ready to go position
        - the total step should not be larger than 57.
        """
        return self._token_q_step_count

    def set_token_q_step_count(self, steps):
        """

        """
        if self.get_token_q_step_count() == -1 and steps != 6:
            return
        elif self.get_token_q_step_count() == -1 and steps == 6:
            self._token_q_step_count = 0
            self._token_q_position = 'R'
        elif self.get_token_q_step_count() >= 0 and self.get_token_q_step_count() + steps < 57:
            self._token_q_step_count += steps
        elif self.get_token_q_step_count() == 57:
            self._token_q_position = 'E'
            return
        else:
            self._token_q_step_count = 57 - ((self.get_token_q_step_count() + steps) % 57)

    def get_space_name(self, total_token_steps):
        """
        - takes as a parameter the total steps of the token
        - returns the name of the space the token has landed on on the board as a string
        - it should be able to return the home yard position (H) and the ready to go position (R) as well
        """
        positions = {-1: 'H', 0: 'R', 57: 'E'}

        if total_token_steps in positions:
            return positions[total_token_steps]
        elif total_token_steps > 50:
            return self._player_position + str(total_token_steps % 50)
        return (total_token_steps + self._start_space - 1) % 56

class LudoGame:
    """
    - represents the game as played
    - contain information about the players and information about the board
    """

    def __init__(self):

        self._playerA = Player('A', 1, 50)
        self._playerB = Player('B', 15, 8)
        self._playerC = Player('C', 29, 22)
        self._playerD = Player('D', 43, 36)
        self._player_list = [self._playerA, self._playerB, self._playerC, self._playerD]

    def get_player_by_position(self, player_position):
        """
        - takes a parameter representing the players position as a string
        - returns the player object
        """
        for player in self._player_list:
            if player_position == player.get_player_position():
                return player
        return "Player not found!"

    def move_token(self, player_object, token_name, steps_taken):
        """
        - this method will take care of one token moving on the board
        - will update the tokens total steps
        - will take care of kicking out other opponent tokens as needed
        - the play_game method will use this method
        """

        if token_name in ['p', 'q'] and player_object.get_token_p_step_count() > 0 and (player_object.get_space_name(player_object.get_token_p_step_count()) == player_object.get_space_name(player_object.get_token_q_step_count())):
            player_object.set_token_p_step_count(steps_taken)
            player_object.set_token_q_step_count(steps_taken)

        elif token_name == 'p':
            player_object.set_token_p_step_count(steps_taken)

        elif token_name == 'q':
            player_object.set_token_q_step_count(steps_taken)

        for player in self._player_list:
            opponent_player_position = player.get_player_position()
            opponent_token_p_space_name = player.get_space_name(player.get_token_p_step_count())
            opponent_token_q_space_name = player.get_space_name(player.get_token_q_step_count())
            current_player_position = player_object.get_player_position()
            current_player_token_p_space_name = player_object.get_space_name(player_object.get_token_p_step_count())
            current_player_token_q_space_name = player_object.get_space_name(player_object.get_token_q_step_count())

            if current_player_position != opponent_player_position and player_object.get_token_p_step_count() > 0:
                if current_player_token_p_space_name == opponent_token_p_space_name:
                    player.set_token_p_position('H')
                    player.set_token_p_step_count(-1 * player.get_token_p_step_count() - 1)
                if current_player_token_p_space_name == opponent_token_q_space_name:
                    player.set_token_q_position('H')
                    player.set_token_q_step_count(-1 * player.get_token_q_step_count() - 1) 
            if current_player_position != opponent_player_position and player_object.get_token_q_step_count() > 0:
                if current_player_token_q_space_name == opponent_token_p_space_name:
                    player.set_token_p_position('H')
                    player.set_token_p_step_count(-1 * player.get_token_p_step_count() - 1)
                if current_player_token_q_space_name == opponent_token_q_space_name:
                    player.set_token_q_position('H')
                    player.set_token_q_step_count(-1 * player.get_token_q_step_count() - 1)
                    
    def play_game(self, players_list, turns_list):
        """
        - the players list is the list of positions players choose, like [A, C] means two players will play the game at position A and C
        - the turns list is a list of tuples with each tuple a roll for one player
        - this method will create the player list first using the players list pass in
        - then move the tokens according to the turns list following the priority rule 
        - update the tokens position and the players game state (whether finished the game or not)
        - after all the moving is done in the turns list, the method will return a list of strings representing the current spaces of all of the tokens for each player 
        - H for home yard, R for ready to go position, E for finished position, and other letters/numbers for the space the token has landed on
        """

        player_object_list = []
        for players in players_list:
            player_object_list.append(self.get_player_by_position(players))

        for turns in turns_list:
            in_turn_player_position = turns[0]
            dice_roll = turns[1]
            players_token_p_list = []
            players_token_q_list = []
            for player_object in player_object_list:
                if in_turn_player_position != player_object.get_player_position():
                    players_token_p_list.append(player_object.get_space_name(player_object.get_token_p_step_count()))
                    players_token_q_list.append(player_object.get_space_name(player_object.get_token_q_step_count()))

            for player_object in player_object_list:
                if in_turn_player_position == player_object.get_player_position():
                    token_p_space = player_object.get_space_name(player_object.get_token_p_step_count())
                    token_q_space = player_object.get_space_name(player_object.get_token_q_step_count())
                    token_p_step_count = player_object.get_token_p_step_count()
                    token_q_step_count = player_object.get_token_q_step_count()
                    if (dice_roll == 6 and token_p_space == 'H'):
                        self.move_token(player_object, 'p', dice_roll)
                    elif dice_roll == 6 and token_q_space == 'H':
                        self.move_token(player_object, 'q', dice_roll)
                    elif token_p_step_count + dice_roll == 57:
                        self.move_token(player_object, 'p', dice_roll)
                    elif token_q_step_count + dice_roll == 57:
                        self.move_token(player_object, 'q', dice_roll)
                    elif player_object.get_space_name(player_object.get_token_p_step_count() + dice_roll) in players_token_p_list or player_object.get_space_name(player_object.get_token_p_step_count() + dice_roll) in players_token_q_list:
                        self.move_token(player_object, 'p', dice_roll)
                    elif player_object.get_space_name(player_object.get_token_q_step_count() + dice_roll) in players_token_p_list or player_object.get_space_name(player_object.get_token_q_step_count() + dice_roll) in players_token_q_list:
                        self.move_token(player_object, 'q', dice_roll)
                    elif token_q_step_count < token_p_step_count and token_q_step_count >= 0:
                        self.move_token(player_object, 'q', dice_roll)
                    else:
                        self.move_token(player_object, 'p', dice_roll)
        
        players_space_names = []
        for player_objects in player_object_list:
            players_space_names.append(str(player_objects.get_space_name(player_objects.get_token_p_step_count())))
            players_space_names.append(str(player_objects.get_space_name(player_objects.get_token_q_step_count())))

        return players_space_names