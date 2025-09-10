"""
HOSPITAL PLACEMENT via Local Search (Hill Climbing)

Your tasks (fill the TODOs):

1) get_cost(hospitals)
   - Return the sum, over all houses, of the Manhattan distance to the closest hospital.

2) get_neighbors(row, col)
   - Return valid neighbor cells for a given (row, col) by moving one step
     up/down/left/right, staying inside bounds, and NOT stepping on houses or hospitals.

3) hill_climb(maximum=None, ...)
   - Start from a random placement of hospitals.
   - Repeatedly consider moving ONE hospital at a time to a neighboring free cell.
   - If a neighbor state strictly improves the cost, move to the (a) best neighbor.
   - Stop when no neighbor improves the cost (local optimum) or when `maximum` steps are done.

Notes:
- Use self.available_spaces() to know which cells are currently free.
- Use self.output_image(filename) if you want to generate frames of the search (optional).
"""

import random


class Space:

    def __init__(self, height, width, num_hospitals):
        """Create a new state space with given dimensions."""
        self.height = height
        self.width = width
        self.num_hospitals = num_hospitals
        self.houses = set()
        self.hospitals = set()

    # ----------------------
    # Utility / Setup
    # ----------------------
    def add_house(self, row, col):
        """Add a house at a particular location in state space."""
        self.houses.add((row, col))

    def available_spaces(self):
        """Returns all cells not currently used by a house or hospital."""
        candidates = set(
            (row, col)
            for row in range(self.height)
            for col in range(self.width)
        )
        for house in self.houses:
            candidates.remove(house)
        for hospital in self.hospitals:
            candidates.remove(hospital)
        return candidates

    # ----------------------
    # TODO 1: Cost Function
    # ----------------------
    def get_cost(self, hospitals):
        """
        TODO: Return the total (Manhattan) distance from each house to its NEAREST hospital.
        """
  
        pass

    # ----------------------
    # TODO 2: Neighbor Generation
    # ----------------------
    def get_neighbors(self, row, col):
        """
        TODO: Return all valid neighbor cells of (row, col) by moving up/down/left/right by one step.

        A neighbor is valid if:
        - It is inside the grid bounds.
        - It is NOT already a house.
        - It is NOT already a hospital.
        """

        pass

    # ----------------------
    # TODO 3: Hill Climbing
    # ----------------------
    def hill_climb(self, maximum=None, image_prefix=None, log=False):
        """
        TODO: Perform hill-climbing to place hospitals.

        Algorithm sketch:
        1) Initialize random positions for the hospitals.
        2) REPEAT:
            a) For each current hospital, try moving it to each of its neighbors.
            b) Evaluate the cost for each neighbor state (move just that one hospital).
            c) Track the neighbor(s) with the BEST (lowest) cost.
        3) If the best neighbor cost is NOT strictly LESS than the current cost:
               stop and return the current hospitals.
           Else:
               move to one of the best neighbors (break ties randomly).
        4) Stop if you reach 'maximum' iterations (if maximum is None, keep going til convergence).


        Visualization (Optional):
        - If image_prefix is provided, you can call:
              self.output_image(f"{image_prefix}{str(step).zfill(3)}.png")
          after each step to save frames.
        """
    
        pass

    
        def random_restart(self, maximum, image_prefix=None, log=False):
        """Repeats hill-climbing multiple times and keeps best hospital position."""
        pass

    # ---------------------------------
    # Provided: Image Output (Optional)
    # ---------------------------------
    def output_image(self, filename):
        """Generates image with all houses and hospitals."""
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 60
        cell_border = 1
        cost_size = 36
        padding = 8

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.width * cell_size,
             self.height * cell_size + cost_size + padding * 2),
            "white"
        )
        try:
            house = Image.open("assets/images/House.png").resize((cell_size, cell_size))
            hospital = Image.open("assets/images/Hospital.png").resize((cell_size, cell_size))
        except Exception:
            # Fallback: draw colored squares if assets are missing
            house = Image.new("RGBA", (cell_size, cell_size), (200, 60, 60, 255))
            hospital = Image.new("RGBA", (cell_size, cell_size), (60, 120, 200, 255))
        try:
            font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 24)
        except Exception:
            from PIL import ImageFont as _F
            font = _F.load_default()
        draw = ImageDraw.Draw(img)

        for i in range(self.height):
            for j in range(self.width):

                # Draw cell
                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                draw.rectangle(rect, fill="#222")

                if (i, j) in self.houses:
                    img.paste(house, rect[0], house)
                if (i, j) in self.hospitals:
                    img.paste(hospital, rect[0], hospital)

        # Add cost bar
        draw.rectangle(
            (0, self.height * cell_size, self.width * cell_size,
             self.height * cell_size + cost_size + padding * 2),
            "#000"
        )
        # Guard against calling before students implement get_cost
        try:
            cost_text = f"Cost: {self.get_cost(self.hospitals)}"
        except Exception:
            cost_text = "Cost: N/A"
        draw.text(
            (padding, self.height * cell_size + padding),
            cost_text,
            fill="white",
            font=font
        )

        img.save(filename)


# ----------------------
# Minimal Driver 
# ----------------------
if __name__ == "__main__":
    # Create a new space
    s = Space(height=8, width=14, num_hospitals=3)

    # Add some random houses (you can tweak this)
    for _ in range(15):
        s.add_house(random.randrange(s.height), random.randrange(s.width))

    # Run hill climbing (students should implement the TODOs)
    # Tip: set image_prefix="frames/step_" to save frames (ensure folder exists)
    hospitals = s.hill_climb(maximum=200, image_prefix=None, log=True)

    print("Hospitals placed at:", hospitals)
