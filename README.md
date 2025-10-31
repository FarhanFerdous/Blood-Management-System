# 🩸 Blood Management System

> *Because saving lives should have a good UX*

A Django-powered blood donation platform that's actually pleasant to use. Think Airbnb, but for... well, blood. (Okay, that came out weird, but you get the idea!)

Built with Django, DRF, and Bootstrap—this isn't your hospital's clunky 90s database interface. It's fast, modern, and comes with a demo mode that lets you play doctor (legally).

---

## 📸 Screenshots

<img width="1533" height="717" alt="Screenshot 2025-10-31 213617" src="https://github.com/user-attachments/assets/60b77c64-2ab2-4d23-876e-575f04938cdf" />
<img width="1509" height="606" alt="Screenshot 2025-10-31 213612" src="https://github.com/user-attachments/assets/835cc55b-3e8b-481b-a8b6-177adc455827" />
<img width="1434" height="554" alt="Screenshot 2025-10-31 213605" src="https://github.com/user-attachments/assets/5aab0cb8-3290-46ef-935b-eed340dc57ff" />
<img width="1575" height="708" alt="Screenshot 2025-10-31 213559" src="https://github.com/user-attachments/assets/dfc231e8-6386-4387-8826-e6c8fe1c908c" />
<img width="1449" height="856" alt="Screenshot 2025-10-31 213028" src="https://github.com/user-attachments/assets/7eb2697d-d050-4095-8d67-c920e6ee8cd3" />
<img width="1894" height="851" alt="Screenshot 2025-10-31 140553" src="https://github.com/user-attachments/assets/44f76ae1-29e6-4653-a089-c04557178e76" />
<img width="1907" height="622" alt="Screenshot 2025-10-31 140532" src="https://github.com/user-attachments/assets/8a33466f-9745-4482-a260-910ed8f382b6" />
<img width="1567" height="895" alt="Screenshot 2025-10-31 213634" src="https://github.com/user-attachments/assets/ad50a116-b647-4252-90cd-0ac3c7c6a58f" />



## ✨ What Makes This Cool?

**For Heroes (Donors)** 🦸
- Swanky dashboard showing off your donation street cred
- Profile with photo (yes, you can look good while doing good)
- Request blood when you or someone else needs it
- Track your donation history like Pokemon badges

**For Admins** 👨‍⚕️
- Command center dashboard with all the stats
- Approve or reject requests faster than you can say "universal donor"
- Manage blood inventory without losing your mind
- Search through donors like you're on Match.com (but wholesomer)

**For Developers** 🤓
- Clean REST APIs ready for your React/Vue/Svelte dreams
- Demo mode with one-click actions (because manual testing is so 2010)
- Dark/light theme toggle (your eyes will thank you)
- Bootstrap 5 responsive UI (mobile-friendly = more donors = more lives saved)

---

## 🎮 Demo Mode: Try Before You Apply

Hit up `/demo` and unleash your inner mad scientist:
- 🔴 **Create Request**: Instantly spawn a blood request (no actual bleeding required)
- ✅ **Approve Request**: Play admin and save the day
- 💉 **Create Donation**: Add units to inventory like a boss

It's basically a video game where the points are people not dying. High stakes!

---

## 🚀 Quick Start (Get This Baby Running)

### You'll Need
- Python 3.12+ (come on, stay current!)
- Git (obviously)
- Coffee ☕ (not technically required, but recommended)

### Let's Do This

```bash
# 1. Grab the code
git clone https://github.com/<your-username>/bms.git
cd bms

# 2. Virtual environment time (Windows PowerShell edition)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 3. Install all the goodies
pip install -r requirements.txt

# 4. Set up the database
python manage.py migrate

# 5. Load demo data (instant playground!)
python manage.py seed_demo

# 6. Fire it up!
python manage.py runserver
```

Now open `http://127.0.0.1:8000/` and watch the magic happen! ✨

---

## 🎭 Meet Your Test Accounts

**The Boss**
- Username: `admin` | Password: `Admin@123`
- *Has all the power, handles all the responsibility*

**The Manager**
- Username: `staff` | Password: `Staff@123`
- *Gets stuff done, asks fewer questions*

**The Heroes**
- `donor1` / `Donor1@123` → Type A+ hero from Dhaka
- `donor2` / `Donor2@123` → Type O- universal savior from Chittagong
- `donor3` / `Donor3@123` → Type B+ champion from Sylhet

---

## 🗺️ Where's Everything At?

