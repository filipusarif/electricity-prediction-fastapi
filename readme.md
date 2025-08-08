# 🇯🇵 Japan Electricity Consumption API 🔌

A **FastAPI-based REST API** for predicting electricity consumption in Japan’s **residential** and **industrial** sectors. This API also provides simple yet effective **visualization endpoints** for forecast and price sensitivity.

---

## 🚀 Features

- 🔮 Predict electricity consumption for:
  - Residential sector
  - Industrial sector
- 📈 Visualize 10-year forecast (residential)
- 💸 Visualize consumption sensitivity to real price changes (residential)
- 🖼️ Return plots as **base64-encoded images** (easy integration with frontend)

---

## 🧠 Models

The API loads two pre-trained machine learning models saved as pipelines:

- `./models/pipeline_res.pkl` — Residential electricity consumption predictor
- `./models/pipeline_ind.pkl` — Industrial electricity consumption predictor

These models were trained on historical electricity data from Japan (1990–2015).

---

## 🛠️ Installation

### 1. Clone this repository

```bash
git clone https://github.com/your-username/electricity-japan-fastapi.git
cd electricity-japan-fastapi
```

Here is the **full markdown README.md** file in English, tailored for your FastAPI project:

---

````markdown
# 🇯🇵 Japan Electricity Consumption API 🔌

A **FastAPI-based REST API** for predicting electricity consumption in Japan’s **residential** and **industrial** sectors. This API also provides simple yet effective **visualization endpoints** for forecast and price sensitivity.

---

## 🚀 Features

- 🔮 Predict electricity consumption for:
  - Residential sector
  - Industrial sector
- 📈 Visualize 10-year forecast (residential)
- 💸 Visualize consumption sensitivity to real price changes (residential)
- 🖼️ Return plots as **base64-encoded images** (easy integration with frontend)

---

## 🧠 Models

The API loads two pre-trained machine learning models saved as pipelines:

- `./models/pipeline_res.pkl` — Residential electricity consumption predictor
- `./models/pipeline_ind.pkl` — Industrial electricity consumption predictor

These models were trained on historical electricity data from Japan (1990–2015).

---

## 🛠️ Installation

### 1. Clone this repository

```bash
git clone https://github.com/your-username/electricity-japan-fastapi.git
cd electricity-japan-fastapi
````

### 2. Create a virtual environment and activate it

```bash
python -m venv env
# For Windows:
env\Scripts\activate
# For macOS/Linux:
source env/bin/activate
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI server

```bash
uvicorn main:app --reload
```

Then, open your browser and go to:
🔗 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📦 API Endpoints

### 📍 `POST /predict/residential`

Predict electricity consumption for the **residential sector**.

#### Request Example:

```json
{
  "Region": 9,
  "Year": 2025,
  "Intensity": 3000.0,
  "NominalPrice": 20.0,
  "RealPrice": 150.0
}
```

#### Response Example:

```json
{
  "prediction_kwh": 2345.67
}
```

---

### 📍 `POST /predict/industrial`

Predict electricity consumption for the **industrial sector**.

#### Request: same format as residential

#### Response:

```json
{
  "prediction_kwh": 4321.89
}
```

---

### 📍 `POST /visualize/residential/forecast`

Generate a **10-year forecast** visualization for residential electricity usage.

#### Request Example:

```json
{
  "Region": 9,
  "Year": 2025,
  "Intensity": 3000.0,
  "NominalPrice": 20.0,
  "RealPrice": 150.0
}
```

#### Response:

```json
{
  "image_base64": "<base64-encoded-image>"
}
```

> You can decode the base64 string into an image on the frontend or using any decoder.

---

### 📍 `POST /visualize/residential/price-sensitivity`

Visualize how **changes in real price** affect residential electricity consumption.

#### Response:

```json
{
  "image_base64": "<base64-encoded-image>"
}
```

---

## 🧪 Test with Thunder Client or Postman

* Method: `POST`
* URL: `http://localhost:8000/predict/residential`
* Body (JSON):

```json
{
  "Region": 9,
  "Year": 2025,
  "Intensity": 3000.0,
  "NominalPrice": 20.0,
  "RealPrice": 150.0
}
```

---

## 📁 Project Structure

```
electricity-japan-fastapi/
│
├── models/
│   ├── pipeline_res.pkl
│   └── pipeline_ind.pkl
│
├── schemas.py
├── main.py
├── requirements.txt
└── README.md
```

---

## 📚 Tech Stack

* ⚡ FastAPI
* 📦 Joblib
* 📊 Matplotlib
* 🧮 Pandas
* ✅ Pydantic
* 🧪 Uvicorn (ASGI server)

---

## 👤 Author

**Filipus Arif Kristiyan**

> Researcher in energy forecasting and smart systems

---

## 📜 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

```

---

Let me know if you'd like help generating the `requirements.txt`, creating the `schemas.py`, or decoding the base64 image in a frontend like Streamlit or React.
```
