class Character():

    def __init__(self,pos_x,pos_y):
        self.position_y = pos_x
        self.position_x = pos_y
        self.movement_speed = 3
        self.frame = 0
        self.state = "stand"
        self.facing_at = "right"
        self.idle_right_states = list()
        self.idle_left_states = list()
        self.walking_right_states = list()
        self.walking_left_states = list()
        self.dying_states = list()

        for i in range (18):
            if i < 10:
                self.walking_right_states.append(
                    "principal_character/Character_Sprites/Walking/Satyr_01_Walking_00" + str(i) + ".png")
            else:
                self.walking_right_states.append(
                    "principal_character/Character_Sprites/Walking/Satyr_01_Walking_0" + str(i) + ".png")

        for i in range(12):
            if(i < 10):
                self.idle_right_states.append(
                    "principal_character/Character_Sprites/Idle/Satyr_01_Idle_00" + str(i) + ".png")
            else:
                self.idle_right_states.append(
                    "principal_character/Character_Sprites/Idle/Satyr_01_Idle_0" + str(i) + ".png")

        for i in range (18):
            if (i < 10):
                self.walking_left_states.append(
                    "principal_character/Character_Sprites/Walking_left/Satyr_01_Walking_left_00" + str(i) + ".png")
            else:
                self.walking_left_states.append(
                    "principal_character/Character_Sprites/Walking_left/Satyr_01_Walking_left_0" + str(i) + ".png")

        for i in range(12):
            if (i < 10):
                self.idle_left_states.append(
                    "principal_character/Character_Sprites/Idle_left/Satyr_01_Idle_00" + str(i) + ".png")
            else:
                self.idle_left_states.append(
                    "principal_character/Character_Sprites/Idle_left/Satyr_01_Idle_0" + str(i) + ".png")

        for i in range(14):
            if i < 10:
                self.dying_states.append(
                    "principal_character/Character_Sprites/Dying/Satyr_01_Dying_00" + str(i) + ".png")
            else:
                self.dying_states.append(
                    "principal_character/Character_Sprites/Dying/Satyr_01_Dying_0" + str(i) + ".png")

    def get_x(self):
        return self.position_x

    def get_y(self):
        return self.position_y

    def set_x(self, pos_x):
        self.position_x = pos_x

    def set_y(self, pos_y):
        self.position_y = pos_y

    def get_movement_speed(self):
        return self.movement_speed

    def set_movement_speed(self, mov_speed):
        self.movement_speed = mov_speed

    def die(self):
        self.state = "dying"
        self.animar_state(self.dying_states)

    def get_image(self):
        if self.state == "stand":
            if self.facing_at == "right":
                return self.idle_right_states[self.frame]
            else:
                return self.idle_left_states[self.frame]

        if self.state == "moving":
            if self.facing_at == "right":
                return self.walking_right_states[self.frame]
            else:
                return self.walking_left_states[self.frame]

        if self.state == "dying":
            return self.dying_states[self.frame]

    def animar_state(self , state):
        if self.frame >= len(state)-1:
            self.frame = 0
        self.frame += 1

    def move(self, direction):
        if direction == "stand":
            self.state = "stand"
        elif direction == "right" or "left" or "up" or "down":
            self.state = "moving"

        if direction == "stand":
            if self.facing_at == "right":
                self.animar_state(self.idle_right_states)
            else:
                self.animar_state(self.idle_left_states)

        if direction == "right":
            self.facing_at = "right"
            self.animar_state(self.walking_right_states)
            self.position_x += self.movement_speed

        if direction == "left":
            self.facing_at = "left"
            self.animar_state(self.walking_left_states)
            self.position_x += -self.movement_speed

        if direction == "up":
            if self.facing_at == "left":
               self.animar_state(self.walking_left_states)
            else:
                self.animar_state((self.walking_right_states))
            self.position_y += -self.movement_speed

        if direction == "down":
            if self.facing_at == "left":
                self.animar_state(self.walking_left_states)
            else:
                self.animar_state((self.walking_right_states))
            self.position_y += self.movement_speed
