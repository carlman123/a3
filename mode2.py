from island import Island
from data_structures.heap import MaxHeap
from random_gen import RandomGen
class Mode2Navigator:
    """
    Student-TODO: short paragraph as per https://edstem.org/au/courses/12108/lessons/42810/slides/294117


    In this code I attempted to use max heaps to represent a fleet of pirate captains. Each pirate captain would want the islands that would give them
    the most profit. The simulate_day method gives the captains an even amount of crew. This method also computed the scores for each island based on the crews that were allocated 
    and the potential profits. 
    

    """

    def __init__(self, n_pirates: int) -> None:
        """
        Student-TODO: Best/Worst Case
        best case and worst case should be O(1)
        """
        self.n_pirates = n_pirates
        self.islands = []
        self.pirates = [MaxHeap(1) for _ in range(n_pirates)]
        self.day = 0

    def add_islands(self, islands: list[Island]):
        """
        Student-TODO: Best/Worst Case
        best case is O(1) 

        worst case is (O(m)) where m is the number of elements in the input list of islands
        occurs when the input list of islands is very large, where assigning the entire list involves compying references to the element list
        """
        self.islands = islands

    def simulate_day(self, crew: int) -> list[tuple[Island|None, int]]:
        """
        Student-TODO: Best/Worst Case
        best case is  O(1) where the input crew is either nothing or really small and there are no islands available
        then none of the loops happen and none of the calculations happen and boom O(1))

        worst case is O(self.n_pirates *len(self.islands*log(N))), where n is the number of isnalds in one captain's heap

        occurs when the crew is really big and all the islands are available with marines and money
        the outer loop runs self.n_pirates times and the inner loop runs len(self.islands) times

        the time complexity depends on the size of the crew and the number of captains 

        """
        results = []

   
        pirate_heaps = [MaxHeap(len(self.islands)) for _ in range(self.n_pirates)] # initializes an empty heap for each pirate captain

   
        crew_per_captain = crew // self.n_pirates # distributes crew evenly to pirate captains

    
        for i in range(self.n_pirates): # calculates the score for each island for each pirate captain
            for j, island in enumerate(self.islands):
                sent_crew = min(crew_per_captain, island.marines)  # sends the maximum possible crew without exceeding marines
                if sent_crew == island.marines:
                    money_earned = island.money
                else:
                    money_earned = min((sent_crew * island.money / island.marines), island.money)
                score = 2 * (crew_per_captain - sent_crew) + money_earned
                pirate_heaps[i].add((-score, island))  # stores the island and its score as a tuple

   
        for i in range(self.n_pirates): # select islands and crew for each pirate captain
            if len(pirate_heaps[i]) > 0:
                best_choice = pirate_heaps[i].get_max()
                island, score = best_choice[1], -best_choice[0]  # get the island and score
                results.append((island, score))  # append the island and score
            else:
                results.append((None, 0))  # no island selected

        return results







    
