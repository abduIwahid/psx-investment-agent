# PSX Investment Agent

An AI investment analyst that specializes in the **Pakistan Stock Exchange (PSX)** while covering global markets too. Ask it to compare stocks and it pulls live prices, fundamentals and analyst recommendations, then presents a structured, table-based analysis with actionable insights.

## What it does

- Live stock data through Yahoo Finance tools — prices, fundamentals, analyst recommendations
- Side-by-side comparisons of PSX and global stocks in clean markdown tables
- PSX-aware out of the box: it knows Pakistani listings trade with the `.KA` suffix (OGDC.KA, LUCK.KA, HBL.KA, …)
- Runs on AgentOS, so you get a proper agent chat UI in the browser

## Tech stack

- **Agno + AgentOS** — agent framework and UI
- **Google Gemini 2.5 Flash** — reasoning model
- **yfinance (Yahoo Finance)** — market data

## Run it locally

```bash
pip install -r requirements.txt
# set your free Google AI Studio key first
export GOOGLE_API_KEY=<redacted>
python investment_agent.py
```

Then open the AgentOS playground URL printed in the terminal and start asking.

## Example questions

- "Compare OGDC.KA and PPL.KA — which looks stronger on fundamentals?"
- "How has LUCK.KA performed over the last year?"
- "Compare HBL.KA and MCB.KA for a long-term investor."
- "AAPL vs MSFT — quick comparison."

> Educational tool only — not financial advice.

## Author

**Abdul Wahid** — AI/ML Developer
[Portfolio](https://www.abdulwahid.me) · [GitHub](https://github.com/abduIwahid) · [LinkedIn](https://www.linkedin.com/in/abdu1wahid)

## Credits

Adapted from a template in the [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) collection by Shubham Saboo, reworked for PSX coverage and Gemini. Licensed under Apache-2.0 — see [LICENSE](LICENSE).
