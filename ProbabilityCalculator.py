import copy
import random

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, quantity in balls.items():
            self.contents.extend([color] * quantity)

    def draw(self, num_balls):
        drawn_balls = random.sample(self.contents, min(num_balls, len(self.contents)))
        for ball in drawn_balls:
            self.contents.remove(ball)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)

        # Check if drawn balls match the expected ones
        match = True
        for color, quantity in expected_balls.items():
            if drawn_balls.count(color) < quantity:
                match = False
                break

        if match:
            successful_experiments += 1

    probability = successful_experiments / num_experiments
    return probability
