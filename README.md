<div align="center">

<img src="assets/header.svg" width="100%" alt="RadioSkyLab: radio astronomy data analysis and visualisation"/>

<br/>

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&duration=3200&pause=900&color=F5B700&center=true&vCenter=true&width=760&lines=Load+real+FITS+radio+images+%F0%9F%93%A1;Visualise+radio+intensity+%F0%9F%8C%8C;Measure+image+statistics+%F0%9F%93%8A;Run+basic+quality+checks+%E2%9C%85;Explore+everything+in+a+Streamlit+dashboard+%E2%9A%A1" alt="Typing animation"/>
</a>

<br/><br/>

![Python](https://img.shields.io/badge/Python-3.9%2B-0B1F3A?style=for-the-badge&logo=python&logoColor=F5B700)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-14B8A6?style=for-the-badge&logo=streamlit&logoColor=white)
![Astropy](https://img.shields.io/badge/Astropy-FITS-F5B700?style=for-the-badge&logoColor=0B1F3A)
![NumPy](https://img.shields.io/badge/NumPy-Arrays-0B1F3A?style=for-the-badge&logo=numpy&logoColor=14B8A6)
![Pandas](https://img.shields.io/badge/Pandas-Tables-14B8A6?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Plots-F5B700?style=for-the-badge&logoColor=0B1F3A)

![Status](https://img.shields.io/badge/Status-In%20Development-F5B700?style=flat-square)
![Domain](https://img.shields.io/badge/Domain-Radio%20Astronomy-14B8A6?style=flat-square)
![Data](https://img.shields.io/badge/Data-FITS-0B1F3A?style=flat-square)
![Survey](https://img.shields.io/badge/FIRST%20Survey-Planned-F5B700?style=flat-square)
![Last commit](https://img.shields.io/github/last-commit/LuthandoCandlovu/RadioSkyLab?style=flat-square&color=14B8A6)
![Stars](https://img.shields.io/github/stars/LuthandoCandlovu/RadioSkyLab?style=flat-square&color=F5B700)

<br/>

[**✨ Features**](#-features) &nbsp;•&nbsp;
[**🧭 How it works**](#-how-it-works) &nbsp;•&nbsp;
[**🖥️ Dashboard**](#%EF%B8%8F-dashboard-tour) &nbsp;•&nbsp;
[**🚀 Quick start**](#-quick-start) &nbsp;•&nbsp;
[**🐍 Python usage**](#-use-the-data-in-python) &nbsp;•&nbsp;
[**📚 Primer**](#-radio-astronomy-primer) &nbsp;•&nbsp;
[**🗺️ Roadmap**](#%EF%B8%8F-roadmap) &nbsp;•&nbsp;
[**❓ FAQ**](#-faq)

</div>

<img src="assets/divider.svg" width="100%" alt=""/>

## 📑 Table of contents

<details open>
<summary><b>Click to collapse or expand</b></summary>

<br/>

| # | Section | What you will find |
|:-:|:--------|:-------------------|
| 1 | [🌌 Overview](#-overview) | What RadioSkyLab is and who it is for |
| 2 | [🎬 Demo](#-demo) | A look at the dashboard |
| 3 | [✨ Features](#-features) | Everything the project does today |
| 4 | [🧭 How it works](#-how-it-works) | Pipeline and data flow diagrams |
| 5 | [🖥️ Dashboard tour](#%EF%B8%8F-dashboard-tour) | A walk through the Streamlit app |
| 6 | [🛠️ Technology](#%EF%B8%8F-technology) | The stack and why each tool is here |
| 7 | [📂 Project structure](#-project-structure) | Where things live |
| 8 | [🚀 Quick start](#-quick-start) | Install and run in a few minutes |
| 9 | [🐍 Use the data in Python](#-use-the-data-in-python) | Code examples for FITS files |
| 10 | [📊 Understanding the statistics](#-understanding-the-statistics) | What each number means |
| 11 | [✅ Quality checks](#-quality-checks) | What to look for in your data |
| 12 | [📚 Radio astronomy primer](#-radio-astronomy-primer) | Short guide to the science |
| 13 | [📡 Data and the FIRST survey](#-data-and-the-first-survey) | Where data comes from |
| 14 | [🗺️ Roadmap](#%EF%B8%8F-roadmap) | What is done and what is next |
| 15 | [🧰 Troubleshooting](#-troubleshooting) | Fixes for common problems |
| 16 | [❓ FAQ](#-faq) | Quick answers |
| 17 | [🤝 Contributing](#-contributing) | How to help |
| 18 | [📖 References](#-references-and-credits) | Papers and tools behind the project |
| 19 | [⚠️ Disclaimer](#%EF%B8%8F-disclaimer) | Scientific limits |
| 20 | [👤 Author](#-author) | Who built it |

</details>

<img src="assets/divider.svg" width="100%" alt=""/>

## 🌌 Overview

**RadioSkyLab** is a Python-based scientific computing project for **inspecting and analysing radio astronomy FITS images**.

Radio telescopes do not take photographs. They measure faint radio emission from the sky and store it as numbers in files, most often in the **FITS** format. Before any serious science can happen, someone has to open those files, look at the data, and ask a simple question: *is this image any good?*

RadioSkyLab answers that question quickly. You load an observation, see the radio intensity as a picture, read a set of summary statistics, run basic quality checks, and do it all from a clean, interactive dashboard.

### 🎯 Who is it for?

| Audience | How RadioSkyLab helps |
|:---------|:----------------------|
| 🎓 **Students** | Learn what a radio image really contains, using real FITS data |
| 🔬 **Early-career researchers** | Get a fast first look at an observation before deeper processing |
| 🛠️ **Developers** | A readable Python codebase for scientific image analysis |
| 🌍 **Educators and outreach teams** | An interactive way to show how radio data is explored |

### 💡 Design goals

- **Clear.** Every number and every plot should be easy to read and easy to explain.
- **Honest.** Exploratory results are labelled as exploratory. See the [disclaimer](#%EF%B8%8F-disclaimer).
- **Real data first.** Built around real FITS observations, not toy images.
- **Simple to run.** One virtual environment, one install command, one run command.
- **Open to growth.** The structure leaves room for survey integration and calibrated workflows.

<img src="assets/divider.svg" width="100%" alt=""/>

## 🎬 Demo

<div align="center">

<!-- 🎬 Record your Streamlit dashboard and save it as docs/demo.gif -->
<img src="docs/demo.gif" alt="RadioSkyLab dashboard demo" width="88%"/>

<sub>📸 Put a screen recording at <code>docs/demo.gif</code> and it appears here.<br/>Tip: keep it under 10 MB and about 10 to 15 seconds long.</sub>

</div>

<details>
<summary><b>🎥 How to record a good demo GIF</b></summary>

<br/>

1. Start the app with `streamlit run app.py`.
2. Open a screen recorder such as **ScreenToGif** (Windows), **Peek** (Linux) or **Kap** (macOS).
3. Record this short story: load a FITS file, show the intensity map, scroll to the statistics, show the quality checks.
4. Export as GIF at about 12 to 15 frames per second and a width near 900 px.
5. Save it as `docs/demo.gif` and commit it.

You can also add still screenshots to `docs/` and link them like this:

```markdown
![Intensity map](docs/intensity-map.png)
```

</details>

<img src="assets/divider.svg" width="100%" alt=""/>

## ✨ Features

<table>
<tr>
<td width="33%" valign="top">

### 📡 FITS loading

Open real astronomical observations with **Astropy**.

- Reads image data from FITS files
- Works with the standard header and data layout
- Built on the tool the astronomy community already uses

</td>
<td width="33%" valign="top">

### 🌈 Intensity visualisation

See the radio sky as an image with **Matplotlib**.

- Colour-mapped intensity view
- Clear axes and colour bar
- Easy to compare different observations

</td>
<td width="33%" valign="top">

### 📊 Image statistics

Summarise the data with **NumPy** and **Pandas**.

- Central values and spread
- Minimum and maximum
- Tidy tables you can read at a glance

</td>
</tr>
<tr>
<td width="33%" valign="top">

### ✅ Quality checks

Catch problem data early.

- Basic image quality checks
- Helps decide if a file is worth deeper analysis
- Designed to be extended with new checks

</td>
<td width="33%" valign="top">

### ⚡ Streamlit dashboard

Explore without writing code.

- Runs in your browser
- Interactive and responsive
- No notebook setup needed

</td>
<td width="33%" valign="top">

### 🛰️ Survey ready

Prepared for survey data.

- Built for real FITS observations
- **FIRST** survey integration planned
- Astroquery is part of the stack

</td>
</tr>
</table>

### 🧾 Feature summary

| Capability | Status | Powered by |
|:-----------|:------:|:-----------|
| FITS image loading | ✅ Available | Astropy |
| Radio intensity visualisation | ✅ Available | Matplotlib |
| Image statistics | ✅ Available | NumPy, Pandas |
| Basic image quality checks | ✅ Available | NumPy |
| Streamlit dashboard | ✅ Available | Streamlit |
| FIRST survey integration | 🛠️ Planned | Astroquery |
| Calibrated analysis workflows | 🔭 Future | To be decided |

<img src="assets/divider.svg" width="100%" alt=""/>

## 🧭 How it works

RadioSkyLab follows a simple pipeline. A FITS file goes in. A set of views and measurements come out.

```mermaid
flowchart LR
    A[📡 FITS file] --> B[🔭 Astropy loader]
    B --> C[🧮 NumPy and Pandas]
    C --> D[✅ Quality checks]
    C --> E[📊 Statistics]
    C --> F[🌈 Matplotlib plots]
    D --> G[⚡ Streamlit dashboard]
    E --> G
    F --> G

    style A fill:#0B1F3A,stroke:#F5B700,color:#fff
    style B fill:#0B1F3A,stroke:#14B8A6,color:#fff
    style C fill:#0B1F3A,stroke:#14B8A6,color:#fff
    style D fill:#14B8A6,stroke:#0B1F3A,color:#0B1F3A
    style E fill:#14B8A6,stroke:#0B1F3A,color:#0B1F3A
    style F fill:#14B8A6,stroke:#0B1F3A,color:#0B1F3A
    style G fill:#F5B700,stroke:#0B1F3A,color:#0B1F3A
```

### 🔁 What happens when you open a file

```mermaid
sequenceDiagram
    autonumber
    actor You
    participant UI as ⚡ Streamlit app
    participant IO as 🔭 Astropy FITS reader
    participant NP as 🧮 NumPy and Pandas
    participant PL as 🌈 Matplotlib

    You->>UI: Choose a FITS file
    UI->>IO: Open the file
    IO-->>UI: Header and image array
    UI->>NP: Clean and summarise the array
    NP-->>UI: Statistics and check results
    UI->>PL: Draw the intensity map
    PL-->>UI: Figure
    UI-->>You: Image, statistics and quality report
```

### 🧱 Layers of the project

```mermaid
flowchart TB
    subgraph L1[Presentation]
        S[Streamlit dashboard]
    end
    subgraph L2[Analysis]
        ST[Statistics]
        QC[Quality checks]
        VZ[Visualisation]
    end
    subgraph L3[Data access]
        FI[FITS loading]
        SV[Survey access, planned]
    end
    S --> ST
    S --> QC
    S --> VZ
    ST --> FI
    QC --> FI
    VZ --> FI
    FI -.-> SV

    style L1 fill:#0B1F3A,stroke:#F5B700,color:#fff
    style L2 fill:#0B1F3A,stroke:#14B8A6,color:#fff
    style L3 fill:#0B1F3A,stroke:#14B8A6,color:#fff
```

<img src="assets/divider.svg" width="100%" alt=""/>

## 🖥️ Dashboard tour

The dashboard is meant to be read from top to bottom, the same way you would inspect a new observation by hand.

### Step 1 · Load an observation

Choose a FITS file. RadioSkyLab reads the image data and the header information so you know what you are looking at before you look at the pixels.

### Step 2 · See the radio sky

The intensity map shows how bright the radio emission is across the image. Bright regions are strong emission. Dark regions are weak emission or noise.

### Step 3 · Read the statistics

A compact table summarises the pixel values. Together with the map, it tells you whether the image looks like a sensible observation.

### Step 4 · Check quality

Basic quality checks flag common problems, so you can decide whether the file is ready for deeper work.

### 🗺️ Where to look first

| If you want to know... | Look at... |
|:-----------------------|:-----------|
| Does the image look like a real observation? | The intensity map |
| How bright is the brightest pixel? | The maximum in the statistics table |
| Is the background quiet? | The spread of values away from bright sources |
| Is anything broken in the file? | The quality checks |
| Where did this file come from? | The header information |

<details>
<summary><b>🧭 A good first-look routine (30 seconds)</b></summary>

<br/>

1. Does the map show structure, or is it flat or noisy everywhere?
2. Are the minimum and maximum values reasonable for the instrument?
3. Do the quality checks report anything unusual?
4. If something looks wrong, check the header before blaming the data.

</details>

<img src="assets/divider.svg" width="100%" alt=""/>

## 🛠️ Technology

<div align="center">

<img src="https://skillicons.dev/icons?i=python,numpy,pandas,matplotlib,git,github,vscode&theme=dark" alt="Technology icons"/>

</div>

| Tool | Role in RadioSkyLab | Why it is here |
|:-----|:--------------------|:---------------|
| 🐍 **Python** | Core language | Readable, and the standard language of modern astronomy software |
| ⚡ **Streamlit** | Dashboard | Turns Python scripts into interactive web apps quickly |
| 🔭 **Astropy** | FITS and astronomy utilities | The community standard for working with astronomical data in Python |
| 🧮 **NumPy** | Array maths | Fast numerical operations on image arrays |
| 🐼 **Pandas** | Tables | Clean summaries and tidy display of results |
| 📈 **Matplotlib** | Plotting | Full control over scientific figures |
| 🛰️ **Astroquery** | Survey access | Planned route to online archives such as the FIRST survey |

### 🧩 How the pieces fit together

```text
        ┌───────────────┐
        │   Streamlit   │   interface
        └───────┬───────┘
                │
   ┌────────────┼─────────────┐
   │            │             │
┌──▼───┐    ┌───▼────┐    ┌───▼──────┐
│Pandas│    │ NumPy  │    │Matplotlib│   analysis and plots
└──┬───┘    └───┬────┘    └───┬──────┘
   └────────────┼─────────────┘
                │
        ┌───────▼───────┐
        │    Astropy    │   FITS reading
        └───────┬───────┘
                │
        ┌───────▼───────┐
        │  FITS files   │   your data
        └───────────────┘
```

<img src="assets/divider.svg" width="100%" alt=""/>

## 📂 Project structure

A recommended layout for the repository. Adjust the names to match your own files.

```text
RadioSkyLab/
├── 📄 app.py                 # Streamlit entry point
├── 📄 requirements.txt       # Python dependencies
├── 📄 README.md              # You are here
├── 📁 assets/                # README header, divider and footer graphics
│   ├── header.svg
│   ├── divider.svg
│   └── footer.svg
├── 📁 docs/                  # Screenshots and the demo GIF
│   └── demo.gif
├── 📁 data/                  # Your FITS files (keep large files out of Git)
│   └── .gitkeep
└── 📁 tests/                 # Optional: automated tests
```

### 📝 Notes on the layout

- Keep **large FITS files out of Git**. Add them to `.gitignore` and share them through a data host instead.
- Keep the README graphics in `assets/` so the page loads fast and works offline on GitHub.
- Screenshots and GIFs belong in `docs/`.

<details>
<summary><b>📄 Suggested <code>.gitignore</code></b></summary>

<br/>

```gitignore
# Python
__pycache__/
*.pyc
.venv/
.env

# Data (large files)
data/*.fits
data/*.fits.gz

# Jupyter and editors
.ipynb_checkpoints/
.vscode/
.idea/

# OS files
.DS_Store
Thumbs.db
```

</details>

<img src="assets/divider.svg" width="100%" alt=""/>

## 🚀 Quick start

### ✅ Requirements

| Requirement | Notes |
|:------------|:------|
| Python | 3.9 or newer is recommended |
| Git | To clone the repository |
| A FITS file | Any radio astronomy image works. See [Data](#-data-and-the-first-survey) |
| A modern browser | The dashboard runs in the browser |

### 1️⃣ Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd RadioSkyLab
```

### 2️⃣ Create a virtual environment

```bash
python -m venv .venv
```

### 3️⃣ Activate it

<table>
<tr>
<th>🪟 Windows (PowerShell or CMD)</th>
<th>🐧 macOS and Linux</th>
</tr>
<tr>
<td>

```bash
.venv\Scripts\activate
```

</td>
<td>

```bash
source .venv/bin/activate
```

</td>
</tr>
</table>

> 💡 You know it worked when your terminal prompt starts with `(.venv)`.

### 4️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Run the dashboard

```bash
streamlit run app.py
```

Streamlit prints a local address, usually:

```text
Local URL: http://localhost:8501
```

Open it in your browser and the dashboard is ready.

### ⏱️ The whole thing in one block

```bash
git clone YOUR_REPOSITORY_URL
cd RadioSkyLab
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS or Linux
pip install -r requirements.txt
streamlit run app.py
```

### 📦 Example `requirements.txt`

If you need to create or check your requirements file, this is the stack the project uses:

```text
streamlit
astropy
numpy
pandas
matplotlib
astroquery
```

> 📌 For reproducible installs, pin versions with `pip freeze > requirements.txt` once everything works.

<img src="assets/divider.svg" width="100%" alt=""/>

## 🐍 Use the data in Python

You do not have to use the dashboard. These examples show how the same ideas work in a few lines of plain Python with Astropy and NumPy. They are a good way to understand what the dashboard is doing.

### 📥 Open a FITS file

```python
from astropy.io import fits

with fits.open("data/my_observation.fits") as hdul:
    hdul.info()                      # list the parts of the file
    header = hdul[0].header          # metadata
    data = hdul[0].data              # the image array

print(data.shape)
```

### 🧐 Read the header

```python
for key in ("OBJECT", "TELESCOP", "INSTRUME", "BUNIT", "CRVAL1", "CRVAL2"):
    print(key, "=", header.get(key, "not present"))
```

> Not every file has every key. Using `.get()` keeps your code from crashing when one is missing.

### 🧹 Handle extra dimensions

Radio images often carry extra axes for frequency and polarisation. Reduce them to a plain 2D image first.

```python
import numpy as np

image = np.squeeze(data)             # drop axes of length 1

while image.ndim > 2:                # keep the first plane of any remaining axes
    image = image[0]

print(image.shape)                   # now (rows, columns)
```

### 📊 Basic statistics

```python
import numpy as np

stats = {
    "min":    np.nanmin(image),
    "max":    np.nanmax(image),
    "mean":   np.nanmean(image),
    "median": np.nanmedian(image),
    "std":    np.nanstd(image),
}

for name, value in stats.items():
    print(f"{name:>7}: {value:.6g}")
```

### 🧾 Put the numbers in a table

```python
import pandas as pd

table = pd.DataFrame(
    {"statistic": list(stats.keys()), "value": list(stats.values())}
)
print(table.to_string(index=False))
```

### 🌈 Plot the intensity map

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7, 6))

low, high = np.nanpercentile(image, [1, 99.5])     # ignore extreme pixels
im = ax.imshow(image, origin="lower", cmap="inferno", vmin=low, vmax=high)

fig.colorbar(im, ax=ax, label="Intensity")
ax.set_title("Radio intensity")
ax.set_xlabel("Pixel x")
ax.set_ylabel("Pixel y")
plt.show()
```

### 🔍 A few simple sanity checks

```python
n_total = image.size
n_nan = int(np.isnan(image).sum())
n_inf = int(np.isinf(image).sum())

print(f"Total pixels : {n_total}")
print(f"NaN pixels   : {n_nan} ({100 * n_nan / n_total:.2f}%)")
print(f"Inf pixels   : {n_inf}")
print(f"All zeros    : {bool(np.all(image == 0))}")
print(f"Constant     : {bool(np.nanmin(image) == np.nanmax(image))}")
```

### 📈 Look at the pixel value distribution

```python
values = image[np.isfinite(image)].ravel()

fig, ax = plt.subplots(figsize=(7, 4))
ax.hist(values, bins=200, log=True, color="#14B8A6")
ax.set_xlabel("Pixel value")
ax.set_ylabel("Count (log scale)")
ax.set_title("Distribution of pixel values")
plt.show()
```

> 🧠 In a good radio image, most pixels are noise that clusters around zero. A long tail toward high values is usually real sources.

<details>
<summary><b>🛰️ Planned: fetching survey data with Astroquery</b></summary>

<br/>

Survey integration is **not part of the current release**. Astroquery provides tools to reach online archives and is part of the stack so the project is ready for this step. Check the [Astroquery documentation](https://astroquery.readthedocs.io/) for the services available when you reach that stage.

</details>

<img src="assets/divider.svg" width="100%" alt=""/>

## 📊 Understanding the statistics

Every statistic tells part of the story. None of them tells all of it.

| Statistic | Plain-language meaning | What to watch for |
|:----------|:-----------------------|:------------------|
| **Minimum** | The faintest or most negative pixel | Very large negative values can point to artefacts |
| **Maximum** | The brightest pixel | A single huge value can be a real bright source or a glitch |
| **Mean** | The average of all pixels | Pulled upward by bright sources |
| **Median** | The middle pixel value | A better picture of the typical background |
| **Standard deviation** | How spread out the values are | Mixes noise and real sources together |

### 🧮 Why mean and median can differ

Most of a radio image is background noise. A few pixels hold bright sources. Those few bright pixels pull the **mean** upward but barely move the **median**. If the two are far apart, the image probably contains strong sources or artefacts.

```text
  background noise                bright source
 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ ███
 └────────── median sits here ──────────────┘  └─ mean is pulled this way
```

### 📏 A rule of thumb for noise

Noise can be estimated from a patch of sky that has no obvious sources. The standard deviation of that patch is a simple first estimate of the **noise level**. The whole-image standard deviation is usually larger because it includes the sources.

```python
patch = image[10:110, 10:110]               # choose a quiet corner by eye
noise = np.nanstd(patch)
peak = np.nanmax(image)

print(f"Noise estimate : {noise:.6g}")
print(f"Peak           : {peak:.6g}")
print(f"Peak / noise   : {peak / noise:.1f}")
```

### 🧯 What the statistics cannot tell you

- They do not tell you whether the **flux scale** is correct.
- They do not tell you whether a feature is a **real source** or an artefact.
- They do not replace proper **calibration and imaging**.

See the [disclaimer](#%EF%B8%8F-disclaimer).

<img src="assets/divider.svg" width="100%" alt=""/>

## ✅ Quality checks

Basic quality checks give you a fast, rough sense of whether an image is usable. The list below describes the kinds of problems worth looking for when you inspect a radio image. Use it alongside the dashboard.

| Problem | Why it matters | Typical sign |
|:--------|:---------------|:-------------|
| 🕳️ **Missing pixels** (NaN) | Statistics can be wrong or fail | Blank patches or edges in the map |
| ♾️ **Infinite values** | Break plots and averages | Extreme scale on the colour bar |
| 🟫 **Empty image** | Nothing to analyse | All values equal or all zero |
| 📏 **Wrong shape** | Extra axes confuse tools | More than two dimensions |
| 🔊 **Very high noise** | Hides faint sources | Grainy map, huge spread |
| 📈 **Extreme outliers** | Skew the colour scale | One pixel far above all others |
| 🧩 **Edge artefacts** | Common in mosaics and cutouts | Bright or dark borders |

### 🚦 Reading the result

| Outcome | What it means | Suggested action |
|:-------:|:--------------|:-----------------|
| 🟢 **Looks fine** | No obvious problems found | Continue to deeper analysis |
| 🟡 **Warnings** | Something unusual was found | Inspect the map and header before trusting numbers |
| 🔴 **Problems** | Data may be unusable | Re-download, re-process or choose another file |

> ⚠️ A passing result does **not** prove the data is scientifically valid. It only means that nothing obviously wrong was found.

### 🧪 Try the checks yourself

```python
def quick_checks(image):
    """Return a few simple facts about a 2D image."""
    total = image.size
    return {
        "shape": image.shape,
        "nan_fraction": float(np.isnan(image).sum()) / total,
        "inf_count": int(np.isinf(image).sum()),
        "is_constant": bool(np.nanmin(image) == np.nanmax(image)),
        "dynamic_range": float(np.nanmax(image) - np.nanmin(image)),
    }

print(quick_checks(image))
```

<img src="assets/divider.svg" width="100%" alt=""/>

## 📚 Radio astronomy primer

A short guide for readers who are new to the science.

### 📡 What is radio astronomy?

Radio astronomy studies the universe through radio waves. These are the same kind of electromagnetic waves used for broadcasting, but at wavelengths and strengths that come from stars, galaxies, black holes and clouds of gas. Radio waves pass through dust and clouds, so they reveal things that visible light hides.

### 🗂️ What is a FITS file?

**FITS** stands for **Flexible Image Transport System**. It is the standard file format in astronomy. A FITS file holds:

| Part | Contents |
|:-----|:---------|
| **Header** | Text metadata: telescope, object, units, coordinates, dates |
| **Data** | The numbers themselves, usually an image array |
| **Extensions** | Extra tables or images stored in the same file |

### 🔤 Words you will meet

| Term | Meaning |
|:-----|:--------|
| **Intensity** | How strong the radio emission is at each point |
| **Flux density** | Radio power per area per frequency, often measured in **Jansky (Jy)** |
| **Jy/beam** | A common radio image unit: flux density per telescope beam |
| **Beam** | The telescope's resolution element, like the blur of the instrument |
| **Noise (RMS)** | The random variation in the image, set by the instrument and the observation |
| **Dynamic range** | Brightest signal compared with the noise level |
| **Source** | A real object that emits radio waves |
| **Artefact** | A false feature created by the instrument or the processing |
| **WCS** | World Coordinate System: maps pixels to positions on the sky |
| **Calibration** | Correcting measurements so they reflect true physical values |
| **Imaging** | Turning raw telescope measurements into a picture of the sky |
| **RFI** | Radio frequency interference: unwanted human-made signals |

### 🌠 Why the picture is not a photograph

A radio image is built from measurements, then processed with careful mathematics. The result depends on how the data was calibrated and imaged. That is why the same patch of sky can look different in two images, and why RadioSkyLab treats its own measurements as exploratory.

### 🧭 The journey from sky to screen

```mermaid
flowchart LR
    A[🌌 Radio sky] --> B[📡 Telescope]
    B --> C[🧾 Raw measurements]
    C --> D[🔧 Calibration]
    D --> E[🖼️ Imaging]
    E --> F[🗂️ FITS image]
    F --> G[🔍 RadioSkyLab inspection]

    style A fill:#0B1F3A,stroke:#F5B700,color:#fff
    style B fill:#0B1F3A,stroke:#14B8A6,color:#fff
    style C fill:#0B1F3A,stroke:#14B8A6,color:#fff
    style D fill:#0B1F3A,stroke:#14B8A6,color:#fff
    style E fill:#0B1F3A,stroke:#14B8A6,color:#fff
    style F fill:#14B8A6,stroke:#0B1F3A,color:#0B1F3A
    style G fill:#F5B700,stroke:#0B1F3A,color:#0B1F3A
```

<img src="assets/divider.svg" width="100%" alt=""/>

## 📡 Data and the FIRST survey

RadioSkyLab is designed to support **real astronomical FITS observations**.

### 🛰️ What is the FIRST survey?

**FIRST** stands for **Faint Images of the Radio Sky at Twenty-Centimeters**. It is a large radio survey made with the Very Large Array in the United States. It maps a big part of the sky at a wavelength of about 20 cm and is widely used for finding and studying radio sources.

> 🚧 **Status:** FIRST survey integration will be added in a subsequent development stage.

### 🧭 Plan for survey integration

```mermaid
flowchart LR
    A[🧭 Choose a sky position] --> B[🛰️ Query the survey archive]
    B --> C[⬇️ Download a cutout]
    C --> D[🗂️ FITS image]
    D --> E[🔍 Same inspection pipeline]

    style A fill:#0B1F3A,stroke:#F5B700,color:#fff
    style B fill:#0B1F3A,stroke:#14B8A6,color:#fff
    style C fill:#0B1F3A,stroke:#14B8A6,color:#fff
    style D fill:#14B8A6,stroke:#0B1F3A,color:#0B1F3A
    style E fill:#F5B700,stroke:#0B1F3A,color:#0B1F3A
```

### 📥 Using your own data today

Until survey integration arrives, bring your own files:

1. Place your FITS file in the `data/` folder.
2. Start the dashboard.
3. Select the file and explore.

### 🧷 Data etiquette

- Respect the **licence and citation rules** of every dataset you use.
- Never commit large or restricted data to a public repository.
- Credit the telescope, survey and authors in anything you publish.

<img src="assets/divider.svg" width="100%" alt=""/>

## 🗺️ Roadmap

### ✅ Done

- [x] FITS image loading with Astropy
- [x] Radio intensity visualisation
- [x] Image statistics
- [x] Basic image quality checks
- [x] Streamlit dashboard

### 🛠️ Next

- [ ] FIRST survey integration with Astroquery
- [ ] Sky position search and cutout download
- [ ] Better handling of multi-axis FITS files
- [ ] Export statistics and reports

### 🔭 Later

- [ ] Source detection and simple source tables
- [ ] Noise map and signal-to-noise view
- [ ] Coordinate overlays using the image WCS
- [ ] Support for calibrated analysis workflows
- [ ] Automated tests and continuous integration

### 🧭 Timeline

```mermaid
gantt
    title RadioSkyLab development stages
    dateFormat  YYYY-MM
    axisFormat  %b %Y
    section Foundation
    FITS loading and statistics   :done,    a1, 2026-01, 2026-04
    Streamlit dashboard           :done,    a2, 2026-03, 2026-06
    section Growth
    FIRST survey integration      :active,  b1, 2026-07, 2026-12
    Reports and export            :         b2, 2026-11, 2027-02
    section Science
    Source detection              :         c1, 2027-01, 2027-05
    Calibrated workflows          :         c2, 2027-04, 2027-09
```

> 🗓️ The dates above are a planning sketch. Update them to match your real schedule.

<img src="assets/divider.svg" width="100%" alt=""/>

## 🧰 Troubleshooting

<details>
<summary><b>❌ <code>streamlit: command not found</code></b></summary>

<br/>

Your virtual environment is probably not active, or the install did not finish.

```bash
# Windows
.venv\Scripts\activate

# macOS or Linux
source .venv/bin/activate

pip install -r requirements.txt
```

You can also run Streamlit as a module:

```bash
python -m streamlit run app.py
```

</details>

<details>
<summary><b>🔒 PowerShell blocks the activate script</b></summary>

<br/>

Windows can block scripts by default. Allow them for your user only:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Or activate with Command Prompt instead:

```bat
.venv\Scripts\activate.bat
```

</details>

<details>
<summary><b>📦 <code>ModuleNotFoundError: No module named 'astropy'</code></b></summary>

<br/>

The package is missing from the active environment.

```bash
pip install astropy
```

Check that you are inside the right environment:

```bash
python -c "import sys; print(sys.executable)"
```

The path should point inside your `.venv` folder.

</details>

<details>
<summary><b>🗂️ The FITS file will not open</b></summary>

<br/>

- Confirm the file is a real FITS file and finished downloading.
- Compressed files such as `.fits.gz` usually open directly with Astropy.
- Try listing the file contents with `hdul.info()` to see which extension holds the image.
- Some files keep the image in extension `1` rather than `0`.

```python
with fits.open("data/file.fits") as hdul:
    hdul.info()
    data = hdul[1].data      # try the next extension
```

</details>

<details>
<summary><b>🧊 The image looks blank or completely black</b></summary>

<br/>

- A few extreme pixels can stretch the colour scale. Clip the display range with percentiles, as shown in the [plotting example](#-use-the-data-in-python).
- Check for `NaN` values and for an image that is all zeros.
- Make sure you are viewing a 2D plane, not a collapsed or empty axis.

</details>

<details>
<summary><b>🐢 The app is slow with big files</b></summary>

<br/>

- Large images take time to load and plot. Try a smaller cutout first.
- Reduce the image before plotting if you only need a quick look.
- Close other heavy programs and restart the app.

</details>

<details>
<summary><b>🌐 The dashboard does not open in my browser</b></summary>

<br/>

- Copy the `Local URL` that Streamlit prints into your browser.
- If port `8501` is busy, pick another one:

```bash
streamlit run app.py --server.port 8502
```

</details>

<details>
<summary><b>🔌 A command fails because of the network</b></summary>

<br/>

Survey and archive access needs an internet connection. Check your connection and any firewall or proxy settings, then try again.

</details>

<img src="assets/divider.svg" width="100%" alt=""/>

## ❓ FAQ

<details>
<summary><b>Do I need a telescope or special equipment?</b></summary>

<br/>

No. You only need a computer and a FITS file. Public radio data is available from many observatories and surveys.

</details>

<details>
<summary><b>Which FITS files work best?</b></summary>

<br/>

Calibrated image files, where the data is a 2D map of the sky or a stack that reduces to one. Raw measurement files are not images and need processing first.

</details>

<details>
<summary><b>Can I use it for research papers?</b></summary>

<br/>

RadioSkyLab gives **exploratory** measurements. For published results, use calibrated, peer-reviewed tools and methods, and cite your data sources properly.

</details>

<details>
<summary><b>Why are the statistics only "exploratory"?</b></summary>

<br/>

Because they are computed directly from pixel values, without calibration-aware treatment of beam, noise structure or source models. They are great for a first look and not enough for final science.

</details>

<details>
<summary><b>Is the FIRST survey available now?</b></summary>

<br/>

Not yet. It is planned for a later development stage. See the [roadmap](#%EF%B8%8F-roadmap).

</details>

<details>
<summary><b>Can I add my own checks or plots?</b></summary>

<br/>

Yes. The project is meant to grow. Add a function that takes a 2D array and returns a result, then show it in the dashboard.

</details>

<details>
<summary><b>Does it work on Windows, macOS and Linux?</b></summary>

<br/>

Yes. The stack is cross-platform. Only the virtual environment activation command differs. See the [quick start](#-quick-start).

</details>

<details>
<summary><b>How do I update to the latest version?</b></summary>

<br/>

```bash
git pull
pip install -r requirements.txt --upgrade
```

</details>

<img src="assets/divider.svg" width="100%" alt=""/>

## 🤝 Contributing

Ideas, bug reports and improvements are welcome.

### 🧭 Ways to help

| You can... | How |
|:-----------|:----|
| 🐞 Report a bug | Open an issue with steps to reproduce and the error message |
| 💡 Suggest a feature | Open an issue describing the problem it would solve |
| 📝 Improve the docs | Fix typos, add examples, clarify steps |
| 🧪 Add tests | Small, focused tests are very welcome |
| 🔭 Share data tips | Point to open FITS datasets that work well |

### 🔧 Development workflow

```bash
# 1. Fork the repository on GitHub, then clone your fork
git clone YOUR_FORK_URL
cd RadioSkyLab

# 2. Create a branch
git checkout -b feature/my-improvement

# 3. Set up the environment
python -m venv .venv
.venv\Scripts\activate           # Windows
# source .venv/bin/activate      # macOS or Linux
pip install -r requirements.txt

# 4. Make your changes and run the app to test them
streamlit run app.py

# 5. Commit and push
git add .
git commit -m "Describe your change"
git push origin feature/my-improvement
```

Then open a **pull request** and describe what you changed and why.

### 🧼 Style guide

- Write clear, readable Python with helpful names.
- Add short docstrings to functions.
- Keep functions small and focused on one job.
- Explain any science in comments so students can follow along.
- Label results honestly as exploratory unless they are properly calibrated.

### 🏷️ Commit message ideas

| Prefix | Use for |
|:-------|:--------|
| `feat:` | A new feature |
| `fix:` | A bug fix |
| `docs:` | Documentation only |
| `refactor:` | Code cleanup with no behaviour change |
| `test:` | Adding or updating tests |

<img src="assets/divider.svg" width="100%" alt=""/>

## 📖 References and credits

RadioSkyLab stands on the work of the open-source and astronomy communities.

### 🧰 Software

| Project | Link |
|:--------|:-----|
| Astropy | [astropy.org](https://www.astropy.org/) |
| Astroquery | [astroquery.readthedocs.io](https://astroquery.readthedocs.io/) |
| Streamlit | [streamlit.io](https://streamlit.io/) |
| NumPy | [numpy.org](https://numpy.org/) |
| Pandas | [pandas.pydata.org](https://pandas.pydata.org/) |
| Matplotlib | [matplotlib.org](https://matplotlib.org/) |

### 📄 Papers worth citing

If you use these tools or data in published work, please cite the original papers.

- Becker, R. H., White, R. L., & Helfand, D. J. (1995). *The FIRST Survey: Faint Images of the Radio Sky at Twenty Centimeters.* The Astrophysical Journal, 450, 559.
- Astropy Collaboration (2013). *Astropy: A community Python package for astronomy.* Astronomy & Astrophysics, 558, A33.
- Astropy Collaboration (2018). *The Astropy Project: Building an open-science project and status of the v2.0 core package.* The Astronomical Journal, 156, 123.
- Astropy Collaboration (2022). *The Astropy Project: Sustaining and growing a community-oriented open-source project and the latest major release (v5.0) of the core package.* The Astrophysical Journal, 935, 167.
- Ginsburg, A., et al. (2019). *astroquery: An Astronomical Web-querying Package in Python.* The Astronomical Journal, 157, 98.

### 🎨 Visual credits

- Header, divider and footer graphics are custom animated SVGs stored in `assets/`.
- Badges by [Shields.io](https://shields.io/).
- Typing animation by [readme-typing-svg](https://github.com/DenverCoder1/readme-typing-svg).
- Technology icons by [skillicons.dev](https://skillicons.dev/).

<img src="assets/divider.svg" width="100%" alt=""/>

## ⚠️ Disclaimer

> **Basic image statistics are exploratory measurements, not a substitute for scientifically calibrated radio astronomy analysis.**

RadioSkyLab is built for learning, inspection and first-look analysis. It does not replace calibrated pipelines, expert review or peer-reviewed methods. Always confirm important findings with established tools and cite your data sources.

<img src="assets/divider.svg" width="100%" alt=""/>

## 👤 Author

<div align="center">

### **Luthando Candlovu**

`Computer Science` &nbsp;•&nbsp; `Scientific Computing` &nbsp;•&nbsp; `Radio Astronomy` &nbsp;•&nbsp; `AI`

<br/>

[![GitHub](https://img.shields.io/badge/GitHub-LuthandoCandlovu-0B1F3A?style=for-the-badge&logo=github&logoColor=F5B700)](https://github.com/LuthandoCandlovu)

<br/>

<img src="https://github-readme-stats.vercel.app/api?username=LuthandoCandlovu&show_icons=true&hide_border=true&bg_color=0B1F3A&title_color=F5B700&icon_color=14B8A6&text_color=FFFFFF&ring_color=F5B700" alt="GitHub stats" width="48%"/>
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=LuthandoCandlovu&layout=compact&hide_border=true&bg_color=0B1F3A&title_color=F5B700&text_color=FFFFFF" alt="Top languages" width="48%"/>

<br/><br/>

⭐ **If RadioSkyLab helped you, give the repository a star.** ⭐

<br/>

<img src="assets/footer.svg" width="100%" alt="RadioSkyLab footer"/>

</div>
