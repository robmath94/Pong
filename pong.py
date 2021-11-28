import sys
import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

# The loop will carry on until the user exit the game (e.g. clicks the close button).
carryOn = True
 
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

start_pos = [10, 225]
end_pos = [10, 275]
 
# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we exit this loop
              # could also just use a break command
 
    # --- Game logic should go here
    #if event is up arrow or down arrow, handle cases

    hasRoomDown = end_pos[1] < 498
    hasRoomUp = start_pos[1] > 2
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP and hasRoomUp:
            print("key up detected")
            start_pos[1] = start_pos[1] - 2
            end_pos[1] = end_pos[1] - 2
        elif event.key == pygame.K_DOWN and hasRoomDown:
            print("key down detected")
            start_pos[1] = start_pos[1] + 2
            end_pos[1] = end_pos[1] + 2
 
 
    # --- Drawing code should go here


    # First, clear the screen to black. 
    screen.fill(BLACK)
    #Draw the net
    pygame.draw.line(screen, WHITE, start_pos, end_pos, 5)
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
    pygame.draw.circle(screen, WHITE, [20, 250], 5)
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
     
    # --- Limit to 60 frames per second
    clock.tick(60)
 
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()