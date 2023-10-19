from island import Island
from data_structures.linked_stack import LinkedStack
from data_structures.heap import MaxHeap

class Mode1Navigator:
    """
    Student-TODO: short paragraph as per https://edstem.org/au/courses/12108/lessons/42810/slides/294117

    
    """

    def __init__(self, islands: list[Island], crew: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        self.islands = islands
        self.crew = crew
        self.profitability_heap = MaxHeap(len(islands))
        self.crew_stack = LinkedStack()
        for island in islands:
            self.profitability_heap.add((-island.money, island))
        

    def select_islands(self) -> list[tuple[Island, int]]:
        """
        Student-TODO: Best/Worst Case
        """
        selected_islands = []
        available_crew = self.crew
        sorted_islands = sorted(self.islands, key=lambda island: (-island.money, island.marines))
        island_copy = [Island(island.name, island.money, island.marines) for island in self.islands]

        for island in sorted_islands:
            if available_crew <= 0:
                break  # No more crew to deploy

            if island.marines > 0:
                pirates = min(available_crew, island.marines)  # Send all available crew if marines are present
                money_earned = min((pirates * (island.money / island.marines)), island.money)
                selected_islands.append((island, pirates))
                available_crew -= pirates
            else:
                pirates = min(available_crew, int(available_crew / 2))
                money_earned = island.money
                selected_islands.append((island, pirates))
                available_crew -= pirates

    # Restore the islands to their initial state
        for island, pirates in selected_islands:
            initial_island = next(i for i in island_copy if i.name == island.name)
            island.money = initial_island.money
            island.marines = initial_island.marines

        return selected_islands


    def select_islands_from_crew_numbers(self, crew_numbers: list[int]) -> list[float]:
        """
        Student-TODO: Best/Worst Case
        """
        money_earned_list = []
        available_crew = self.crew
        for crew_count in crew_numbers:
            selected_islands = self.select_islands()  # Re-select islands for each crew count
            total_money_earned = 0

            for island, pirates in selected_islands:
                if island.marines > 0:
                    money_earned = min((pirates * island.money / island.marines), island.money)
                    total_money_earned += money_earned

                # Update available_crew, island.money, and island.marines
                    available_crew -= pirates
                    island.money -= money_earned
                    island.marines -= pirates

                else:
                    money_earned = island.money
                    total_money_earned += money_earned

                # Update available_crew and island.money
                    available_crew = 0
                    island.money = 0

            money_earned_list.append(total_money_earned)

        return money_earned_list

    def update_island(self, island: Island, new_money: float, new_marines: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        if new_money < 0:
            new_money = 0
        if new_marines < 0:
            new_marines = 0
        island.money = new_money
        island.marines = new_marines

    # Find the index of the island within the heap and update it
        for i in range(1, self.profitability_heap.length + 1):
            if self.profitability_heap.the_array[i][1] == island:
                self.profitability_heap.the_array[i] = (-new_money, island)
                self.profitability_heap.sink(i)
            break
