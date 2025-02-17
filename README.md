# 🍽️ Image To Recipe Converter  

The Image-to-Recipe Converter is an AI-powered application that identifies food items from images and generates detailed step-by-step recipes. By simply uploading a food image, users can receive a comprehensive recipe, including ingredients and cooking instructions. This project combines computer vision and natural language processing to provide an interactive and seamless cooking experience, making it easier for users to discover new recipes and prepare meals based on what they have in their kitchen.

## 🚀 Project Overview  
This project utilizes computer vision and natural language processing (NLP) to classify food images and generate structured recipes based on the predicted dish.  

### 🔹 Features  
- Upload an image of food and get the predicted dish name.  
- Automatically generate a well-structured recipe using GPT-based models.  
- FastAPI backend for model inference and API responses.  
- Streamlit-based frontend for an interactive user experience.  

---

## 🛠️ Tech Stack  
### Backend:  
- **FastAPI** → Handles API requests and model inference.  
- **PyTorch/TensorFlow** → For image classification using CLIP/ViT models.  
- **Hugging Face Transformers** → For text generation (GPT-based recipe generation).  
- **OpenAI API/LangChain** → Enhancing recipe generation capabilities.  
- **spaCy & NLTK** → Text preprocessing and NLP utilities.  

### Frontend:  
- **Streamlit** → Interactive UI for image uploads and displaying results.  
- **PIL (Pillow)** → Image processing before sending requests to the backend.  
- **Requests** → API communication between Streamlit frontend and FastAPI backend.  

---

## 📌 Installation & Setup  

### 🔹 1. Clone the Repository  
```bash
git clone https://github.com/alokranjan1803/image-to-recipe.git
cd image-to-recipe
```
### 🔹 2. Install Dependencies
```bash
pip install -r requirements.txt
```
### 🔹 3. Run the Backend (FastAPI)
```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```
### 🔹 4. Run the Frontend (Streamlit)
```bash
streamlit run app.py
```

## 📌 Usage
1. Upload an image of a food item via the Streamlit UI.
2. The backend predicts the food category using CLIP/ViT.
3. The model generates a structured recipe using GPT-based text generation.
4. The output displays the predicted dish name along with a detailed recipe.

## 📸 Screenshots
![image](https://github.com/user-attachments/assets/395f6cd7-c996-41fb-b5cc-bb7aa55fda4f)
![image](https://github.com/user-attachments/assets/f9fde9dc-ef71-4637-848a-9e05e405e43c)
### Samosa Recipe
#### Ingredients:
1. 2 cups boiled potatoes, mashed
2. 1 cup mixed vegetables (peas, carrots, etc.), boiled
3. 1 medium onion, chopped
4. 2 green chilies, chopped
5. 1 tsp ginger-garlic paste
6. 1 tsp cumin seeds
7. 1 tsp coriander powder
8. 1 tsp garam masala
9. 1/2 tsp turmeric powder
10. 1 tsp red chili powder
11. Salt to taste
12. 1 tbsp oil

#### Instructions:
1. Heat oil in a pan, add cumin seeds, then sauté onions, chilies, and ginger-garlic paste.
2. Add boiled veggies and spices; cook for 5-7 minutes.
3. Cool the mixture and shape into small portions.
4. Fold samosa wrappers into cones, fill with the mixture, and seal the edges.
5. Heat oil in a pan and deep fry samosas until golden brown.
6. Serve hot with chutney or ketchup. Enjoy your crispy samosas! 🌶️🥔

## 📖 Future Enhancements
- **Improve food classification accuracy using fine-tuned models.**
- **Add multi-language support for recipe generation.**
- **Implement real-time ingredient recognition for more personalized recipes.**

## 💡 Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.



