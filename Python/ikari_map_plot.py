import sys
from PIL import Image

# Constants
TILE_WIDTH = 16
TILE_HEIGHT = 16
TILES_PER_ROW = 16  # screen width in tiles
PIXELS_PER_TILE = TILE_WIDTH * TILE_HEIGHT
BYTES_PER_TILE = PIXELS_PER_TILE // 2  # 4bpp -> 2 pixels per byte


def load_palette(palette_file):
    palette = []
    with open(palette_file, 'rb') as f:
        data = f.read()
        for i in range(0, len(data), 3):
            r = data[i]
            g = data[i + 1]
            b = data[i + 2]
            palette.append((r, g, b))
    return palette


def load_tiles(tiles_file):
    with open(tiles_file, 'rb') as f:
        return f.read()


def load_map(map_file):
    map_data = []
    with open(map_file, 'rb') as f:
        raw = f.read()
        for i in range(0, len(raw), 2):
            word = raw[i] | (raw[i+1] << 8)
            word = word & 0x3FF  # Mask to $000-$3FF range
            map_data.append(word)
    return map_data


def draw_map(tiles_data, map_data, palette, output_file):
    # Calculate dimensions
    num_tiles = len(map_data)
    rows = (num_tiles + TILES_PER_ROW - 1) // TILES_PER_ROW

    image_width = TILES_PER_ROW * TILE_WIDTH
    image_height = rows * TILE_HEIGHT

    img = Image.new('RGB', (image_width, image_height))
    pixels = img.load()

    for index, tile_index in enumerate(map_data):
        tile_x = (index % TILES_PER_ROW) * TILE_WIDTH
        tile_y = image_height - ((index // TILES_PER_ROW) + 1) * TILE_HEIGHT  # bottom to top

        tile_offset = tile_index * BYTES_PER_TILE
        tile_data = tiles_data[tile_offset:tile_offset + BYTES_PER_TILE]

        for y in range(TILE_HEIGHT):
            for x in range(0, TILE_WIDTH, 2):
                byte_index = (y * TILE_WIDTH + x) // 2
                byte = tile_data[byte_index]

                pixel1 = (byte & 0xF0) >> 4
                pixel2 = (byte & 0x0F)

                pixels[tile_x + x, tile_y + y] = palette[pixel1]
                pixels[tile_x + x + 1, tile_y + y] = palette[pixel2]

    img.save(output_file)


def main():
    if len(sys.argv) != 5:
        print("Usage: python ikari_map_plot.py tiles.bin map.bin palette.bin output.png")
        return

    tiles_file = sys.argv[1]
    map_file = sys.argv[2]
    palette_file = sys.argv[3]
    output_file = sys.argv[4]

    palette = load_palette(palette_file)
    tiles_data = load_tiles(tiles_file)
    map_data = load_map(map_file)

    draw_map(tiles_data, map_data, palette, output_file)


if __name__ == "__main__":
    main()
