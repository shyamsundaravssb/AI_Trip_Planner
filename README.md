# 🌍 AI Trip Planner

An AI-powered travel planning agent that generates comprehensive, day-by-day trip itineraries with real-time data. Built with **LangGraph** for agentic workflows, **FastAPI** for the backend, and **Streamlit** for an interactive chat UI.

---

## ✨ Features

- **Agentic Workflow** — Uses LangGraph's `StateGraph` with a ReAct-style tool-calling loop to autonomously research and plan trips.
- **Dual Itineraries** — Generates two plans per request: one for popular tourist spots and another for off-beat, hidden-gem locations.
- **Real-Time Place Search** — Discovers attractions, restaurants, activities, and transportation via **Foursquare** with **Tavily** as a fallback.
- **Live Weather Data** — Fetches current conditions and multi-day forecasts from **OpenWeatherMap**.
- **Currency Conversion** — Converts costs between currencies in real-time using **ExchangeRate API**.
- **Expense Estimation** — Calculates hotel costs, total trip expenses, and daily budget breakdowns.
- **Markdown Export** — Saves each generated travel plan as a timestamped `.md` file in the `output/` directory.
- **Multi-Provider LLM Support** — Supports **Groq** (Llama 3.3 70B) and **OpenAI** as model providers.

---

## 🏗️ Architecture

```
AI_Trip_Planner/
├── main.py                  # FastAPI server with /query endpoint
├── streamlit_app.py         # Streamlit chat UI
├── agent/
│   └── agentic_workflow.py  # LangGraph StateGraph builder (ReAct agent)
├── tools/                   # LangChain tool wrappers
│   ├── place_search_tool.py       # Attractions, restaurants, activities, transport
│   ├── weather_info_tool.py       # Current weather & forecast
│   ├── currency_conversion_tool.py
│   └── expense_calculator_tool.py
├── utils/                   # Core service implementations
│   ├── model_loader.py      # Groq / OpenAI model loader
│   ├── place_info_search.py # Foursquare & Tavily search clients
│   ├── weather_info.py      # OpenWeatherMap client
│   ├── currency_converter.py
│   ├── expense_calculator.py
│   ├── save_to_document.py  # Markdown export utility
│   └── config_loader.py     # YAML config loader
├── config/
│   └── config.yaml          # Model provider & model name config
├── prompt_library/
│   └── prompt.py            # System prompt for the travel agent
├── output/                  # Generated travel plan documents
├── requirements.txt
├── setup.py
└── pyproject.toml
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.13+**
- API keys for the following services:

| Service                                               | Env Variable             | Purpose                  |
| ----------------------------------------------------- | ------------------------ | ------------------------ |
| [Groq](https://console.groq.com/)                     | `GROQ_API_KEY`           | LLM inference            |
| [Foursquare](https://developer.foursquare.com/)       | `FOURSQUARE_API_KEY`     | Place search             |
| [Tavily](https://tavily.com/)                         | `TRAVILY_API_KEY`        | Fallback web search      |
| [OpenWeatherMap](https://openweathermap.org/api)      | `OPENWEATHERMAP_API_KEY` | Weather data             |
| [ExchangeRate API](https://www.exchangerate-api.com/) | `EXCHANGE_RATE_API_KEY`  | Currency conversion      |
| [OpenAI](https://platform.openai.com/) _(optional)_   | `OPENAI_API_KEY`         | Alternative LLM provider |

### Installation

```bash
# Clone the repository
git clone https://github.com/shyamsundaravssb/AI_Trip_Planner.git
cd AI_Trip_Planner

# Create and activate a virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the project root with your API keys:

```env
GROQ_API_KEY=your_groq_api_key
FOURSQUARE_API_KEY=your_foursquare_api_key
TRAVILY_API_KEY=your_tavily_api_key
OPENWEATHERMAP_API_KEY=your_openweathermap_api_key
EXCHANGE_RATE_API_KEY=your_exchange_rate_api_key
```

You can also customize the LLM model in `config/config.yaml`:

```yaml
llm:
  groq:
    provider: "groq"
    model_name: "llama-3.3-70b-versatile"
```

---

## ▶️ Usage

### 1. Start the FastAPI Backend

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`. You can test it at `http://localhost:8000/docs` (Swagger UI).

### 2. Start the Streamlit Frontend

In a separate terminal:

```bash
streamlit run streamlit_app.py
```

Open the URL shown in the terminal (typically `http://localhost:8501`) and start planning your trip!

### Example Query

> _"Plan a 5-day trip to Goa with a budget of ₹50,000"_

The agent will autonomously:

1. Search for attractions, restaurants, and activities in Goa
2. Fetch current weather and forecasts
3. Calculate hotel costs and daily budgets
4. Generate a detailed day-by-day itinerary with cost breakdowns

---

## 🔌 API Reference

### `POST /query`

**Request Body:**

```json
{
  "question": "Plan a trip to Goa for 5 days"
}
```

**Response:**

```json
{
  "answer": "# 🌍 AI Travel Plan\n\n## Day 1: Arrival in Goa..."
}
```

---

## 🛠️ Tech Stack

| Layer                 | Technology                   |
| --------------------- | ---------------------------- |
| **LLM Orchestration** | LangGraph, LangChain         |
| **LLM Provider**      | Groq (Llama 3.3 70B), OpenAI |
| **Backend**           | FastAPI, Uvicorn             |
| **Frontend**          | Streamlit                    |
| **Place Search**      | Foursquare API, Tavily       |
| **Weather**           | OpenWeatherMap API           |
| **Currency**          | ExchangeRate API             |

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

**Shyam** — [shyamsundaravssb@gmail.com](mailto:shyamsundaravssb@gmail.com)
