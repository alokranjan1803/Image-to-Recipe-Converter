# 🍽️ Image-to-Recipe Converter  

A deep learning-based application that predicts food items from images and generates step-by-step recipes using NLP models.

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


## 📖 Future Enhancements
- **Improve food classification accuracy using fine-tuned models.**
- **Add multi-language support for recipe generation.**
- **Implement real-time ingredient recognition for more personalized recipes.**

## 💡 Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.



