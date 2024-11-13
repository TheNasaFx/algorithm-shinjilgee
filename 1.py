def calculate_video_ram(lines, columns, num_colors):
    bits_per_character = int(num_colors).bit_length()  
    total_characters = lines * columns
    total_bits = total_characters * bits_per_character
    total_bytes = total_bits / 8
    return total_bytes

def video_ram_for_graphics_mode(width, height, num_colors):
    bits_per_pixel = int(num_colors).bit_length()  
    total_pixels = width * height
    total_bits = total_pixels * bits_per_pixel
    total_bytes = total_bits / 8
    return total_bytes

def time_for_text_processing(num_characters, speed_ns):
    total_ns = num_characters * speed_ns
    total_seconds = total_ns / 1e9
    return total_seconds

# Text display calculations
lines_text_display = 25
columns_text_display = 80
num_colors_text_display = 4

# Graphics mode calculations
width_graphics_mode_1 = 800
height_graphics_mode_1 = 640
num_colors_graphics_mode_1 = 16

width_graphics_mode_2 = 600
height_graphics_mode_2 = 400
bits_per_pixel_graphics_mode_2 = 8  # 8-bit color

# Text processing calculations
pages_book_1 = 500
lines_per_page_1 = 30
characters_per_line_1 = 60

pages_book_2 = 100
lines_per_page_2 = 20
characters_per_line_2 = 50

# Speed assumptions (nanoseconds per character)
speed_cache_ns = 5
speed_ram_ns = 50
speed_ssd_us = 200
speed_hdd_ms = 10

# Calculate video RAM for text display
video_ram_text_display = calculate_video_ram(lines_text_display, columns_text_display, num_colors_text_display)
print(f"Video RAM needed for {lines_text_display}x{columns_text_display} display with {num_colors_text_display} colors: {video_ram_text_display:.2f} bytes")

# Calculate video RAM for graphics modes
video_ram_graphics_mode_1 = video_ram_for_graphics_mode(width_graphics_mode_1, height_graphics_mode_1, num_colors_graphics_mode_1)
print(f"Video RAM needed for {width_graphics_mode_1}x{height_graphics_mode_1} graphics mode with {num_colors_graphics_mode_1} colors: {video_ram_graphics_mode_1:.2f} bytes")

video_ram_graphics_mode_2 = video_ram_for_graphics_mode(width_graphics_mode_2, height_graphics_mode_2, bits_per_pixel_graphics_mode_2)
print(f"Video RAM needed for {width_graphics_mode_2}x{height_graphics_mode_2} graphics mode with {bits_per_pixel_graphics_mode_2}-bit color: {video_ram_graphics_mode_2:.2f} bytes")

# Text processing time
num_characters_book_1 = pages_book_1 * lines_per_page_1 * characters_per_line_1
num_characters_book_2 = pages_book_2 * lines_per_page_2 * characters_per_line_2

time_cache_book_1 = time_for_text_processing(num_characters_book_1, speed_cache_ns)
time_ram_book_1 = time_for_text_processing(num_characters_book_1, speed_ram_ns)
time_ssd_book_1 = time_for_text_processing(num_characters_book_1, speed_ssd_us * 1e3)  # Convert microseconds to nanoseconds
time_hdd_book_1 = time_for_text_processing(num_characters_book_1, speed_hdd_ms * 1e6)  # Convert milliseconds to nanoseconds

time_cache_book_2 = time_for_text_processing(num_characters_book_2, speed_cache_ns)
time_ram_book_2 = time_for_text_processing(num_characters_book_2, speed_ram_ns)
time_ssd_book_2 = time_for_text_processing(num_characters_book_2, speed_ssd_us * 1e3)  # Convert microseconds to nanoseconds
time_hdd_book_2 = time_for_text_processing(num_characters_book_2, speed_hdd_ms * 1e6)  # Convert milliseconds to nanoseconds

print(f"\nTime to check the text of the first book:")
print(f"  Cache Memory: {time_cache_book_1:.2f} seconds")
print(f"  RAM Memory: {time_ram_book_1:.2f} seconds")
print(f"  SSD Disk: {time_ssd_book_1:.2f} seconds")
print(f"  HDD Disk: {time_hdd_book_1:.2f} seconds")

print(f"\nTime to search for letters in the 'Policies' book:")
print(f"  Cache Memory: {time_cache_book_2:.2f} seconds")
print(f"  RAM Memory: {time_ram_book_2:.2f} seconds")
print(f"  SSD Disk: {time_ssd_book_2:.2f} seconds")
print(f"  HDD Disk: {time_hdd_book_2:.2f} seconds")
