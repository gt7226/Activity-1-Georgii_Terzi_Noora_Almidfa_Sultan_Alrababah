import turtle

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("purple")  # Set the background color to purple

# Create a turtle named cake to draw the cake
cake = turtle.Turtle()
cake.speed(2)  # Set the speed of the turtle

# Function to draw a rectangle tabletop or cake layers
def draw_rectangle(width, height, color):
    cake.fillcolor(color)
    cake.begin_fill()
    for _ in range(2):
        cake.forward(width)
        cake.left(90)
        cake.forward(height)
        cake.left(90)
    cake.end_fill()

# Ask the user for table color
table_color = input("Please enter the color of the table: ")

# Ask for cake size
while True:
    cake_size = int(input("Please enter the size of the cake (between 100-150): "))
    if 100 <= cake_size <= 150:
        break
    else:
        print("Cake size must be between 100 and 220.")

# Set table size to be 50 units wider than the first layer of the cake
table_size = cake_size * 2 + 50

# Draw the tabletop
cake.penup()         
cake.goto(-table_size // 2, -130)  
cake.pendown()       
draw_rectangle(table_size, 30, table_color)  # Draw the tabletop with user-specified color

# Draw table legs, making sure they are proportional to the table size
def draw_leg(x, y):
    cake.penup()         
    cake.goto(x, y)      
    cake.pendown()       
    draw_rectangle(10, 90, table_color)  # Draw the legs with the table color

# Calculate leg positions based on table size
leg_offset = table_size // 2 - 20  # Adjust the distance of legs from the tables center
draw_leg(-leg_offset, -220)  # Left leg
draw_leg(leg_offset - 10, -220)   # Right leg
draw_leg(leg_offset - 30, -220)   # Another right leg
draw_leg(-leg_offset + 20, -220)  # Another left leg

# Scale cake layers  to the cake size
layer_height = 50  # Fixed height for each cake layer
cake_width_scale = cake_size  # Use the input cake size as a base for scaling layers

# Draw the first layer of the cake largest layer
cake.penup()
cake.goto(-cake_width_scale, -100)
cake.pendown()
draw_rectangle(cake_width_scale * 2, layer_height, "pink")  # First layer of cake

# Draw the second layer of the cake 75% of the first layers width
cake.penup()
cake.goto(-cake_width_scale * 3 // 4, -50)
cake.pendown()
draw_rectangle(cake_width_scale * 1.5, layer_height, "white")  # Second layer of cake

# Draw the top layer of the cake 50% of the first layer width
cake.penup()
cake.goto(-cake_width_scale // 2, 0)
cake.pendown()
draw_rectangle(cake_width_scale, layer_height, "red")  # Top layer of cake

# Draw candles on the cake  making sure they're centered on the top layer
def draw_candle(x, y):
    cake.penup()
    cake.goto(x, y)
    cake.setheading(0)  # Make the turtle face east before starting to draw
    cake.pendown()

    # Draw the candle body
    cake.fillcolor("yellow")
    cake.begin_fill()
    for _ in range(2):
        cake.forward(10)  # Width of the candle
        cake.left(90)
        cake.forward(30)  # Height of the candle
        cake.left(90)
    cake.end_fill()

    # Draw the candle flame
    cake.penup()
    cake.forward(10)  
    cake.left(90)
    cake.forward(30)
    cake.pendown()

    cake.fillcolor("orange")
    cake.begin_fill()
    cake.circle(5)  # Draw the flame as a circle
    cake.end_fill()

# Draw three candles evenly spaced on the top layer of the cake
candle_spacing = cake_width_scale // 3  # Space candles based on the cake size
draw_candle(-candle_spacing, 50)  # Left candle
draw_candle(0, 50)                # Middle candle
draw_candle(candle_spacing, 50) 

# Hide the turtle and wait for a click to close the window
cake.hideturtle()

# Message to exit
screen.textinput("Exit", "Press Any Character To Exit")
turtle.bye()
