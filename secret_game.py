def play_secret_game(wins):
    import sys, os, random

    try:
        from pathlib import Path
    except ImportError:
        import subprocess
        subprocess.run([sys.executable, "-m", "pip", "install", "pathlib"], check=True)
        try:
            from pathlib import Path
        except ImportError:
            print("Missing pathlib, could not install, please try doing it yourself.")

    try:
        import pygame, pygame.mixer
    except ImportError:
        import subprocess
        subprocess.run([sys.executable, "-m", "pip", "install", "pygame"], check=True)
        try:
            import pygame, pygame.mixer
        except ImportError:
            import subprocess
            subprocess.run([sys.executable, "-m", "pip", "install", "pygame"], check=True)
            print("Missing pygame, could not install, please try doing it yourself.")


    try:
        from dotenv import load_dotenv
    except ImportError:
        import subprocess
        subprocess.run([sys.executable, "-m", "pip", "install", "dotenv"])
        try:
            from dotenv import load_dotenv
        except:
            print("Missing dotenv, could not install, please try doing it yourself.")

    try:
        import psycopg2
    except ImportError:
        import subprocess
        subprocess.run([sys.executable, "-m", "pip", "install", "psycopg2"], check=True)
        try:
            import psycopg2
        except ImportError:
            print("Missing psycopg2, could not install, please try doing it yourself.")


    env_path = Path(__file__).parent / ".env" # This is the path to the .env file
    load_dotenv(env_path) # This is the loading of the .env file
    # Below are the variables for the game, some from the .env file and some from the input of the user
    total_clicks_taken = 0

    def draw_score(total_clicks_taken, font, space_width, space_height, font_size, screen, max_score):
        text_surface = font.render(f"Current score: {max_score - total_clicks_taken}", True, (255,255,255)) # This is the text for the score  
        text_rect = text_surface.get_rect(center=(space_width / 2 * font_size, space_height / 2)) # This is the rect of the text
        screen.blit(text_surface, text_rect)
        pygame.display.update() 

    user_text = ''
    end = True # This is the end of the game
    pygame.init()
    clicked_squares = [] # This is the list of clicked squares used to check if the square has been clicked
    matched_squares = [] # This is the list of matched squares
    unmatched_timer = None
    info = pygame.display.Info()
    screen_width = info.current_w # This is the width of the screen
    screen_height = info.current_h # This is the height of the screen
    game_width = screen_height * 9 / 16 # This is the width of the game
    game_height = screen_height # This is the height of the game
    # clock = pygame.time.Clock() # This is the clock
    grid_height = 4
    grid_width = 3
    scale_x = screen_width / game_width # This is the scale of the x
    scale_y = screen_height / game_height # This is the scale of the y
    scale = min(scale_x, scale_y)
    scaled_width = int(game_width * scale) # This is the scale of the width
    scaled_height = int(game_height * scale) # This is the scale of the height 

    input_rect = pygame.Rect(screen_width / 2 - screen_width / 6, screen_height / 2 - screen_height / 18, screen_width / 3, screen_height / 9)

    grid_colors = [] # This is the list of grid colors
    idx = 0
    font_size = 50
    font = pygame.font.Font(None, font_size)
    space_width, space_height = font.size(" ") # This is the width and height of the space

    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
    game_surface = pygame.Surface((game_width, game_height))

    buttons = {
        "Easy": pygame.Rect(0, scaled_height / 2, scaled_width / 3, scaled_width / 3),
        "Medium": pygame.Rect(screen_width / 2 - scaled_width / 6, scaled_height / 2, scaled_width / 3, scaled_width / 3),
        "Hard": pygame.Rect(screen_width - scaled_width / 3, scaled_height / 2, scaled_width / 3, scaled_width / 3),
        "Custom": pygame.Rect(screen_width / 2 - scaled_width / 6, scaled_height - scaled_height / 4, scaled_width / 3, scaled_width / 3)
    }

    selected_difficulty = None
    running = True
    menu = True
    color_active = pygame.Color('lightskyblue3')
    color_passive = pygame.Color('gray15')
    active = False
    name = True

    while menu: # Used to run the menu without conflicting with the game
        while name: # Used to run the name input without conflicting with the game or other parts of the menu
            name_text = "Enter your name:" # This is the text for the name
            title = font.render(name_text, True, (255, 255, 255))
            screen.blit(title, (screen_width / 2 - ((screen_width / 180) * len(name_text)) ,  screen_height / 2 - screen_height / 10)) 
            for event in pygame.event.get(): # Used to get the events from the pygame
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect.collidepoint(event.pos):
                        active = True
                    else:
                        active = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1] # This is the removal of the last character
                    elif event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                        user_text = user_text.strip() # This is the removal of the whitespace
                        name = False # This is the condition for the name to be false
                        screen.fill("black")
                        pygame.display.flip() # This is the display of the screen
                        break
                    else:
                        user_text += event.unicode # This is the addition of the input to the user_text
            if active:
                color = color_active
            else:
                color = color_passive
            pygame.draw.rect(screen, color, input_rect)
            text_surface = font.render(user_text, True, (0, 0, 0))
            screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
            input_rect.w = max(100, text_surface.get_width() + 10)
            pygame.display.flip()
        if not name:
            screen.fill("black") 
        dif = "Select Difficulty"
        title = font.render(dif, True, (255, 255, 255))
        screen.blit(title, (screen_width / 2 - ((screen_width / 180) * len(dif)) ,  10)) 
        for label, rect in buttons.items(): # Used to draw the buttons
            pygame.draw.rect(screen, "white", rect)
            text = font.render(label, True, (0, 0, 0))
            text_rect = text.get_rect(center=rect.center)
            screen.blit(text, text_rect)
        pygame.display.flip()
        for event in pygame.event.get(): # Used to get the events from the pygame
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button, rect in buttons.items():
                    if rect.collidepoint(event.pos): # This is the condition for the button to be clicked
                        selected_difficulty = button
                        menu = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
                os._exit(0)
    if selected_difficulty: # Used to run the selected difficulty without conflicting with the game or other parts of the menu
        menu = False # Stops running the menu so it doesn't conflict with the game
        running = False
        # This is the selected difficulty part, allowing users to select the difficulty of the game, including custom
        if selected_difficulty == "Easy":
            grid_height = 4
            grid_width = 3
            all_colors = ["red", "blue", "green", "yellow", "purple", "orange"] * 2
        elif selected_difficulty == "Medium":
            grid_height = 4
            grid_width = 4
            all_colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown"] * 2
        elif selected_difficulty == "Hard":
            grid_height = 5
            grid_width = 4
            all_colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "gray", "white"] * 2
        elif selected_difficulty == "Custom":
            custom_done = False
            listed_colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "gray", "white"]
            user_height = ""
            user_width = ""
            active_field = "height"
            input_rect = pygame.Rect(screen_width / 2 - 200, screen_height / 2, 400, 50)
            while not custom_done: # Used to run the custom difficulty without conflicting with the game or other parts of the menu
                screen.fill("black")
                prompt = f"Enter grid {active_field} (positive integer):"
                title = font.render(prompt, True, (255, 255, 255))
                screen.blit(title, (screen_width / 2 - title.get_width() // 2, screen_height / 2 - 100))
                pygame.draw.rect(screen, "white", input_rect)
                active_text = user_height if active_field == "height" else user_width
                text_surface = font.render(active_text, True, (0, 0, 0))
                screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
                pygame.display.flip()
                for event in pygame.event.get(): # Used to get the events from the pygame
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            if active_field == "height":
                                user_height = user_height[:-1]
                            else:
                                user_width = user_width[:-1]
                        elif event.key == pygame.K_RETURN:
                            if active_field == "height": # This is the condition for the input to be a digit
                                active_field = "width"
                            else:
                                if user_height.isdigit() and user_width.isdigit(): # This is the condition for the input to be a digit
                                    h = int(user_height)
                                    w = int(user_width)
                                    slots = h * w
                                    if slots <= 0: # This is the condition for the grid being too small
                                        user_height = ""
                                        user_width = ""
                                        active_field = "height"
                                    elif slots > 25: # This is the condition for the grid being too large
                                        msg = f"Grid too large (max 25 slots). You entered {slots}."
                                        user_height = ""
                                        user_width = ""
                                        active_field = "height"
                                    elif slots % 2 != 0: # This is the condition for the grid having an odd number of slots
                                        msg = f"Grid must have an even number of slots. You entered {slots}."
                                        user_height = ""
                                        user_width = ""
                                        active_field = "height"
                                    else: # This is the condition for the grid being valid
                                        custom_done = True
                                else:
                                    user_height = "" # This is the reset of the height input
                                    user_width = "" # This is the reset of the width input
                                    active_field = "height"
                        else:
                            if event.unicode.isdigit(): # This is the condition for the input to be a digit
                                if active_field == "height": 
                                    user_height += event.unicode 
                                else: 
                                    user_width += event.unicode
            grid_height = int(user_height)
            all_colors = []
            grid_width = int(user_width)
            slots = grid_height * grid_width
            needed_pairs = slots // 2
            if needed_pairs <= len(listed_colors): # Doubles the number of pairs needed, to make sure the user hasn't entered invalid input
                for i in range(needed_pairs):
                    all_colors.append(listed_colors[i])
                    all_colors.append(listed_colors[i])
            else:
                for i in range(needed_pairs):
                    all_colors.append(listed_colors[i])
                    all_colors.append(listed_colors[i])
            random.shuffle(all_colors) # This is the shuffling of the colors
        total_pairs = len(all_colors) // 2
        max_score = total_pairs * 10
        running = True
    idx = 0
    grid_colors = []
    for i in range(grid_height): # Draws the grid
        row_colors = []
        for col in range(grid_width):
            if idx >= len(all_colors):
                row_colors.append(random.choice(["red","blue","green","yellow","purple","orange","pink","brown","gray","white"]))
            else:
                row_colors.append(all_colors[idx])
            idx += 1
        grid_colors.append(row_colors)

    square_size = int(min(game_width, game_height) * 0.25)
    margin_x = (game_width - grid_width * square_size) / (grid_width + 1)
    margin_y = (game_height - grid_height * square_size) / (grid_height + 1)
    def draw_square(i, col, reveal=False): # Draws the square
        square_x = margin_x + col * (square_size + margin_x)
        square_y = margin_y + i * (square_size + margin_y)
        pygame.draw.rect(game_surface, "white", (square_x, square_y, square_size, square_size))
        if reveal == True:
            color = grid_colors[i][col]
            pygame.draw.rect(game_surface, "black", (square_x, square_y, square_size, square_size))
            pygame.draw.circle(game_surface, color, (square_x + square_size//2, square_y + square_size//2), square_size//2)

    while running: # Starts the actual part of the game
        now = pygame.time.get_ticks()
        if unmatched_timer and now - unmatched_timer > 500:
            clicked_squares.clear() # This is the list of clicked squares
            unmatched_timer = None                                     
        x_offset = (screen_width - scaled_width) // 2
        y_offset = (screen_height - scaled_height) // 2

        if max_score - total_clicks_taken <= 0: # Checks 
            game_surface.fill("black")
            text_surface = font.render(f"You failed.", True, (255,255,255))
            text_rect = text_surface.get_rect(center=(screen_width/2, screen_height/2))
            screen.fill((0, 0, 0))
            screen.blit(text_surface, text_rect)
            pygame.display.flip()
            pygame.time.wait(3000)
            running = False
        else:
            wins += 1
        for event in pygame.event.get(): # Used to get the events from the pygame, for example, the mouse button down to click on the squares, or escape to quit the game
            if event.type == pygame.QUIT:
                running = False 
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x_game = (event.pos[0] - x_offset) / scale
                y_game = (event.pos[1] - y_offset) / scale
                draw_score(total_clicks_taken, font, space_width, space_height, font_size, screen, max_score)
                pygame.display.flip()
                for i in range(grid_height): # Used to check if the square has been clicked, and if so which square
                    for col in range(grid_width):
                        square_x = margin_x + col * (square_size + margin_x)
                        square_y = margin_y + i * (square_size + margin_y)
                        if square_x <= x_game <= square_x + square_size and square_y <= y_game <= square_y + square_size:
                            pygame.mixer.init()
                            pygame.mixer.music.load("click.wav")
                            pygame.mixer.music.play()
                            if (i, col) not in clicked_squares and (i, col) not in matched_squares:
                                total_clicks_taken += 1
                                clicked_squares.append((i, col))
                                if len(clicked_squares) == 2:
                                    pos1, pos2 = clicked_squares
                                    if grid_colors[pos1[0]][pos1[1]] == grid_colors[pos2[0]][pos2[1]]:
                                        matched_squares.extend(clicked_squares)
                                        clicked_squares.clear()
                                    else: 
                                        unmatched_timer = now
        draw_score(total_clicks_taken, font, space_width, space_height, font_size, screen, max_score) # Function to draw the score in the top right corner of the screen
        game_surface.fill("black")
        for i in range(grid_height):
            for col in range(grid_width):
                reveal = (i, col) in clicked_squares or (i, col) in matched_squares
                draw_square(i, col, reveal) # Function to draw the squares
        screen.fill("black")
        scaled_surface = pygame.transform.scale(game_surface, (scaled_width, scaled_height)) # This is the scaling of the game surface to the screen
        screen.blit(scaled_surface, (x_offset, y_offset))

        # Below is the code for the winning of the game / completion of the game
        # Player finished the game
        if len(matched_squares) == (total_pairs * 2) and end:
            end = False  # Mark game finished
            delta = total_clicks_taken - (total_pairs * 2)

            msg = f"You made it {user_text}! And only in {delta} extra clicks."
            text_surface = font.render(msg, True, (255,255,255))
            text_rect = text_surface.get_rect(center=(screen_width/2, screen_height/2))
            screen.fill((0, 0, 0))
            screen.blit(text_surface, text_rect)
            pygame.display.flip()
            pygame.time.wait(3000)
            running = False
    pygame.quit() # This is the end of the game, and the pygame window will close
    return wins
    sys.exit(1) # This is the end of the game, and the program will close