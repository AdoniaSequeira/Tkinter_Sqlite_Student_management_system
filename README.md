# 📚 Student Information System & Performance Manager

A feature-rich desktop application built with **Python (Tkinter)** that allows educational institutions to manage student records seamlessly. This system supports **CRUD operations**, visual performance analysis, and integrates **real-time utilities** like weather updates and motivational quotes to enhance user engagement.

---

## 🚀 Features

### 🎯 Core Functionalities

- **Add, View, Update, Delete Student Records** via an intuitive Tkinter GUI  
- **Data validation** to ensure input integrity (name, roll number, marks)  
- **SQLite integration** for local, persistent storage  

### 📊 Performance Analytics

- Generate and display **bar charts** of top 5 students based on marks using Matplotlib  
- **Export charts to PDF** with timestamped filenames for academic reporting  

### 🌐 Real-time Add-ons

- **Quote of the Day** from BrainyQuote (web scraped via BeautifulSoup)  
- **Current Temperature & Location** using IPInfo and OpenWeather APIs  

### 📁 Modular GUI Windows

- Multiple Toplevel windows: Add Student, View Student, Update Student, Delete Student  
- Consistent and clean UI design using Tkinter components  

---

## 🛠️ Tech Stack

| Component          | Technology                       |
| ------------------ | ------------------------------- |
| GUI                | Tkinter                          |
| Database           | SQLite3                          |
| Data Visualization | Matplotlib                       |
| Web APIs           | requests, BeautifulSoup          |
| APIs Used          | IPInfo, OpenWeather, BrainyQuote |

---

## 🧠 Input Validation

- **Roll Number**: Must be a positive integer  
- **Name**: Must contain only alphabets, min 2 characters  
- **Marks**: Must be between 0 and 100  

Automatic error handling using `tkinter.messagebox.showerror()` with rollback support for invalid transactions.

---

## 📦 File Structure

```
student_management/
├── main.py                  # Main application script
├── management.db            # SQLite database file (auto-generated)
├── chart_<timestamp>.pdf    # Exported performance chart
├── README.md                # Project documentation
```

---

## 🧪 How to Run

1. Install required libraries:

```bash
pip install requests beautifulsoup4 matplotlib
```

2. Run the application:

```bash
python main.py
```

3. The main menu will launch with all functionality accessible via buttons.

---

## 🧾 Credits

- **OpenWeatherMap API** – Weather data  
- **IPInfo.io** – Geolocation via IP  
- **BrainyQuote.com** – Daily motivational quote  
- **Matplotlib** – Chart generation  
- **BeautifulSoup** – Web scraping  

---

## 👩‍💻 Author

**Adonia Sequeira**  
M.S. Computer Science @ George Washington University (May 2025)  
Award-winning student employee | Developer focused on Software, AI/ML, Cloud, Data & UI/UX  
🔗 [LinkedIn](https://linkedin.com/in/adonia-sequeira)  
🌐 [Portfolio](https://adoniasequeira.github.io/Adonia_Sequeira.github.io)

---

## 🏁 Future Improvements

- Implement student performance trend analytics over time  
- Add login/authentication for multi-user support  
- Improve UI responsiveness and design using `ttk` or frameworks like PyQt5  
- Add export-to-Excel option for broader compatibility  

