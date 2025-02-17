import uvicorn
import nest_asyncio
import torch
import io
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from transformers import pipeline, CLIPProcessor, CLIPModel
from PIL import Image

# Initialize FastAPI
app = FastAPI()

# Load CLIP Model for Image Classification
clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# Load GPT-2 Model for Recipe Generation
generator = pipeline("text-generation", model="gpt2")

# Define Food Categories
food_classes = [
    "Biryani", "Butter Chicken", "Paneer Tikka", "Dal Makhani", "Chole Bhature", "Dosa", "Idli", "Vada Pav",
    "Pav Bhaji", "Samosa", "Pani Puri", "Tandoori Chicken", "Aloo Paratha", "Rogan Josh", "Malai Kofta", "Korma",
    "Momos", "Hyderabadi Biryani", "Pizza", "Pasta", "Lasagna", "Ravioli", "Risotto", "Bruschetta", "Gnocchi",
    "Carbonara", "Tiramisu", "Burger", "Hot Dog", "Fried Chicken", "Grilled Cheese", "BBQ Ribs", "Buffalo Wings",
    "Mac and Cheese", "Pancakes", "Waffles", "Brownie", "Cheesecake", "Tacos", "Burrito", "Quesadilla", "Nachos",
    "Churros", "Guacamole", "Fajitas", "Fried Rice", "Chow Mein", "Spring Rolls", "Dumplings", "Sweet and Sour Chicken",
    "Peking Duck", "Mapo Tofu", "Hot and Sour Soup", "Gyoza", "Sushi", "Ramen", "Tempura", "Udon", "Miso Soup",
    "Takoyaki", "Onigiri", "Hummus", "Falafel", "Shawarma", "Kebab", "Baba Ganoush", "Tabbouleh", "Croissant",
    "Baguette", "Quiche", "Ratatouille", "Crème Brûlée", "French Toast", "Curry", "Steak", "Sandwich", "Soup",
    "Noodles", "Ice Cream", "Fries", "Donuts", "Salad", "Pudding", "Gulab Jamun", "Halwa", "Tandoori Roti",
    "Kimchi", "Kimchi Fried Rice", "Ceviche", "Paella", "Pho", "Empanadas", "Bibimbap", "Shakshuka", "Schnitzel"
]

@app.get("/")
def read_root():
    return {"message": "FastAPI is running successfully!"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    """Predicts the food category from an image and generates a recipe using GPT-2."""
    
    try:
        # Read Image File
        image = Image.open(io.BytesIO(await file.read()))

        # Process Image using CLIP
        inputs = clip_processor(
            images=image, 
            text=food_classes, 
            return_tensors="pt",
            padding=True, 
            truncation=True
        )
        outputs = clip_model(**inputs)

        # Determine the most probable food category
        probs = torch.softmax(outputs.logits_per_image, dim=1)
        predicted_food = food_classes[torch.argmax(probs).item()]

        # Generate Recipe Prompt
        prompt = f"""
        Provide a well structured, detailed and step-by-step recipe for {predicted_food} . 

        
        """

        # Generate Recipe using GPT-2
        recipe = generator(
            prompt,
            max_length=300,  # Reduced max length to avoid excessive text
            num_return_sequences=1,
            truncation=True,
            pad_token_id=50256
        )

        return JSONResponse({
            "food_category": predicted_food,
            "recipe": recipe[0]["generated_text"]
        })

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Apply nest_asyncio to avoid runtime issues
nest_asyncio.apply()

# Run FastAPI in a separate thread
import threading
threading.Thread(target=uvicorn.run, args=(app,), kwargs={"host": "0.0.0.0", "port": 8000, "log_level": "info"}).start()
