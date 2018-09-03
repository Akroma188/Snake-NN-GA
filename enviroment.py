

import individual
import population
import pygame
import gameFunctions

#pylint: disable=E1101
#pylint: disable=W0614

BACKGROUND = (62, 62, 62)
FPS = 20
GREEN = (0, 155, 0)

# TODO need to work on this enviroment, this will be my main file where the action is developed

batch = population.Population()
game = gameFunctions.Game()

game.game_intro()

gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                game.pause()		
    game.clock.tick()
    dt = 0
    while not batch.check_alive_population():
        for snake in batch.population:
            print('step:' ,dt)
            dt+=1
            if snake.alive:
                snake.decide_where_to_move()
                snake.move()
                if snake.collision():
                    snake.alive = False
                if snake.eaten_apple():
                    snake.apple_on_game = False
                if not snake.apple_on_game:
                    snake.spawn_apple()
                snake.calcFitness()

    batch.new_generation()
    bestOne= batch.bestIndividial
    # play best snake in generation
    
    pygame.display.flip()
    while bestOne.alive:
        
        bestOne.decide_where_to_move()
        bestOne.move()
        if bestOne.collision():
            bestOne.alive = False
        if bestOne.eaten_apple():
            bestOne.apple_on_game = False
        if not bestOne.apple_on_game:
            bestOne.spawn_apple()        
        
        game.screen.fill(BACKGROUND)
        game.print_time(bestOne.get_time_alive())
        game.print_best_fitness(bestOne.calcFitness())
        game.print_generation(batch.generation)
        game.score(bestOne.score)
        game.drawApple(bestOne.apple_position)
        game.draw_snake(bestOne.head_position, bestOne.body, bestOne.direction, game.snakeHead, game.bodyPart)
        pygame.display.flip()
        game.clock.tick(FPS)
    game.screen.fill(BACKGROUND)
    game.message_to_screen('Running new Gen...', GREEN, -100, 'large')
    pygame.display.flip()



pygame.quit()
quit()
