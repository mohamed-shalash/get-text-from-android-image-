package com.example.text__image;

import androidx.appcompat.app.AppCompatActivity;

import android.graphics.Bitmap;
import android.graphics.drawable.BitmapDrawable;
import android.os.Bundle;
import android.util.Base64;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.Toast;

import com.chaquo.python.PyObject;
import com.chaquo.python.Python;
import com.chaquo.python.android.AndroidPlatform;

import java.io.ByteArrayOutputStream;

public class MainActivity extends AppCompatActivity {
    Button btn;
    ImageView iv;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        btn =findViewById(R.id.button);
        iv =findViewById(R.id.imageView);
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (!Python.isStarted()) {
                    Python.start(new AndroidPlatform(getBaseContext()));
                }

                BitmapDrawable drawable = (BitmapDrawable) iv.getDrawable();
                Bitmap bitmap = drawable.getBitmap();
                String imagestring = getstringimage(bitmap);

                Python py = Python.getInstance();
                PyObject pyobj = py.getModule("imagetextconverter");

                PyObject obj = pyobj.callAttr("main_text", imagestring);
                String str = String.copyValueOf(obj.toString().toCharArray());

                Toast.makeText(getBaseContext(), str, Toast.LENGTH_LONG).show();
            }
        });
        /*
        *  if (!Python.isStarted()) {
                        Python.start(new AndroidPlatform(getBaseContext()));
                    }

                    BitmapDrawable drawable = (BitmapDrawable) im.getDrawable();
                    bitmap = drawable.getBitmap();
                    String imagestring = getstringimage(bitmap);

                    Python py = Python.getInstance();
                    PyObject pyobj = py.getModule("imagetextconverter");

                    PyObject obj = pyobj.callAttr("main", imagestring);
                    String str = String.copyValueOf(obj.toString().toCharArray());
                    str = str.substring(3, str.length() - 1);
                    ///str=str.replaceAll("\\\\","\\");
                    String x[]=str.split("\\n");
                    //Toast.makeText(getBaseContext(),str.substring(5,7), Toast.LENGTH_LONG).show();
                    for (String y:x) {
                        Toast.makeText(getBaseContext(), y, Toast.LENGTH_LONG).show();
                    }
                    Toast.makeText(getBaseContext(), str, Toast.LENGTH_LONG).show();
                    tv.setText(str);*/
    }
    private String getstringimage(Bitmap bitmap){
        ByteArrayOutputStream baos =new ByteArrayOutputStream();
        bitmap.compress(Bitmap.CompressFormat.PNG,100,baos);
        byte[] imagebyte =baos.toByteArray();
        String encodedImage = android.util.Base64.encodeToString(imagebyte, Base64.DEFAULT);
        return encodedImage;
    }
}