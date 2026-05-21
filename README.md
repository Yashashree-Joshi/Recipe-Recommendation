# 🍽️ AI Recipe Assistant (Ollama + Google Search)

A command-line recipe assistant that:
- Generates recipes using a **local AI model (Ollama)**
- Searches real recipes using **Google Custom Search**
- Uses keyword-based input with smart preprocessing

This project works **fully offline for AI generation** and **online for Google search**.

---

## ✨ Features

- 🧠 Local AI recipe generation (no OpenAI API needed)
- 🔍 Google recipe search option
- 🧺 Ingredient & taste preference detection
- ⚠️ Warnings for unclear inputs
- 🔐 Secure API key handling using `.env`
- 🖥️ Interactive CLI with exit support

---

## 🛠 Requirements

- Python 3.9+
- Ollama installed and running
- `llama3` model pulled
- Google Custom Search API (for search mode)

---

## 🚀 Setup Instructions

### 1️⃣ Clone or download the repository
(If downloading from GitHub website, extract the files)

### 2️⃣ Install Python dependencies

### 3️⃣ Setup Google API (Required for Search Option)

### 4️⃣ Setup Ollama

ollama pull llama3

---

### 🧑‍🍳 How to Use
Option 1: Generate Recipe (AI)

### Choose option 1

Enter at least 5 ingredients (comma-separated)

Add optional taste preferences like sweet, tangy, spicy

Wait while the recipe is generated

### Option 2: Search Recipe (Google)

Choose option 2

Enter ingredients

View real recipe links from Google


--- 

### Sample Output

<img width="322" height="202" alt="image" src="https://github.com/user-attachments/assets/c0d3a049-2213-4ed9-9c72-10955082bcf1" />
<img width="1566" height="263" alt="image" src="https://github.com/user-attachments/assets/6e5bf437-94eb-470f-9552-f7aacba33ea3" />

---

### 🛑 Exit

Type bye anytime to exit the program


