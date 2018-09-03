import individual
import random

POPULATION = 50
NATURAL_RATE = 0.1
MUTATION_THRESHOLD = 10

class Population:
    def __init__(self):
        self.population = []
        self.next_population = []
        self.generation = 1
        self.bestIndividial = 0
        for x in range(POPULATION):
            element = individual.Snake()
            self.population.append(element)

    def check_alive_population(self):
        # check if all members are dead
        number = sum(element.alive == False for element in self.population)
        print("Died so far: ", number)
        print("len: ", len(self.population))
        if number == len(self.population):
            return True
        else:
            return False

            

    def sort_by_fitness(self):
        self.population.sort(key = lambda pop: pop.fitness)


    def natural_selection(self):
        survived = round(POPULATION * NATURAL_RATE) # just to be safe
        for x in range(survived):
            survivor = self.population[x]
            self.next_population.append(survivor)


    def crossover(self, parent_1, parent_2):
        child = individual.Snake()
        # [r, c] = parent_1.wih.shape
        # rand_r = random.randint(0, r-1)
        # rand_c = random.randint(0, c-1)
        # TODO need to check elements of lists and lengths because -1 elements -> done I think, but check again
        a = round(random.random(), 4) 
        child.brain.wih = parent_1.brain.wih * a + parent_2.brain.wih *(1-a)
        child.brain.whh = parent_1.brain.whh * a + parent_2.brain.whh *(1-a) 
        child.brain.who = parent_1.brain.who * a + parent_2.brain.who *(1-a)
        return child 
        
    def mutate(self, child):
        wih = child.brain.wih
        whh = child.brain.whh
        who = child.brain.who

        matrices = [wih, whh, who]

        for matrix in matrices:
            [r, c] = matrix.shape
            for i in range(r):
                for j in range(c):
                    # random number for mutation rate if it is below the threshold mutate the snake
                    random_number = random.randint(0,100)
                    if random_number < MUTATION_THRESHOLD:
                        value = [-10, 10]
                        pick = random.randint(0, 1)
                        matrix[i, j] = matrix[i, j] * (1 - value[pick]/100)
                    if matrix[i, j] < -1:
                        matrix[i, j] = -1
                    elif matrix[i, j] > 1:
                        matrix[i, j] = 1

        child.brain.wih = matrices[0]
        child.brain.whh = matrices[1]
        child.brain.who = matrices[2]    
        return child

    def new_generation(self):
        next_population = []
        self.sort_by_fitness()
        self.natural_selection()

        while len(next_population) < POPULATION:
            rand_1 = random.randint(0, POPULATION*NATURAL_RATE-1) 
            rand_2 = random.randint(0, POPULATION*NATURAL_RATE-1) 
            parent_1 = self.population[rand_1]
            parent_2 = self.population[rand_2]
            child = self.crossover(parent_1, parent_2)
            child = self.mutate(child)
            next_population.append(child)

        for element in next_population:
            element.reset()
        
        self.population = next_population
        self.bestIndividial = self.population[0]
        self.generation += 1
        


# this = Population()
# print(this.population)
