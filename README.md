<div align="center">

<!-- 🌊 Animated Header Wave -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0B1F3A,50:14B8A6,100:F5B700&height=260&section=header&text=RadioSkyLab&fontSize=72&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=Radio%20Astronomy%20Data%20Analysis%20%26%20Visualisation%20Platform&descAlignY=58&descSize=20" width="100%" alt="RadioSkyLab banner"/>

<!-- ⌨️ Typing Animation -->
<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=2800&pause=800&color=F5B700&center=true&vCenter=true&width=750&height=60&lines=Load+real+FITS+radio+images+%F0%9F%93%A1;Visualise+radio+intensity+maps+%F0%9F%8C%8C;Run+quality+checks+%26+statistics+%F0%9F%93%8A;Explore+it+all+in+a+Streamlit+dashboard+%E2%9A%A1;Built+with+Python+%2B+Astropy+%F0%9F%90%8D" alt="Typing animation" />
</a>

<br/>

<!-- 🛡️ Animated Badges -->
<p>
  <img src="https://img.shields.io/badge/Python-3.9%2B-0B1F3A?style=for-the-badge&logo=python&logoColor=F5B700" alt="Python"/>
  <img src="https://img.shields.io/badge/Streamlit-Dashboard-14B8A6?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit"/>
  <img src="https://img.shields.io/badge/Astropy-FITS-F5B700?style=for-the-badge&logoColor=0B1F3A" alt="Astropy"/>
  <img src="https://img.shields.io/badge/NumPy-Arrays-0B1F3A?style=for-the-badge&logo=numpy&logoColor=14B8A6" alt="NumPy"/>
</p>

<p>
  <img src="https://img.shields.io/badge/Status-In%20Development-F5B700?style=for-the-badge&logo=statuspage&logoColor=0B1F3A" alt="Status"/>
  <img src="https://img.shields.io/badge/License-MIT-14B8A6?style=for-the-badge" alt="License"/>
  <img src="https://img.shields.io/badge/PRs-Welcome-F5B700?style=for-the-badge&logo=git&logoColor=0B1F3A" alt="PRs"/>
  <img src="https://img.shields.io/badge/Made%20with-%E2%9D%A4%EF%B8%8F-14B8A6?style=for-the-badge" alt="Made with love"/>
</p>

<br/>

<!-- 🧭 Navigation -->
<p>
  <a href="#-overview"><b>🌌 Overview</b></a> &nbsp;•&nbsp;
  <a href="#-features"><b>✨ Features</b></a> &nbsp;•&nbsp;
  <a href="#-architecture"><b>🏗️ Architecture</b></a> &nbsp;•&nbsp;
  <a href="#-how-it-works"><b>🧭 How it works</b></a> &nbsp;•&nbsp;
  <a href="#-quick-start"><b>🚀 Quick start</b></a> &nbsp;•&nbsp;
  <a href="#%EF%B8%8F-roadmap"><b>🗺️ Roadmap</b></a> &nbsp;•&nbsp;
  <a href="#-author"><b>👤 Author</b></a>
</p>

</div>

---

## 🌌 Overview

<table>
<tr>
<td width="60%" valign="middle">

**RadioSkyLab** is a Python-based scientific computing platform for **inspecting and analysing radio astronomy FITS images**.

Load an observation, see the radio intensity, check the data quality, and get quick statistics — all from one clean, interactive dashboard.

### 🎯 What makes it special?

- 📡 **Real science data** — powered by Astropy
- 🌈 **Beautiful visuals** — Matplotlib intensity maps
- 📊 **Instant stats** — NumPy-powered analytics
- ⚡ **Zero notebooks** — pure Streamlit interface

</td>
<td width="40%" align="center" valign="middle">

<!-- 🎬 Animated GIF placeholder -->
<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="320" alt="Space animation"/>

<sub>📸 <i>Replace with your <code>docs/demo.gif</code></i></sub>

</td>
</tr>
</table>

---

## ✨ Features

<div align="center">

<table>
<tr>
<td width="50%" align="center" valign="top">

### 📡 FITS Loading
<br/>

<img src="https://user-images.githubusercontent.com/74038190/216122041-518ac897-8d92-4c6b-9b3f-ca01dcaf38ee.gif" width="100" alt="FITS"/>

<br/>

Read real astronomical FITS observations using **Astropy**.

</td>
<td width="50%" align="center" valign="top">

### 🌈 Intensity Visualisation
<br/>

<img src="https://user-images.githubusercontent.com/74038190/212257467-871d32b7-e401-42e8-a166-fcfd7baa4c6b.gif" width="100" alt="Visualisation"/>

<br/>

Render radio intensity maps with **Matplotlib**.

</td>
</tr>
<tr>
<td width="50%" align="center" valign="top">

### 📊 Image Statistics
<br/>

