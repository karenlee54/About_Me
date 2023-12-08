import js as p5

program_state = 'START'
Font = p5.loadFont('Neue Haas Unica W1G.otf')

class Point:
  def __init__(self, x = -100, y = -100):
    self.x = x
    self.y = y
    p5.imageMode(p5.CENTER)
    self.T = p5.loadImage('End.png')

  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    p5.image(self.T, 0, 0, 20, 20)
    p5.pop()

point = Point()
point_list = [point]

class Logo:
  x = 350
  y = 430

  def __init__(self):
    self.img1 = p5.loadImage('Logo/Logo.png')

  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    p5.imageMode(p5.CENTER)
    p5.image(self.img1, 0, 0, 300, 270)
    p5.textAlign(p5.CENTER)
    p5.textFont(Font, 25)
    p5.text('About Me', 0, 240)
    p5.textFont(Font, 15)
    p5.text('Click to start', 0, 275)
    p5.pop()


class Button:
  x = 350
  y = 1000

  def __init__(self):
    self.img2 = p5.loadImage('Logo/Logo_Horizontal.jpg')

  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    p5.imageMode(p5.CENTER)
    p5.image(self.img2, 0, 0, 650, 150)
    p5.pop()

class Karen:
  def __init__(self, x = 102.5, y = 1000):
    p5.imageMode(p5.CENTER)
    self.KL = p5.loadImage('Karen/K.png')
    self.KE = p5.loadImage('Karen/KAREN_E.png')
    self.KK = p5.loadImage('Karen/KAREN_K.png')
    self.timer = p5.millis()
    self.x = x
    self.y = y

class Karen_K(Karen):
  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    if(p5.millis() % 1000 < 500):
      p5.image(self.KE, 0, 0, 153.12, 45)
    else:
      p5.image(self.KK, 0, 0, 104.51, 45)
    p5.pop()

  def update(self):
    if(p5.millis() > self.timer + 500):
      self.y -= 4

class Seoyoung:
  def __init__(self, x = 270, y = 1000):
    p5.imageMode(p5.CENTER)
    self.SL = p5.loadImage('Seoyoung/S.png')
    self.SE = p5.loadImage('Seoyoung/SEOYOUNG_E.png')
    self.SK = p5.loadImage('Seoyoung/SEOYOUNG_K.png')
    self.timer = p5.millis()
    self.x = x
    self.y = y

class Seoyoung_S(Seoyoung):
  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    if(p5.millis() % 1000 < 500):
      p5.image(self.SE, 0, 0, 263.25, 55.84)
    else:
      p5.image(self.SK, 0, 0, 104.50, 45)
    p5.pop()

  def update(self):
    if(p5.millis() > self.timer + 500):
      self.y -= 4

class Lee:
  def __init__(self, x = 436, y = 1000):
    p5.imageMode(p5.CENTER)
    self.LL = p5.loadImage('Lee/L.png')
    self.LE = p5.loadImage('Lee/LEE_E.png')
    self.LK = p5.loadImage('Lee/LEE_K.png')
    self.timer = p5.millis()
    self.x = x
    self.y = y

class Lee_L(Lee):
  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    if(p5.millis() % 1000 < 500):
      p5.image(self.LE, 0, 0, 95.58, 45)
    else:
      p5.image(self.LK, 0, 0, 47.75, 45)
    p5.pop()

  def update(self):
    if(p5.millis() > self.timer + 500):
      self.y -= 4

class Triangle:
  def __init__(self, x = 25, y = 30):
    p5.imageMode(p5.CORNER)
    self.E = p5.loadImage('Full Name/Name_E.png')
    self.K = p5.loadImage('Full Name/Name_K.png')
    self.L = p5.loadImage('Logo Animation.gif')
    self.timer = p5.millis()
    self.x = x
    self.y = y

class Triangle_T(Triangle):
  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    p5.fill(255)
    p5.noStroke()
    p5.rect(-25, -30, 700, 1100)
    p5.imageMode(p5.CORNER)
    p5.image(self.E, 210, 0, 419.64, 45)
    p5.image(self.L, -5, -10, 198, 180)
    p5.textAlign(p5.LEFT)
    p5.fill(102, 103, 102)
    p5.textFont(Font, 25)
    p5.text('Graphic Designer', 210, 90)
    p5.text('UI/UX Designer', 210, 110)
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
    p5.text('karenseoyounglee.com', 0, 1050) 
    
    if (program_state == 'END'):
      for i in range(len(point_list)):
        point = point_list[i]
        point.draw()

      if(p5.mouseIsPressed == True):
        point = Point(x = p5.mouseX, y = p5.mouseY)
        point_list.append(point)
      else:
        None
    p5.pop()


#print('Assignment #8 (Final Project Part B)')

logo = Logo()
button = Button()
karen = Karen_K()
seoyoung = Seoyoung_S()
lee = Lee_L()
triangle = Triangle_T()



def setup():
  p5.createCanvas(700, 1100)  

def draw():
  p5.background(255)   
  p5.fill(0)  
  cursor_xy = (int(p5.mouseX), int(p5.mouseY))
  p5.text(cursor_xy, 10, 20)  # cursor (x, y) 

  global program_state, karen, seoyoung, lee

  if (program_state == 'END'):
    p5.textAlign(p5.CORNER)
    triangle.draw()

  if (program_state == 'START'):
    logo.draw()
      
  if (program_state == 'PLAY'):

    p5.textAlign(p5.CORNER)
    p5.textFont(Font, 25)
    p5.text('Click each of the symbols,', 25, 40)
    p5.text('it means...', 25, 80)
    
    #Karen
    if (p5.mouseX > 25) and (p5.mouseX < 180) and (p5.mouseY > 925) and (p5.mouseY < 1075):
      karen.draw()
      karen.update()
    else:
      karen.x = karen.x
      karen.y = 1000

    #Seoyoung
    if (p5.mouseX > 195) and (p5.mouseX < 345) and (p5.mouseY > 925) and (p5.mouseY < 1075):
      seoyoung.draw()
      seoyoung.update()
    else:
      seoyoung.x = 270
      seoyoung.y = 1000

    #Lee
    if (p5.mouseX > 360) and (p5.mouseX < 510) and (p5.mouseY > 925) and (p5.mouseY < 1075):
      lee.draw()
      lee.update()
    else:
      lee.x = 435
      lee.y = 1000

    #Triangle
    if (p5.mouseX > 525) and (p5.mouseX < 675) and (p5.mouseY > 925) and (p5.mouseY < 1075):
      program_state = 'END'

    button.draw()
    
    # for i in range(len(point_list)):
    #   point = point_list[i]
    #   point.draw()

    # if(p5.mouseIsPressed == True):
    #   point = Point(x = p5.mouseX, y = p5.mouseY)
    #   point_list.append(point)

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


  
