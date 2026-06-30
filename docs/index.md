# Rubén Jiménez Mejías

**Robotics engineer — end-to-end on real hardware.**

I build robots from the chassis up — mechanical, electronics, embedded firmware, and high-level software. My current project is an autonomous outdoor kart; same toolkit applies to manipulators, drones, mobile robots, surgical robotics, or any platform where the layers have to actually work together. I find my best work happens where they meet.

*Stack: CAD · 3D printing · steel welding · carbon fiber · custom PCBs · BMS · ESP32 · STM32 · FreeRTOS · ROS 2 · perception · control · Linux/Jetson.*

Currently finishing my degree and looking for robotics roles in Switzerland.

[:fontawesome-brands-linkedin: LinkedIn](https://www.linkedin.com/in/rubenayla/){ .md-button }
[:fontawesome-brands-github: GitHub](https://github.com/rubenayla){ .md-button }
[:material-file-pdf-box: Resume (EN)](files/CV_Ruben_Jimenez_EN.pdf){ .md-button }
[:material-file-pdf-box: CV (ES)](files/CV_Ruben_Jimenez_ES.pdf){ .md-button }

---

<video width="100%" controls autoplay muted loop playsinline>
  <source src="videos/kart-hero.mp4" type="video/mp4">
</video>

## Projects

### [Driverless Kart](projects/kart.md) &nbsp; <small>:material-star: **Flagship project**</small>

A real Tony Kart converted into a ROS 2 outdoor autonomous testbed. Jetson AGX Orin + ZED 2 stereo + custom ESP32 safety MCU, in-house steering actuation, custom emergency-brake system, custom wheel sensor PCB. First completed 5 laps autonomously on a cone-defined track in April 2026; manual mode fully operational, autonomous mode actively integrated.

**Tech:** ROS 2 Humble, YOLOv5, Jetson, Linux/RT, ESP32 / FreeRTOS, custom PCBs, planetary gear design, pneumatics

---

### [Formula Student](projects/formula-student.md) — driverless subsystems

My driverless work for Ü Motorsport on the UM05 car: custom PCBs, drive-by-wire steering, a fail-safe pneumatic emergency brake, and wheel-speed sensorization — plus the cone-detection software I took from ~8 to ~50 FPS. Where my autonomy work started, before the kart.

**Tech:** Custom PCBs, drive-by-wire steering, FESTO pneumatics, CAN bus, Python (multithreading, OpenCV/YOLO), CFRP

---

### [Partle](projects/partle.md) — agent-native marketplace

Marketplace platform built for AI agents as first-class users: a public MCP server lets agents search products, list items for sale, and broker purchases on a user's behalf — a substrate for agent-managed shopping, ads, and listings. Passkey auth, interactive map, Elasticsearch, community reliability ratings. Live service.

**Tech:** React/TypeScript, FastAPI, PostgreSQL, Elasticsearch, Leaflet, FIDO2 passkeys, MCP server

---

### [Cyberwheel](https://rubenayla.github.io/cyberwheel/) — open-source EUC

Electric unicycle that "never cuts power," addressing critical safety concerns in commercial products. Sealed electronics, crash-resistant, fully open hardware + firmware.

**Tech:** Embedded systems, motor control, BMS, mechanical design

---

### [Investment Analysis](projects/invest.md) — systematic stock valuation

Configuration-driven framework for stock analysis. Multiple valuation models (DCF, RIM) plus an LSTM/Transformer neural network at 78.64% accuracy across 500+ S&P 500 stocks.

**Tech:** Python, PyTorch, SQLite, Pandas, financial modelling

---

**Also on:** [:fontawesome-solid-cube: GrabCAD](https://grabcad.com/ruben.jimenez-15/models)

[More about me →](about.md)
