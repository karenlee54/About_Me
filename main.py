import js as p5

program_state = 'START'
Font = p5.loadFont('Neue Haas Unica W1G.otf')

class Point:
  def __init__(self, x = -20, y = -20):
    self.x = x
    self.y = y
    p5.imageMode(p5.CENTER)
    self.T = p5.loadImage('End.png')

  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    p5.image(self.T, 0, 0, 20, 20)
    p5.pop()

class Logo:
  x = 200
  y = 280

  def __init__(self):
    self.img1 = p5.loadImage('Logo.png')

  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    p5.imageMode(p5.CENTER)
    p5.image(self.img1, 0, 0, 200, 180)
    p5.textAlign(p5.CENTER)
    p5.textFont(Font, 20)
    p5.text('About Me', 0, 140)
    p5.textFont(Font, 15)
    p5.text('Click to start', 0, 275)
    p5.pop()


class Button:
  x = 200
  y = 540

  def __init__(self):
    self.img2 = p5.loadImage('Logo_Horizontal.jpg')

  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    p5.imageMode(p5.CENTER)
    p5.image(self.img2, 0, 0, 350, 80)
    p5.pop()

class Karen:
  def __init__(self, x = 25, y = 500):
    p5.imageMode(p5.CENTER)
    self.KE = p5.loadImage('KAREN_E.png')
    self.KK = p5.loadImage('KAREN_K.png')
    self.timer = p5.millis()
    self.x = x
    self.y = y

class Karen_K(Karen):
  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    if(p5.millis() % 1000 < 500):
      p5.image(self.KE, 0, 0, 102.1, 30)
    else:
      p5.image(self.KK, 0, 0, 69.67, 30)
    p5.pop()

  def update(self):
    if(p5.millis() > self.timer + 500):
      self.y -= 3

class Seoyoung:
  def __init__(self, x = 155, y = 500):
    p5.imageMode(p5.CENTER)
    self.SE = p5.loadImage('SEOYOUNG_E.png')
    self.SK = p5.loadImage('SEOYOUNG_K.png')
    self.timer = p5.millis()
    self.x = x
    self.y = y

class Seoyoung_S(Seoyoung):
  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    if(p5.millis() % 1000 < 500):
      p5.image(self.SE, 0, 0, 178.66, 37.89)
    else:
      p5.image(self.SK, 0, 0, 69.67, 30)
    p5.pop()

  def update(self):
    if(p5.millis() > self.timer + 500):
      self.y -= 3

class Lee:
  def __init__(self, x = 245, y = 500):
    p5.imageMode(p5.CENTER)
    self.LE = p5.loadImage('LEE_E.png')
    self.LK = p5.loadImage('LEE_K.png')
    self.timer = p5.millis()
    self.x = x
    self.y = y

class Lee_L(Lee):
  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    if(p5.millis() % 1000 < 500):
      p5.image(self.LE, 0, 0, 63.72, 30)
    else:
      p5.image(self.LK, 0, 0, 31.83, 30)
    p5.pop()

  def update(self):
    if(p5.millis() > self.timer + 500):
      self.y -= 3

class Triangle:
  def __init__(self, x = 25, y = 30):
    p5.imageMode(p5.CORNER)
    self.E = p5.loadImage('Name_E.png')
    self.K = p5.loadImage('Name_K.png')
    self.L = p5.loadImage('Logo Animation.gif')
    self.timer = p5.millis()
    self.x = x
    self.y = y

class Triangle_T(Triangle):
  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    p5.imageMode(p5.CORNER)
    p5.image(self.E, 116.5, 0, 233.13, 25)
    p5.image(self.L, -5, -5, 110, 100)
    p5.textAlign(p5.LEFT)
    p5.textFont(Font, 17)
    p5.text('Graphic Designer', 116.5, 65)
    p5.text('UI/UX Designer', 116.5, 88)
    p5.textFont(Font, 20)
    p5.text('Triangle means end like a period', 0, 260)
    p5.textFont('Helvetica', 20)
    p5.text('△', 293, 260)
    p5.textFont(Font, 15)
    p5.text('But draw anything you want here!', 0, 300)
    p5.text('This is your place ', 0, 322)
    p5.textFont('Helvetica', 15)
    p5.text('△', 118, 322)
    p5.textFont(Font, 14)
    p5.text('+1 626.491.5982', 0, 497)
    p5.text('karenslee911@gmail.com', 0, 519)
    p5.text('karenseoyounglee.com', 0, 540) 
    p5.pop()

point = Point()
point_list = [point]


# print('Assignment #8 (Final Project Part B)')

logo = Logo()
button = Button()
karen = Karen_K()
seoyoung = Seoyoung_S()
lee = Lee_L()
triangle = Triangle_T()



def setup():
  p5.createCanvas(800, 1400)  

def draw():
  p5.background(255)   
  p5.fill(0)  
  # cursor_xy = (int(p5.mouseX), int(p5.mouseY))
  # p5.text(cursor_xy, 10, 20)  # cursor (x, y) 

  global program_state, karen, seoyoung, lee

  if (program_state == 'START'):
    logo.draw()
      
  if (program_state == 'PLAY'):

    p5.textAlign(p5.CORNER)
    p5.textFont(Font, 18)
    p5.text('Click each of the symbols,', 25, 40)
    p5.text('it means...', 25, 65)
    
    #Karen
    if (p5.mouseX > 25) and (p5.mouseX < 105) and (p5.mouseY > 500) and (p5.mouseY < 600):
      karen.draw()
      karen.update()
    else:
      karen.x = 65
      karen.y = 540

    #Seoyoung
    if (p5.mouseX > 115) and (p5.mouseX < 195) and (p5.mouseY > 500) and (p5.mouseY < 600):
      seoyoung.draw()
      seoyoung.update()
    else:
      seoyoung.x = 155
      seoyoung.y = 540

    #Lee
    if (p5.mouseX > 205) and (p5.mouseX < 285) and (p5.mouseY > 500) and (p5.mouseY < 600):
      lee.draw()
      lee.update()
    else:
      lee.x = 245
      lee.y = 540

    #Triangle
    if (p5.mouseX > 295) and (p5.mouseX < 375) and (p5.mouseY > 500) and (p5.mouseY < 600):
      program_state = 'END'

    button.draw()
  
  if (program_state == 'END'):
    p5.textAlign(p5.CORNER)
    triangle.draw()
    
    for i in range(len(point_list)):
      point = point_list[i]
      point.draw()

    if(p5.mouseIsPressed == True):
      point = Point(x = p5.mouseX, y = p5.mouseY)
      point_list.append(point)

# event function below need to be included,
# even if they don't do anything

def keyPressed(event):
  #print('keyPressed.. ' + str(p5.key))
  pass

def keyReleased(event):
  #print('keyReleased.. ' + str(p5.key))
  pass

def mousePressed(event):
  #print('mousePressed..')
  global program_state
  
  if (program_state == 'START'):
    program_state = 'PLAY'

  point = Point(x = p5.mouseX, y = p5.mouseY)
  point_list.append(point)

def mouseReleased(event):
  #print('mouseReleased..')
  pass


  
