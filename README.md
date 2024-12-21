# Probability Experiment Simulator

This project simulates a probability experiment where colored balls are drawn from a hat. It calculates the likelihood of drawing a specific combination of balls based on the number of trials.

## Features

- **Customizable Hat**: Create a hat with a specified number of colored balls.
- **Random Drawing**: Simulate the random drawing of balls.
- **Probability Calculation**: Determine the probability of drawing a desired combination of balls over multiple experiments.

## How It Works

### Core Components

1. **Hat Class**:
   - Initializes a hat with the specified number of balls of each color.
   - Provides a `draw` method to randomly select a number of balls.

2. **Experiment Function**:
   - Simulates multiple experiments where a specified number of balls are drawn.
   - Compares the drawn balls against the expected combination to determine success.

### Example Workflow

- Define the contents of the hat, e.g., 3 red balls, 2 green balls, etc.
- Specify the expected combination of balls to be drawn, e.g., 2 red and 1 green.
- Run the `experiment` function to simulate the process over a large number of trials.
- Get the probability of drawing the expected combination.

## Usage

### Prerequisites

- Python 3.x installed.

### Running the Code

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/probability-experiment.git
   cd probability-experiment
