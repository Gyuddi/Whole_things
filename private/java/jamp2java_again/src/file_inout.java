<<<<<<< HEAD
import java.io.FileOutputStream;
import java.io.IOException;

public class file_inout {
    public static void main(String[] args) throws IOException {
        FileOutputStream output = new FileOutputStream("c:/sout.txt");
        for(int i=1; i<11; i++) {
            String data = i+" 번째 줄입니다.\r\n";
            output.write(data.getBytes());
        }
        output.close();
    }
=======
import java.io.FileOutputStream;
import java.io.IOException;

public class file_inout {
    public static void main(String[] args) throws IOException {
        FileOutputStream output = new FileOutputStream("c:/sout.txt");
        for(int i=1; i<11; i++) {
            String data = i+" 번째 줄입니다.\r\n";
            output.write(data.getBytes());
        }
        output.close();
    }
>>>>>>> 58110c72042666d64e8117b99a8afe7db8511558
}