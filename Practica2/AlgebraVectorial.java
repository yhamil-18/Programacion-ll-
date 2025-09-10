public class AlgebraVectorial {
    private double x;
    private double y;
    private double z;
    

    public AlgebraVectorial() {
        this.x = 0.0;
        this.y = 0.0;
        this.z = 0.0;
    }
    

    public AlgebraVectorial(double x, double y, double z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }
    

    public AlgebraVectorial(AlgebraVectorial vector) {
        this.x = vector.x;
        this.y = vector.y;
        this.z = vector.z;
    }
    

    public double getX() {
        return x;
    }
    
    public double getY() {
        return y;
    }
    
    public double getZ() {
        return z;
    }
    
    public void setX(double x) {
        this.x = x;
    }
    
    public void setY(double y) {
        this.y = y;
    }
    
    public void setZ(double z) {
        this.z = z;
    }
    

    public double magnitud() {
        return Math.sqrt(x * x + y * y + z * z);
    }
    

    public double productoPunto(AlgebraVectorial otroVector) {
        return (this.x * otroVector.x + 
                this.y * otroVector.y + 
                this.z * otroVector.z);
    }
    

    public AlgebraVectorial productoVectorial(AlgebraVectorial otroVector) {
        double nuevoX = this.y * otroVector.z - this.z * otroVector.y;
        double nuevoY = this.z * otroVector.x - this.x * otroVector.z;
        double nuevoZ = this.x * otroVector.y - this.y * otroVector.x;
        return new AlgebraVectorial(nuevoX, nuevoY, nuevoZ);
    }
    

    // a) |a + b| = |a - b|
    public boolean esPerpendicular1(AlgebraVectorial otroVector) {
        AlgebraVectorial suma = new AlgebraVectorial(
            this.x + otroVector.x,
            this.y + otroVector.y,
            this.z + otroVector.z
        );
        AlgebraVectorial resta = new AlgebraVectorial(
            this.x - otroVector.x,
            this.y - otroVector.y,
            this.z - otroVector.z
        );
        return Math.abs(suma.magnitud() - resta.magnitud()) < 1e-10;
    }
    
    // b) |a - b| = |b - a|
    public boolean esPerpendicular2(AlgebraVectorial otroVector) {
        AlgebraVectorial ab = new AlgebraVectorial(
            this.x - otroVector.x,
            this.y - otroVector.y,
            this.z - otroVector.z
        );
        AlgebraVectorial ba = new AlgebraVectorial(
            otroVector.x - this.x,
            otroVector.y - this.y,
            otroVector.z - this.z
        );
        return Math.abs(ab.magnitud() - ba.magnitud()) < 1e-10;
    }
    
    // c) a · b = 0
    public boolean esPerpendicular3(AlgebraVectorial otroVector) {
        return Math.abs(this.productoPunto(otroVector)) < 1e-10;
    }
    
    // d) |a + b|² = |a|² + |b|²
    public boolean esPerpendicular4(AlgebraVectorial otroVector) {
        AlgebraVectorial suma = new AlgebraVectorial(
            this.x + otroVector.x,
            this.y + otroVector.y,
            this.z + otroVector.z
        );
        double magnitudSumaCuad = Math.pow(suma.magnitud(), 2);
        double magnitudACuad = Math.pow(this.magnitud(), 2);
        double magnitudBCuad = Math.pow(otroVector.magnitud(), 2);
        return Math.abs(magnitudSumaCuad - (magnitudACuad + magnitudBCuad)) < 1e-10;
    }
    
    // Métodos sobrecargados para paralelismo
    
    // e) a = r*b (existe un escalar r tal que a = r*b)
    public boolean esParalelo1(AlgebraVectorial otroVector) {
        if (otroVector.magnitud() < 1e-10) {
            return false;
        }
        
        double r = 0.0;
        boolean rEncontrado = false;
        
        if (Math.abs(this.x) > 1e-10 && Math.abs(otroVector.x) > 1e-10) {
            r = this.x / otroVector.x;
            rEncontrado = true;
        } else if (Math.abs(this.y) > 1e-10 && Math.abs(otroVector.y) > 1e-10) {
            r = this.y / otroVector.y;
            rEncontrado = true;
        } else if (Math.abs(this.z) > 1e-10 && Math.abs(otroVector.z) > 1e-10) {
            r = this.z / otroVector.z;
            rEncontrado = true;
        }
        
        if (!rEncontrado) {
            return false;
        }
        
        return (Math.abs(this.x - r * otroVector.x) < 1e-10 &&
                Math.abs(this.y - r * otroVector.y) < 1e-10 &&
                Math.abs(this.z - r * otroVector.z) < 1e-10);
    }
    
    // f) a × b = 0
    public boolean esParalelo2(AlgebraVectorial otroVector) {
        AlgebraVectorial productoCruz = this.productoVectorial(otroVector);
        return productoCruz.magnitud() < 1e-10;
    }
    
    // g) Proyección de a sobre b: (a·b/|b|²) * b
    public AlgebraVectorial proyeccion(AlgebraVectorial otroVector) {
        if (Math.abs(otroVector.magnitud()) < 1e-10) {
            return new AlgebraVectorial(0, 0, 0);
        }
        
        double escalar = this.productoPunto(otroVector) / Math.pow(otroVector.magnitud(), 2);
        return new AlgebraVectorial(
            escalar * otroVector.x,
            escalar * otroVector.y,
            escalar * otroVector.z
        );
    }
    
    // h) Componente de a en b: (a·b)/|b|
    public double componente(AlgebraVectorial otroVector) {
        if (Math.abs(otroVector.magnitud()) < 1e-10) {
            return 0.0;
        }
        
        return this.productoPunto(otroVector) / otroVector.magnitud();
    }
    
    // Método para representación string del vector
    @Override
    public String toString() {
        return String.format("(%.2f, %.2f, %.2f)", x, y, z);
    }
    
    // Método main para pruebas
    public static void main(String[] args) {
        // Crear vectores de prueba
        AlgebraVectorial v1 = new AlgebraVectorial(1, 2, 3);
        AlgebraVectorial v2 = new AlgebraVectorial(4, 5, 6);
        AlgebraVectorial v3 = new AlgebraVectorial(0, 0, 1);
        AlgebraVectorial v4 = new AlgebraVectorial(1, 0, 0);
        AlgebraVectorial v5 = new AlgebraVectorial(2, 4, 6);
        
        System.out.println("Vectores:");
        System.out.println("v1 = " + v1.toString());
        System.out.println("v2 = " + v2.toString());
        System.out.println("v3 = " + v3.toString());
        System.out.println("v4 = " + v4.toString());
        System.out.println("v5 = " + v5.toString());
        System.out.println();
        
        // Pruebas de perpendicularidad
        System.out.println("Perpendicularidad v3 y v4:");
        System.out.println("Método 1: " + v3.esPerpendicular1(v4));
        System.out.println("Método 2: " + v3.esPerpendicular2(v4));
        System.out.println("Método 3: " + v3.esPerpendicular3(v4));
        System.out.println("Método 4: " + v3.esPerpendicular4(v4));
        System.out.println();
        
        // Pruebas de paralelismo
        System.out.println("Paralelismo v1 y v5:");
        System.out.println("Método 1: " + v1.esParalelo1(v5));
        System.out.println("Método 2: " + v1.esParalelo2(v5));
        System.out.println();
        
        // Pruebas de proyección y componente
        System.out.println("Proyección de v1 sobre v2:");
        AlgebraVectorial proyeccion = v1.proyeccion(v2);
        System.out.println("Proyección: " + proyeccion.toString());
        
        System.out.println("Componente de v1 en v2:");
        double componente = v1.componente(v2);
        System.out.println("Componente: " + String.format("%.4f", componente));
    }
}