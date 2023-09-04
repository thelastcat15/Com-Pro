import turtle
import tkinter.font

# Create a turtle screen
screen = turtle.Screen()

# Get the available fonts
available_fonts = tkinter.font.families()

# Set font size and line spacing
font_size = 24
line_spacing = 50
fonts_per_line = 5  # Number of fonts per line

# Create a turtle
t = turtle.Turtle()
t.penup()
t.goto(-100, 0)

# Create a canvas to capture the output
capture_canvas = turtle.Screen().getcanvas()

# Loop through available fonts and print "STOP"
i = 1
for idx, font_name in enumerate(available_fonts):
    try:
        font = (font_name, font_size, "normal")
        t.write("STOP", font=font)
        print(font_name)
        if i == 8 : break
        t.forward(100)  # Move turtle to the right for the next font
        i += 1
        # Check if the end of line is reached
        if (idx + 1) % fonts_per_line == 0:
            t.goto(-100 , t.ycor() - line_spacing)  # Move turtle to the next line
    except:
        pass  # Ignore fonts that can't be used

# Save the canvas as an image
capture_canvas.postscript(file="font_output.eps", colormode='color')

# Close the turtle graphics window

input()