import turtle

# Set the background color to purple
turtle.bgcolor("purple")

# Function to draw a rectangle 
def draw_rectangle(width, height, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.end_fill()

# Ask the user for table color
table_color = input("Please enter the color of the table: ")

# Ask for cake size
cake_size = int(input("Please enter the size of the cake between 100-150: "))

# Set table size to be 50 units wider than the first layer of the cake
table_size = cake_size * 2 + 50

# Draw the tabletop
turtle.penup()         
turtle.goto(-table_size // 2, -130)  
turtle.pendown()       
draw_rectangle(table_size, 30, table_color)  # Draw the tabletop with user-specified color

# Draw table legs
def draw_leg(x, y):
    turtle.penup()         
    turtle.goto(x, y)      
    turtle.pendown()       
    draw_rectangle(10, 90, table_color)  # Draw the legs with the table color

# Calculate leg positions based on table size
leg_offset = table_size // 2 - 20
draw_leg(-leg_offset, -220)  # Left leg
draw_leg(leg_offset - 10, -220)   # Right leg
draw_leg(leg_offset - 30, -220)   # Another right leg
draw_leg(-leg_offset + 20, -220)  # Another left leg

# Scale cake layers to the cake size
layer_height = 50  # Fixed height for each cake layer
cake_width_scale = cake_size  # Use the input cake size as a base for scaling layers

# Draw the first layer of the cake
turtle.penup()
turtle.goto(-cake_width_scale, -100)
turtle.pendown()
draw_rectangle(cake_width_scale * 2, layer_height, "pink")  # First layer of cake

# Draw the second layer of the cake
turtle.penup()
turtle.goto(-cake_width_scale * 3 // 4, -50)
turtle.pendown()
draw_rectangle(cake_width_scale * 1.5, layer_height, "white")  # Second layer of cake

# Draw the top layer of the cake
turtle.penup()
turtle.goto(-cake_width_scale // 2, 0)
turtle.pendown()
draw_rectangle(cake_width_scale, layer_height, "red")  # Top layer of cake

# Draw candles on the cake
def draw_candle(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0)  # Make the turtle face east before starting to draw
    turtle.pendown()

    # Draw the candle body
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    
    turtle.forward(10)  
    turtle.left(90)
    turtle.forward(30)  
    turtle.left(90)
    turtle.forward(10) 
    turtle.left(90)
    turtle.forward(30)  
    
    turtle.end_fill()

    # Draw the candle flame
    turtle.penup()
    turtle.setheading(0) # Make the turtle face east before starting to draw
    turtle.forward(10)  
    turtle.left(90)
    turtle.forward(30)
    turtle.pendown()

    turtle.fillcolor("orange")
    turtle.begin_fill()
    turtle.circle(5)  # Draw the flame as a circle
    turtle.end_fill()

# Draw three candles evenly spaced on the top layer of the cake
candle_spacing = cake_width_scale // 3
draw_candle(-candle_spacing, 50)  # Left candle
draw_candle(0, 50)                # Middle candle
draw_candle(candle_spacing, 50)   # Right candle

# Hide the turtle
turtle.hideturtle()

# Message to exit 
input("Press Enter to close the window ")

# Close the turtle graphics window
turtle.bye()
