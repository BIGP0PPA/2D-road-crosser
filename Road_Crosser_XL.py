import pygame

screen_title = 'Road Crosser XL'
screen_width = 600
screen_height = 600
white_color = (255,255,255)
black_color = (0,0,0)
red_color = (255,0,0)
blue_color = (0,0,255)
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('broadway', 70)

class Game:
    tick_rate = 60
    

    def __init__(self, image_path, title, width, height):
        self.title = title
        self.width = width
        self.height = height
        self.game_window = pygame.display.set_mode((width, height))
        self.game_window.fill(white_color)
        pygame.display.set_caption(title)
        
        background = pygame.image.load(image_path)
        self.image = pygame.transform.scale(background, (width, height))


    def run_game_loop(self, level_speed):
        is_game_over = False
        did_win = False 
        direction = 0

        player_character = PlayerCharacter('player.png', 275, 500, 30, 30)
        enemy_0 = NonPlayerCharacter('enemy.png', 20, 400, 30, 30)
        enemy_0.speed *= level_speed
        enemy_1 = NonPlayerCharacter('enemy.png', self.width - 60, 250, 30, 30)
        enemy_1.speed *= level_speed
        enemy_2 = NonPlayerCharacter('enemy.png', 20, 100, 30, 30)
        enemy_2.speed *= level_speed
        goal = GameObject('treasure.png', 275, 50, 30, 30)


        while not is_game_over:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        direction = 1
                    elif event.key == pygame.K_DOWN:
                        direction = -1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0

            
            self.game_window.fill(white_color)
            self.game_window.blit(self.image, (0,0))
            goal.draw(self.game_window)
            player_character.move(direction, self.height)
            player_character.draw(self.game_window)
            enemy_0.move(self.width)
            enemy_0.draw(self.game_window)

            if level_speed >= 2:
                enemy_1.move(self.width)
                enemy_1.draw(self.game_window)

            if level_speed >= 4:
                enemy_2.move(self.width)
                enemy_2.draw(self.game_window)

            if player_character.collision(enemy_0):
                is_game_over = True
                did_win = False
                text = font.render('LOSER!!!', True, red_color)
                self.game_window.blit(text, (150,275))
                pygame.display.update()
                clock.tick(3)
                break
            if player_character.collision(enemy_1):
                is_game_over = True
                did_win = False
                text = font.render('LOSER!!!', True, red_color)
                self.game_window.blit(text, (150,275))
                pygame.display.update()
                clock.tick(3)
                break
            if player_character.collision(enemy_2):
                is_game_over = True
                did_win = False
                text = font.render('LOSER!!!', True, red_color)
                self.game_window.blit(text, (150,275))
                pygame.display.update()
                clock.tick(2)
                break
            elif player_character.collision(goal):
                is_game_over = True
                did_win = True
                text = font.render('WINNER!!', True, blue_color)
                self.game_window.blit(text, (150,275))
                pygame.display.update()
                clock.tick(2)
                break

            pygame.display.update()
            clock.tick(self.tick_rate)

        if did_win:
            self.run_game_loop(level_speed + 0.75)
        else:
            return





class GameObject:

    def __init__(self, image_path,x, y, width, height):
        object_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(object_image, (width,height))
        self.x_pos = x
        self.y_pos = y
        self.width = width
        self.height = height

    def draw(self,background):
        background.blit(self.image, (self.x_pos,self.y_pos))


class PlayerCharacter(GameObject):

    speed = 5
        
    def __init__(self,image_path,x,y,width,height):
        super().__init__(image_path,x,y,width,height)
        
    def move(self, direction, max_height):
        if direction > 0:
            self.y_pos -= self.speed
        elif direction < 0:
            self.y_pos += self.speed
        if self.y_pos >= max_height - 60:
            self.y_pos = max_height - 60
        if self.y_pos <= 20:
            self.y_pos = 20


    def collision(self,other_object):
        if self.y_pos > other_object.y_pos + other_object.height:
            return False 
        elif self.y_pos + self.height < other_object.y_pos:
            return False 

        if self.x_pos > other_object.x_pos + other_object.width:
            return False 
        elif self.x_pos +self.width < other_object.x_pos:
            return False

        return True 

class NonPlayerCharacter(GameObject):

    speed = 2
            
    def __init__(self,image_path,x,y,width,height):
        super().__init__(image_path,x,y,width,height)
            
    def move(self,max_width):
        if self.x_pos <= 20:
            self.speed = abs(self.speed)
        elif self.x_pos >= max_width - 60:
            self.speed = -abs(self.speed)
        self.x_pos += self.speed 
       
        



pygame.init()

new_game = Game('background.png', screen_title, screen_width, screen_height)
new_game.run_game_loop(1)

  

pygame.quit()   
quit()
