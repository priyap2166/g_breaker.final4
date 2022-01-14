import pygame

from pygame_gui.elements import UIButton
from pygame_gui import UI_BUTTON_PRESSED

# setting width and height variables of window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
FRAME_RATE = 400


# declaring tutorial class
class TutorialState:
    # initialising attributes
    def __init__(self, window_surface, ui_manager):
        self.transition_target = None
        # screen surface
        self.window_surface = window_surface
        # button manager
        self.ui_manager = ui_manager
        self.title_font = pygame.font.Font(None, 64)
        self.big_font = pygame.font.SysFont('Roboto', 30)
        self.tutorial_font = pygame.font.SysFont('Roboto', 25)

        self.tutorial_rect = None

        # images
        self.background_img = None
        self.image = None
        self.image_pos_rect = None

        self.coin_img = None
        self.obstacle_img = None

        # text
        self.welcome_text = None
        self.tutorial_text = None
        self.good_luck_text = None
        self.coin_text_one = None
        self.coin_text_two = None
        self.obstacle_text_one = None
        self.obstacle_text_two = None
        self.controls_text_one = None
        self.controls_text_two = None

        # positions
        self.welcome_text_pos = (265, 220)
        self.tutorial_text_pos = (155, 250)
        self.good_luck_text_pos = (255, 480)

        self.coin_text_one_pos = (165, 300)
        self.coin_text_two_pos = (165, 320)
        self.coin_img_pos = (105, 300)

        self.obstacle_text_one_pos = (105, 360)
        self.obstacle_text_two_pos = (105, 380)
        self.obstacle_img_pos = (605, 360)

        self.controls_text_one_pos = (160, 420)
        self.controls_text_two_pos = (175, 440)

        # button
        self.back_button = None

    def start(self):
        self.transition_target = None
        # creating background image + positioning
        self.background_img = pygame.transform.scale(pygame.image.load('img/bg.png').convert_alpha(), (1200, 640))
        self.image = pygame.image.load('MAIN LOGO.png')
        self.image_pos_rect = self.image.get_rect()
        self.image_pos_rect.center = (400, 150)

        self.coin_img = pygame.image.load('img/tile/18.png')
        self.obstacle_img = pygame.image.load('img/tile/17.png')

        # creating tutorial text
        self.welcome_text = self.big_font.render('Welcome to Ground Breaker!', True, (225, 116, 25))
        self.tutorial_text = self.tutorial_font.render('In this platform game, there are some things you need to know:'
                                                       , True, (225, 116, 25))
        # coin text
        self.coin_text_one = self.tutorial_font.render('There are coins to collect at every level!'
                                                       , True, (225, 116, 25))
        self.coin_text_two = self.tutorial_font.render('Each coin gives you 15'
                                                       ' points! You will start off with 100 points.'
                                                       , True, (225, 116, 25))
        # obstacle text
        self.obstacle_text_one = self.tutorial_font.render('Be careful! There are occasional spikes.'
                                                           , True, (225, 116, 25))
        self.obstacle_text_two = self.tutorial_font.render('Each obstacle loses 20 points and decreases health too.'
                                                           , True, (225, 116, 25))
        # exit text
        self.controls_text_one = self.tutorial_font.render('There are two controls you can use: WASD or Arrow Keys.'
                                                           , True, (225, 116, 25))
        self.controls_text_two = self.tutorial_font.render('You can switch between these controls at any point!'
                                                           , True, (225, 116, 25))
        # ending text
        self.good_luck_text = self.big_font.render('That is all for now, Good luck!'
                                                   , True, (225, 116, 25))

        # creating back button
        self.back_button = UIButton(pygame.Rect((550, 550), (150, 35)),
                                    'Back to menu', self.ui_manager)

    def stop(self):
        # killing all variables
        self.background_img = None
        self.image = None
        self.image_pos_rect = None

        self.back_button.kill()
        self.back_button = None

    def handle_events(self, event):
        # back to main menu on click back button
        if event.type == pygame.USEREVENT and event.user_type == UI_BUTTON_PRESSED:
            if event.ui_element == self.back_button:
                self.transition_target = 'main_menu'

    def update(self, time_delta):
        self.window_surface.blit(self.background_img, (0, 0))         # clear the window to the background surface
        self.window_surface.blit(self.image, self.image_pos_rect)

        self.tutorial_rect = pygame.draw.rect(self.window_surface, (128, 57, 0), (90, 205, 610, 310))

        self.window_surface.blit(self.welcome_text, self.welcome_text_pos)
        self.window_surface.blit(self.tutorial_text, self.tutorial_text_pos)

        self.window_surface.blit(self.coin_text_one, self.coin_text_one_pos)
        self.window_surface.blit(self.coin_text_two, self.coin_text_two_pos)
        self.window_surface.blit(self.coin_img, self.coin_img_pos)

        self.window_surface.blit(self.obstacle_text_one, self.obstacle_text_one_pos)
        self.window_surface.blit(self.obstacle_text_two, self.obstacle_text_two_pos)
        self.window_surface.blit(self.obstacle_img, self.obstacle_img_pos)

        self.window_surface.blit(self.controls_text_one, self.controls_text_one_pos)
        self.window_surface.blit(self.controls_text_two, self.controls_text_two_pos)

        self.window_surface.blit(self.good_luck_text, self.good_luck_text_pos)

        self.ui_manager.draw_ui(self.window_surface)  # Draw the UI Bits
