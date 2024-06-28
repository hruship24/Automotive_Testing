package com.capstone.hrushi.thirdeyesurveillance;

import android.content.Context;
import android.graphics.Bitmap;
import android.location.Location;
import android.os.Environment;
import android.util.Log;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;

public class StorageHelper {

    private static final String TAG = "StorageHelper";
    private static final String DIRECTORY_NAME = "ThirdEyeSurveillance";

    // Method to save a compressed image with metadata
    public static void saveCompressedImage(Context context, Bitmap imageBitmap, Location location) throws IOException {
        String timeStamp = new SimpleDateFormat("yyyyMMdd_HHmmss", Locale.getDefault()).format(new Date());
        File storageDir = getStorageDir(context);
        File imageFile = new File(storageDir, "IMG_" + timeStamp + ".jpg");

        FileOutputStream outputStream = new FileOutputStream(imageFile);
        imageBitmap.compress(Bitmap.CompressFormat.JPEG, 80, outputStream); // Compress bitmap
        outputStream.flush();
        outputStream.close();

        // Add metadata handling here (e.g., saving location information to a database)
        saveMetadata(imageFile, location);
    }

    // Method to save a captured video with metadata
    public static void saveVideo(Context context, String videoPath, Location location) throws IOException {
        File storageDir = getStorageDir(context);
        File videoFile = new File(storageDir, "VIDEO_" + System.currentTimeMillis() + ".mp4");

        // Example: Move the captured video to the storage directory
        // Replace with your actual video saving logic
        File originalFile = new File(videoPath);
        if (originalFile.exists()) {
            originalFile.renameTo(videoFile);
        }

        // Add metadata handling here (e.g., saving location information to a database)
        saveMetadata(videoFile, location);
    }

    // Method to save metadata (e.g., location, timestamp) associated with the media file
    private static void saveMetadata(File file, Location location) {
        // Example: Save location and timestamp metadata to a database or file associated with 'file'
        // Replace with your actual metadata saving logic
        Log.d(TAG, "Saved metadata for: " + file.getName());
        if (location != null) {
            Log.d(TAG, "Location: " + location.getLatitude() + ", " + location.getLongitude());
        }
    }

    // Helper method to create directory if it doesn't exist
    private static File getStorageDir(Context context) {
        File file = new File(context.getExternalFilesDir(Environment.DIRECTORY_PICTURES), DIRECTORY_NAME);
        if (!file.exists()) {
            if (!file.mkdirs()) {
                Log.e(TAG, "Failed to create directory: " + DIRECTORY_NAME);
            }
        }
        return file;
    }
}
