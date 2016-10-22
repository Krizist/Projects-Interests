float time = 0;
Frame f;
Point A, B, C;
Point[] ps;
boolean forward = true;

void setup()
{
   size(800, 800);
   A = new Point(100, 100);
   B = new Point(50, 100);
   C = new Point(100, 50);
   f = new Frame(A, B, C);
   f.Add(new Point(55, 80));
   f.Add(new Point(80, 80));
   f.Add(new Point(80, 55));
   f.Add(new Point(55, 55));
   ps = new Point[4];
   ps[0] = new Point(100,329);
   ps[1] = new Point(100,169);
   ps[2] = new Point(353,423);
   ps[3] = new Point(636,696);
}

void draw()
{    
  background(#FFFFFF);
  noFill();
  stroke(#000000); 
  strokeWeight(3);
  float a =spiralAngle(ps[0],ps[1],ps[2],ps[3]); 
  float m =spiralScale(ps[0],ps[1],ps[2],ps[3]);
  Point F = SpiralCenter(a, m, ps[0], ps[2]);  
  ellipse(F.x, F.y, 5, 5);
  beginShape();
    for(float t=-1.0; t<=1; t+=0.05) 
      edge(spiralPt(ps[0],F,m,a,t),spiralPt(ps[1],F,m,a,t));
  endShape();
  Point p = spiralPt(ps[0],F,m,a,time);
  A.x = p.x + 25;
  A.y = p.y + 25;
  B.x = p.x + 25;
  B.y = p.y - 25;
  C.x = p.x - 25;
  C.y = p.y + 25;
  f.Show(mouseX, mouseY, time);
  if(forward)
    time += .01;
  else
    time -= .01;
  if(time > 1)
    forward = false;
  if(time < -1)
    forward = true;
}


// Code from Jarek below
void edge(Point P, Point Q) 
{
  line(P.x,P.y,Q.x,Q.y); 
}   

float spiralAngle(Point A, Point B, Point C, Point D) 
{
  return angle(new Point(B.x-A.x, B.y-A.y), new Point(D.x-C.x, D.y-C.y));
}
float spiralScale(Point A, Point B, Point C, Point D) 
{
  return d(C,D)/d(A,B);
}
// angle <U,V> (between -PI and PI)
float angle (Point U, Point V) 
{
  return atan2(det(U,V), dot(U,V)); 
}  
// ||AB|| (Distance)
float d(Point P, Point Q) 
{
  return sqrt(d2(P,Q));
}                                                       
float d2(Point P, Point Q) 
{
  return sq(Q.x-P.x)+sq(Q.y-P.y); 
} 

Point SpiralCenter(float a, float m, Point A, Point C)
{
  float c=cos(a), s=sin(a);
  Point U = new Point(m*c-1,m*s);
  float u2 = dot(U, U);
  Point CA = new Point(A.x - C.x, A.x - C.x);
  Point V = new Point(dot(U,CA)/u2, det(U,CA)/u2);
  return new Point(V.x + A.x, V.y + A.y);
}

Point spiralPt(Point A, Point F, float m, float a, float t)
{
  return L(F,R(A,t*a,F),pow(m,t));
}  

// (1-s)U+sV (Linear interpolation between vectors)
Point L(Point U, Point V, float s) 
{
  return new Point(U.x+s*(V.x-U.x),U.y+s*(V.y-U.y));
}                      

// Q rotated by angle a around point C
Point R(Point Q, float a, Point C) 
{
  float dx=Q.x-C.x, dy=Q.y-C.y, c=cos(a), s=sin(a); 
  return new Point(C.x+c*dx-s*dy, C.y+s*dx+c*dy);
}  


public float dot(Point U, Point V) 
{
  return U.x*V.x+U.y*V.y; 
}
public float det(Point U, Point V) 
{
  return dot(R(U),V); 
} 
public Point R(Point V) 
{
  return new Point(-V.y,V.x);
}