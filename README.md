# on-device-paper-template
On Device Paper Template



# TinyML On-Device Training Paper Template

This repository template is designed for **TinyML / MCU research papers** where experiments must be reproducible.

It includes a standardized structure for:

• firmware  
• datasets  
• hardware documentation  
• experiment results  
• reproduction instructions  

---

# Repository Structure

```
paper/        → LaTeX and figures for the paper
firmware/     → MCU training and inference code
hardware/     → bill of materials and wiring notes
dataset/      → dataset examples and capture protocol
results/      → logs and measurements
reproduce/    → experiment reproduction capsules
docs/         → tutorials and setup guides
```

---

# Reproducibility Philosophy

Each major experiment should be assigned an **Experiment ID**.

Example:

```
EXP-S3-CNN-042
```

The experiment ID should appear in:

• firmware header  
• dataset folder  
• result logs  
• paper figures  

This ensures all results can be traced to a specific experiment.

---

# Quick Start

1 Install Arduino IDE  
2 Install ESP32 board support  
3 Enable PSRAM  
4 Upload firmware

```
firmware/firmware.ino
```

Full setup instructions:

```
docs/getting-started.md
```

---

# Reproducing Experiments

Reproduction capsules are stored in:

```
reproduce/
```

Each experiment folder contains:

• firmware version  
• dataset sample  
• step-by-step run procedure  
• expected results  

---

# License

MIT License
