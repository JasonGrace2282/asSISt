# asSISt
![Logo](assist_logo.png)

An app designed to help calculate grades from StudentVUE by Synergy.
![Screenshot of Application UI](https://github.com/JasonGrace2282/asSISt/assets/110117391/bd5c61d5-c0cc-46f3-885c-4b9fd20b164e)


- Native support for weighted gradebooks 💪
- Blazing fast grade recalculation ⏲️
- See the effect of multiple sets of assignments on your grade 🏆
- Faster loading speed than native SIS 🏃
- Minimalistic UI 🪶
- Cross-county compatibility 🤝🏻

## Installation Instructions

Run the following commands:
```bash
git clone https://github.com/JasonGrace2282/asSISt.git
cd asSISt
python3 -m pip install -r requirements.txt
python3 manage.py runserver # to host website locally
```
Then open [http://localhost:8000](http://localhost:8000) (or [http://127.0.0.1:8000/](http://127.0.0.1:8000/)) in your preferred web browser.

On future launches, all you should have to do is navigate to the cloned directory (`asSISt` in this case)
and run the last command

## Known Bugs
- The program crashes with an `IndexError` if the gradebook doesn't have any assignments
