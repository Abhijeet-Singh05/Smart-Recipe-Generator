# ChefAI: Recipe Generator from image

A Full-Stack AI application that allow users to upload food ingridient images and it will generate creative recipes from them using **Google Gemini**.

## Features

* **AI Vision Analysis:** Upload a photo of any food or ingredient list, and the AI identifies it instantly.
* **Creative Recipe Generation:** Uses **Google Gemini** to invent detailed recipes based *only* on what it sees.
* **Cloud Image Storage:** Automatically uploads and hosts user images on **Cloudinary**.
* **Database:** Saves recipe, image URL, and upload timestamp to **MongoDB Atlas**.
* **Smart Video Linking:** AI intelligently searches and provides a **YouTube tutorial link** for the generated dish.
* **Clean UI:** A responsive, modern interface built with HTML5, CSS3, and  JavaScript.

##  Tech Stack
* **Backend:** Python, FastAPI, Uvicorn
* **AI:** Google Gemini (Generative AI)
* **Database:** MongoDB Cloudinary
* **Frontend:** HTML, CSS, JavaScript

##  How to Run
1. Clone the repo

2. Create a `.env` file and add your 
2.1 Google Gemini AI
GEMINI_API_KEY=your_gemini_key_here

2.2 Cloudinary (Image Storage)
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret

2.3 MongoDB (Database)
MONGODB_URL=your_mongodb_connection_string
DB_NAME=chef_db

3. Install dependencies: `pip install -r requirements.txt`

4. Run server: `python main.py`