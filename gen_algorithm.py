from connect_four import play_once
import random
  
#Evolves a strong Connect-4 player using genetic algorithm.

#Takes in population size and number of generations
#Executes a "natural selection" style elimination on weaker players and breeds the stronger players to maintain population size
#Returns most successful Connect-4 player from the final generation

def evolve_player(pop_size,num_gen):  
    
    current_gen = pop_initialize(pop_size) #starting population
    generation = 1
    while generation<=num_gen:
 
        strong_list = []
        while len(strong_list)<2: 
            for i in current_gen:
                if measure_fitness(i,current_gen,pop_size):
                    strong_list = strong_list + [i]
               
        while len(strong_list)<pop_size:
            ind1 = strong_list[random.randrange(len(strong_list))]
            ind2 = strong_list[random.randrange(len(strong_list))]
            strong_list = strong_list + [combine(ind1,ind2)]
        current_gen = strong_list
        generation += 1
    
    #Finding strongest player from the final generation by having each individual play 100 games
    strongest_gen = []
    for player in current_gen:
        score = 0
        for i in range(100):
            if play_once(player,current_gen[random.randrange(len(current_gen))])[0] ==1:
                score += 1
        strongest_gen = strongest_gen + [[player,score]]
    
    strongest_gen = sorted(strongest_gen, key = lambda x: int(x[1]))
    strongest_player = strongest_gen[-1]
    
    return  strongest_player[0]
    
#Initializes and returns population by creating binary representations of players.  For example, "0011100"
def pop_initialize(n):
    start_list = []
    for i in range(n):
        start_ind = ""
        for m in range(7): 
            start_ind = start_ind+str(random.randrange(2)) 
        start_list = start_list+[start_ind]
    return start_list

#Measure of fitness: returns True if individual wins at least 4 out of 5 games against randomly selected players from the same generation
def measure_fitness(individual,current_population,n):
    score = 0
    for i in range(5):
        t_res = play_once(individual,current_population[random.randrange(n)])
        if t_res[0] == 1: #win
            score += 1
    if score >=4:
        return True
    else:
        return False
   
#Exchanges at least one bit of both "strong" individuals to return new individual
def combine(ind1,ind2):
    comb_point = random.randrange(1,7)
    part_1 = ind1[0:comb_point]
    part_2 = ind2[comb_point:]
    return part_1+part_2

"""
#Example Case
print evolve_player(100,3)

"""
           
