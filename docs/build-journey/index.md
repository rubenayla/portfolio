# Build Journey

Posts documenting the build of a competition kart turned autonomous vehicle. Roughly one a week on Wednesdays. New posts append at the bottom — read straight through.

[Follow on LinkedIn :fontawesome-brands-linkedin:](https://www.linkedin.com/in/rubenayla/){ .md-button }

**Jump to:** [Intro](#intro) · [Motor](#motor) · [AI Inventory](#inventory-ai) · [Battery](#battery) · [Why 48V](#why-48v) · [Roll hoop](#main-hoop) · [First drive](#first-drive) · [Steering](#steering-actuator) · [Planetary reducer](#planetary-reducer)

---

## Turning a kart into a driverless racing car { #intro }

*2026-04-22 · [Original on LinkedIn →](https://www.linkedin.com/posts/rubenayla_formulastudent-driverless-umotorsport-activity-7452662533024395266-dB_m)*

We're turning a kart into a driverless racing car.

![Kart arrival](../images/build-journey/2026-04-22-intro/01_kart_arrival_full_edited.jpg){ loading=lazy }

Huge thanks to Henakart. They gave us the whole kart, minus the engine. The rest is on us: the full autonomous stack. I'm on Ü Motorsport Driverless, the URJC student team in Madrid.

I'll post the build from day one, one piece every Wednesday, until the kart's lapping with no one in the seat.

Three stages:

1. Make it electric, so it moves under its own power.
2. Make it remote-controlled, and safe.
3. Make it driverless, so it drives itself around a cone track.

Coming up: motor → battery → braking → steering → compute → testing.

Everything's going into the [kart docs](https://um-driverless.github.io/kart-docs/) so anyone can build it themselves.

---

## Mounting the motor, and why the first bracket failed { #motor }

*2026-04-29 · [Original on LinkedIn →](https://www.linkedin.com/feed/update/urn:li:activity:7455251314227429377/)*

For our kart, the first step is to attach the motor. We kept it simple: a 48V 2000W BLDC kit, which included the controller, throttle sensor, and wiring. Our engineering goes into the battery, the safety system, and the autonomy stack.

Mounting it to a Tony Kart frame was a different job.

The first bracket was PLA, printed on a Bambu Lab. It bolted to the kart's tube frame and held the motor leveled with the rear axle. The bolt holes let us slide the motor to set chain tension. The kart ran on it for months.

![PLA bracket, first version](../images/build-journey/2026-04-29-motor/01_pla_bracket.jpg){ loading=lazy }

Then it failed in a specific way. The bolt nuts were embedded inside the print, hex pockets buried in the plastic. The nuts were nylon-locking. Tightening the bolts meant fighting the nylon insert's friction, which took enough torque to crack the pocket walls from the inside. The nuts started spinning instead of gripping, the bolts went loose, and we couldn't retighten them because the nuts were buried inside a part we'd have had to destroy to reach them.

Standing in the workshop thinking about the replacement, we asked a better question. Why are we holding the motor horizontally to the sprocket, elevated from the chassis? There's no real reason. We can place the motor on the chassis itself, with a flat welded steel plate. And we can do that ourselves, without waiting for orders.

![Motor mounted to the welded steel plate, with chain](../images/build-journey/2026-04-29-motor/02_motor_with_chain.jpg){ loading=lazy }

We considered fancier options. A grid of shifted holes for positive locking. A tensioner bolt in the style of combustion-engine karts. The slot won because it's the simplest approach, and we could always add a tensioner if the slot ever started moving — but it didn't happen.

![Motor controller installed](../images/build-journey/2026-04-29-motor/03_controller_installed.jpg){ loading=lazy }

The kit also shipped with a chain in a different pitch than the kart's: T8F (8 mm) versus #219 (7.774 mm). The two look almost identical. We standardized on #219 and laser-cut a custom pinion to fit the motor's D-shaped shaft.

![Drivetrain at the rear wheel](../images/build-journey/2026-04-29-motor/04_drivetrain_rear_wheel.jpg){ loading=lazy }

Months later, the question "wait, which pitch did we use?" kept coming up. That's why everything goes into the [kart docs](https://github.com/UM-Driverless/kart-docs).

---

## Using an AI Inventory to design PCBs { #inventory-ai }

*2026-05-04 · [Original on LinkedIn →](https://www.linkedin.com/feed/update/urn:li:activity:7456983051160481793/)*

We're using an AI Inventory to design PCBs.

"Do we have any DAC chips in stock?" If answering that means going on a trip to the workshop and spending an hour looking for them between bags, we're doing something wrong.

![The team photographing components on a tripod rig](../images/build-journey/2026-05-04-inventory-ai-workflow/01_team_with_tripod.jpg){ loading=lazy }

Nobody wants to do an inventory, so we made it as easy as possible. We set up a tripod over a workshop table, and took pictures of all 270 bags with components.

![Handwritten LM393P component bag](../images/build-journey/2026-05-04-inventory-ai-workflow/04_lm393p_handwritten_bag.jpg){ loading=lazy }

Then, Claude identified each component, looked the manufacturer part number up online for description and datasheet, and saved the data into [Notion](https://www.notion.so/) using their MCP connector. It worked at first try.

![Notion inventory database](../images/build-journey/2026-05-04-inventory-ai-workflow/03_notion_inventory_database.png){ loading=lazy }

Now we can ask things like:

> "Hey Claude, we need to generate two analog signals from an ESP32 — one 0–5V, one 0–10V. What can we use from the inventory?"

And get back:

> "Use the DAC7574 (quad 12-bit I²C, 2 in stock). With VREF = 5V, the first channel gives 0–5V directly. For the 0–10V channel, route the second channel through an LM358 wired non-inverting at gain 2 (R1 = R2 = 10 kΩ, both in stock). Power the op-amp from the kart's 12V rail. Heads up: you're down to 2 DAC7574s. Probably worth adding a few to the next Mouser order."

<div style="max-width: 315px; margin: 1em auto;">
  <div style="position: relative; padding-bottom: 177.78%; height: 0;">
    <iframe
      src="https://www.youtube.com/embed/xWUMcP6Wm6w"
      title="Our Inventory is AI — Formula Student kart"
      frameborder="0"
      loading="lazy"
      allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
      allowfullscreen
      style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
  </div>
</div>

Huge thanks to Gabriel Fernández Romero and Adrián for the help.

If you have a similar workflow, try this and share your experience — I'm loving it so far.

---

## Building the battery pack from bare cells { #battery }

*2026-05-14 · [Original on LinkedIn →](https://www.linkedin.com/feed/update/urn:li:activity:7460644047704100864/)*

We made the battery pack ourselves. Why?

To practice. And because we had a bunch of cells lying around from a past project that never used them: 60 Molicel P42A 21700 cells, bought for an electric-vehicle experiment that never happened.

![The finished 13S battery pack](../images/build-journey/2026-05-14-battery/01_pack_assembled_upright.jpg){ loading=lazy }

We needed roughly 48V, so 13 cells in series, 46.8V nominal. The motor draws around 2 kW continuous, so the pack could deliver close to five times what the kart actually asks for. It's the first pack we've ever built, so we wanted big safe margins and no power issues for the computer.

![Molicel P42A cells loaded into the holder grid](../images/build-journey/2026-05-14-battery/03_cells_loaded_grid.jpg){ loading=lazy }

We connected the cells with classic nickel strips. All the current actually flows through the series connections between groups, so the first strip goes in series, then a parallel strip, then another series strip. That's 8 strips per series link sharing the load. At 43 A continuous that's about 5 A per strip. Plenty of margin, and even at the per-cell limit of 45 A each strip stays inside its burst range.

We did the welding with a kWeld. It's funny how it pulses so much current that the magnetic field between its two leads shoves them sideways.

<div style="max-width: 280px; margin: 1em auto;">
  <video controls playsinline preload="metadata" style="width: 100%; border-radius: 8px;">
    <source src="../videos/battery-spot-weld.mp4" type="video/mp4">
  </video>
</div>

![Welding nickel strips between the cells](../images/build-journey/2026-05-14-battery/04_welding_in_progress.jpg){ loading=lazy }

For monitoring, a JBD (Jiabaida) smart BMS with Bluetooth, so we can watch every cell's voltage and state of charge. The Bluetooth advertises continuously waiting for a phone to pair, which we assumed would slowly drain the pack, but after months sitting idle the voltage barely moved.

The pack lives inside a 3D-printed shell with fireproof expanding foam packed around the cells. We drilled two holes, one for the nozzle and another to vent the displaced air, but didn't have the proper applicator gun. The photo below is the result of using pliers to push the bottle open. It was a mess, but it worked. We learned that waiting to do things "properly" can make you wait forever; sometimes you just do it with what you have. Counterintuitively, aiming for fast progress catches errors earlier and makes the end result higher quality.

![Lowering the pack into its 3D-printed enclosure](../images/build-journey/2026-05-14-battery/06_pack_into_enclosure.jpg){ loading=lazy }

![Expanding foam, applied with pliers instead of a proper gun](../images/build-journey/2026-05-14-battery/07_foam_mess.jpg){ loading=lazy }

The whole thing took over 10 hours of work: cells in holders, several layers of nickel strips welded between them, 13 BMS wires soldered and routed cleanly, kapton tape and fish paper so nothing shorts, the printed box, the foam, the cure, plus all the planning and buying the right components. Now I understand why packs cost so much more than just the cells. The amount of time it takes is ridiculous.

But we got a fantastic pack in the end. We can drive as hard as we can, continuously, and the internal temperature never rises more than 10°C above ambient.

It's interesting to think about how we'd build this at scale. The process would have to be entirely different: CNC machines doing the spot welding, pre-made connectors with the layout, maybe a dedicated channel in the cell holders to route the wires through with a jig to place them easily. Automating the BMS-wire soldering would be awkward.

---

## Why 48V, and not more { #why-48v }

*2026-05-18 · [Original on LinkedIn →](https://www.linkedin.com/feed/update/urn:li:activity:7462034279871643649/)*

A common question is: why 48V for the kart battery?

There are two reasonable battery voltages for our kart: under 50V, or several hundred volts. The middle doesn't make sense.

What hurts you is the current through nerves and the heart. Voltage is what drives that current, and your body's resistance to it isn't constant. Skin is mostly capacitive, so it lets AC through more easily than DC, because alternating current keeps charging and discharging the outer layer and leaking into the nerves underneath.

The resistance of skin drops when you raise the voltage, as it starts breaking down, so doubling the voltage doesn't make it twice as dangerous: it causes roughly 3x the current and the safe exposure time drops an order of magnitude. Around 10 mA your muscles lock around the wire and you can't let go. Around 50 mA your heart fibrillates.

![Touch voltage vs exposure time, from IEC 60479-1. Our 48V pack sits at the edge of the perceptible zone.](../images/build-journey/2026-05-18-why-48v/01_iec_60479_voltage_vs_time.png){ loading=lazy }

There's no clean threshold, but in the 40–60V range the risk rises very fast, from negligible to significant.

So our pack lands at 13 cells in series, near the highest that can be touched without worry. Anything higher and we'd be building a high-voltage kart: isolation, interlocks, insulated tools, training for anyone who touches it.

---

## A roll hoop, a bearing spacer, and a throttle sensor { #main-hoop }

*2026-05-21 · [Original on LinkedIn →](https://www.linkedin.com/feed/update/urn:li:activity:7462759132736114688/)*

Karts don't come with roll hoops. They sit low, weigh little, and drivers don't wear seatbelts. In a flip, an unbelted driver gets thrown clear: the kart slides on, the driver lands and tumbles. A hoop bolted overhead turns that into a cage you can't be ejected from, and a kart you can be pinned under. So competition karts ride open.

In our driverless kart we want to be as close to a Formula Student car as possible, and FS cars have seatbelts and roll hoops. On top of that, we needed a high, rigid spot for the stereo camera, which a roll hoop gives us.

We reused the main hoop from a past season's FS car. Its tube ends were round, but bolts need a flat surface to clamp against. We heated the ends with an oxy-propane torch until red, pressed them flat in a hydraulic press, drilled the bolt holes, and bolted the hoop down. It still needs a support bar across the top to stiffen it. That's the next job.

![The reused FS roll hoop placed on the kart](../images/build-journey/2026-05-21-main-hoop/01_hoop_placed_on_kart_day_one.jpg){ loading=lazy }

Thanks to our friends at RB Sistemas for helping with this part.

Next are the wheel bearings. Each wheel has two, one on each side of the rim, with the axle through both. We torqued the axle nut and the wheel didn't spin freely: without a spacer between the inner races, the clamp force could only travel through the bearings themselves. So we cut a tube to length as a spacer and installed it, so the inner races are pressed against the spacer by the nut. Now the bearing only has to take the lateral loads of the kart turning.

![The spacer on the axle, between the inner bearing races](../images/build-journey/2026-05-21-main-hoop/03_bearing_spacer_on_axle.jpg){ loading=lazy }

The kart already had its own accelerator pedal. We needed a sensor on it to read its position, so we took the hall sensor that came with the motor kit and installed it on our pedal with a threaded rod to the chassis. It reads the strength of a magnet and outputs an analog voltage between 0 and 5V.

![The hall throttle sensor mounted on the pedal](../images/build-journey/2026-05-21-main-hoop/04_throttle_sensor_in_situ_on_chassis.jpg){ loading=lazy }

Next: the first manual drive. Everything's going into the [kart docs](https://um-driverless.github.io/kart-docs/) so anyone can build it themselves.

---

## The first manual drive { #first-drive }

*2026-05-27 · [Original on LinkedIn →](https://www.linkedin.com/feed/update/urn:li:activity:7465296164049977346/)*

Finally, the kart works.

<div style="max-width: 315px; margin: 1em auto;">
  <video controls playsinline preload="metadata" style="width: 100%; border-radius: 8px;">
    <source src="../videos/first-manual-drive.mp4" type="video/mp4">
  </video>
</div>

On one of the first runs, the motor pinion gave out. It was a 3D-printed plastic placeholder; we'd been waiting months for the proper machined metal one. The D-profile on the bore rounded off against the motor shaft. The actual cause was the nut backing off, letting the pinion wobble. We swapped in a left-handed nylon locking nut instead of the one that came with the kit, and that fixed it.

We have a kart that moves. Next step is to make it remote-controlled.

In parallel, we're working on the code. There's a [legacy Python codebase](https://github.com/UM-Driverless/driverless) with multithreading from before LLMs were a thing, and the plan is to rewrite it in ROS 2.

---

## Making the kart steer itself: the actuator search { #steering-actuator }

*2026-06-10 · [Original on LinkedIn →](https://www.linkedin.com/feed/update/urn:li:activity:7470401788328914944/)*

Here we are, with a completely manual kart, and we have to make it turn itself.

![The kart's manual steering column](../images/build-journey/2026-06-10-steering-actuator-search/01_manual_kart_steering.jpg){ loading=lazy }

The idea is simple: put an actuator on the steering column to turn it.

But you can't imagine how hard it was to find components for that. Some companies make custom actuators, but we didn't find simple off-the-shelf solutions. They're either too weak, designed for a street car, or built for industrial applications: huge, heavy, and expensive.

For reference, we need about 8 Nm of torque at the steering column to fully turn the wheels while the kart is stopped and loaded with a driver, on grippy floor, which is the worst case. We set a maximum of 0.15 seconds to move the wheels side to side (50 degrees). That's about 6 rad/s, so P = τ·ω = 8 Nm × 6 rad/s ≈ 47W.

There are two main ways to turn it:

1. A rotary system, where you put a gear on the steering column and another on the servo, and that transfers the turning motion.
2. A linear system, where the actuator moves linearly and acts on a lever that turns the steering column.

Linear actuators can provide a lot of force in a compact way, but they can't be backdriven (they lock up), so the kart can't be ridden manually with one unless you use ball screws, which are expensive. On top of that they're slow. You get a lot of reduction, but watt for watt they can't deliver that much mechanical power, and the movement ends up too slow to compensate.

Think about it intuitively: power = torque × angular velocity (P = τ·ω). We can get the same power with a lot of torque or a lot of angular speed.

The torque a motor applies comes from the current flowing through it, which also heats the coils. The coils have a maximum temperature they can withstand, so cooling capacity limits torque directly. For speed, the limits are the mechanical strength of the rotor (so it doesn't explode) and the back-EMF it generates by turning fast. To hit those limits the motor has to spin really fast.

So if we want a lot of power from a small motor, we make it spin fast and gear it down for the torque we need. That's why we went with a rotary actuator.

![Four ways to gear a fast motor down: gear train, planetary, cycloidal, harmonic drive](../images/build-journey/2026-06-10-steering-actuator-search/02_reducer_mechanisms_diagram.png){ loading=lazy }

How would you gear it down? Anything from the diagram above, or something else?

Steering system docs: [um-driverless.github.io/kart-docs/assembly/steering](https://um-driverless.github.io/kart-docs/assembly/steering/).

---

## Why a planetary reducer { #planetary-reducer }

*2026-06-29 · [Original on LinkedIn →](https://www.linkedin.com/feed/update/urn:li:activity:7477360277299208192/)*

Last time we talked about the decision to make our own actuator. Why a planetary reducer, of all things?

A belt needs a tensioner. A worm or a screw won't backdrive, so the wheels lock if the power dies. A harmonic drive needs a steel flexspline you can't just print if you want any strength.

We could use a plain gear train between the motor and the steering column, using both shafts. The disadvantage is the added slack.

A cycloidal drive could also work, but it's more complex and needs specific components we'd have to order, which would delay the project, especially while we still don't know the details of this little subsystem. It's a good alternative, and we're not discarding it, but for now we go with the (somewhat) simpler planetary reducer.

For us, the fastest way to get a prototype working is to 3D-print the planetary reducer to match a motor we already have. That motor comes from an old massage chair.

<video controls playsinline muted preload="metadata" style="width: 100%; max-width: 720px; display: block; margin: 1em auto; border-radius: 8px;">
  <source src="../videos/planetary-cad.mp4" type="video/mp4">
</video>

Our first prints stripped out under the steering loads. A tougher filament would probably hold, but a spool of it costs more than just buying the gear. So we stopped printing and adjusted the design to use a standard steel gear from Norelem.

Next week we'll talk about the exact design.

Steering/planetary docs: [um-driverless.github.io/kart-docs/assembly/steering](https://um-driverless.github.io/kart-docs/assembly/steering/).

---

<!--
PLACEHOLDER — upcoming post: "Making it fast" (cone detection → 81 FPS on the Jetson Orin)
Stage 2 of the perception-speed story. Stage 1 (Deteccion_conos, multithreading + polymorphic
rewrite, ~8→50 FPS) lives on the Formula Student page. This post covers the ROS 2 + AI-era
optimizations: FP16 + TensorRT (.pt → .engine, layer fusion), sky-crop, jetson_clocks, ZED VGA
672x376, nano→small model → 81 FPS while running the dashboard + server. Source draft:
~/ruben-files/videos/kart/linkedin/posts/making_it_fast/ (Rubén publishes, then migrate here).
Add as a dated ## section with #anchor and update the "Jump to:" line when it ships.
-->

*That's the latest post. New ones land roughly every Wednesday — [follow on LinkedIn](https://www.linkedin.com/in/rubenayla/) to catch them as they ship, or check back here.*