<img src="https://user-images.githubusercontent.com/74038190/212257454-16e3712e-945a-4ca2-b238-408ad0bf87e6.gif" width="100" alt="Statistics"/>

<br/>

Mean, median, std deviation, min and max — via **NumPy**.

</td>
<td width="50%" align="center" valign="top">

### ✅ Quality Checks
<br/>

<img src="https://user-images.githubusercontent.com/74038190/216122041-518ac897-8d92-4c6b-9b3f-ca01dcaf38ee.gif" width="100" alt="Quality"/>

<br/>

Basic image quality checks to flag problem data early.

</td>
</tr>
<tr>
<td colspan="2" align="center" valign="top">

### ⚡ Streamlit Dashboard

<img src="https://user-images.githubusercontent.com/74038190/212257468-1e9a91f1-b626-4baa-b15d-5c385dfa7ed2.gif" width="100" alt="Dashboard"/>

<br/>

Everything in an interactive web interface — no notebooks needed.

</td>
</tr>
</table>

</div>

---

## 🏗️ Architecture

<div align="center">

```mermaid
%%{init: {'theme':'dark', 'themeVariables': { 'primaryColor':'#0B1F3A','primaryTextColor':'#F5B700','primaryBorderColor':'#14B8A6','lineColor':'#14B8A6','secondaryColor':'#F5B700','tertiaryColor':'#0B1F3A'}}}%%
graph TB
    subgraph "🖥️ Presentation Layer"
        A[⚡ Streamlit Dashboard]
        A1[📤 File Uploader]
        A2[📊 Interactive Charts]
        A3[📈 Statistics Panel]
    end

    subgraph "🧠 Application Layer"
        B[🎛️ App Controller]
        B1[📡 FITS Loader]
        B2[✅ Quality Checker]
        B3[📊 Stats Engine]
        B4[🌈 Plot Renderer]
    end

    subgraph "🔬 Science Layer"
        C[🔭 Astropy]
        C1[🧮 NumPy]
        C2[🐼 Pandas]
        C3[📈 Matplotlib]
        C4[🛰️ Astroquery]
    end

    subgraph "💾 Data Layer"
        D[📁 FITS Files]
        D1[🌐 FIRST Survey]
    end

    A --> A1 --> B
    A --> A2 --> B
    A --> A3 --> B
    B --> B1 --> C
    B --> B2 --> C1
    B --> B3 --> C1
    B --> B4 --> C3
    C --> C4 --> D1
    B1 --> D

    style A fill:#F5B700,stroke:#0B1F3A,color:#0B1F3A
    style B fill:#14B8A6,stroke:#0B1F3A,color:#0B1F3A
    style C fill:#0B1F3A,stroke:#F5B700,color:#F5B700
    style D fill:#0B1F3A,stroke:#14B8A6,color:#14B8A6
</div>
🧭 How it works
<div align="center">
%%{init: {'theme':'dark', 'themeVariables': { 'primaryColor':'#0B1F3A','primaryTextColor':'#F5B700','primaryBorderColor':'#14B8A6','lineColor':'#14B8A6'}}}%%
flowchart LR
    A[📡<br/>FITS File] --> B[🔭<br/>Astropy<br/>Loader]
    B --> C[🧮<br/>NumPy /<br/>Pandas]
    C --> D[✅<br/>Quality<br/>Checks]
    C --> E[📊<br/>Statistics]
    C --> F[🌈<br/>Matplotlib<br/>Plots]
    D --> G[⚡<br/>Streamlit<br/>Dashboard]
    E --> G
    F --> G
    G --> H[👨‍🔬<br/>Researcher]

    style A fill:#0B1F3A,stroke:#F5B700,color:#F5B700
    style B fill:#0B1F3A,stroke:#14B8A6,color:#14B8A6
    style C fill:#0B1F3A,stroke:#14B8A6,color:#14B8A6
    style D fill:#14B8A6,stroke:#0B1F3A,color:#0B1F3A
    style E fill:#14B8A6,stroke:#0B1F3A,color:#0B1F3A
    style F fill:#14B8A6,stroke:#0B1F3A,color:#0B1F3A
    style G fill:#F5B700,stroke:#0B1F3A,color:#0B1F3A
    style H fill:#0B1F3A,stroke:#F5B700,color:#F5B700
</div>
🔄 Processing Pipeline
<div align="center">
Step	Stage	Description
1️⃣	Load	Read FITS file via Astropy
2️⃣	Parse	Extract data array + header metadata
3️⃣	Analyse	Compute statistics with NumPy
4️⃣	Validate	Run quality checks on pixel data
5️⃣	Render	Plot intensity map with Matplotlib
6️⃣	Present	Stream results to Streamlit UI
</div>
🛠️ Technology Stack
<div align="center"><img src="https://skillicons.dev/icons?i=python,numpy,pandas,matplotlib,git,github,vscode&theme=dark" alt="Tech stack icons"/>



<table> <tr> <td align="center" width="20%"> <img src="https://user-images.githubusercontent.com/74038190/212257472-08e52665-c503-4bd9-aa20-f5a4c7e9cc80.gif" width="50" alt="Python"/> <br/><b>🐍 Python</b> <br/><sub>Core language</sub> </td> <td align="center" width="20%"> <img src="https://user-images.githubusercontent.com/74038190/212257468-1e9a91f1-b626-4baa-b15d-5c385dfa7ed2.gif" width="50" alt="Streamlit"/> <br/><b>⚡ Streamlit</b> <br/><sub>Dashboard</sub> </td> <td align="center" width="20%"> <img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="50" alt="Astropy"/> <br/><b>🔭 Astropy</b> <br/><sub>FITS reading</sub> </td> <td align="center" width="20%"> <img src="https://user-images.githubusercontent.com/74038190/212257454-16e3712e-945a-4ca2-b238-408ad0bf87e6.gif" width="50" alt="NumPy"/> <br/><b>🧮 NumPy</b> <br/><sub>Array maths</sub> </td> <td align="center" width="20%"> <img src="https://user-images.githubusercontent.com/74038190/212257467-871d32b7-e401-42e8-a166-fcfd7baa4c6b.gif" width="50" alt="Matplotlib"/> <br/><b>📈 Matplotlib</b> <br/><sub>Plots</sub> </td> </tr> </table></div>
🚀 Quick start
<div align="center">
⚡ Get running in 4 steps
</div>
bash
# 1️⃣ Clone the repository
git clone YOUR_REPOSITORY_URL
cd RadioSkyLab

# 2️⃣ Create a virtual environment
python -m venv .venv

# 3️⃣ Activate it
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

# 4️⃣ Install dependencies
pip install -r requirements.txt
▶️ Launch the Dashboard
bash
streamlit run app.py
<div align="center">
Then open http://localhost:8501 in your browser 🎉

</div>
📂 Data
<div align="center"><table> <tr> <td align="center">
🛰️ Supported Data
RadioSkyLab is designed to support real astronomical FITS observations.

</td> </tr> <tr> <td align="center">
🔮 Coming Next
🛰️ Integration with the FIRST survey
(Faint Images of the Radio Sky at Twenty-Centimeters)

<img src="https://user-images.githubusercontent.com/74038190/216122041-518ac897-8d92-4c6b-9b3f-ca01dcaf38ee.gif" width="80" alt="Satellite"/></td> </tr> </table></div>
🗺️ Roadmap
<div align="center">
%%{init: {'theme':'dark', 'themeVariables': { 'primaryColor':'#0B1F3A','primaryTextColor':'#F5B700','primaryBorderColor':'#14B8A6','lineColor':'#14B8A6'}}}%%
timeline
    title RadioSkyLab Development Journey
    section Foundation
        FITS Loading : Done
        Intensity Viz : Done
        Statistics : Done
    section Dashboard
        Quality Checks : Done
        Streamlit UI : Done
    section Next Up
        FIRST Survey : Planned
        Calibrated Workflows : Planned
</div><table align="center"> <tr> <td align="center" width="33%">
✅ Completed
☑ FITS image loading
☑ Intensity visualisation
☑ Image statistics
☑ Basic quality checks
☑ Streamlit dashboard
</td> <td align="center" width="33%">
🚧 In Progress
□ FIRST survey integration
□ Calibrated analysis workflows
</td> <td align="center" width="33%">
🔮 Future Ideas
□ Multi-band support
□ Export reports
□ ML anomaly detection
□ Public demo
</td> </tr> </table>
⚠️ Disclaimer
<div align="center"><table> <tr> <td align="center" width="80">
⚠️

</td> <td align="left">
Basic image statistics are exploratory measurements, not a substitute for scientifically calibrated radio astronomy analysis. Always validate results against proper reduction pipelines before drawing scientific conclusions.

</td> </tr> </table></div>
👤 Author
<div align="center"><img src="https://user-images.githubusercontent.com/74038190/229223263-cf2e4b07-2615-4f87-9c38-e37600f8381a.gif" width="120" alt="Coding animation"/>
Luthando Candlovu
<p> <code>Computer Science</code> &nbsp;•&nbsp; <code>Scientific Computing</code> &nbsp;•&nbsp; <code>Radio Astronomy</code> &nbsp;•&nbsp; <code>AI</code> </p>
<a href="https://github.com/LuthandoCandlovu"> <img src="https://img.shields.io/badge/GitHub-LuthandoCandlovu-0B1F3A?style=for-the-badge&logo=github&logoColor=F5B700" alt="GitHub"/> </a>



⭐ If you find this project useful, give the repo a star! ⭐


<img src="https://capsule-render.vercel.app/api?type=waving&color=0:F5B700,50:14B8A6,100:0B1F3A&height=140&section=footer" width="100%" alt="footer wave"/></div> ```
