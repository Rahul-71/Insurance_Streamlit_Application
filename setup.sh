mkdir -p ~/.streamlit/
echo "[general]
email = "rahultiwari.201307@gmail.com"
" > ~/.streamlit/credentials.toml
echo "[server]
headless = true
enableCORS=false
port = $PORT
" > ~/.streamlit/config.toml