#  Notes App - AWS EC2 t3.micro Production Deployment

**Full-stack Flask notes app + production AWS deployment (10-second redeploy)**

##  Production Achievements
**AWS EC2 t3.micro** - Mumbai (ap-south-1) - Successfully deployed  
**VPC + Public Subnet** - Fixed route table (0.0.0.0/0 → IGW)  
**Security Groups** - SSH(22) + App(5000) production config  
**Amazon Linux 2** - yum package management + systemctl fixes  
**restart.sh** - 10-second production redeploy script  
**Cost Optimization** - Stop/start Free Tier strategy (₹0)  

## Tech Stack
Backend: Flask + Gunicorn + Flask-SQLAlchemy + SQLite
Infra: AWS EC2 t3.micro + VPC + Security Groups
Deployment: Git → EC2 (10-second restart.sh)

## Production Deployment (5 minutes first time)
```bash
# Launch EC2 t3.micro (Amazon Linux 2)
sudo yum install git python3-pip -y
git clone https://github.com/atharvakadam-7/notes-app
cd notes-app
pip3 install -r requirements.txt
gunicorn app:app --bind 0.0.0.0:5000 &

```
 10-Second Redeploy (After EC2 Stop/Start)
cd ~ && ./restart.sh  # → LIVE on NEW_IP:5000!
Repository Files
app.py              # Flask + SQLite ORM (production)
requirements.txt    # Dependencies (your original)
templates/          # Your HTML templates  
restart.sh          # 10-second redeploy automation
Real-World Skills Demonstrated
AWS Production Networking - VPC/Subnet/Route Tables troubleshooting

EC2 t3.micro - Instance Connect + Security Group configuration

Linux Package Management - Amazon Linux (yum) vs Ubuntu (apt)

Production Deployment - Gunicorn + persistent SQLite database

Cost Management - Free Tier t3.micro optimization (₹0)

 Cost Strategy
 t3.micro = FREE TIER (750 hours/month)
 Stop when not demoing = 100% free
 Start → ./restart.sh → LIVE in 10 seconds
