class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        deck.sort()

        # Queue of indices to simulate the reveal process
        queue = deque(range(n))

        result = [0] * n
        for i in range(n):
            # The front of the queue is the next position to be revealed
            result[queue.popleft()] = deck[i]
            # Move the next position to the bottom of the deck
            if queue:
                queue.append(queue.popleft())

        return result