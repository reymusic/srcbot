echo "Cloning Repo...."
git clone https://github.com/nikhivishwa/srcbot.git /srcbot
cd /srcbot
pip3 install -r requirements.txt
echo "Starting Bot...."
python3 main.py
