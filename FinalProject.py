# Author: Marcello Borges
# GitHub username: marcborg
# Date: 1/3/2024
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
    A class to represent a Ludo game player with a position between A-D, a start/end space, current position and current state
    """
    def __init__(self, player_position, start_space, end_space, token_p_position="H", token_q_position="H", current_state="STILL PLAYING"):
        """
        The constructor for the Player class.
        :param player_position: a position between A-D
        :param start_space: start space for the player which depends on which position they are in
        :param end_space: end space for the player which depends on which position they are in
        :param token_p_position: position of the player's token p (in the home yard (H), ready to go (R), somewhere on the board, or has finished (E))
        :param token_q_position: position of the player's token q (in the home yard (H), ready to go (R), somewhere on the board, or has finished (E))
        :param current_state: denotes whether the player has won and finished the game or is still playing
        Initializes the required data members. All data members are private.
        """
        self._player_position = player_position
        self._start_space = start_space
        self._end_space = end_space
        self._token_p_position = token_p_position
        self._token_q_position = token_q_position
        self._current_state = current_state
        self._token_p_step_count = -1
        self._token_q_step_count = -1
        
    def get_player_position(self):
        """
        Takes no parameters and returns the player position between A-D
        """
        return self._player_position
    
    def get_completed(self):
        """
        Method that takes no parameters and returns True or False if the players has finished the game or not
        """
        if self._current_state == "STILL PLAYING":
            return False
        return True

    def set_completed(self):
        """
        Takes no parameters and sets current_state to FINISHED to denote player has finsihsed the game being played
        """
        self._current_state == "FINISHED"

    def get_token_p_position(self):
        """
        Takes no parameters and returns the number of steps the token p has taken on the board.
        The total steps should not be larger than 57.
        """
        return self._token_p_position

    def get_token_q_position(self):
        """
        Takes no parameters and returns the number of steps the token q has taken on the board.
        The total steps should not be larger than 57.
        """
        return self._token_q_position

    def set_token_p_position(self, position):
        """
        Method that sets token p to desired position
        :param position: position to move token p to (i.e. H for home yard)
        """
        self._token_p_position = position

    def set_token_q_position(self, position):
        """
        Method that sets token q to desired position
        :param position: position to move token q to (i.e. H for home yard)
        """
        self._token_q_position = position

    def get_token_p_step_count(self):
        """
        Takes no parameters and returns the total steps the token p has taken on the board
        Use steps = -1 for home yard position and steps = 0 for ready to go position
        The total step should not be larger than 57
        """
        return self._token_p_step_count

    def set_token_p_step_count(self, steps):
        """
        Method that sets token p step count based on combination of decision making algorithm and provided in rules
        :param steps: the number of steps token p will move, eventually emulating dice roll
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
            if self._token_q_position == 'E':
                self._current_state = "FINISHED"
        else:
            self._token_p_step_count = 57 - ((self.get_token_p_step_count() + steps) % 57)
        
    def get_token_q_step_count(self):
        """
        Method that sets token q step count based on game rules
        :param steps: the number of steps token q will move, eventually emulating dice roll
        """
        return self._token_q_step_count

    def set_token_q_step_count(self, steps):
        """
        Method that sets token p step count based on game rules
        :param steps: the number of steps token p will move, eventually emulating dice roll
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
            if self._token_p_position == 'E':
                self._current_state = "FINISHED"
        else:
            self._token_q_step_count = 57 - ((self.get_token_q_step_count() + steps) % 57)

    def get_space_name(self, total_token_steps):
        """
        Method that returns the name of the space the token has landed on on the board as a string.
        :param total_token_steps: the count of the steps the respective token has taken
        Method is also able to return the home yard position (H) and the ready to go position (R)
        """
        positions = {-1: 'H', 0: 'R', 57: 'E'}

        if total_token_steps in positions:
            # if steps value equals dictionary key, return key value
            return positions[total_token_steps]
        elif total_token_steps > 50:
            # else if steps are greater than 50, the token has landed in their respective home squares
            return self._player_position + str(total_token_steps % 50)
        return (total_token_steps + self._start_space - 1) % 56 # returns space name based on calculation of steps taken and player's start space

class LudoGame:
    """
    A class to represent the game as played and should contain information about the players as well as information about the board.
    """

    def __init__(self):
        """
        The constructor for the LudoGame class. 
        Takes no parameters. 
        Initializes the required data members.
        All data members are private.
        """
        self._playerA = Player('A', 1, 50)
        self._playerB = Player('B', 15, 8)
        self._playerC = Player('C', 29, 22)
        self._playerD = Player('D', 43, 36)
        self._player_list = [self._playerA, self._playerB, self._playerC, self._playerD]

    def get_player_by_position(self, player_position):
        """
        Method that returns the player_position object and if not a valid player, returns player not found.
        :param player_position: represents the players position as a string
        """
        for player in self._player_list:
            if player_position == player.get_player_position():
                return player
        return "Player not found!"

    def move_token(self, player_object, token_name, steps_taken):
        """
        Method moves one token of a player on the board and updates the token's total steps
        :param player_object: object representing the player whose turn it is
        :param token_name: string representing the token 'p' or 'q'
        :param steps_to_move: integer representing the number of steps the token will move on the board
        It will take care of kicking out another opponent token if it needs. Will be used by the play_game method 
        """
        if token_name in ['p', 'q'] and player_object.get_token_p_step_count() > 0 and (player_object.get_space_name(player_object.get_token_p_step_count()) == player_object.get_space_name(player_object.get_token_q_step_count())):
            # checks if player tokens are stacked and moves both, if so
            player_object.set_token_p_step_count(steps_taken)
            player_object.set_token_q_step_count(steps_taken)

        elif token_name == 'p':
            player_object.set_token_p_step_count(steps_taken)

        elif token_name == 'q':
            player_object.set_token_q_step_count(steps_taken)

        for player in self._player_list:
            # iterates through player list for purpose of kicking out opponent's token if current player lands on same space name
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
        This method creates the player list first using the players list pass in and then moves the tokens according to the turns list following the priority rule.
        It will update the token's position and the player's game state whether they finish or not.
        :param players_list: represents the list of positions players choose
        :param turns_list: represents the list of tuples with each tuple a roll for one player
        Returns a list of strings representing the current spaces of all the tokens for each player in the list after moving the tokens following the rules described.
        """

        player_object_list = []
        for players in players_list:
            player_object_list.append(self.get_player_by_position(players))

        for turns in turns_list:
            # looks at player in turn and appends opponent player space names for verification of same space name to kick out token
            in_turn_player_position = turns[0]
            dice_roll = turns[1]
            players_token_p_list = []
            players_token_q_list = []
            for player_object in player_object_list:
                if in_turn_player_position != player_object.get_player_position():
                    players_token_p_list.append(player_object.get_space_name(player_object.get_token_p_step_count()))
                    players_token_q_list.append(player_object.get_space_name(player_object.get_token_q_step_count()))

            for player_object in player_object_list:
                # moves token based on decision making algorithm
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
            # creates list that will have all player's p and q token space names
            players_space_names.append(str(player_objects.get_space_name(player_objects.get_token_p_step_count())))
            players_space_names.append(str(player_objects.get_space_name(player_objects.get_token_q_step_count())))

        return players_space_names
