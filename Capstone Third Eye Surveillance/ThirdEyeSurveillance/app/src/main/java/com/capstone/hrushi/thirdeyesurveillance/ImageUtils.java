package com.capstone.hrushi.thirdeyesurveillance;


import android.content.Context;
import android.graphics.Bitmap;
import android.os.Environment;
import android.util.Log;
import android.widget.Toast;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;

public class ImageUtils {

    private static final String TAG = "ImageUtils";

    public static void saveCompressedImage(Context context, Bitmap bitmap) throws IOException {
        // Create a compressed version of the image
        File storageDir = new File(context.getExternalFilesDir(Environment.DIRECTORY_PICTURES), "ThirdEyeSurveillance");
        File imageFile1 = new File(storageDir,"Compressed_image.jpg");
        if (!storageDir.exists()) {
            storageDir.mkdirs();
            if(imageFile1.exists()){
                Log.d(TAG,"Compressed image Found : "+imageFile1.getAbsolutePath());
            }
        }

        // Generate a timestamped file name
        String timeStamp = new SimpleDateFormat("yyyyMMdd_HHmmss", Locale.US).format(new Date());
        File imageFile = new File(storageDir, "IMG_" + timeStamp + ".jpg");

        // Compress and save the image
        FileOutputStream fos = new FileOutputStream(imageFile);
        bitmap.compress(Bitmap.CompressFormat.JPEG, 80, fos); // 80 is the quality (0-100)
        fos.flush();
        fos.close();

        // Log and show a toast with the image file path
        Log.d(TAG, "Compressed image saved at: " + imageFile.getAbsolutePath());
        Toast.makeText(context, "Compressed image saved", Toast.LENGTH_SHORT).show();
    }
}
