class conversion         
{
   public static void main(String args[])
   {
    byte b;
    int i=500;
    float f=123.942f;
    System.out.println("ln conversion of float to byte");
    b=(byte)f;
    System.out.println("float was "+f+"and byte "+b);
    System.out.println("ln conversion of int to float");
    f=i;
    System.out.println("integer was "+i+"and float is "+f);
   }
}