# Driverless Kart

:material-star: **Flagship project** · 2020 – present · Outdoor autonomous vehicle testbed built on a real competition kart.

<video width="100%" controls autoplay muted loop playsinline>
  <source src="../../videos/kart-hero.mp4" type="video/mp4">
</video>

📚 [Documentation](https://um-driverless.github.io/kart-docs/) · 💻 [kart-brain (perception + control)](https://github.com/UM-Driverless/kart-brain) · [kart-docs (mechanical/electrical/process)](https://github.com/um-driverless/kart-docs) · [driverless (legacy Python stack)](https://github.com/UM-Driverless/driverless)

!!! success "Status — May 2026"
    ROS 2 migration complete. Manual mode fully operational. **First
    autonomous run completed 5 full laps on a cone-defined track**
    (April 2026) before a printed PLA sun gear in the steering reducer
    snapped on the 6th lap — a known PLA-creep failure with a brass
    upgrade already designed. Autonomous mode actively integrated.

[:material-book-open-variant: **Read the Build Journey**](#build-journey){ .md-button .md-button--primary }
[:material-file-document-multiple: Full technical documentation (kart-docs)](https://um-driverless.github.io/kart-docs/){ .md-button }

## What it is

A modular autonomous platform built on a real Tony Kart chassis, designed as an **outdoor testbed** for perception, planning, and control algorithms. Maintains manual drive capability so a safety driver can take over at any time, which makes it a practical platform for real-world algorithm validation rather than a simulator-bound demo.

## Hardware

- **Compute** — NVIDIA Jetson AGX Orin (JetPack 6.2.2, CUDA 12.6, 62 GB RAM, Ubuntu 22.04)
- **Perception sensor** — ZED 2 stereo camera (USB 3.0, GPU-accelerated depth)
- **Microcontroller** — ESP32 "Kart Medulla" custom PCB, FreeRTOS, UART link to the Orin at 115200 baud
- **Steering actuation** — DC motor + planetary reducer (in-house design)
- **Emergency brake** — fail-safe pneumatic system on STM32
- **Wheel sensorisation** — custom PCB for hall-effect odometry
- **Frame** — 2024 Tony Kart competition chassis
- **Power** — custom 18650 lithium pack with JBD BMS, spot-welded in-house

## Software architecture

Everything from cone perception to steering commands runs in **ROS 2 Humble** on the Orin. The ESP32 is the safety boundary: if the high-level loop dies, the kart fails into a known mechanical-safe state independent of the Linux side.

- **Perception** — YOLOv11 cone detector (trained in-house on our own cone dataset) + stereo depth localiser. 3D cone positions published to ROS 2 in real time on the Jetson's GPU.
- **Control** — geometric / pure-pursuit controllers. Each controller publishes its picked target point to `/kart/target`; the dashboard HUD subscribes to the same topic, so what the user sees and what the controller commands cannot disagree.
- **Pre-ROS legacy stack** — earlier 100% Python pipeline ran at ~50 Hz end-to-end on the same hardware. [Walkthrough video](https://youtu.be/wZSFr2eYE4M?si=JckY54OkSBQb4r1M).

??? note "Build photos"

    <div class="grid cards" markdown>

    - ![Full kart](../images/kart/full-kart.jpg){ loading=lazy }
    - ![Chassis arrival](../images/kart/chassis-arrival.jpg){ loading=lazy }
    - ![ZED 2 camera mount](../images/kart/zed2-mount.jpg){ loading=lazy }
    - ![Kart Medulla custom PCB](../images/kart/kart-medulla-pcb.png){ loading=lazy }
    - ![Steering planetary gear motor](../images/kart/steering-planetary.jpg){ loading=lazy }
    - ![Battery pack assembled](../images/kart/battery-pack.jpg){ loading=lazy }

    </div>

## Links

- **[kart-brain](https://github.com/UM-Driverless/kart-brain)** — Jetson-side perception, control, ROS 2 nodes
- **[kart-docs](https://github.com/um-driverless/kart-docs)** — mechanical, electrical, hydraulics, BOM
- **[driverless (legacy)](https://github.com/UM-Driverless/driverless)** — pre-ROS Python stack, ~50 Hz reference
- **[How Our Autonomous Kart Software Works](https://youtu.be/wZSFr2eYE4M?si=JckY54OkSBQb4r1M)** — walkthrough video of the legacy stack

---

--8<-- "build-journey/index.md"
