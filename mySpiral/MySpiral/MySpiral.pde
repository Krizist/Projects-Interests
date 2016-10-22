pts P = new pts(); // class containing array of points, used to standardize GUI
color black=#000000, white=#FFFFFF, // set more colors using Menu >  Tools > Color Selector
   red=#FF0000, green=#00FF01, blue=#0300FF, yellow=#FEFF00, cyan=#00FDFF, magenta=#FF00FB, grey=#5F5F5F;
boolean change = false, forward = true;
float t = 0, f = 0;

void setup()               // executed once at the begining 
  {
  size(800, 800);            // window size
  frameRate(30);             // render 30 frames per second
  smooth();                  // turn on antialiasing
  P.declare(); // declares all points in P. MUST BE DONE BEFORE ADDING POINTS 
  P.resetOnCircle(4); 
  }

void draw()
{
  background(black);
  pt A = P.G[0], B = P.G[1], C = P.G[2], D = P.G[3], anim = P.G[1];
  
  pen(white, 1);
  showId(A, "0");
  showId(B, "2");
  showId(C, "3");
  showId(D, "1");
  pen(blue, 50);
  //showId(anim, "yay");
  
  pen(green, 1);
  edge(A, B);
  edge(C, D);
  
  pen(white, 1);
  show(SpiralCenter2(A, B, C, D), 20);
  showSpiralPattern(A, B, C, D);
  float angle = spiralAngle(A, B, C, D);
  float scale = spiralScale(A, B, C, D);
  pt center = SpiralCenter(angle, scale, A, C);
  beginShape();
    for(float x=-1.0; x<=1; x+=0.05) 
      edge(spiralPt(A,center,scale,angle,x),spiralPt(B,center,scale,angle,x));
  endShape();
  pt p = spiralPt(A,center,scale,angle,t);
  //pen(blue,1); 
  //showSpiralThrough3Points(center, A, C); 
  pen(yellow, 50);
  //showId(p, "p");
  show(SpiralCenter(p.x, p.y, p, A));
  //pushMatrix();
  //translate(width*0.1, height*0.05);
  //rotate(frameCount / -5.0);
  //star(400, 200, 30, 70, 5);
  //popMatrix();
  //anim.x = p.x + 25;
  //anim.y = p.y + 25;
  if(forward)
    t += .01;
  else
    t -= .01;
  if(t > 1)
    forward = false;
  if(t < -1)
    forward = true;
}

void mousePressed()   // executed when the mouse is pressed
  {
  P.pickClosest(Mouse()); // pick vertex closest to mouse: sets pv ("picked vertex") in pts
  if (keyPressed) 
     {
     if (key=='a')  P.addPt(Mouse()); // appends vertex after the last one
     if (key=='i')  P.insertClosestProjection(Mouse()); // inserts vertex at closest projection of mouse
     if (key=='d')  P.deletePickedPt(); // deletes vertex closeset to mouse
     }  
  change=true;
  }

void mouseDragged() // executed when the mouse is dragged (while mouse buttom pressed)
  {
  if (!keyPressed || (key=='a')|| (key=='i')) P.dragPicked();   // drag selected point with mouse
  if (keyPressed) {
      if (key=='.') f+=2.*float(mouseX-pmouseX)/width;  // adjust current frame   
      if (key=='t') P.dragAll(); // move all vertices
      if (key=='r') P.rotateAllAroundCentroid(Mouse(),Pmouse()); // turn all vertices around their center of mass
      if (key=='z') P.scaleAllAroundCentroid(Mouse(),Pmouse()); // scale all vertices with respect to their center of mass
      }
  change=true;
  }  

void pen(color c, float w) {stroke(c); strokeWeight(w);}

void star(float x, float y, float radius1, float radius2, int npoints) {
  float angle = TWO_PI / npoints;
  float halfAngle = angle/2.0;
  beginShape();
  for (float a = 0; a < TWO_PI; a += angle) {
    float sx = x + cos(a) * radius2;
    float sy = y + sin(a) * radius2;
    vertex(sx, sy);
    sx = x + cos(a+halfAngle) * radius1;
    sy = y + sin(a+halfAngle) * radius1;
    vertex(sx, sy);
  }
  endShape(CLOSE);
}