import time
import pygame

def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surface_sz = 480   # Desired physical surface size, in pixels.

    # Create surface of (width, height), and its window.
    main_surface = pygame.display.set_mode((surface_sz, surface_sz))

    #Image
    ball = pygame.image.load("/usr/lib/python2.7/site-packages/pygame/docs/tut/intro/ball.gif")

    #Font
    my_font = pygame.font.SysFont("Courier",16)

    # Set up some data to describe a small rectangle and its color
    small_rect = (300, 200, 150, 90)
    some_color = (255, 0, 0)        # A color is a mix of (Red, Green, Blue)

    frame_count= 0
    frame_rate= 0
    t0 = time.clock ()
    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop

        #Time
        frame_count += 1
        if frame_count %500 == 0:
            t1 = time.clock()
            frame_rate = 500/(t1-t0)
            t0=t1

        # Update your game objects and data structures here...

        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        main_surface.fill((0, 200, 255))
        
        #Load Ball Image
        main_surface.blit(ball,(100,120))

        #Text
        the_text = my_font.render("Frame={0}, rate = {1:.2f} fps".format(frame_count,frame_rate), True, (0,0,0))
        main_surface.blit (the_text,(10,10))
        # Overpaint a smaller rectangle on the main surface
        main_surface.fill(some_color, small_rect)

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()

    pygame.quit()     # Once we leave the loop, close the window.

main()