### The Good Stuff (UI)
```
/                    → Home sweet home
/login/              → Get in here
/register/           → Join the cause
/dashboard/donor/    → Donor HQ
/dashboard/admin/    → Admin control center
/donors/             → Find your match
/requests/new/       → Need blood? Start here
/demo                → Playground mode
```

### The API Sauce
```
/api/donors/profiles/       → All the donors
/api/banks/inventory/       → Stock check
/api/donations/donations/   → Donation records
/api/donations/requests/    → Blood requests
```

**Pro tip:** Login through the UI first, then your API calls inherit the session. It's like magic, but it's actually just cookies.

---

## 🏗️ Under The Hood

```
bms/                    # The brain (settings, URLs)
├─ accounts/           # Login/logout/register jazz
├─ donors/             # Donor profiles & hero stats
├─ banks/              # Blood banks & inventory magic
├─ donations/          # Donations & requests
├─ dashboards/         # Pretty dashboards
├─ templates/          # Bootstrap goodness
└─ static/             # Custom CSS (Bootstrap is CDN-ed)
```

---

## 🧬 The Data Science

**DonorProfile** (The Heroes)
- Linked to User account
- Blood type, phone, city, availability status
- Last donation date (we track recovery times!)
- Photo (for that professional donor look)

**BloodBank & BloodInventory** (The Storage)
- Multiple banks, each with its own inventory
- Tracks units per blood type
- Unique constraint per bank + blood type combo

**Donation & BloodRequest** (The Action)
- Donations: who gave, how much, when
- Requests: who needs, what type, urgency level
- Status tracking: pending → approved/rejected

---

## 🎯 Business Rules (aka "Don't Break The System")

✅ **DO:**
- Use valid blood types (A±, B±, AB±, O±)
- Wait for recovery between donations
- Have enough inventory before approving requests

❌ **DON'T:**
- Try to store blood type "unicorn tears"
- Approve requests when inventory is empty
- Forget to upload Pillow for photo support

---

## 🚢 Ship It to Production

### General Wisdom
- Set `DEBUG=False` (seriously, do this)
- Add your domain to `ALLOWED_HOSTS`
- Use real database (PostgreSQL > SQLite for prod)
- Set up cloud storage for media files (S3, Cloudinary, etc.)

### Deploy to Render
1. Push to GitHub (commit your changes first, genius)
2. Create Web Service on Render
3. Build: `pip install -r requirements.txt && python manage.py migrate`
4. Start: `gunicorn bms.wsgi:application --preload --bind 0.0.0.0:$PORT`
5. Set env vars: `PYTHON_VERSION=3.12`, `DEBUG=False`

### Deploy to PythonAnywhere
1. Upload via Git or file upload
2. Create virtualenv: `mkvirtualenv --python=/usr/bin/python3.12 mysite`
3. Install: `pip install -r requirements.txt`
4. Configure WSGI to point at `bms.wsgi`
5. Run migrations once: `python manage.py migrate`
6. Map static/media directories in PA dashboard

**"Static files not loading"**
- Dev: Make sure `static/` folder exists (create it if missing)
- Prod: Run `python manage.py collectstatic`

**"API returns 403 Forbidden"**
- Login through the UI first (session auth)
- Or set up token authentication if you're going headless

---

## 🤝 Wanna Contribute?

Hell yeah! Here's how:

1. **Fork it** (top right button on GitHub)
2. **Branch it** (`git checkout -b feature/mind-blowing-feature`)
3. **Code it** (make it awesome)
4. **Commit it** (`git commit -m "Add mind-blowing feature"`)
5. **Push it** (`git push origin feature/mind-blowing-feature`)
6. **PR it** (Open a Pull Request)

For big changes, open an issue first so we can chat about it!

---
## 🛠️ Tech Stack (For The Nerds)

- **Django 5** - Because we're not living in the past
- **Django REST Framework** - APIs that don't suck
- **django-filter** - Search without the headache
- **Bootstrap 5** - Making ugly, beautiful since 2021
- **SQLite** - Dev database (upgrade for prod!)
- **Your enthusiasm** - The most important ingredient

---

## 📜 License

MIT License - Do whatever you want, just don't sue us.

---

## 💭 Final Thoughts

This is more than just code—it's a platform that could genuinely help save lives. Whether you're building this for a school project, a local blood bank, or just to learn Django, remember: every line of code you write here has the potential to make a real difference.

Now go forth and build something awesome! 🚀

---

**Questions? Issues? High-fives?**  
Open an issue on GitHub or slide into the PRs. We're friendly, I promise.

**Star this repo if it helped you!** ⭐  
*Your GitHub profile will thank you, and so will the next person who finds this.*
