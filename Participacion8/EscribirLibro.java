package Participacion8;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class EscribirLibro {
    public static void main(String[] args) {
        List<Libro> libros = new ArrayList<>();
        libros.add(new Libro("Cien años de soledad", "Gabriel Garcia Marquez"));
        libros.add(new Libro("1984", "George Orwell"));
        libros.add(new Libro("El Quijote", "Miguel de Cervantes"));
        
        Gson gson = new GsonBuilder().setPrettyPrinting().create();
        
        try (FileWriter writer = new FileWriter("libros.json")) {
            gson.toJson(libros, writer);
            System.out.println("3 libros guardados exitosamente en libros.json");
        } catch (IOException e) {
            System.err.println("Error al escribir el archivo: " + e.getMessage());
        }
    }
}

