
package Participacion8;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import java.io.FileReader;
import java.io.IOException;
import java.lang.reflect.Type;
import java.util.List;


public class LeerLibro {
    public static void main(String[] args) {
        Gson gson = new Gson();
        
        try (FileReader reader = new FileReader("libros.json")) {
            Type listType = new TypeToken<List<Libro>>(){}.getType();
            
            List<Libro> libros = gson.fromJson(reader, listType);
            
            System.out.println("Libros leidos desde libros.json:");
            
            for (int i = 0; i < libros.size(); i++) {
                Libro libro = libros.get(i);
                System.out.println((i + 1) + ". " + libro.toString());
            }
            
        } catch (IOException e) {
            System.err.println("Error al leer el archivo: " + e.getMessage());
        }
    }
}
