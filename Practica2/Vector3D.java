public class Vector3D {
    private double x;
    private double y;
    private double z;
    
    // Constructores
    public Vector3D() {
        this(0.0, 0.0, 0.0);
    }
    
    public Vector3D(double x, double y, double z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }
    
    // Getters y Setters
    public double getX() { return x; }
    public double getY() { return y; }
    public double getZ() { return z; }
    public void setX(double x) { this.x = x; }
    public void setY(double y) { this.y = y; }
    public void setZ(double z) { this.z = z; }
    
    // Métodos para operaciones (simulan sobrecarga de operadores)
    public Vector3D add(Vector3D other) {
        return new Vector3D(this.x + other.x, this.y + other.y, this.z + other.z);
    }
    
    public Vector3D subtract(Vector3D other) {
        return new Vector3D(this.x - other.x, this.y - other.y, this.z - other.z);
    }
    
    public Vector3D multiply(double scalar) {
        return new Vector3D(this.x * scalar, this.y * scalar, this.z * scalar);
    }
    
    public double dotProduct(Vector3D other) {
        return this.x * other.x + this.y * other.y + this.z * other.z;
    }
    
    public Vector3D crossProduct(Vector3D other) {
        return new Vector3D(
            this.y * other.z - this.z * other.y,
            this.z * other.x - this.x * other.z,
            this.x * other.y - this.y * other.x
        );
    }
    
    // Operaciones vectoriales
    public double magnitud() {
        return Math.sqrt(x * x + y * y + z * z);
    }
    
    public Vector3D normalizar() {
        double mag = magnitud();
        if (mag < 1e-10) return new Vector3D(0, 0, 0);
        return new Vector3D(x/mag, y/mag, z/mag);
    }
    
    // Métodos de análisis
    public boolean esPerpendicular(Vector3D other) {
        return Math.abs(this.dotProduct(other)) < 1e-10;
    }
    
    public boolean esParalelo(Vector3D other) {
        Vector3D cross = this.crossProduct(other);
        return cross.magnitud() < 1e-10;
    }
    
    public Vector3D proyeccion(Vector3D other) {
        double magSq = other.magnitud() * other.magnitud();
        if (magSq < 1e-10) return new Vector3D(0, 0, 0);
        double scalar = this.dotProduct(other) / magSq;
        return other.multiply(scalar);
    }
    
    public double componente(Vector3D other) {
        double mag = other.magnitud();
        if (mag < 1e-10) return 0.0;
        return this.dotProduct(other) / mag;
    }
    
    @Override
    public String toString() {
        return String.format("(%.2f, %.2f, %.2f)", x, y, z);
    }
    
    // Método main para pruebas
    public static void main(String[] args) {
        System.out.println("=== PROGRAMA DE ÁLGEBRA VECTORIAL EN JAVA ===");
        System.out.println();
        
        // Crear vectores de prueba
        Vector3D a = new Vector3D(1, 2, 3);
        Vector3D b = new Vector3D(4, 5, 6);
        Vector3D c = new Vector3D(0, 0, 1);
        Vector3D d = new Vector3D(1, 0, 0);
        Vector3D e = new Vector3D(2, 4, 6);  // Paralelo a a (e = 2*a)
        
        System.out.println("Vectores:");
        System.out.println("a = " + a);
        System.out.println("b = " + b);
        System.out.println("c = " + c);
        System.out.println("d = " + d);
        System.out.println("e = " + e);
        System.out.println();
        
        // Operaciones básicas
        System.out.println("Operaciones básicas:");
        System.out.println("a + b = " + a.add(b));
        System.out.println("a - b = " + a.subtract(b));
        System.out.println("a * 2 = " + a.multiply(2));
        System.out.println("a · b (producto escalar) = " + String.format("%.2f", a.dotProduct(b)));
        System.out.println("a × b (producto vectorial) = " + a.crossProduct(b));
        System.out.println("|a| (magnitud) = " + String.format("%.2f", a.magnitud()));
        System.out.println("a_normalizado = " + a.normalizar());
        System.out.println();
        
        // Análisis de vectores
        System.out.println("Análisis de vectores:");
        System.out.println("c ⟂ d (perpendiculares): " + c.esPerpendicular(d));
        System.out.println("a ∥ e (paralelos): " + a.esParalelo(e));
        System.out.println("Proyección de a sobre b: " + a.proyeccion(b));
        System.out.println("Componente de a en b: " + String.format("%.2f", a.componente(b)));
        System.out.println();
        
        // Verificación de propiedades
        System.out.println("Verificación de propiedades:");
        System.out.println("a · c = " + String.format("%.2f", a.dotProduct(c)));
        System.out.println("|a × e| = " + String.format("%.2f", a.crossProduct(e).magnitud()) + 
                        " (debe ser ≈ 0 para paralelos)");
    }
}
