REM this will combine all the bitplanes for the BG graphics
copy /b p17.4d+p18.2d+p19.4b+p20.2b bg-origin.bin
REM first reverse the bytes
python .\python\reversebyte.py bg-origin.bin
REM now rotate the characters 90 degrees anti-clockwise, beuuase the game screen in the arcade is actually sideways
python .\python\rotate90.py reverse_bg-origin.bin rotated_bg.original.bin 16 16
REM Now we rotate the data back
python .\python\reversebyte.py rotated_bg.original.bin
REM this swaps over the 4bits in each byte to and up with the final data needed.
python .\python\swapnybbles.py reverse_rotated_bg.original.bin

python .\python\make_palette4.py a6002-1.1k a6002-2.2l a6002-3.1l all_palettes

REM All tile maps for large chunks
python .\python\savebit.py 2.8p all_maps.bin 1040 8000
python .\python\splitchunks.py all_maps.bin level_map 4096

REM game map very small data set which is just the large map tile chunk numbers
python .\python\savebit.py 2.8p Map_offset_data.bin 1000 40
REM generate one giant PNG for entire game map
python .\python\ikari_map_plot2.py swapped_reverse_rotated_bg.original.bin all_maps.bin all_palettes_2.bin Map_offset_data.bin Big_final_level.png


REM this is just chunks of data as a test for level
python .\python\ikari_map_plot.py swapped_reverse_rotated_bg.original.bin level_map_1 all_palettes_2.bin level1.png
python .\python\ikari_map_plot.py swapped_reverse_rotated_bg.original.bin level_map_2 all_palettes_2.bin level2.png
python .\python\ikari_map_plot.py swapped_reverse_rotated_bg.original.bin level_map_3 all_palettes_2.bin level3.png
python .\python\ikari_map_plot.py swapped_reverse_rotated_bg.original.bin level_map_4 all_palettes_2.bin level4.png
python .\python\ikari_map_plot.py swapped_reverse_rotated_bg.original.bin level_map_5 all_palettes_2.bin level5.png
python .\python\ikari_map_plot.py swapped_reverse_rotated_bg.original.bin level_map_6 all_palettes_2.bin level6.png
python .\python\ikari_map_plot.py swapped_reverse_rotated_bg.original.bin level_map_7 all_palettes_2.bin level7.png
python .\python\ikari_map_plot.py swapped_reverse_rotated_bg.original.bin level_map_8 all_palettes_2.bin level8.png
python .\python\ikari_map_plot.py swapped_reverse_rotated_bg.original.bin all_maps.bin all_palettes_2.bin All_levels.png
