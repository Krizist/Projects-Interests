class Point
{
   float x, y, a, b, c;
   Point A, B, C;
   boolean barycentric;
   
   Point(float x, float y)
   {
     this.x = x;
     this.y = y;
     barycentric = false;
   }
   
   void Barycentric(Point A, Point B, Point C)
   {
      this.A = A;
      this.B = B;
      this.C = C;      
      Point AP = new Point(x-A.x,y-A.y);
      Point AB = new Point(B.x-A.x,B.y-A.y);
      Point AC = new Point(C.x-A.x,C.y-A.y);
      float x = det(AP,AC) / det(AB, AC);
      float y = det(AP,AB) / det(AC, AB);
      a = 1 - x - y;
      b = x;
      c = y;
      barycentric = true;
   }
   
   void Show()
   {
      float i = x, j = y;
      if(barycentric)
      {
        i = a * A.x + b * B.x + c* C.x;
        j = a * A.y + b * B.y + c* C.y;
      }
      ellipse(i, j, 10, 10);
      vertex(i,j);
   }
}

class Frame
{
    ArrayList<Point> arr;
    Point A, B, C;
    
    Frame(Point A, Point B, Point C)
    {
       this.A = A;
       this.B = B;
       this.C = C;
       arr = new ArrayList<Point>();
    }
    
    void Add(Point p)
    {
       p.Barycentric(A,B,C);
       arr.add(p);
    }
    
    void Show(float mX, float mY, float time)
    {
        Point centroid = new Point((A.x + B.x + C.x)/3, (A.y + B.y + C.y)/3);
        Point temp = R(A, time * (1 + d(centroid, new Point(mX, mY))/100), centroid);
        A.x = temp.x;
        A.y = temp.y;
        temp = R(B, time * (1 + d(centroid, new Point(mX, mY))/100), centroid);
        B.x = temp.x;
        B.y = temp.y;
        temp = R(C, time * (1 + d(centroid, new Point(mX, mY))/100), centroid);
        C.x = temp.x;
        C.y = temp.y;
        
        line(B.x, B.y, A.x, A.y);  
        line(A.x, A.y, C.x, C.y);
        beginShape();
        for(Point p : arr)
          p.Show();       endShape();
    }
}