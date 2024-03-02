# asSISt
![Logo](assist_logo.png)

An app designed to help calculate grades from StudentVUE by Synergy.
![Screenshot of Application UI](https://github.com/JasonGrace2282/hacktj24/assets/110117391/b245847e-a2d9-4924-a892-d26c84063c45)


- Native support for weighted gradebooks 💪
- Blazing fast grade recalculation ⏲️
- See the effect of multiple sets of assignments on your grade 🏆
- Faster loading speed than native SIS 🏃
- Lightweight and minimalistic UI 🪶
- Cross-county compatibility 🤝🏻
- Robust Framework for more extensibility 🤖

## Installation Instructions

Run the following commands:
```bash
git clone https://github.com/JasonGrace2282/hacktj24.git
cd hacktj24
python3 -m pip install -r requirements.txt
python3 -u main.py # to run the app
cd docs && python3 -m streamlit run website.py # to host site locally
```

## Known Bugs
- The program crashes with an `IndexError` if the gradebook doesn't have any assignments
