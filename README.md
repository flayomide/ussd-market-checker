# USSD Market Checker (Africa's Talking + Flask)

This is a simple USSD app built with Flask for farmers to check real-time market prices.

## How It Works
- User dials your USSD code (e.g. `*347*179#`)
- Backend (this app) returns product options
- User selects a crop
- Price is displayed and session ends

## Deployment Instructions
1. Push this repo to GitHub
2. Create a free account at [https://render.com](https://render.com)
3. Click "New Web Service" and connect your GitHub
4. Deploy using settings in `render.yaml`
5. Copy the live URL and add `/ussd` at the end
6. Paste that into your Africa’s Talking USSD callback field

🎉 You're live!

