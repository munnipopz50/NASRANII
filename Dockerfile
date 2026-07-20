# 1. ബേസ് ഇമേജ് (Python-ന്റെ ലേറ്റസ്റ്റ് വേർഷൻ)
FROM python:3.10-slim

# 2. വർക്കിംഗ് ഡയറക്ടറി സെറ്റ് ചെയ്യുക
WORKDIR /app

# 3. ആവശ്യമായ ലൈബ്രറികൾ ഇൻസ്റ്റാൾ ചെയ്യുക
# ആദ്യം requirements.txt കോപ്പി ചെയ്ത് ഇൻസ്റ്റാൾ ചെയ്യുന്നു (ഇതാണ് നല്ല രീതി)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. ബാക്കി എല്ലാ കോഡ് ഫയലുകളും കോപ്പി ചെയ്യുക
COPY . .

# 5. ബോട്ട് റൺ ചെയ്യാനുള്ള കമാൻഡ്
CMD ["python3", "bot.py"]
