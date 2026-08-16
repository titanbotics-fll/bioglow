# 🤖 Titanbotics Python

Welcome to the **Titanbotics** Python code repository!

This repository contains the Python code for our FLL robot, written using **Pybricks**.

Our goal is to keep our team's code organized, safe, and easy for everyone to understand.

---

## 🧑‍💻 How We Work

We use **Pybricks Code** to write and test our programs.

We use **GitHub** to save and organize code that the team wants to keep.

Our normal workflow is:

1. Write your code in **Pybricks Code**.
2. Test your code on the robot.
3. Fix problems and test again.
4. Make sure the code works.
5. Copy the working code from Pybricks.
6. Put it in the correct folder in this repository.
7. Save the changes to GitHub.

### Important

**Pybricks is where we write, experiment, and test.**

**GitHub is where we save our team's code.**

You do not need to save every small experiment to GitHub.

---

## 📁 Repository Structure

Our repository has three main folders:

- `missions/` — Programs that run the robot to complete FLL missions.
- `common/` — Reusable code that can be used by multiple missions.
- `experiments/` — A safe place to try new ideas before adding them to official team code.

---

## 🏆 1. Missions

### Purpose

The `missions/` folder contains programs that are used to complete specific FLL missions.

Each mission should normally have its own Python file.

### Examples

- `mission-01.py`
- `mission-02.py`
- `mission-03.py`

### What Belongs Here

Put code in `missions/` when:

- The code is specifically for one FLL mission.
- The code has been tested on the robot.
- The code is ready for the team to use.

### What Does Not Belong Here

Do not put general-purpose code here if it will be used by multiple missions.

That code belongs in `common/`.

### File Naming

Use clear names such as:

- `mission-01.py`
- `mission-02.py`
- `mission-03.py`

Do not use names such as:

- `new.py`
- `test.py`
- `final.py`
- `final-final.py`
- `mission-new.py`

Clear names make it easier for everyone to find the correct program.

---

## 🧰 2. Common

### Purpose

The `common/` folder contains **reusable code** that can be used by more than one mission.

Examples include:

- Driving
- Turning
- Moving a specific distance
- Using sensors
- Controlling motors
- Controlling attachments
- Other reusable functions

### Example Files

- `drive.py`
- `sensors.py`
- `attachments.py`

### When Should Code Go Here?

Ask yourself:

> "Will more than one mission need this code?"

If the answer is **yes**, it may belong in `common/`.

If the answer is **no**, keep it in the mission's file.

### Why Use Common Code?

Imagine that five missions need the robot to drive straight.

Instead of writing the same driving code five times, we can create the code once and reuse it.

This makes our programs:

- Shorter
- Easier to understand
- Easier to fix
- Easier for teammates to use

---

## 🧪 3. Experiments

### Purpose

The `experiments/` folder is our **safe playground**.

Use it when you want to try something new without changing working team code.

### Examples

- Testing a new way to turn
- Testing a sensor
- Testing a new attachment
- Trying a different driving strategy
- Testing a new idea for a mission

Example file names:

- `test-new-turn.py`
- `test-color-sensor.py`
- `try-new-attachment.py`

### Experiments Do Not Have to Be Perfect

It is okay for experimental code to be messy.

The purpose of an experiment is to:

1. Try an idea.
2. Test it.
3. Learn what works.
4. Improve it.

Do not worry about making experimental code perfect.

---

## ⭐ 4. Moving Experimental Code Into Team Code

Sometimes an experiment works really well.

When that happens:

1. Test it again.
2. Make sure it works reliably.
3. Show it to the team.
4. Clean up the code.
5. Decide whether it belongs in `missions/` or `common/`.
6. Save the improved version in the correct folder.

For example:

`experiments/test-new-turn.py`

might eventually become part of:

`common/drive.py`

Do not move experimental code into official team code until it has been tested.

---

## 🧹 5. Keep Our Code Clean

Good code is easier for teammates to understand.

### Use Clear File Names

Good:

- `mission-01.py`
- `mission-02.py`
- `test-color-sensor.py`
- `drive.py`

Not so good:

- `thing.py`
- `stuff.py`
- `asdf.py`
- `new.py`
- `test2.py`

### Add Comments

Comments help teammates understand your code.

Add comments when something might not be obvious.

Do not add comments to every single line.

---

## 🚦 6. Before Changing Working Code

Be careful with code that already works.

Before making a big change:

1. Make sure you understand what the code does.
2. Make your change.
3. Test your change on the robot.
4. Make sure the robot still works.
5. Ask a teammate or coach if you are unsure.

> **Working code is valuable!**

If you want to try a completely different idea, try it in `experiments/` first.

---

## 💾 7. Saving Code to GitHub

When your program is working:

1. Open the program in **Pybricks Code**.
2. Copy the Python code.
3. Open the correct folder in this repository.
4. Create or open the correct `.py` file.
5. Paste the code.
6. Check that the code is correct.
7. Save the changes to GitHub.

### Before Saving, Ask Yourself

- Is this the correct folder?
- Is the filename clear?
- Does the code actually work?
- Did I accidentally change something unrelated?
- Did I copy the latest working version from Pybricks?

---

## 🔄 8. Do Not Overwrite Someone Else's Work

We are a team of programmers.

Someone else may be working on the same mission.

**Do not replace someone else's code without talking to them first.**

If you want to try a different approach:

1. Make a copy in `experiments/`.
2. Try your idea there.
3. Test it.
4. Compare the results.
5. Decide as a team which version is better.

---

## 🧠 9. Reuse Code

If you find yourself copying the same code into several missions, stop and ask:

> **"Should this become common code?"**

For example, if several missions use the same type of turn, that turning code may belong in `common/drive.py`.

Reusable code makes our programs:

- Shorter
- Easier to understand
- Easier to fix
- Easier for teammates to use

---

## 🤖 10. Pybricks Rules

**Pybricks Code is our programming and testing environment.**

Use Pybricks to:

- Write code
- Run code
- Test the robot
- Debug problems
- Try new ideas

Use GitHub as our team's:

- Code library
- Backup
- History of working code
- Place to share code with teammates

---

## 🆘 11. Something Went Wrong?

Don't panic!

If your code stops working:

1. Stop.
2. Do not delete anything.
3. Check what you changed.
4. Test the previous working version.
5. Ask a teammate or coach for help.

**Never delete someone else's code because you think it is wrong.**

---

## 🏁 12. Our Team Rules

### Rule 1

**Test before saving.**

### Rule 2

**Do not overwrite someone else's work.**

### Rule 3

**Use clear file names.**

### Rule 4

**Put code in the correct folder.**

### Rule 5

**Use `experiments/` for new ideas.**

### Rule 6

**Put reusable code in `common/`.**

### Rule 7

**Keep mission-specific code in `missions/`.**

### Rule 8

**Ask for help when you are stuck.**

### Rule 9

**Help your teammates.**

### Rule 10

**Have fun building! 🤖**

---

# 🏆 Go Titanbotics!

We are here to learn, experiment, solve problems, and build an awesome robot.
