import os
import random
from faker import Faker
from PIL import Image
import string

# Define the directory where the synthetic files will be created
output_dir = "synthetic_data"

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

fake = Faker()

# Categories and their associated words
categories = {
    "photography": [
        "portrait", "landscape", "sunset", "macro", "street",
        "reflection", "silhouette", "vintage", "blackandwhite", "HDR",
        "panorama", "bokeh", "dof", "candid", "monochrome",
        "exposure", "aperture", "composition", "shutter", "focus",
        "contrast", "lighting", "retouching", "colorgrading", "framing",
        "polaroid", "negative", "grain", "digitalart", "photoshop",
        "ruleofthirds", "goldenratio", "depthoffield", "ruleofodds", "leadinglines",
        "ruleofspace", "simmetry", "cropping", "burstmode", "highkey", "lowkey",
        "overexposure", "underexposure", "motionblur", "ruleofsymmetry", "candid",
        "portrait", "panning", "zoom", "infrared", "dutchangle"
    ],
    "programming": [
        "algorithm", "code", "database", "function", "variable",
        "compiler", "interpreter", "debugger", "syntax", "semantics",
        "IDE", "versioncontrol", "repository", "commit", "branch",
        "merge", "bug", "error", "exception", "runtime",
        "objectoriented", "procedural", "functional", "logic", "dynamic",
        "static", "testing", "unittest", "integration", "regression",
        "agile", "waterfall", "scrum", "Kanban", "SDLC",
        "HTTP", "API", "REST", "SOAP", "JSON",
        "XML", "SQL", "NoSQL", "frontend", "backend",
        "fullstack", "responsive", "UX", "UI", "algorithm",
        "datastructure", "BigO", "recursion", "iteration", "heap",
        "linkedlist", "binarytree", "stack", "queue", "hashmap",
        "linkedlist", "array", "pointer", "algorithm", "program",
        "script", "development", "coding", "logic", "software"
    ],
    "cooking": [
        "lasagna", "sushi", "burger", "soufflé", "risotto",
        "tiramisu", "omelette", "curry", "sashimi", "paella",
        "ratatouille", "schnitzel", "casserole", "padthai", "moussaka",
        "ceviche", "goulash", "calzone", "croissant", "dumplings",
        "carbonara", "gnocchi", "gratin", "kebabs", "tacos",
        "ramen", "crepe", "biryani", "couscous", "poutine",
        "pilaf", "quiche", "jambalaya", "tartare", "stroganoff",
        "okonomiyaki", "borsch", "lobsterbisque", "guacamole", "hummus",
        "chowder", "barbecue", "bruschetta", "cannoli", "pancake",
        "scone", "enchilada", "tostada", "nachos", "kale",
        "pepperoni", "strawberry", "lettuce", "spinach", "papaya",
        "rhubarb", "potato", "onion", "asparagus", "artichoke",
        "broccoli", "zucchini", "cabbage", "cauliflower", "garlic"
    ],
    "gaming": [
        "Minecraft", "The Legend of Zelda", "Fortnite", "Overwatch", "Sims",
        "World of Warcraft", "Call of Duty", "GTA V", "Red Dead Redemption", "Cyberpunk 2077",
        "Final Fantasy VII", "Resident Evil", "Super Mario", "Dark Souls", "Halo",
        "Uncharted", "Mortal Kombat", "FIFA", "PES", "League of Legends",
        "Dota 2", "Counter-Strike", "Battlefield", "Assassin's Creed", "Rainbow Six",
        "Doom", "Fallout", "Skyrim", "Pokémon", "The Witcher",
        "Mass Effect", "Metal Gear Solid", "Starcraft", "Diablo", "Borderlands",
        "Destiny", "Bioshock", "Half-Life", "Baldur's Gate", "Undertale",
        "Stardew Valley", "Terraria", "RimWorld", "Factorio", "Among Us",
        "Animal Crossing", "The Sims", "SimCity", "Civilization", "Age of Empires",
        "Command & Conquer", "Warcraft", "Star Wars", "Star Trek", "Hearthstone",
        "Cyberpunk 2077.mp4", "GTA V.mp4", "Red Dead Redemption.mp4", "Call of Duty.mp4", "Minecraft.mp4"
    ]
}

# Function to generate random text content
def generate_text_content(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

# Function to generate a simple code snippet
def generate_code_content():
    code = f"""def main():
    print("{generate_text_content(10)}")

if __name__ == "__main__":
    main()
"""
    return code

# Function to generate a random image
def generate_image_content(category):
    width, height = 200, 200
    img = Image.new("RGB", (width, height))
    pixels = img.load()

    for i in range(width):
        for j in range(height):
            r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            pixels[i, j] = (r, g, b)

    img.save(os.path.join(output_dir, f"{random.choice(categories[category])}.png"), "PNG")

# Create synthetic files
num_files = 1000  # Number of synthetic files to generate

for i in range(num_files):
    category = random.choice(list(categories.keys()))
    if category == "cooking":
        file_type = random.choice(["txt", "png", "mp4"])
    elif category == "gaming":
        file_type = random.choice(["exe", "png", "mp4"])
    else:
        file_type = random.choice(["txt", "py", "png"])

    file_name = f"{random.choice(categories[category])}.{file_type}"

    if file_type == "txt":
        content = generate_text_content(random.randint(100, 1000))
    elif file_type == "py":
        content = generate_code_content()
    elif file_type == "png":
        generate_image_content(category)
        content = "Image file"
    elif file_type == "exe":
        content = "Executable file"
    elif file_type == "mp4":
        content = "Video file"

    with open(os.path.join(output_dir, file_name), "w") as file:
        file.write(content)

print(f"Generated {num_files} synthetic files in the '{output_dir}' directory.")
