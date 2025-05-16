# ikari
Python script will generate the Arcade Game Ikari Warriors maps into a PNG format images.
# Ikari Warriors Map Plotter (`ikari_map_plot.py`)

This repository contains tools for visualising tile-based background maps from the classic arcade game **Ikari Warriors** by SNK (1986). The main script, `ikari_map_plot.py`, takes binary map and graphics data extracted from the game's ROM and generates full-resolution visual maps in PNG format. This effort is only intended for historical preservation, technical analysis, and educational purposes.

---

## 📁 Data Format Overview

Ikari Warriors uses a custom tilemap format optimised for arcade hardware of the 1980s. Through reverse engineering, we identified the following formats:

### 1. Character Tiles (Graphics)

* Stored in a binary file (`gfx.bin` or similar)
* Tile size: **8×8 pixels**
* Color depth: **4 bits per pixel (4bpp)**
* Each tile: **32 bytes** (8 rows × 4 bytes per row)
* Sequential tile storage; referenced by tile index

### 2. Palette File

* 768 bytes total (for the background graphics)
* 16 palettes × 16 colors each
* Each colour: 3 bytes (RGB)
* 48 bytes per palette
* Palette index per tile comes from the attribute byte

### 3. Map Data Format

Each tile block entry is **3 bytes**, structured as:

```
[ tile_low ] [ tile_high ] [ attribute ]
```

* **Tile Number**: 16-bit little-endian value
* **Attribute Byte**:

  * Bits 0–3: Palette index (0–15)
  * Bit 6: Flip X
  * Bit 7: Flip Y

### 4. Map Structure

* The game uses **8×6 character tile blocks** (64x48 pixels per block)
* Map layout consists of **columns** of tile blocks
* Each column contains eight or more blocks forming a vertically scrollable area
* The full map is rendered by combining these columns horizontally

---

## 🛠️ Script Functionality

`ikari_map_plot.py` performs the following:

* Reads and decodes character tile data
* Loads and applies palette data
* Interprets map entries and their attributes
* Handles X/Y flip for tile rendering
* Constructs and saves a full PNG image
* Optional debug modes for overlaying the grid or targeting specific blocks

---

## ⚡ Usage

```bash
python ikari_map_plot.py gfx.bin palette.bin map.bin output.png
```

### Optional Flags

* `--grid`: Draw a white grid to outline tile blocks
* `--block <index>`: Render only a specific tile block (0–255)

---

## 📃 Disclaimer

This repository does not include any ROM data or copyrighted game content. To use the batch script, you must put your legally obtained ROM files (Unzipped!) into the folder. All data will be re-created.
Many of the same scripts can also be used on other titles of IREM, as the hardware is almost identical, but they may process the tile data differently.

All reverse-engineered information is provided for educational and preservation purposes. To use this tool, you'll need to provide legal binary data obtained from Ikari Warriors.

---

## 📄 License

This project is released under the MIT License. See `LICENSE` for details.
